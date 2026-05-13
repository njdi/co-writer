// save-x-article.js
// 用法: node save-x-article.js <article_url> <ws_url>
// 依赖: Node.js >= 21 (内置 WebSocket，无需第三方包)

import https from 'https';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { URL } from 'url';

const [,, ARTICLE_URL, WS_URL, OUT_DIR_ARG] = process.argv;
if (!ARTICLE_URL || !WS_URL) {
  console.error('用法: node save-x-article.js <article_url> <ws_url> [out_dir]');
  process.exit(1);
}

const STATUS_ID = ARTICLE_URL.match(/\/status\/(\d+)/)?.[1];
if (!STATUS_ID) {
  console.error('无法从 URL 中解析 status ID:', ARTICLE_URL);
  process.exit(1);
}

const OUT_DIR = OUT_DIR_ARG || `/tmp/${STATUS_ID}`;
const IMAGES_DIR = path.join(OUT_DIR, 'images');
const SCREENSHOTS_DIR = path.join(OUT_DIR, 'screenshots');

let msgId = 1;
const pending = new Map();
const eventWaiters = new Map();

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    url = url.replace(/name=(small|medium|orig)/, 'name=large');
    const parsed = new URL(url);
    const client = parsed.protocol === 'https:' ? https : http;
    const file = fs.createWriteStream(dest);
    const req = client.get(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://x.com/',
      }
    }, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        file.close();
        fs.unlinkSync(dest);
        return downloadFile(res.headers.location, dest).then(resolve).catch(reject);
      }
      res.pipe(file);
      file.on('finish', () => { file.close(); resolve(); });
    });
    req.on('error', (err) => { fs.unlink(dest, () => {}); reject(err); });
  });
}

async function main() {
  console.log('Connecting to Chrome CDP...');
  const ws = new WebSocket(WS_URL);

  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve);
    ws.addEventListener('error', (e) => reject(new Error(e.message || 'WebSocket error')));
  });

  ws.addEventListener('message', (event) => {
    const msg = JSON.parse(event.data);
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
    eventWaiters.set(eventName, (params) => { clearTimeout(timer); resolve(params); });
  });

  await send('Page.enable');
  await send('Runtime.enable');

  // 导航到文章
  console.log('Navigating to article...');
  await send('Page.navigate', { url: ARTICLE_URL });
  await waitEvent('Page.loadEventFired');
  console.log('Page loaded, waiting for React render...');
  await sleep(4000);

  // 滚动触发懒加载，同时截图
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
    await sleep(300);

    const shot = await send('Page.captureScreenshot', { format: 'jpeg', quality: 80 });
    const shotFile = path.join(SCREENSHOTS_DIR, `shot-${String(shotIdx).padStart(2, '0')}.jpg`);
    fs.writeFileSync(shotFile, Buffer.from(shot.data, 'base64'));
    shotIdx++;
    pos += step;
  }

  await send('Runtime.evaluate', { expression: `window.scrollTo(0, 0)`, returnByValue: true });
  console.log(`Screenshots: ${shotIdx} captured`);
  await sleep(2000);

  // 提取文字与图片的交替序列（保留图片在正文中的原始位置）
  const { result: { value: extracted } } = await send('Runtime.evaluate', {
    expression: `(() => {
      const article = document.querySelector('main article') || document.body;
      const seen = new Set();
      const saved = [];

      // 找到所有符合条件的图片，替换为占位符
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

      // 获取包含占位符的文本
      const text = article.innerText;

      // 还原 DOM
      saved.forEach(({ img, ph }) => ph.replaceWith(img));

      return JSON.stringify({ text, count: saved.length, urls: saved.map(s => s.url) });
    })()`,
    returnByValue: true,
  });

  const { text: rawText, urls: imageUrls } = JSON.parse(extracted);
  console.log(`Found ${imageUrls.length} images`);

  // 下载图片
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
      console.error(`  Failed: img ${i} — ${err.message}`);
    }
  }

  // 按占位符分割，构建文字与图片的交替序列
  const parts = rawText.split(/\s*___IMG_(\d+)___\s*/);
  const sequence = [];
  for (let i = 0; i < parts.length; i++) {
    if (i % 2 === 0) {
      if (parts[i].trim()) sequence.push({ type: 'text', content: parts[i] });
    } else {
      const idx = parseInt(parts[i]);
      if (fileMap[idx]) sequence.push({ type: 'image', file: fileMap[idx] });
    }
  }

  // 提取 HTML（原始 + 清洗后的语义版本）
  const { result: { value: htmlData } } = await send('Runtime.evaluate', {
    expression: `(() => {
      const article = document.querySelector('main article') || document.body;
      const rawHtml = article.innerHTML;

      // 清洗 HTML：只保留语义标签，去掉所有 class/style/data-*/aria-* 属性
      const clone = article.cloneNode(true);
      clone.querySelectorAll('*').forEach(el => {
        const keep = ['href', 'src', 'alt', 'type'];
        Array.from(el.attributes).forEach(attr => {
          if (!keep.includes(attr.name)) el.removeAttribute(attr.name);
        });
      });
      // 移除 script/style 节点
      clone.querySelectorAll('script, style, noscript').forEach(el => el.remove());
      const cleanHtml = clone.innerHTML;

      return JSON.stringify({ rawHtml, cleanHtml });
    })()`,
    returnByValue: true,
  });

  const { rawHtml, cleanHtml } = JSON.parse(htmlData);

  // 写入所有原始数据文件
  const raw = { url: ARTICLE_URL, sequence };
  fs.writeFileSync(path.join(OUT_DIR, 'raw.json'), JSON.stringify(raw, null, 2), 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-clean.html'), cleanHtml, 'utf8');
  fs.writeFileSync(path.join(OUT_DIR, 'article-raw.html'), rawHtml, 'utf8');

  console.log(`\nDone!`);
  console.log(`raw.json:           ${OUT_DIR}/raw.json`);
  console.log(`article-clean.html: ${OUT_DIR}/article-clean.html`);
  console.log(`article-raw.html:   ${OUT_DIR}/article-raw.html`);
  console.log(`Images:             ${IMAGES_DIR}/ (${Object.keys(fileMap).length} files)`);
  console.log(`Screenshots:        ${SCREENSHOTS_DIR}/ (${shotIdx} files)`);

  ws.close();
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
