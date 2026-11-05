"""a'mie-identity vertical video ads (720x1280), modelled on a'mie's own Snap ads (AM2610-0xx):
footage on top, smoky-white panel at the bottom with a taupe Arabic headline, grey sub-line and a taupe
«اطلبي الآن» pill; handwritten English accent (Reenie Beanie) over the footage; a'mie end card.
Usage: python3 -I amie_style_video.py <workdir> <spec.json>
spec: {name, suffix, clips:[[src,start,dur]], states:[[headline, sub, t0, t1]], script, card:{bundle, items, price, note, dates}}"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

WD, SPEC = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
FONTS = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/fonts'
LOGO = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/brand/logo.png'
AR_B, AR_R, SCRIPT = f'{FONTS}/ReadexPro-AR-Bold.ttf', f'{FONTS}/ReadexPro-AR-Regular.ttf', f'{FONTS}/ReenieBeanie.ttf'
W, H, VH = 720, 1280, 990          # footage height; panel below
PANEL, TAUPE, GREY, INK = (247, 247, 245), '#7A6957', '#8C8782', '#191919'
TAG = 'setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709'
OUTTAG = ['-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709']
name = SPEC['name']; D = f'{WD}/{name}'; os.makedirs(D, exist_ok=True)

def run(cmd): subprocess.run(cmd, check=True, stdin=subprocess.DEVNULL)
def font(p, s): return ImageFont.truetype(p, s, layout_engine=ImageFont.Layout.RAQM)
def ar_center(d, y, txt, f, fill, maxw=W - 80):
    l, t, r, b = d.textbbox((0, 0), txt, font=f, direction='rtl', language='ar')
    d.text(((W - (r - l)) / 2 - l, y - t), txt, font=f, fill=fill, direction='rtl', language='ar')
def fit(txt, path, size, maxw):
    d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    while size > 22:
        f = font(path, size); l, t, r, b = d.textbbox((0, 0), txt, font=f, direction='rtl', language='ar')
        if r - l <= maxw: return f
        size -= 2
    return font(path, size)
def pill(d, cx, y, txt, fill, color, f, padx=34, h=56):
    l, t, r, b = d.textbbox((0, 0), txt, font=f, direction='rtl', language='ar'); tw = r - l
    d.rounded_rectangle((cx - tw / 2 - padx, y, cx + tw / 2 + padx, y + h), radius=h // 2, fill=fill)
    d.text((cx - tw / 2 - l, y + (h - (b - t)) / 2 - t), txt, font=f, fill=color, direction='rtl', language='ar')

def panel_png(path, head, sub):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((0, VH, W, H), fill=PANEL)
    ar_center(d, VH + 42, head, fit(head, AR_B, 40, W - 90), TAUPE)
    if sub: ar_center(d, VH + 108, sub, fit(sub, AR_R, 28, W - 100), GREY)
    pill(d, W / 2, VH + 172, 'اطلبي الآن', TAUPE, 'white', font(AR_B, 28))
    im.save(path)

def script_png(path, txt):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); lay = Image.new('RGBA', (W, 220), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = ImageFont.truetype(SCRIPT, 80); tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2 + 2, 52), txt, font=f, fill=(0, 0, 0, 90)); d.text(((W - tw) / 2, 50), txt, font=f, fill=(255, 255, 255, 255))
    lay = lay.rotate(5, resample=Image.BICUBIC); im.alpha_composite(lay, (0, 70)); im.save(path)

def card_png(path, c):
    # minimal end card: script, logo, bundle name, quiet price line, dates, CTA
    im = Image.new('RGB', (W, H), PANEL); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(SCRIPT, 84); tw = d.textlength('Glow Friday', font=f); d.text(((W - tw) / 2, 330), 'Glow Friday', font=f, fill=INK)
    lg = Image.open(LOGO).convert('RGBA'); lw = 240; lg = lg.resize((lw, int(lg.height * lw / lg.width))); im.paste(lg, ((W - lw) // 2, 470), lg)
    ar_center(d, 625, c['bundle'], fit(c['bundle'], AR_B, 38, W - 120), TAUPE)
    ar_center(d, 690, c['price_line'], font(AR_R, 28), GREY)
    ar_center(d, 740, c['dates'], font(AR_R, 24), GREY)
    pill(d, W / 2, 815, 'اطلبي الآن', TAUPE, 'white', font(AR_B, 26), h=54)
    tw = d.textlength('amie-sa.com', font=font(f'{FONTS}/Montserrat-Light.ttf', 22))
    d.text(((W - tw) / 2, 905), 'amie-sa.com', font=font(f'{FONTS}/Montserrat-Light.ttf', 22), fill=GREY)
    im.save(path)

# footage segments -> 720x1280 (footage area is the top VH px)
segs = []
for i, (src, a, dur) in enumerate(SPEC['clips']):
    o = f'{D}/c{i}.mp4'
    if not os.path.exists(o):
        tr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=color_transfer', '-of', 'csv=p=0', src],
                            capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
        vf = f'scale={W}:{VH}:force_original_aspect_ratio=increase,crop={W}:{VH},pad={W}:{H}:0:0:color=0xF7F7F5'
        if tr == 'arib-std-b67':
            vf = 'zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,' + vf
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-t', str(dur), '-i', src, '-an', '-vf', f'{vf},fps=30,format=yuv420p,setsar=1,{TAG}',
             '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', o])
    segs.append((o, dur))
card_png(f'{D}/card.png', SPEC['card'])
run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', '3.0', '-i', f'{D}/card.png', '-vf', f'fps=30,format=yuv420p,{TAG}',
     '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', f'{D}/card.mp4'])
segs.append((f'{D}/card.mp4', 3.0))

inputs, fc, off, prev, XF = [], [], 0.0, '0:v', 0.06
for o, _ in segs: inputs += ['-i', o]
for k in range(1, len(segs)):
    xf = 0.35 if k == len(segs) - 1 else XF
    off += segs[k - 1][1] - xf
    fc.append(f'[{prev}][{k}:v]xfade=transition=fade:duration={xf}:offset={off:.2f}[x{k}]'); prev = f'x{k}'
total = off + segs[-1][1]; tend = total - segs[-1][1]
n = len(segs)
for j, (head, sub, t0, t1) in enumerate(SPEC['states']):
    panel_png(f'{D}/p{j}.png', head, sub); inputs += ['-i', f'{D}/p{j}.png']
    fc.append(f"[{prev}][{n + j}:v]overlay=0:0:enable='between(t,{t0},{min(t1, tend):.2f})'[o{j}]"); prev = f'o{j}'
if SPEC.get('script'):
    script_png(f'{D}/script.png', SPEC['script']); inputs += ['-i', f'{D}/script.png']
    fc.append(f"[{prev}][{n + len(SPEC['states'])}:v]overlay=0:0:enable='between(t,0,{tend:.2f})'[sc]"); prev = 'sc'
fc.append(f'[{prev}]format=yuv420p,{TAG}[v]')
out = f"{WD}/amie-{name}{SPEC.get('suffix', '')}.mp4"
run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', '[v]', '-t', f'{total:.2f}', '-c:v', 'libx264',
     '-preset', 'medium', '-crf', '21', '-profile:v', 'high', '-pix_fmt', 'yuv420p', *OUTTAG, '-movflags', '+faststart', out])
print(out, round(total, 2))
