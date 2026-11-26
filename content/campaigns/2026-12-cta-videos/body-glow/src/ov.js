const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve('ov.html')); await p.waitForTimeout(800);
for (const k of ['b1','b2','b3','b4','mask','end']){ await p.evaluate(k=>show(k),k); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
 await p.screenshot({path:`${k}.png`,omitBackground:k==='mask'}); }
await b.close(); console.log('ov ok');})();
