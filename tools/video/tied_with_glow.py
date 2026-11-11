"""Glow Friday 'Tied with glow' film (direction A): ballet footage in B&W slow motion,
the burgundy-ribbon basket, end card. 1080x1920, 30 fps, no audio.
Usage: python3 tied_with_glow.py <orig_dir> <work_dir> <out.mp4>
orig_dir holds the Drive originals as <n>.mov (n from drive-video-library.csv); work_dir holds title.png and end.png."""
import subprocess, sys, os, numpy as np, cv2
ORIG, WD, OUT = sys.argv[1:4]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
PLATE = f'{ROOT}/content/campaigns/2026-11-glow-friday/video/basket-reel/layers/plate-9x16.png'
ENC = ['-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '30', '-an']
FILM = "noise=alls=7:allf=t+u,vignette=PI/5.5"
BW = "hue=s=0,eq=contrast=1.16:brightness=-0.015:gamma=0.96,colorbalance=rm=0.015:bm=-0.02"
def run(a): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + a, check=True)
def real(i, n, ss, out_d, push=0.04, xoff=0.5, yoff=0.5, z=1.0, lift=''):
    """60 fps source played at half speed, slow push-in, B&W film look"""
    o = f'{WD}/s{i}.mp4'
    vf = (f"setpts=2*PTS,fps=30,scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
          f"scale=eval=frame:w='2*trunc(540*{z}*(1+{push}*t/{out_d}))':h=-2:flags=bicubic,"
          f"crop=1080:1920:(iw-1080)*{xoff}:(ih-1920)*{yoff},setsar=1,{BW}{lift},{FILM}")
    run(['-ss', str(ss), '-t', str(out_d/2 + 0.1), '-i', f'{ORIG}/{n}.mov', '-vf', vf, '-t', str(out_d)] + ENC + [o]); return o
def bow(i, d):
    """the real basket photo: everything B&W except the burgundy ribbon; slow push, light sweep, title fades in"""
    o = f'{WD}/s{i}.mp4'; R = cv2.imread(PLATE).astype(np.float32); H, W = R.shape[:2]
    hsv = cv2.cvtColor(R.astype(np.uint8), cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 1] > 70) & ((hsv[..., 0] > 160) | (hsv[..., 0] < 8)) & (hsv[..., 2] > 35)).astype(np.uint8)*255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((21, 21), np.uint8)); mf = cv2.GaussianBlur(m.astype(np.float32)/255, (0, 0), 1.5)[..., None]
    g = cv2.cvtColor(R.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32); g = np.clip((g-128)*1.12+126, 0, 255)
    base = R*mf + np.stack([g*0.97, g*0.985, g], -1)*(1-mf)
    T = cv2.imread(f'{WD}/title.png', cv2.IMREAD_UNCHANGED).astype(np.float32); ta = T[..., 3:4]/255
    yy, xx = np.mgrid[0:H, 0:W]; n = int(d*30)
    ff = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-vf', FILM] + ENC + [o], stdin=subprocess.PIPE)
    for k in range(n):
        t = k/(n-1); e = t*t*(3-2*t)
        c = -400 + min(max((t-0.25)/0.55, 0), 1)*(W*0.9+H*0.35+800)
        f = base + np.exp(-((xx*0.9+yy*0.35-c)/190.0)**2)[..., None]*34
        s = 1.24 + 0.10*e; M = cv2.getRotationMatrix2D((540, 1105), 0, s)
        f = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        a = ta*min(max((t-0.22)/0.25, 0), 1)
        f = T[..., :3]*a + f*(1-a)
        ff.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait(); return o
def card(i, d):
    o = f'{WD}/s{i}.mp4'
    run(['-loop', '1', '-t', str(d), '-i', f'{WD}/end.png', '-vf', f'fps=30,format=yuv420p,{FILM}', '-t', str(d)] + ENC + [o]); return o
X = 0.45   # dissolve length
D = [2.95, 2.95, 3.45, 2.45, 3.6, 2.6]
clips = [real(1, 114, 5.0, D[0], 0.05, 0.08, 0.15, z=1.2), real(2, 39, 3.0, D[1], 0.04), real(3, 113, 36.5, D[2], 0.035, 0.5, 0.62, z=1.28, lift=',eq=brightness=0.05:gamma=1.12'),
         real(4, 101, 8.8, D[3], 0.04, 0.5, 0.3), bow(5, D[4]), card(6, D[5])]
ins = sum((['-i', c] for c in clips), []); fc = []; cur = '[0:v]'; off = 0.0
for k in range(1, len(clips)):
    off += D[k-1] - X; lab = f'[x{k}]'
    fc.append(f"{cur}[{k}:v]xfade=transition=fade:duration={X}:offset={off:.3f}{lab}"); cur = lab
fc.append(f"{cur}fade=t=in:st=0:d=0.5,fade=t=out:st={off+D[-1]-0.5:.3f}:d=0.5[o]")
run(ins + ['-filter_complex', ';'.join(fc), '-map', '[o]', '-c:v', 'libx264', '-crf', '21', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', OUT])
print('done', OUT)
