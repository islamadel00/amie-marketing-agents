// node render_glow_hero.js <layout mobile|desktop> <text 1|0> <out.mp4>
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const [layout, text, out] = process.argv.slice(2);
  const size = (layout === 'desktop' || layout === 'desktoplight') ? { width: 1920, height: 1080 } : layout === 'slider' ? { width: 1080, height: 1620 } : { width: 720, height: 1280 };
  const scale = layout === 'mobile' ? 1.5 : 1;               // mobile out = 1080x1920
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: size, deviceScaleFactor: scale });
  await p.goto('file://' + path.resolve(__dirname, 'glow_hero.html') + `?layout=${layout}&text=${text}`);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
  const fps = 30, n = 6 * fps;
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '21', '-preset', 'slow', '-movflags', '+faststart', '-an', out]);
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => render(t), i / fps);
    const buf = await p.screenshot({ type: 'png' });
    if (i === 0) require('fs').writeFileSync(out.replace(/\.mp4$/, '-poster.jpg.png'), buf);
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('done', out);
})();
