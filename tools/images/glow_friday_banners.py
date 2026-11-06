"""Glow Friday banners: Higgsfield B&W backgrounds + live typography (discount is a parameter).
Usage: python3 glow_friday_banners.py <banners_dir> [discount=20]   (renders with node + playwright)
Writes <banners_dir>/glow-friday-<name>-<discount>.png (1080x1350) and moodboard.png."""
import sys, os, json, subprocess
D = os.path.abspath(sys.argv[1]); P = sys.argv[2] if len(sys.argv) > 2 else '20'
ROSE, INK = '#8E5A55', '#141414'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
BASE = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;font-family:'IBM Plex Sans Arabic',sans-serif;color:{INK}}}
.bg{{position:absolute;inset:0;background-size:cover;background-position:center bottom}} .logo{{position:absolute;height:46px}}
.num{{font-family:'Cormorant Garamond',serif;font-weight:600;line-height:.85;letter-spacing:-4px}} .ar{{direction:rtl}}
.eyebrow{{font-family:Inter;font-weight:500;letter-spacing:.45em;font-size:20px}} .pill{{display:inline-block;border:1.5px solid {INK};border-radius:40px;padding:12px 34px;font-size:26px}}"""

def a(bg):   # Forte style: huge number centred, eyebrow bar
    return f"""<div class=bg style="background-image:url('src/{bg}')"></div>
<img class=logo src="src/logo-dark.png" style="top:56px;left:50%;transform:translateX(-50%)">
<div style="position:absolute;top:126px;width:100%;text-align:center">
 <div class=eyebrow style="display:inline-block;background:{INK};color:#fff;padding:12px 26px 12px 34px">GLOW FRIDAY</div>
 <div style="display:flex;justify-content:center;align-items:flex-end;gap:22px;margin-top:26px">
  <div class=num style="font-size:250px">{P}%</div>
  <div class=ar style="font-size:60px;font-weight:600;padding-bottom:28px">خصم</div></div>
 <div class=ar style="font-size:32px;margin-top:0">على منتجات مختارة فقط</div></div>"""

def b(bg):   # Gisou style: headline left/right, bottom bar
    return f"""<div class=bg style="background-image:url('src/{bg}')"></div>
<img class=logo src="src/logo-dark.png" style="top:56px;left:50%;transform:translateX(-50%)">
<div style="position:absolute;top:150px;width:100%;display:flex;justify-content:center;align-items:center;gap:34px">
 <div class=num style="font-size:190px">{P}%</div>
 <div class=ar style="text-align:right"><div style="font-size:58px;font-weight:600;line-height:1.15">خصم Glow Friday</div>
 <div style="font-size:32px;margin-top:8px">على منتجات مختارة فقط</div></div></div>
<div class=ar style="position:absolute;bottom:0;width:100%;height:120px;background:{INK};color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;gap:18px">
 <span>مجموعة الليمون قراس</span><span style="color:{ROSE}">●</span><span style="font-family:Inter;letter-spacing:.2em;font-size:22px">AMIE-SA.COM</span></div>"""

def c(bg):   # editorial: eyebrow, number, pill
    return f"""<div class=bg style="background-image:url('src/{bg}')"></div>
