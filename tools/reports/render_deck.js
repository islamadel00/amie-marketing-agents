const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('file://'+process.argv[2],{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const ov=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((pg,i)=>{const b=pg.querySelector('.body');if(!b)return null;const over=b.scrollHeight-b.clientHeight;const w=b.scrollWidth-b.clientWidth;return (over>2||w>2)?[i+1,over,w]:null}).filter(Boolean));
console.log('overflow',JSON.stringify(ov));
await p.pdf({path:process.argv[3],width:'1280px',height:'720px',printBackground:true,preferCSSPageSize:true});
const n=await p.evaluate(()=>document.querySelectorAll('.page').length);
for(const i of (process.argv[4]||'').split(',').filter(Boolean)){const el=(await p.$$('.page'))[+i-1];await el.screenshot({path:`shot_${i}.png`});}
await b.close();console.log('pages',n)})();
