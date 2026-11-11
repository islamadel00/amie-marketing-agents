const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:2400,height:1560}});
for (const d of ['A','B']){ await p.goto('file://'+path.resolve('board.html')+'?d='+d); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(1500);
 await p.screenshot({path:`moodboard-${d}.png`}); }
await b.close(); console.log('ok');})();
