"""Paste the real Sleek Secret and Hair Wax label print (from content/brand/product-refs/hair-set-products.jpg) over AI-garbled text on the Glow Friday hair-set background.
Usage: python3 -I fix_hair_set_labels.py <bg_in.png> <hair-set-products.jpg> <out.png>   (coordinates are for bg-hair-set-ai-original.png, 1792x2240)"""
import numpy as np, sys
from PIL import Image, ImageFilter
bgp, refp, out = sys.argv[1:4]
bg = np.asarray(Image.open(bgp).convert('RGB')).astype(float)
ref = np.asarray(Image.open(refp).convert('L')).astype(float)

def erase(a, x0, y0, x1, y1, top, bot, f=6):
    """fill box per column (linear between row medians above/below), feathered f px at the box edge"""
    t = np.median(a[top[0]:top[1], x0-f:x1+f], axis=0); b = np.median(a[bot[0]:bot[1], x0-f:x1+f], axis=0)
    yt, yb = (top[0]+top[1])/2, (bot[0]+bot[1])/2
    fill = np.stack([t*(1-(y-yt)/(yb-yt)) + b*(y-yt)/(yb-yt) for y in range(y0-f, y1+f)])
    fill = np.asarray(Image.fromarray(np.clip(fill,0,255).astype(np.uint8)).filter(ImageFilter.BoxBlur(3))).astype(float)
    fill += np.random.default_rng(1).normal(0, 2.2, fill.shape[:2])[..., None]   # keep the paper/matte grain
    m = np.zeros(fill.shape[:2]); m[f:-f, f:-f] = 1
    m = np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(f/2))).astype(float)[..., None]/255
    m = np.maximum(m, np.pad(np.ones((y1-y0, x1-x0)), f)[..., None])
    a[y0-f:y1+f, x0-f:x1+f] = a[y0-f:y1+f, x0-f:x1+f]*(1-m) + fill*m

def ink(box, sample_rows, dark):
    x0,y0,x1,y1 = box; r = ref[y0:y1, x0:x1]
    loc = np.median(ref[sample_rows[0]:sample_rows[1], x0:x1], axis=0)[None, :]
    a = (loc - r)/np.maximum(loc, 1) if dark else (r - loc)/np.maximum(255-loc, 1)
    return np.clip((a-0.08)/0.6, 0, 1)

def paste(a, alpha, x, y, scale, colour):
    h, w = alpha.shape; im = Image.fromarray((alpha*255).astype(np.uint8)).resize((int(w*scale), int(h*scale)), Image.LANCZOS)
    al = np.asarray(im.filter(ImageFilter.GaussianBlur(0.5))).astype(float)[..., None]/255
    H, W = al.shape[:2]; reg = a[y:y+H, x:x+W]; a[y:y+H, x:x+W] = reg*(1-al) + np.array(colour)*al

# Sleek Secret tube: erase old print, paste real print (dark grey ink)
erase(bg, 1126, 1236, 1248, 1468, (1205, 1230), (1472, 1498))
paste(bg, ink((818, 688, 884, 834), (838, 858), True), 1133, 1238, 1.52, (62, 62, 62))
# Hair Wax: erase invented small lines, paste real (light ink)
erase(bg, 832, 1760, 992, 1792, (1756, 1760), (1792, 1798))
paste(bg, ink((558, 985, 662, 1015), (1016, 1024), False), 833, 1761, 1.5, (222, 222, 222))
Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8)).save(out)
