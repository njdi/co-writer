// Usage: node open-target.js <article_url> <browser_ws_url>

const [,, ARTICLE_URL, BROWSER_WS_URL] = process.argv;

if (!ARTICLE_URL || !BROWSER_WS_URL) {
  console.error('Usage: node open-target.js <article_url> <browser_ws_url>');
  process.exit(1);
}

let msgId = 1;
const pending = new Map();

const ws = new WebSocket(BROWSER_WS_URL);

function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = msgId++;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
}

ws.addEventListener('message', event => {
  const msg = JSON.parse(event.data);
  if (!msg.id || !pending.has(msg.id)) return;
  const { resolve, reject } = pending.get(msg.id);
  pending.delete(msg.id);
  if (msg.error) reject(new Error(msg.error.message));
  else resolve(msg.result);
});

ws.addEventListener('open', async () => {
  try {
    const result = await send('Target.createTarget', { url: ARTICLE_URL });
    console.log(result.targetId);
    ws.close();
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
});

ws.addEventListener('error', event => {
  console.error(event.message || 'WebSocket error');
  process.exit(1);
});
