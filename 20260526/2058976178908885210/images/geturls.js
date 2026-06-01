const { execSync } = require('child_process');
const fs = require('fs');

const lines = fs.readFileSync('./tokens.txt','utf8').trim().split('\n');
const fileTokenMap = {};
lines.forEach(l => { const [f,t]=l.trim().split(' '); if(f&&t) fileTokenMap[f]=t; });

function getUrls(tokens){
  const urlMap={}; const BATCH=5;
  for(let i=0;i<tokens.length;i+=BATCH){
    const batch=tokens.slice(i,i+BATCH);
    const params=JSON.stringify({file_tokens:batch});
    const raw=execSync(`lark-cli api GET /open-apis/drive/v1/medias/batch_get_tmp_download_url --params '${params}' 2>/dev/null`,{encoding:'utf8'});
    const result=JSON.parse(raw);
    (result.data.tmp_download_urls||[]).forEach(({file_token,tmp_download_url})=>{ urlMap[file_token]=tmp_download_url; });
  }
  return urlMap;
}

const urlMap=getUrls(Object.values(fileTokenMap));

const mdPath='../article-replica.md';
let md=fs.readFileSync(mdPath,'utf8');
let n=0;
Object.entries(fileTokenMap).forEach(([filename,token])=>{
  const url=urlMap[token];
  if(url){ const before=md; md=md.replaceAll(`images/${filename}`,url); if(md!==before) n++; }
  else console.error('NO URL for',filename);
});
fs.writeFileSync(mdPath,md,'utf8');
console.log('replaced',n,'image refs');
