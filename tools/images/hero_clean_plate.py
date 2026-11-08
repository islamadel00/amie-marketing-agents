"""Glow Friday hero: remove the stray 'e' on the ribbon and erase the baked-in offer text,
producing a clean plate for the animated hero. Usage: python3 hero_clean_plate.py <in> <out_dir>"""
import sys, cv2, numpy as np
src, out = sys.argv[1], sys.argv[2]
im = cv2.imread(src)  # BGR
h, w = im.shape[:2]

# 1) stray 'e' on the vertical ribbon (~x360,y641): copy ribbon from just above, feathered
x0, y0, s = 350, 631, 22
patch = im[y0-26:y0-26+s, x0:x0+s].astype(np.float32)
m = np.zeros((s, s), np.float32); cv2.circle(m, (s//2, s//2), s//2-2, 1, -1)
m = cv2.GaussianBlur(m, (7, 7), 0)[..., None]
roi = im[y0:y0+s, x0:x0+s].astype(np.float32)
im[y0:y0+s, x0:x0+s] = (patch*m + roi*(1-m)).astype(np.uint8)
cv2.imwrite(f"{out}/hero-fixed.png", im)  # same as original, only the 'e' removed

# 2) erase the offer text above the basket
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
mask = np.zeros((h, w), np.uint8)
top = 272
mask[:top][gray[:top] < 150] = 255
mask = cv2.dilate(mask, np.ones((7, 7), np.uint8), 2)
mask[top:] = 0
clean = cv2.inpaint(im, mask, 9, cv2.INPAINT_TELEA)
# soften the filled area and add matching grain so it doesn't look painted
blur = cv2.GaussianBlur(clean, (0, 0), 6)
mf = cv2.GaussianBlur(mask.astype(np.float32)/255, (0, 0), 4)[..., None]
noise = np.random.default_rng(1).normal(0, 2.2, clean.shape)
filled = np.clip(blur + noise, 0, 255)
clean = (filled*mf + clean*(1-mf)).astype(np.uint8)
cv2.imwrite(f"{out}/hero-clean-plate.png", clean)
cv2.imwrite(f"{out}/text-mask.png", mask)
print("ok")