<img class=logo src="src/logo-dark.png" style="top:56px;left:72px">
<div class=eyebrow style="position:absolute;top:70px;right:72px;color:{ROSE}">GLOW FRIDAY</div>
<div style="position:absolute;top:140px;left:72px">
 <div class=num style="font-size:200px">{P}<span style="font-size:120px">%</span></div>
 <div class=ar style="font-size:40px;font-weight:600;margin-top:6px;text-align:left">خصم على مجموعة الشعر</div>
 <div class=ar style="font-size:26px;margin-top:4px;text-align:left;color:#444">منتجات مختارة فقط · لفترة محدودة</div></div>"""

BANNERS = [('scrub-butter', a, 'bg-scrub-butter.png'), ('lemongrass-set', b, 'bg-lemongrass-set.png'), ('hair-set', c, 'bg-hair-set.png')]

def page(body, w=1080, h=1350, extra=''):
    return f"<!doctype html><html><head><meta charset=utf-8>{FONTS}<style>{BASE} body{{width:{w}px;height:{h}px}} {extra}</style></head><body>{body}</body></html>"

def moodboard(files):
    sw = [(ROSE, 'Rose ribbon · #8E5A55'), (INK, 'Ink · #141414'), ('#F4F3F1', 'Paper · #F4F3F1'), ('#BEBEBE', 'Studio grey · #BEBEBE'), ('linear-gradient(135deg,#f4f4f4,#a9a9a9 45%,#ececec 60%,#8d8d8d)', 'Silver foil · text on ribbon')]
    sws = ''.join(f'<div style="flex:1"><div style="height:120px;border-radius:14px;background:{c};border:1px solid #ddd"></div><div style="font:500 17px Inter;margin-top:10px">{t}</div></div>' for c, t in sw)
    refs = ''.join(f'<img src="src/{r}" style="height:300px;border-radius:12px;object-fit:cover">' for r in ['ref-bow.png', 'ref-ribbon-wrap.png', 'ref-ribbon-colour.png'])
    ban = ''.join(f'<img src="{f}" style="width:520px;border-radius:12px;box-shadow:0 8px 30px rgba(0,0,0,.12)">' for f in files)
    body = f"""<div style="padding:70px 80px;background:#F4F3F1;height:100%">
 <div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class=eyebrow style="color:{ROSE}">a'mie · MOODBOARD</div>
 <div style="font:600 76px 'Cormorant Garamond';margin-top:10px">Glow Friday</div></div>
 <div class=ar style="font-size:24px;max-width:700px;text-align:right;line-height:1.6">تصوير أبيض وأسود، والشريطة بس بلون a'mie الوردي الساتان ومكتوب عليها GLOW FRIDAY بالفضي. نسبة الخصم تتغيّر حسب قرار صالح، ونكتب دايماً «على منتجات مختارة فقط».</div></div>
 <div style="display:flex;gap:28px;margin-top:44px">{sws}</div>
 <div style="font:500 18px Inter;letter-spacing:.3em;margin:46px 0 16px">REFERENCES</div><div style="display:flex;gap:22px">{refs}</div>
 <div style="font:500 18px Inter;letter-spacing:.3em;margin:46px 0 16px">TYPE</div>
 <div style="display:flex;gap:60px;align-items:flex-end"><div class=num style="font-size:120px">{P}%</div><div style="font:600 46px 'IBM Plex Sans Arabic'" class=ar>خصم على منتجات مختارة فقط</div><div class=eyebrow>GLOW FRIDAY</div></div>
 <div style="font:500 18px Inter;letter-spacing:.3em;margin:46px 0 16px">BANNERS</div><div style="display:flex;gap:30px">{ban}</div></div>"""
    return page(body, 1800, 1880)

RENDER = """const {chromium}=require('playwright');(async()=>{const jobs=JSON.parse(process.argv[2]);const b=await chromium.launch();
for(const [h,o,w,ht] of jobs){const p=await b.newPage({viewport:{width:w,height:ht}});await p.goto('file://'+h,{waitUntil:'networkidle'});await p.waitForTimeout(800);await p.screenshot({path:o});await p.close();}await b.close();})();"""

def render(jobs):
    js = os.path.join(D, '_render.js'); open(js, 'w').write(RENDER)
    subprocess.run(['node', js, json.dumps(jobs)], check=True, cwd='/tmp'); os.remove(js)
    for h, *_ in jobs: os.remove(h)

out, jobs = [], []
for name, fn, bg in BANNERS:
    h = os.path.join(D, f'_{name}.html'); open(h, 'w', encoding='utf-8').write(page(fn(bg)))
    f = f'glow-friday-{name}-{P}.png'; out.append(f); jobs.append([h, os.path.join(D, f), 1080, 1350])
render(jobs)
h = os.path.join(D, '_mood.html'); open(h, 'w', encoding='utf-8').write(moodboard(out))
render([[h, os.path.join(D, f'moodboard-{P}.png'), 1800, 1880]]); print(out)
