"""Lighten skin one shade. Usage: lighten.py in out mask_preview stickbox(x0,y0,x1,y1)"""
import sys, numpy as np
from PIL import Image, ImageFilter
src, out, prev, box = sys.argv[1], sys.argv[2], sys.argv[3], [int(v) for v in sys.argv[4].split(',')]
im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(np.float32) / 255
hsv = np.asarray(im.convert('HSV')).astype(np.float32) / 255
h, s, v = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
m = ((h > 8) & (h < 40) & (s > 0.18) & (s < 0.85) & (v > 0.22)).astype(np.float32)
x0, y0, x1, y1 = box  # chocolate stick: keep only bright fingers inside it
inner = np.zeros_like(m); inner[y0:y1, x0:x1] = 1
m[(inner == 1) & ((v < 0.62) | (s > 0.62))] = 0
mi = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(7)).filter(ImageFilter.GaussianBlur(6))
m = np.asarray(mi).astype(np.float32)[..., None] / 255
light = a ** 0.86                                   # lift midtones ~one shade
g = light.mean(-1, keepdims=True); light = g + (light - g) * 0.90  # a bit less orange/tan
res = a * (1 - m) + light * m
Image.fromarray((np.clip(res, 0, 1) * 255).round().astype(np.uint8)).save(out, quality=95)
mi.save(prev)
