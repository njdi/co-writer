// save-x-article.js
// Usage: node save-x-article.js <article_url> <ws_url> <out_dir>
// Requires Node.js >= 21 (built-in WebSocket).

import https from 'https';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { URL } from 'url';
import net from 'net';
import crypto from 'crypto';
import { EventEmitter } from 'events';

const [,, ARTICLE_URL, WS_URL, OUT_DIR_ARG] = process.argv;
if (!ARTICLE_URL || !WS_URL || !OUT_DIR_ARG) {
  console.error('Usage: node save-x-article.js <article_url> <ws_url> <out_dir>');
  process.exit(1);
}

const STATUS_ID = ARTICLE_URL.match(/\/status\/(\d+)/)?.[1];
if (!STATUS_ID) {
  console.error('Cannot parse status ID:', ARTICLE_URL);
  process.exit(1);
}

const OUT_DIR = OUT_DIR_ARG;
const IMAGES_DIR = path.join(OUT_DIR, 'images');
const SCREENSHOTS_DIR = path.join(OUT_DIR, 'screenshots');

let msgId = 1;
const pending = new Map();
const eventWaiters = new Map();

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
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
    }, res => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        file.close();
        fs.unlinkSync(dest);
        return downloadFile(res.headers.location, dest).then(resolve).catch(reject);
      }
      if (res.statusCode && res.statusCode >= 400) {
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
    req.on('error', err => {
      fs.unlink(dest, () => {});
      reject(err);
    });
  });
}

function encodeFrame(text) {
  const payload = Buffer.from(text);
  const mask = crypto.randomBytes(4);
  let header;
  if (payload.length < 126) {
    header = Buffer.alloc(2);
    header[1] = 0x80 | payload.length;
  } else if (payload.length < 65536) {
    header = Buffer.alloc(4);
    header[1] = 0x80 | 126;
    header.writeUInt16BE(payload.length, 2);
  } else {
    header = Buffer.alloc(10);
    header[1] = 0x80 | 127;
    header.writeBigUInt64BE(BigInt(payload.length), 2);
  }
  header[0] = 0x81;
  const masked = Buffer.alloc(payload.length);
  for (let i = 0; i < payload.length; i++) masked[i] = payload[i] ^ mask[i % 4];
  return Buffer.concat([header, mask, masked]);
}

function createCdpSocket(wsUrl) {
  const parsed = new URL(wsUrl);
  const emitter = new EventEmitter();
  const socket = net.createConnection({
    host: parsed.hostname,
    port: Number(parsed.port || 80),
  });
  let buffer = Buffer.alloc(0);
  let handshakeDone = false;
  let continuation = [];

  socket.on('connect', () => {
    const key = crypto.randomBytes(16).toString('base64');
    socket.write([
      `GET ${parsed.pathname}${parsed.search} HTTP/1.1`,
      `Host: ${parsed.host}`,
      'Upgrade: websocket',
      'Connection: Upgrade',
      `Sec-WebSocket-Key: ${key}`,
      'Sec-WebSocket-Version: 13',
      '',
      '',
    ].join('\r\n'));
  });

  socket.on('data', chunk => {
    buffer = Buffer.concat([buffer, chunk]);
    if (!handshakeDone) {
      const end = buffer.indexOf('\r\n\r\n');
      if (end === -1) return;
      const header = buffer.slice(0, end).toString('utf8');
      if (!header.includes(' 101 ')) {
        emitter.emit('error', new Error(header.split('\r\n')[0]));
        socket.destroy();
        return;
      }
      handshakeDone = true;
      buffer = buffer.slice(end + 4);
      emitter.emit('open');
    }

    while (buffer.length >= 2) {
      const first = buffer[0];
      const second = buffer[1];
      const fin = Boolean(first & 0x80);
      const opcode = first & 0x0f;
      const masked = Boolean(second & 0x80);
      let offset = 2;
      let length = second & 0x7f;
      if (length === 126) {
        if (buffer.length < offset + 2) return;
        length = buffer.readUInt16BE(offset);
        offset += 2;
      } else if (length === 127) {
        if (buffer.length < offset + 8) return;
        length = Number(buffer.readBigUInt64BE(offset));
        offset += 8;
      }
      let mask;
      if (masked) {
        if (buffer.length < offset + 4) return;
        mask = buffer.slice(offset, offset + 4);
        offset += 4;
      }
      if (buffer.length < offset + length) return;
      let payload = buffer.slice(offset, offset + length);
      buffer = buffer.slice(offset + length);
      if (masked) {
        const unmasked = Buffer.alloc(payload.length);
        for (let i = 0; i < payload.length; i++) unmasked[i] = payload[i] ^ mask[i % 4];
        payload = unmasked;
      }
      if (opcode === 0x8) {
        socket.end();
        emitter.emit('close');
        return;
      }
      if (opcode === 0x9) {
        socket.write(Buffer.from([0x8a, 0x00]));
        continue;
      }
      if (opcode === 0x1 || opcode === 0x0) {
        continuation.push(payload);
        if (fin) {
          emitter.emit('message', Buffer.concat(continuation).toString('utf8'));
          continuation = [];
        }
      }
    }
  });

  socket.on('error', err => emitter.emit('error', err));
  socket.on('close', () => emitter.emit('close'));

  return {
    on: (...args) => emitter.on(...args),
    send: text => socket.write(encodeFrame(text)),
    close: () => socket.end(),
  };
}

