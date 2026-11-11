"""Glow Friday basket build-up (stop-motion), composited locally from the REAL photo.
Layers (1080x1920, aligned): E = empty basket (AI plate), N = boxes without ribbon
(real photo; AI only under the ribbon footprint), R = the real photo.
Usage: python3 basket_build.py <layers_dir> <out_dir>
Writes seg0..seg5 mp4 (30 fps): empty / scrub+butter boxes / hair box / glow box / lip+hand boxes / ribbon+hold."""
import sys, subprocess, numpy as np, cv2
L, OUT = sys.argv[1], sys.argv[2]
E = cv2.imread(f'{L}/E.png').astype(np.float32); N = cv2.imread(f'{L}/N.png').astype(np.float32)
R = cv2.imread(f'{L}/plate-9x16.png').astype(np.float32); RB = cv2.imread(f'{L}/ribbon-mask.png', 0)
H, W = 1920, 1080; FPS = 12
BOX = {  # polygons in full-frame pixels
 'mono':  [(298,806),(567,806),(567,1097),(298,1097)],
 'hand':  [(580,733),(702,738),(697,1004),(576,1001)],
 'sleek': [(699,783),(802,786),(788,1156),(699,1152)],
 'hid':   [(316,1108),(548,1108),(548,1218),(316,1218)],
 'glow':  [(563,1001),(714,1001),(714,1472),(563,1472)],
 'lip':   [(704,1150),(803,1150),(803,1448),(704,1448)],
 'lemon': [(270,1243),(570,1243),(570,1492),(270,1492)],
}
def pmask(name, grow=6):
    m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [np.array(BOX[name], np.int32)], 255)
    m = cv2.dilate(m, np.ones((grow*2+1, grow*2+1), np.uint8))
    return cv2.GaussianBlur(m.astype(np.float32)/255, (0, 0), 3)
M = {k: pmask(k) for k in BOX}
def base(done):
    f = E.copy()
    for k in done:
        a = M[k][..., None]; f = N*a + f*(1-a)
    return f
def pop(frame, name, s, dy, alpha=1.0):
    """draw box `name` scaled by s, lifted by dy px, with a soft shadow"""
    m = M[name]; ys, xs = np.where(m > 0.02); x0, x1, y0, y1 = xs.min(), xs.max()+1, ys.min(), ys.max()+1
    patch = N[y0:y1, x0:x1]; pm = m[y0:y1, x0:x1]
    w, h = int((x1-x0)*s), int((y1-y0)*s)
    patch = cv2.resize(patch, (w, h), interpolation=cv2.INTER_LINEAR); pm = cv2.resize(pm, (w, h))
    cx, cy = (x0+x1)//2, (y0+y1)//2 - int(dy)
    X0, Y0 = cx-w//2, cy-h//2
    out = frame.copy()
    # shadow (offset grows with lift)
    sh = np.zeros((H, W), np.float32); off = int(10+dy*0.5)
    xa, ya = max(X0+off, 0), max(Y0+off, 0); xb, yb = min(X0+off+w, W), min(Y0+off+h, H)
    sh[ya:yb, xa:xb] = pm[ya-(Y0+off):yb-(Y0+off), xa-(X0+off):xb-(X0+off)]
    sh = cv2.GaussianBlur(sh, (0, 0), 12+dy*0.15)[..., None]*0.38
    out = out*(1-sh)
    xa, ya = max(X0, 0), max(Y0, 0); xb, yb = min(X0+w, W), min(Y0+h, H)
    a = (pm[ya-Y0:yb-Y0, xa-X0:xb-X0]*alpha)[..., None]
    out[ya:yb, xa:xb] = patch[ya-Y0:yb-Y0, xa-X0:xb-X0]*a + out[ya:yb, xa:xb]*(1-a)
    return out
POP = [(1.20, 60, .9), (1.09, 22, 1), (0.985, 0, 1), (1.0, 0, 1)]   # scale, lift, alpha per stop-motion frame
# ribbon stages: straight bands first, then bow + tails
rbf = cv2.GaussianBlur(RB.astype(np.float32)/255, (0, 0), 2)
ys, xs = np.where(RB > 0); cx, cy = 540, int(np.median(ys))
yy, xx = np.mgrid[0:H, 0:W]
bow = (((xx-cx)/250.0)**2 + ((yy-cy-40)/250.0)**2) < 1
hband = rbf*((~bow) & (np.abs(yy-cy) < 90)); vband = rbf*((~bow) & (np.abs(xx-cx) < 70))
RSTAGE = [hband, np.maximum(hband, vband), rbf]
def ribbon(frame, stage):
    a = cv2.dilate(RSTAGE[stage], np.ones((9, 9), np.uint8)); a = cv2.GaussianBlur(a, (0, 0), 3)[..., None]
    return R*a + frame*(1-a)
def zoom(f, t):   # slow continuous push-in over the whole build (t in 0..1)
    s = 1.0 + 0.06*t; M2 = cv2.getRotationMatrix2D((540, 1090), 0, s)
    return cv2.warpAffine(f, M2, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
def sheen(f, p):  # p 0..1 diagonal light sweep
    x = (xx*0.9 + yy*0.35); c = -300 + p*(W*0.9+H*0.35+600)
    g = np.exp(-((x-c)/170.0)**2)[..., None]*38
    return f + g
SEGS = [
 ('seg0', [('hold', [], 26)]),
 ('seg1', [('pop', 'mono'), ('pop', 'lemon'), ('hold', None, 3)]),
 ('seg2', [('pop', 'hid'), ('pop', 'sleek'), ('hold', None, 3)]),
 ('seg3', [('pop', 'glow'), ('hold', None, 5)]),
 ('seg4', [('pop', 'lip'), ('pop', 'hand'), ('hold', None, 3)]),
 ('seg5', [('rib', 0), ('rib', 1), ('rib', 2), ('final', None, 22)]),
]
total = sum((len(POP)+1 if a[0] == 'pop' else 3 if a[0] == 'rib' else a[2]) for _, acts in SEGS for a in acts)
done, gi = [], 0
for name, acts in SEGS:
    ff = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', f'{OUT}/{name}.mp4'], stdin=subprocess.PIPE)
    def emit(f):
        global gi
        ff.stdin.write(np.clip(zoom(f, gi/total), 0, 255).astype(np.uint8).tobytes()); gi += 1
    for a in acts:
        if a[0] == 'hold':
            for _ in range(a[2]): emit(base(done))
        elif a[0] == 'pop':
            b = base(done)
            for s, dy, al in POP: emit(pop(b, a[1], s, dy, al))
            done.append(a[1]); emit(base(done))
        elif a[0] == 'rib':
            full = N if len(done) == len(BOX) else base(done)
            for _ in range(3): emit(ribbon(full, a[1]))
        elif a[0] == 'final':
            for i in range(a[2]): emit(sheen(R, i/(a[2]-1)))
    ff.stdin.close(); ff.wait(); print(name, 'ok', flush=True)
