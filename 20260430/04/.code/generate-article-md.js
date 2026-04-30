import fs from 'fs';
import path from 'path';

const OUT_DIR = '/Users/miaoyurun/workspace/co-writer/20260430/04';
const raw = JSON.parse(fs.readFileSync(path.join(OUT_DIR, 'raw.json'), 'utf8'));

const title = "Life is a mind game. Here's how you win.";
const authorName = 'DAN KOE';
const handle = 'thedankoe';
const published = '2:00 AM · Apr 27, 2026';
const sourceUrl = raw.url;

const text = raw.sequence
  .filter((item) => item.type === 'text')
  .map((item) => item.content)
  .join('\n');

const lines = text.split('\n').map((line) => line.trim()).filter(Boolean);
const start = lines.indexOf('At some point, usually in your 20s, you’ll notice that the people around you stop believing in themselves. And no matter how hard you try, you can’t save them. By all means, do not let it infect your mind. Stay on your path.');
const end = lines.indexOf('– Dan');
if (start === -1 || end === -1) {
  throw new Error('Could not identify article body boundaries');
}

const headings = new Set([
  'Your mind is a collection of survival strategies, that’s why it’s so hard to change',
  'You can’t escape the mind game, but you can master it',
  '1 – You need a reason with extremely high gravitational pull, and when that one fades, you must find another.',
  '2 – You need to become brutally aware of who you don’t want to become.',
  '3 – You need to change your environment faster than the identity can recalibrate.',
  '4 – You need to increase the gap between impulse and response.',
  'Winning the game is how you discover it’s the wrong game',
]);

const quotes = new Set([
  'At some point, usually in your 20s, you’ll notice that the people around you stop believing in themselves. And no matter how hard you try, you can’t save them. By all means, do not let it infect your mind. Stay on your path.',
  'Everything is a religion. Your morning routine is a religion. Your political opinions are a religion. Your identity as a gamer, a lifter, a minimalist, a stoic, a craft beer enthusiast... all religions. With social media and global access to information, we’re experiencing the religionization of everything. Very few people actually do things because they want to anymore. Almost everyone’s life is built around actions that allows them to fit into the digital tribe.',
  'Effortless self discipline happens when the desire to become the highest version of yourself outweighs the desires of the lowest version of yourself.',
  'If you want to change your life fast, the most useful thing you can do is immerse your mind in the environment of your future self. Bathe your psyche in the opinions, beliefs, and education that person would have without judgement.',
  'Break the pattern today, or you will repeat the loop tomorrow.',
  'The greatest trait you can acquire is to work with tremendous intensity on things that matter to you, and more importantly, be strangely unbothered when those things don’t work out.',
]);

function formatLine(line) {
  if (headings.has(line)) return `## ${line}`;
  if (quotes.has(line)) return `> ${line}`;
  if (line.startsWith('Physical survival – ')) return `1. **Physical survival** – ${line.slice('Physical survival – '.length)}`;
  if (line.startsWith('Psychological/conceptual survival – ')) return `2. **Psychological/conceptual survival** – ${line.slice('Psychological/conceptual survival – '.length)}`;
  return line.replace('$100m', '\\$100m');
}

const body = lines.slice(start, end + 1).map(formatLine).join('\n\n');
const markdown = [
  `# ${title}`,
  '',
  `**Author:** ${authorName} ([@${handle}](https://x.com/${handle}))  `,
  `**Published:** ${published}  `,
  `**Source:** [${title}](${sourceUrl})`,
  '',
  body,
  '',
].join('\n');

fs.writeFileSync(path.join(OUT_DIR, 'article.md'), markdown, 'utf8');