async function main() {
  console.log('Connecting to Chrome CDP...');
  const ws = createCdpSocket(WS_URL);

  await new Promise((resolve, reject) => {
    ws.on('open', resolve);
    ws.on('error', reject);
  });

  ws.on('message', data => {
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
  });

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = msgId++;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });

  const waitEvent = (eventName, timeout = 20000) => new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`Timeout: ${eventName}`)), timeout);
    eventWaiters.set(eventName, params => {
      clearTimeout(timer);
      resolve(params);
    });
  });

  await send('Page.enable');
  await send('Runtime.enable');

  console.log('Navigating to article...');
  await send('Page.navigate', { url: ARTICLE_URL });
  await waitEvent('Page.loadEventFired');
  console.log('Page loaded, waiting for React render...');
  await sleep(5000);

  console.log('Scrolling and taking screenshots...');
  fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

  const { result: { value: pageInfo } } = await send('Runtime.evaluate', {
    expression: `({ scrollHeight: document.body.scrollHeight, viewHeight: window.innerHeight })`,
    returnByValue: true,
  });

  const step = Math.floor(pageInfo.viewHeight * 0.8);
  let pos = 0;
  let shotIdx = 0;

  while (pos < pageInfo.scrollHeight) {
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

  await send('Runtime.evaluate', { expression: `window.scrollTo(0, 0)`, returnByValue: true });
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

  fs.mkdirSync(IMAGES_DIR, { recursive: true });
  console.log('Downloading images...');
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
      const idx = Number.parseInt(parts[i], 10);
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
      const cleanHtml = clone.innerHTML;
      return JSON.stringify({ rawHtml, cleanHtml });
    })()`,
    returnByValue: true,
  });

  const { rawHtml, cleanHtml } = JSON.parse(htmlData);

  fs.writeFileSync(path.join(OUT_DIR, 'raw.json'), JSON.stringify({ url: ARTICLE_URL, sequence }, null, 2), 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-clean.html'), cleanHtml, 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-raw.html'), rawHtml, 'utf8');

  console.log('\\nDone!');
  console.log(`raw.json:           ${OUT_DIR}/raw.json`);
  console.log(`article-clean.html: ${OUT_DIR}/article-clean.html`);
  console.log(`article-raw.html:   ${OUT_DIR}/article-raw.html`);
  console.log(`Images:             ${IMAGES_DIR}/ (${Object.keys(fileMap).length} files)`);
  console.log(`Screenshots:        ${SCREENSHOTS_DIR}/ (${shotIdx} files)`);

  ws.close();
}

main().catch(err => {
  console.error('Error:', err?.stack || err?.message || String(err));
  process.exit(1);
});
