const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:2400,height:1400}});
await p.goto('file://'+path.resolve('sb.html')); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(1500);
await p.screenshot({path:'storyboard-A.png',fullPage:true}); await b.close(); console.log('ok');})();
