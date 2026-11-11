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
def real(i, n, ss, out_d, push=0.04, xoff=0.5, yoff=0.5, z=1.0, lift='', slow=2.0, blend=False):
    """source slowed by `slow` (2.0 for 60 fps footage; other values use frame blending), slow push-in, B&W film look"""
    o = f'{WD}/s{i}.mp4'
    sm = f"setpts={slow}*PTS,minterpolate=fps=30:mi_mode=blend" if blend else f"setpts={slow}*PTS,fps=30"   # blend only for 30 fps sources
    vf = (f"{sm},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
          f"scale=eval=frame:w='2*trunc(540*{z}*(1+{push}*t/{out_d}))':h=-2:flags=bicubic,"
          f"crop=1080:1920:(iw-1080)*{xoff}:(ih-1920)*{yoff},setsar=1,{BW}{lift},{FILM}")
    run(['-ss', str(ss), '-t', str(out_d/slow + 0.1), '-i', f'{ORIG}/{n}.mov', '-vf', vf, '-t', str(out_d)] + ENC + [o]); return o
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
def pack(i, d, path):
    """product packshot (already B&W with the burgundy ribbon): slow push toward the products, light sweep"""
    o = f'{WD}/s{i}.mp4'; R = cv2.imread(path).astype(np.float32); H, W = R.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W]; n = int(d*30)
    ff = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-vf', FILM] + ENC + [o], stdin=subprocess.PIPE)
    for k in range(n):
        t = k/(n-1); e = t*t*(3-2*t)
        c = -400 + min(max((t-0.15)/0.6, 0), 1)*(W*0.9+H*0.35+800)
        f = 255*(R/255)**0.88 + np.exp(-((xx*0.9+yy*0.35-c)/190.0)**2)[..., None]*30
        M = cv2.getRotationMatrix2D((540, 1330), 0, 1.62 + 0.12*e)
        f = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        ff.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait(); return o
def card(i, d):
    o = f'{WD}/s{i}.mp4'
    run(['-loop', '1', '-t', str(d), '-i', f'{WD}/end.png', '-vf', f'fps=30,format=yuv420p,{FILM}', '-t', str(d)] + ENC + [o]); return o
X = 0.45   # dissolve length
D = [2.05, 2.05, 2.5, 3.3, 2.7, 3.6, 2.8]   # shots 1-3 (no product) are shorter and faster
clips = [real(1, 114, 5.0, D[0], 0.05, 0.08, 0.15, z=1.2, slow=1.25), real(2, 39, 3.0, D[1], 0.04, slow=1.25), real(3, 113, 36.5, D[2], 0.035, 0.5, 0.62, z=1.28, lift=',eq=brightness=0.05:gamma=1.12', slow=1.25),
         real(4, 12, 4.05, D[3], 0.04, 0.5, 0.45, z=1.0, lift=',eq=gamma=1.12', slow=1.35, blend=True),   # real close-up: Hair Wax label, cap comes off
         pack(5, D[4], f'{ROOT}/content/campaigns/2026-11-glow-friday/video/start-frames/sf-03-hairset-9x16.png'),
         bow(6, D[5]), card(7, D[6])]
ins = sum((['-i', c] for c in clips), []); fc = []; cur = '[0:v]'; off = 0.0
for k in range(1, len(clips)):
    off += D[k-1] - X; lab = f'[x{k}]'
    fc.append(f"{cur}[{k}:v]xfade=transition=fade:duration={X}:offset={off:.3f}{lab}"); cur = lab
total = off + D[-1]
fc.append(f"{cur}fade=t=in:st=0:d=0.5,fade=t=out:st={total-0.5:.3f}:d=0.5[o]")
VO = f'{WD}/vo-raw.mp3'   # optional voice-over: three phrases, placed on shots 1, 3 and the basket
silent = f'{WD}/silent.mp4'
run(ins + ['-filter_complex', ';'.join(fc), '-map', '[o]', '-c:v', 'libx264', '-crf', '21', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', silent])
if os.path.exists(VO):
    # the audio track is built on its own, then muxed (mixing it inside the video graph stalled ffmpeg)
    cuts = [(0.0, 2.15, 0.4), (2.15, 5.05, sum(D[:2]) - 2*X + 0.3), (5.05, None, sum(D[:5]) - 5*X + 0.35)]
    a_in, a_fc = [], []
    for j, (a, b, at) in enumerate(cuts):
        part = f'{WD}/a{j}.wav'; run(['-i', VO, '-ss', str(a)] + (['-to', str(b)] if b else []) + [part])
        a_in += ['-i', part]; a_fc.append(f"[{j+1}:a]adelay={int(at*1000)}:all=1[b{j}]")
    a_fc.append("[0:a]" + ''.join(f'[b{j}]' for j in range(3)) + "amix=inputs=4:normalize=0:duration=first,volume=1.6[a]")
    track = f'{WD}/vo-track.wav'
    run(['-f', 'lavfi', '-t', f'{total:.2f}', '-i', 'anullsrc=r=44100:cl=stereo'] + a_in + ['-filter_complex', ';'.join(a_fc), '-map', '[a]', '-t', f'{total:.2f}', track])
    run(['-i', silent, '-i', track, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT])
else:
    run(['-i', silent, '-c', 'copy', '-movflags', '+faststart', OUT])
print('done', OUT)
