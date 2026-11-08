"""Glow Friday desktop hero, light-beige variant: lift the wall of the real photo to a light beige
with a smooth illumination gain map (label contrast kept), then build a matching 1920x1080 wall."""
import numpy as np, cv2
from PIL import Image
from scipy.ndimage import gaussian_filter, gaussian_filter1d
T = np.array([238., 231., 220.])            # target light beige #EEE7DC
base = 'content/campaigns/2026-11-glow-friday/hero/src/'
p = np.asarray(Image.open(base+'hero-plate-nologo.png').convert('RGB')).astype(np.float32)
h, w = p.shape[:2]
sm = cv2.resize(p, (72,128), interpolation=cv2.INTER_AREA)
m = np.zeros((128,72), np.uint8); m[25:106, 5:70] = 255
est = cv2.inpaint(np.clip(sm,0,255).astype(np.uint8), m, 15, cv2.INPAINT_TELEA).astype(np.float32)
est = cv2.GaussianBlur(cv2.resize(est, (w,h), interpolation=cv2.INTER_CUBIC), (0,0), 40)
gain = np.clip(T/np.maximum(est,1), 1.0, 1.9)
L = p.mean(2, keepdims=True)
wl = np.clip((L-90)/50, 0, 1); wl = wl*wl*(3-2*wl)
out = p*(1+(gain-1)*wl)
knee = 238.; over = np.maximum(out-knee, 0)
out = np.where(out>knee, knee+(255-knee)*(1-np.exp(-over/(255-knee))), out)
pl = np.clip(out,0,255)
Image.fromarray(pl.astype(np.uint8)).save(base+'hero-plate-nologo-light.png')
# wall: per-row colour at the plate edges, evened toward T on the far left, plus soft mottling and grain
s = 1080/1280; pw = round(w*s)
ps = cv2.resize(pl, (pw,1080), interpolation=cv2.INTER_AREA)
edge = gaussian_filter1d(np.median(np.concatenate([ps[:,0:14], ps[:,pw-12:pw]],1),1), 50, axis=0, mode='nearest')
X0 = 1920-170-pw
x = np.arange(1920)[None,:,None]
t = np.clip((X0-x)/700.0, 0, 1); t = t*t*(3-2*t)
bg = edge[:,None,:]*(1-t) + T*t
rng = np.random.default_rng(3)
mott = gaussian_filter(rng.normal(0,1,(1080,1920)), 70); mott = mott/mott.std()*1.8
bg = bg + mott[...,None] + rng.normal(0,1.3,(1080,1920,3))
Image.fromarray(np.clip(bg,0,255).astype(np.uint8)).save(base+'desktop-bg-light.jpg', quality=93)
print('edge top/bottom', edge[0].round(), edge[-1].round())
