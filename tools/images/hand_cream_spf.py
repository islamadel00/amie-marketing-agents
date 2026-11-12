"""Hand Cream 30 ml store images: change the label line «SPF 15» to «SPF 10» (local edit, no AI).
Each spot: centre of the old text, its length and cap height in px, and its angle (degrees CCW).
Usage: python3 hand_cream_spf.py <site_dir> <font.ttf> <out_dir>"""
import sys, math, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SITE, FONT, OUT = sys.argv[1:4]
TEXT = 'SPF 10'
JOBS = {
 '577d8c52-7f4f-4abf-b23c-3053e4ea6908': ('hand-cream-1-front',   [((669.0, 661.6), 43.5, 9.6, 90.0, (122, 48, 40))]),
 'ec4d458f-6a2b-4654-ad88-bf56fcd77056': ('hand-cream-2-texture', [((544.5, 679.2), 36.8, 8.4, 90.0, (150, 44, 52)), ((1142.5, 715.0), 35.6, 8.2, 42.7, (150, 44, 52))]),
 '4f9f5fe6-38d3-41a3-a8ed-efb8f69e2644': ('hand-cream-3-in-use',  [((763.0, 789.0), 34.2, 7.8, 40.2, (112, 62, 58))]),
}
S = 8   # supersampling
def rect(c, L, Hh, ang, pad):
    a = math.radians(ang); ux, uy = math.cos(a), -math.sin(a); vx, vy = -uy, ux
    l, h = L/2+pad, Hh/2+pad
    return np.array([[c[0]+sx*l*ux+sy*h*vx, c[1]+sx*l*uy+sy*h*vy] for sx, sy in ((-1,-1),(1,-1),(1,1),(-1,1))], np.float32)
def edit(img, c, L, Hh, ang, INK):
    a = np.asarray(img).copy()
    ink = np.array(INK)   # print colour, measured on the larger label text of the same tube
    # erase the old text (and its JPEG halo) from the tube surface
    m = np.zeros(a.shape[:2], np.uint8); cv2.fillPoly(m, [np.round(rect(c, L, Hh, ang, 2.6)).astype(np.int32)], 255)
    a = cv2.inpaint(a, m, 4, cv2.INPAINT_TELEA)
    base = Image.fromarray(a)
    # new text, drawn large, scaled to the old text's length, rotated, then pasted
    f = ImageFont.truetype(FONT, 200); x0, y0, x1, y1 = f.getbbox(TEXT)
    tw = sum(f.getlength(ch) for ch in TEXT) + 10*(len(TEXT)-1)
    t = Image.new('L', (int(tw)+20, y1-y0+20), 0); d = ImageDraw.Draw(t); x = 10
    for ch in TEXT: d.text((x, 10-y0), ch, font=f, fill=255); x += f.getlength(ch) + 10      # light tracking, like the label
    bb = t.getbbox(); t = t.crop(bb)
    k = L*S/t.width; t = t.resize((max(1, round(t.width*k)), max(1, round(t.height*k))), Image.LANCZOS)
    t = t.rotate(ang, resample=Image.BICUBIC, expand=True)
    t = t.resize((max(1, round(t.width/S)), max(1, round(t.height/S))), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.35))
    alpha = t.point(lambda v: min(255, int(v*1.12)))
    layer = Image.new('RGB', t.size, tuple(int(v) for v in ink))
    base.paste(layer, (round(c[0]-t.width/2), round(c[1]-t.height/2)), alpha)
    return base, ink
for src, (name, spots) in JOBS.items():
    im = Image.open(f'{SITE}/{src}.jpg').convert('RGB')
    for c, L, Hh, ang, INK in spots:
        im, ink = edit(im, c, L, Hh, ang, INK); print(name, c, 'ink', ink.round())
    im.save(f'{OUT}/{name}-SPF10-1200x1600.jpg', quality=96, subsampling=0)
    im.resize((2400, 3200), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2)).save(f'{OUT}/{name}-SPF10-2x-2400x3200.png')
