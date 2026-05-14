// 通过浏览器级 CDP 打开新标签页并导航到目标 URL，返回页面 WebSocket 地址
import { URL } from 'url';

const BROWSER_WS = process.argv[2];
const TARGET_URL = process.argv[3];

const ws = new WebSocket(BROWSER_WS);
let msgId = 1;
const pending = new Map();

await new Promise((resolve, reject) => {
  ws.addEventListener('open', resolve);
  ws.addEventListener('error', (e) => reject(new Error(e.message || 'WS error')));
});

ws.addEventListener('message', (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    const { resolve, reject } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) reject(new Error(msg.error.message));
    else resolve(msg.result);
  }
});

const send = (method, params = {}) => new Promise((resolve, reject) => {
  const id = msgId++;
  pending.set(id, { resolve, reject });
  ws.send(JSON.stringify({ id, method, params }));
});

// 创建新标签页
const { targetId } = await send('Target.createTarget', { url: TARGET_URL });
console.log('targetId:', targetId);

// 获取页面列表找到对应的 WebSocket 地址
await new Promise(r => setTimeout(r, 1000));

const http = await import('http');
const data = await new Promise((resolve, reject) => {
  http.default.get('http://localhost:9222/json/list', (res) => {
    let body = '';
    res.on('data', chunk => body += chunk);
    res.on('end', () => resolve(JSON.parse(body)));
    res.on('error', reject);
  });
});

const page = data.find(p => p.id === targetId);
if (page) {
  console.log('wsUrl:', page.webSocketDebuggerUrl);
} else {
  console.error('Page not found in list');
}

ws.close();
