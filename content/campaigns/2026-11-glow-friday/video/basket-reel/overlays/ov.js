const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve('ov.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(1500);
for (const k of await p.evaluate(()=>keys)){ await p.evaluate(k=>show(k),k); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(150);
 await p.screenshot({path:`ov/${k}.png`,omitBackground:true}); }
await b.close(); console.log('ov ok');})();
