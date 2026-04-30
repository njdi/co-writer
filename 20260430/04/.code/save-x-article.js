// save-x-article.js
// Usage: node save-x-article.js <article_url> <ws_url> <out_dir>

import https from 'https';
import http from 'http';
import fs from 'fs';
import path from 'path';
import net from 'net';
import crypto from 'crypto';
import { URL } from 'url';

const [,, ARTICLE_URL, WS_URL, OUT_DIR_ARG] = process.argv;
if (!ARTICLE_URL || !WS_URL || !OUT_DIR_ARG) {
  console.error('Usage: node save-x-article.js <article_url> <ws_url> <out_dir>');
  process.exit(1);
}

const OUT_DIR = OUT_DIR_ARG;
const IMAGES_DIR = path.join(OUT_DIR, 'images');
const SCREENSHOTS_DIR = path.join(OUT_DIR, 'screenshots');

let msgId = 1;
const pending = new Map();
const eventWaiters = new Map();

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    url = url.replace(/name=(small|medium|orig)/, 'name=large');
    const parsed = new URL(url);
    const client = parsed.protocol === 'https:' ? https : http;
    const file = fs.createWriteStream(dest);
    const req = client.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'Referer': 'https://x.com/',
      },
    }, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        file.close();
        fs.unlinkSync(dest);
        return downloadFile(res.headers.location, dest).then(resolve).catch(reject);
      }
      if (res.statusCode < 200 || res.statusCode >= 300) {
        file.close();
        fs.unlink(dest, () => {});
        reject(new Error(`HTTP ${res.statusCode}`));
        return;
      }
      res.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve();
      });
    });
    req.on('error', (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

class CdpSocket {
  constructor(wsUrl) {
    this.url = new URL(wsUrl);
    this.socket = null;
    this.buffer = Buffer.alloc(0);
    this.handshaken = false;
    this.onMessage = () => {};
  }

  async open() {
    this.socket = net.createConnection({
      host: this.url.hostname,
      port: Number(this.url.port || 80),
    });

    await new Promise((resolve, reject) => {
      this.socket.once('connect', resolve);
      this.socket.once('error', reject);
    });

    const key = crypto.randomBytes(16).toString('base64');
    this.socket.write([
      `GET ${this.url.pathname} HTTP/1.1`,
      `Host: ${this.url.host}`,
      'Upgrade: websocket',
      'Connection: Upgrade',
      `Sec-WebSocket-Key: ${key}`,
      'Sec-WebSocket-Version: 13',
      '',
      '',
    ].join('\r\n'));

    await new Promise((resolve, reject) => {
      const onData = (chunk) => {
        this.buffer = Buffer.concat([this.buffer, chunk]);
        const idx = this.buffer.indexOf('\r\n\r\n');
        if (idx === -1) return;
        const header = this.buffer.slice(0, idx).toString('utf8');
        if (!header.startsWith('HTTP/1.1 101')) {
          reject(new Error(`WebSocket handshake failed: ${header.split('\r\n')[0]}`));
          return;
        }
        this.buffer = this.buffer.slice(idx + 4);
        this.socket.off('data', onData);
        this.handshaken = true;
        this.socket.on('data', (data) => this.read(data));
        if (this.buffer.length) this.read(Buffer.alloc(0));
        resolve();
      };
      this.socket.on('data', onData);
      this.socket.once('error', reject);
    });
  }

  read(chunk) {
    if (chunk.length) this.buffer = Buffer.concat([this.buffer, chunk]);
    while (this.buffer.length >= 2) {
      const first = this.buffer[0];
      const second = this.buffer[1];
      const opcode = first & 0x0f;
      const masked = Boolean(second & 0x80);
      let offset = 2;
      let length = second & 0x7f;
      if (length === 126) {
        if (this.buffer.length < offset + 2) return;
        length = this.buffer.readUInt16BE(offset);
        offset += 2;
      } else if (length === 127) {
        if (this.buffer.length < offset + 8) return;
        const bigLength = this.buffer.readBigUInt64BE(offset);
        if (bigLength > BigInt(Number.MAX_SAFE_INTEGER)) throw new Error('Frame too large');
        length = Number(bigLength);
        offset += 8;
      }
      let mask;
      if (masked) {
        if (this.buffer.length < offset + 4) return;
        mask = this.buffer.slice(offset, offset + 4);
        offset += 4;
      }
      if (this.buffer.length < offset + length) return;
      let payload = this.buffer.slice(offset, offset + length);
      this.buffer = this.buffer.slice(offset + length);
      if (masked) {
        payload = Buffer.from(payload.map((byte, i) => byte ^ mask[i % 4]));
      }
      if (opcode === 1) this.onMessage(payload.toString('utf8'));
      if (opcode === 8) this.close();
    }
  }

  sendText(text) {
    const payload = Buffer.from(text, 'utf8');
    let headerLength = 2;
    if (payload.length >= 126 && payload.length < 65536) headerLength += 2;
    else if (payload.length >= 65536) headerLength += 8;
    const mask = crypto.randomBytes(4);
    const frame = Buffer.alloc(headerLength + 4 + payload.length);
    frame[0] = 0x81;
    let offset = 2;
    if (payload.length < 126) {
      frame[1] = 0x80 | payload.length;
    } else if (payload.length < 65536) {
      frame[1] = 0x80 | 126;
      frame.writeUInt16BE(payload.length, offset);
      offset += 2;
    } else {
      frame[1] = 0x80 | 127;
      frame.writeBigUInt64BE(BigInt(payload.length), offset);
      offset += 8;
    }
    mask.copy(frame, offset);
    offset += 4;
    for (let i = 0; i < payload.length; i++) {
      frame[offset + i] = payload[i] ^ mask[i % 4];
    }
    this.socket.write(frame);
  }

  close() {
    if (this.socket) this.socket.end();
  }
}

async function connect(wsUrl) {
  const ws = new CdpSocket(wsUrl);
  await ws.open();

  ws.onMessage = (data) => {
    const msg = JSON.parse(data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(new Error(msg.error.message));
      else resolve(msg.result);
    }
    if (msg.method && eventWaiters.has(msg.method)) {
      eventWaiters.get(msg.method)(msg.params);
      eventWaiters.delete(msg.method);
    }
  };

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = msgId++;
    pending.set(id, { resolve, reject });
    ws.sendText(JSON.stringify({ id, method, params }));
  });

  const waitEvent = (eventName, timeout = 20000) => new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Timeout: ${eventName}`)), timeout);
    eventWaiters.set(eventName, (params) => {
      clearTimeout(timer);
      resolve(params);
    });
  });

  return { ws, send, waitEvent };
}

async function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.mkdirSync(IMAGES_DIR, { recursive: true });
  fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

  console.log('Connecting to Chrome CDP...');
  const { ws, send, waitEvent } = await connect(WS_URL);

  await send('Page.enable');
  await send('Runtime.enable');

  console.log('Navigating to article...');
  const loadEvent = waitEvent('Page.loadEventFired', 30000).catch(() => null);
  await send('Page.navigate', { url: ARTICLE_URL });
  await loadEvent;
  console.log('Page loaded, waiting for React render...');
  await sleep(5000);

  console.log('Scrolling and taking screenshots...');
  const { result: { value: pageInfo } } = await send('Runtime.evaluate', {
    expression: `({ scrollHeight: document.body.scrollHeight, viewHeight: window.innerHeight })`,
    returnByValue: true,
  });

  const step = Math.max(400, Math.floor(pageInfo.viewHeight * 0.8));
  let pos = 0;
  let shotIdx = 0;

  while (pos < pageInfo.scrollHeight + step) {
    await send('Runtime.evaluate', {
      expression: `window.scrollTo(0, ${pos})`,
      returnByValue: true,
    });
    await sleep(350);

    const shot = await send('Page.captureScreenshot', { format: 'jpeg', quality: 80 });
    const shotFile = path.join(SCREENSHOTS_DIR, `shot-${String(shotIdx).padStart(2, '0')}.jpg`);
    fs.writeFileSync(shotFile, Buffer.from(shot.data, 'base64'));
    shotIdx++;
    pos += step;
  }

  await send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0)', returnByValue: true });
  console.log(`Screenshots: ${shotIdx} captured`);
  await sleep(2000);

  const { result: { value: extracted } } = await send('Runtime.evaluate', {
    expression: `(() => {
      const article = document.querySelector('main article') || document.body;
      const seen = new Set();
      const saved = [];

      Array.from(article.querySelectorAll('img')).forEach(img => {
        const src = img.src || '';
        if (!src || src.startsWith('data:')) return;
        if (src.includes('profile_images') || src.includes('emoji')) return;
        if (img.width <= 80) return;
        if (seen.has(src)) return;
        seen.add(src);
        const i = saved.length;
        const ph = document.createElement('span');
        ph.textContent = ' ___IMG_' + i + '___ ';
        img.replaceWith(ph);
        saved.push({ img, ph, url: src });
      });

      const text = article.innerText;
      saved.forEach(({ img, ph }) => ph.replaceWith(img));
      return JSON.stringify({ text, count: saved.length, urls: saved.map(s => s.url) });
    })()`,
    returnByValue: true,
  });

  const { text: rawText, urls: imageUrls } = JSON.parse(extracted);
  console.log(`Found ${imageUrls.length} images`);

  const fileMap = {};
  for (let i = 0; i < imageUrls.length; i++) {
    const filename = i === 0 ? 'cover.jpg' : `img-${String(i).padStart(2, '0')}.jpg`;
    const dest = path.join(IMAGES_DIR, filename);
    try {
      await downloadFile(imageUrls[i], dest);
      fileMap[i] = filename;
      console.log(`  Downloaded: ${filename}`);
    } catch (err) {
      console.error(`  Failed: img ${i} - ${err.message}`);
    }
  }

  const parts = rawText.split(/\s*___IMG_(\d+)___\s*/);
  const sequence = [];
  for (let i = 0; i < parts.length; i++) {
    if (i % 2 === 0) {
      if (parts[i].trim()) sequence.push({ type: 'text', content: parts[i] });
    } else {
      const idx = parseInt(parts[i], 10);
      if (fileMap[idx]) sequence.push({ type: 'image', file: fileMap[idx] });
    }
  }

  const { result: { value: htmlData } } = await send('Runtime.evaluate', {
    expression: `(() => {
      const article = document.querySelector('main article') || document.body;
      const rawHtml = article.innerHTML;
      const clone = article.cloneNode(true);
      clone.querySelectorAll('*').forEach(el => {
        const keep = ['href', 'src', 'alt', 'type'];
        Array.from(el.attributes).forEach(attr => {
          if (!keep.includes(attr.name)) el.removeAttribute(attr.name);
        });
      });
      clone.querySelectorAll('script, style, noscript').forEach(el => el.remove());
      return JSON.stringify({ rawHtml, cleanHtml: clone.innerHTML });
    })()`,
    returnByValue: true,
  });

  const { rawHtml, cleanHtml } = JSON.parse(htmlData);
  fs.writeFileSync(path.join(OUT_DIR, 'raw.json'), JSON.stringify({ url: ARTICLE_URL, sequence }, null, 2), 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-clean.html'), cleanHtml, 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-raw.html'), rawHtml, 'utf8');

  console.log('Done!');
  console.log(`raw.json: ${path.join(OUT_DIR, 'raw.json')}`);
  console.log(`Images: ${IMAGES_DIR} (${Object.keys(fileMap).length} files)`);
  console.log(`Screenshots: ${SCREENSHOTS_DIR} (${shotIdx} files)`);
  ws.close();
}

main().catch((err) => {
  console.error('Error:', err.stack || err.message || err);
  process.exit(1);
});
