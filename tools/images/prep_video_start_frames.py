"""Free local prep of Glow Friday video start/end frames (storyboard §3). No AI.
python3 tools/images/prep_video_start_frames.py"""
import numpy as np, cv2
from PIL import Image
C = 'content/campaigns/2026-11-glow-friday'
OUT = f'{C}/video/start-frames'
import os; os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
rng = np.random.default_rng(7)

def save(img, name, q=95):
    p = f'{OUT}/{name}'
    Image.fromarray(img).save(p, quality=q) if name.endswith('.jpg') else Image.fromarray(img).save(p)
    print(name, img.shape[1], 'x', img.shape[0])

def fit(img):
    return cv2.resize(img, (W, H), interpolation=cv2.INTER_LANCZOS4 if img.shape[1] < W else cv2.INTER_AREA)

def end_crop(img, cw, ch, x, y):
    return fit(img[y:y+ch, x:x+cw])

def ribbon_target():
    a = cv2.cvtColor(np.asarray(Image.open(f'{C}/hero/src/hero-plate-nologo.png').convert('RGB')), cv2.COLOR_RGB2HSV).reshape(-1, 3).astype(float)
    m = (a[:, 1] > 90) & ((a[:, 0] > 160) | (a[:, 0] < 8)) & (a[:, 2] > 40)
    return np.median(a[m], 0)          # OpenCV HSV (H 0-180)

def recolour_ribbon(rgb, tgt):
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(float)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    mask = (s > 22) & ((h > 150) | (h < 15))
    mask = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
    src_s, src_v = np.median(s[mask]), np.median(v[mask])
    out = hsv.copy()
    out[..., 0][mask] = tgt[0]
    out[..., 1][mask] = np.clip(s[mask] * tgt[1] / src_s, 0, 255)
    out[..., 2][mask] = np.clip(v[mask] * tgt[2] / src_v, 0, 255)
    soft = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 1.2)[..., None]
    res = cv2.cvtColor(out.astype(np.uint8), cv2.COLOR_HSV2RGB).astype(float)
    print('  ribbon px', int(mask.sum()), 'src S/V', round(src_s), round(src_v))
    return (res * soft + rgb * (1 - soft)).astype(np.uint8)

def pad_extend(rgb, top, bottom):
    """extend plain studio background up/down: replicate edge rows, then blur the new area + grain"""
    h, w = rgb.shape[:2]
    big = cv2.copyMakeBorder(rgb, top, bottom, 0, 0, cv2.BORDER_REPLICATE).astype(float)
    for (a, b) in [(0, top), (top + h, top + h + bottom)]:
        if b > a:
            blk = cv2.GaussianBlur(big[a:b], (0, 0), 25)
            big[a:b] = blk + rng.normal(0, 1.4, blk.shape)
    # feather the joins
    for y in (top, top + h):
        lo, hi = max(0, y - 30), min(big.shape[0], y + 30)
        big[lo:hi] = cv2.GaussianBlur(big[lo:hi], (1, 0), 0, sigmaY=6) if False else big[lo:hi]
    return np.clip(big, 0, 255).astype(np.uint8)

tgt = ribbon_target(); print('ribbon target HSV', tgt.round())

# S1 car
car = np.asarray(Image.open(f'{C}/key-visuals/kv-convertible-real-bags.jpg').convert('RGB'))
car = car[0:2240, 140:1400]
# neutral white balance: scale channels so the brightest bag paper (top 2% luminance) reads neutral
lum = car.mean(2); sel = lum > np.percentile(lum, 98)
ref = car[sel].mean(0); gain = ref.mean() / ref
car = np.clip(car * (0.5 + 0.5 * gain), 0, 255).astype(np.uint8)   # half-strength, keeps warmth in seats
s1 = fit(car); save(s1, 'sf-01-car-9x16.jpg'); save(end_crop(s1, 1000, 1778, 40, 120), 'sf-01-car-9x16-end.jpg')

# S2 basket
b = np.asarray(Image.open(f'{C}/hero/src/hero-plate-nologo.png').convert('RGB'))
s2 = fit(b); save(s2, 'sf-02-basket.png'); save(end_crop(s2, 1000, 1778, 40, 116), 'sf-02-basket-end.png')

# S3 hair set
hs = np.asarray(Image.open(f'{C}/banners/src/bg-hair-set.png').convert('RGB'))
hs = recolour_ribbon(hs, tgt); hs = pad_extend(hs, 600, 346)
s3 = fit(hs); save(s3, 'sf-03-hairset-9x16.png'); save(end_crop(s3, 982, 1745, 66, 175), 'sf-03-hairset-end.png')

# S4 scrub + butter
sb = np.asarray(Image.open(f'{C}/banners/src/bg-scrub-butter.png').convert('RGB'))
sb = recolour_ribbon(sb, tgt); sb = pad_extend(sb, 400, 546)
s4 = fit(sb); save(s4, 'sf-04-scrubbutter-9x16.png'); save(end_crop(s4, 982, 1745, 49, 0), 'sf-04-scrubbutter-end.png')

# S5-B body glow packshot
g = np.asarray(Image.open('content/brand/product-refs/body-glow-front.jpg').convert('RGB'))
g = pad_extend(g, 267, 266)
s5 = fit(g); save(s5, 'sf-05b-glow-9x16.png'); save(end_crop(s5, 1019, 1811, 61, 63), 'sf-05b-glow-9x16-end.png')

# S5-A model close-up (only used after modesty OK)
m = np.asarray(Image.open(f'{C}/images/amie-chocolate-bodyglow-closeup-a.jpg').convert('RGB'))[0:2048, 830:1982]
s5a = fit(m); save(s5a, 'sf-05a-glow-9x16.jpg'); save(end_crop(s5a, 1048, 1864, 16, 28), 'sf-05a-glow-9x16-end.jpg')

# end-card background
ec = cv2.GaussianBlur(s2, (0, 0), 14).astype(float) * 0.82
save(np.clip(ec, 0, 255).astype(np.uint8), 'ec-bg.jpg')
