"""Glow Friday vertical videos (720x1280, bt709) from existing a'mie footage segments.
Usage: python3 -I glow_friday_video.py <workdir> <spec.json>
spec: {"name":..., "clips":[[path, start, dur, slowmo(bool)]...], "supers":[[text, t0, t1]...],
       "card": {"bundle":..., "was":..., "now":..., "sub":...}}
Arabic is rendered with PIL+raqm into PNGs (ffmpeg drawtext breaks Arabic shaping)."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

WD, SPEC = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
FONTS = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/fonts'
LOGO = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/brand/logo.png'
AR_B, AR_R = f'{FONTS}/ReadexPro-AR-Bold.ttf', f'{FONTS}/ReadexPro-AR-Regular.ttf'
EN_L, EN_R = f'{FONTS}/Montserrat-Light.ttf', f'{FONTS}/Montserrat-Regular.ttf'
W, H = 720, 1280
ROSE, INK, GREY, BG = '#5E2E21', '#191919', '#8C8580', (240, 238, 234)
TAG = 'setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709'
OUTTAG = ['-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709']
name = SPEC['name']
os.makedirs(f'{WD}/{name}', exist_ok=True)
D = f'{WD}/{name}'

def run(cmd):
    subprocess.run(cmd, check=True, stdin=subprocess.DEVNULL)

def font(p, s):
    return ImageFont.truetype(p, s, layout_engine=ImageFont.Layout.RAQM)

def text_c(d, y, txt, f, fill, ar=True, spacing=0):
    kw = dict(direction='rtl', language='ar') if ar else {}
    if spacing and not ar:  # letter-spaced latin
        widths = [d.textlength(c, font=f) for c in txt]
        tw = sum(widths) + spacing * (len(txt) - 1); x = (W - tw) / 2
        for c, w in zip(txt, widths):
            d.text((x, y), c, font=f, fill=fill); x += w + spacing
        return
    l, t, r, b = d.textbbox((0, 0), txt, font=f, **kw)
    d.text(((W - (r - l)) / 2 - l, y - t), txt, font=f, fill=fill, **kw)
    return r - l, b - t

def pill(path, txt, y, size=46):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    while True:
        f = font(AR_B, size)
        l, t, r, b = d.textbbox((0, 0), txt, font=f, direction='rtl', language='ar')
        if r - l <= W - 120 or size <= 28: break
        size -= 2
    tw, th = r - l, b - t; x = (W - tw) // 2; px, py = 30, 20
    d.rounded_rectangle((x - px, y - py, x + tw + px, y + th + py), radius=(th + 2 * py) // 2, fill=(242, 240, 237, 235))
    d.text((x - l, y - t), txt, font=f, fill=INK, direction='rtl', language='ar')
    im.save(path)

def card(path, c):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    text_c(d, 250, 'GLOW FRIDAY', font(EN_L, 34), ROSE, ar=False, spacing=9)
    lg = Image.open(LOGO).convert('RGBA'); lw = 330; lg = lg.resize((lw, int(lg.height * lw / lg.width)))
    im.paste(lg, ((W - lw) // 2, 340), lg)
    text_c(d, 520, c['bundle'], font(AR_B, 44), INK)
    if c.get('items'): text_c(d, 588, c['items'], font(AR_R, 27), GREY)
    # prices: was (struck) and now
    fw, fn = font(EN_R, 40), font(EN_R, 92)
    was, now = f"{c['was']}", f"{c['now']}"
    ww = d.textlength(was, font=fw); nw = d.textlength(now, font=fn); cur = font(AR_R, 30)
    gap = 34; total = ww + gap + nw; x0 = (W - total) / 2; yb = 720
    if c.get('was_label'):
        d.text(((W - nw) / 2, yb - 38), now, font=fn, fill=ROSE)
        text_c(d, 890, c['was_label'], font(AR_R, 26), GREY)
    else:
        d.text((x0 + nw + gap, yb), was, font=fw, fill=GREY)
        d.line((x0 + nw + gap - 4, yb + 26, x0 + nw + gap + ww + 4, yb + 26), fill=GREY, width=3)
        d.text((x0, yb - 38), now, font=fn, fill=ROSE)
    text_c(d, 840, 'ر.س', cur, ROSE)
    text_c(d, 960, c['sub'], font(AR_R, 30), INK)
    text_c(d, 1030, 'amie-sa.com', font(EN_L, 28), GREY, ar=False)
    im.save(path)

# 1) clips -> normalized segments
segs = []
for i, (src, a, dur, slow) in enumerate(SPEC['clips']):
    o = f'{D}/c{i}.mp4'
    vf = 'scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280'
    tr = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=color_transfer', '-of', 'csv=p=0', src],
                        capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
    if tr == 'arib-std-b67':
        vf = 'zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,' + vf
    if slow: vf += ',setpts=2*PTS'
    read = dur / 2 if slow else dur
    run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-t', str(read), '-i', src, '-an', '-vf',
         f'{vf},fps=30,format=yuv420p,setsar=1,{TAG}', '-t', str(dur), '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', o])
    segs.append((o, dur))
# 2) end card (3s, gentle zoom)
card(f'{D}/card.png', SPEC['card'])
run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', '3.2', '-i', f'{D}/card.png', '-vf',
     f"scale=760:-1,zoompan=z='min(1+0.0008*on,1.05)':d=96:s=720x1280:fps=30,format=yuv420p,{TAG}",
     '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', f'{D}/card.mp4'])
segs.append((f'{D}/card.mp4', 3.2))
# 3) xfade chain
inputs, fc, off, prev = [], [], 0.0, '0:v'
for o, _ in segs: inputs += ['-i', o]
XF = SPEC.get('xf', 0.3)
for k in range(1, len(segs)):
    off += segs[k - 1][1] - XF
    fc.append(f'[{prev}][{k}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}[x{k}]'); prev = f'x{k}'
total = off + segs[-1][1]
# 4) supers overlay
for j, (txt, t0, t1) in enumerate(SPEC['supers']):
    pill(f'{D}/s{j}.png', txt, SPEC.get('super_y', 980)); inputs += ['-i', f'{D}/s{j}.png']
    idx = len(segs) + j
    fc.append(f"[{prev}][{idx}:v]overlay=0:0:enable='between(t,{t0},{t1})'[o{j}]"); prev = f'o{j}'
if SPEC.get('top'):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = font(AR_B, SPEC.get('top_size', 54))
    from PIL import ImageFilter
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    y = SPEC.get('top_y', 210)
    for line in SPEC['top'].split('\n'):
        l, t, r, b = d.textbbox((0, 0), line, font=f, direction='rtl', language='ar'); x = (W - (r - l)) / 2 - l
        ds.text((x + 2, y - t + 3), line, font=f, fill=(0, 0, 0, 170), direction='rtl', language='ar')
        d.text((x, y - t), line, font=f, fill='white', direction='rtl', language='ar'); y += int(SPEC.get('top_size', 54) * 1.5)
    sh = sh.filter(ImageFilter.GaussianBlur(4)); sh.alpha_composite(im); sh.save(f'{D}/top.png')
    inputs += ['-i', f'{D}/top.png']; idx = len(segs) + len(SPEC['supers'])
    tend = total - segs[-1][1]
    fc.append(f"[{prev}][{idx}:v]overlay=0:0:enable='between(t,0,{tend:.2f})'[tp]"); prev = 'tp'
fc.append(f'[{prev}]format=yuv420p,{TAG}[v]')
out = f'{WD}/amie-glow-friday-{name}{SPEC.get("suffix", "")}.mp4'
run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', '[v]', '-t', f'{total:.2f}',
     '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-profile:v', 'high', '-pix_fmt', 'yuv420p', *OUTTAG, '-movflags', '+faststart', out])
run(['ffmpeg', '-v', 'error', '-y', '-ss', '1', '-i', out, '-frames:v', '1', '-q:v', '3', out.replace('.mp4', '-poster.jpg')])
print(out, round(total, 2))
