const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({args:['--allow-file-access-from-files']});
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2], {waitUntil:'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: process.argv[3], format:'A4', printBackground:true, preferCSSPageSize:true,
    displayHeaderFooter:true, headerTemplate:'<div></div>',
    footerTemplate:'<div style="width:100%;font-size:7px;color:#999;padding:0 13mm;display:flex;justify-content:space-between;font-family:sans-serif"><span>a\'mie · Internal · Nov 2026</span><span class="pageNumber"></span></div>'});
  for (const n of [1,2,3,5,6,7]) {}
  await b.close();
})();
