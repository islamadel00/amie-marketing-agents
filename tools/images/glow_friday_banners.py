"""Glow Friday banners: Higgsfield B&W backgrounds + live typography (discount is a parameter).
Usage: python3 glow_friday_banners.py <banners_dir> [discount=20]   (renders with node + playwright)
Writes <banners_dir>/glow-friday-<name>-<discount>.png (1080x1350) and moodboard.png."""
import sys, os, json, subprocess
D = os.path.abspath(sys.argv[1]); P = sys.argv[2] if len(sys.argv) > 2 else '20'
ROSE, INK = '#8E5A55', '#141414'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=IBM+Plex+Sans+Arabic:wght@300;400;500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">'
FOIL = "background:linear-gradient(100deg,#3c3c3c 0%,#9b9b9b 20%,#4a4a4a 38%,#c4c4c4 55%,#454545 75%,#8e8e8e 100%);-webkit-background-clip:text;background-clip:text;color:transparent"
GRAIN = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")"
BASE = f"""*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;font-family:'IBM Plex Sans Arabic',sans-serif;color:{INK};position:relative}}
.bg{{position:absolute;inset:0;background-size:cover;background-position:center bottom}}
.fx{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.10) 100%),{GRAIN};opacity:.32;mix-blend-mode:multiply}}
.frame{{position:absolute;inset:30px;border:1px solid rgba(20,20,20,.28)}}
.logo{{position:absolute;height:38px;top:70px;left:50%;transform:translateX(-50%)}}
.num{{font-family:'Cormorant Garamond',serif;font-weight:500;line-height:.82;letter-spacing:-3px}} .ar{{direction:rtl}}
.foil{{font-family:Inter;font-weight:500;letter-spacing:.55em;font-size:19px;{FOIL};filter:drop-shadow(0 1px 0 rgba(255,255,255,.6))}}
.rule{{display:flex;align-items:center;justify-content:center;gap:22px}} .rule i{{display:block;width:70px;height:1px;background:linear-gradient(90deg,transparent,#8d8d8d,transparent)}}
.eye{{font-family:Inter;font-weight:500;letter-spacing:.55em;font-size:19px;color:#1c1c1c}}
.sub{{font-weight:300;font-size:30px;letter-spacing:.01em}}"""

def shell(bg, inner):
    return f"""<div class=bg style="background-image:url('src/{bg}')"></div><div class=fx></div><div class=frame></div>
<img class=logo src="src/logo-dark.png">{inner}"""

def a(bg):   # centred number, foil eyebrow
    return shell(bg, f"""<div style="position:absolute;top:150px;width:100%;text-align:center">
 <div class=rule><i></i><span class=eye>GLOW FRIDAY</span><i></i></div>
 <div class=num style="font-size:230px;margin-top:30px">{P}%</div>
 <div class="ar sub" style="margin-top:18px">خصم على منتجات مختارة فقط</div></div>""")

def b(bg):   # number + line side by side, slim foil footer
    return shell(bg, f"""<div style="position:absolute;top:160px;width:100%;text-align:center"><div class=rule><i></i><span class=foil>GLOW FRIDAY</span><i></i></div></div>
<div style="position:absolute;top:220px;width:100%;display:flex;justify-content:center;align-items:center;gap:40px">
 <div class=num style="font-size:170px">{P}%</div><div style="width:1px;height:110px;background:#9a9a9a"></div>
 <div class=ar style="text-align:right"><div style="font-size:44px;font-weight:400">خصم</div><div class=sub style="font-size:28px;margin-top:4px">على منتجات مختارة فقط</div></div></div>
<div style="position:absolute;bottom:30px;left:30px;right:30px;height:92px;background:{INK};display:flex;align-items:center;justify-content:center;gap:20px">
 <span class=foil style="font-size:17px;background:linear-gradient(100deg,#9a9a9a,#f2f2f2 35%,#a8a8a8 60%,#e6e6e6);-webkit-background-clip:text;background-clip:text;filter:none">AMIE-SA.COM</span></div>""")

def c(bg):   # left editorial
    return shell(bg, f"""<div style="position:absolute;top:128px;left:90px">
 <div class=eye style="letter-spacing:.5em">GLOW FRIDAY</div>
 <div class=num style="font-size:165px;margin-top:22px">{P}%</div>
 <div class=ar style="font-size:34px;font-weight:400;margin-top:10px;text-align:left">خصم على مجموعة الشعر</div>
 <div class="ar sub" style="font-size:23px;margin-top:2px;text-align:left;color:#3a3a3a">منتجات مختارة فقط · لفترة محدودة</div></div>""")

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
