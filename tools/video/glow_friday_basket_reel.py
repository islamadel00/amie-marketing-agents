"""Assemble the Glow Friday 'basket' reel: real footage + local basket build-up + hero end card.
Usage: python3 glow_friday_basket_reel.py <proxy_dir> <build_seg_dir> <overlay_dir> <work_dir> <out.mp4>
Real clips are Drive proxies named <drive_file_id>.mp4 (see drive-video-library.csv, column n)."""
import csv, subprocess, sys, os
PX, SEG, OV, WD, OUT = sys.argv[1:6]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
C = f'{ROOT}/content/campaigns/2026-11-glow-friday'
rows = {int(r['n']): r['drive_file_id'] for r in csv.DictReader(open(f'{C}/drive-video-library.csv', encoding='utf-8-sig'))}
ENC = ['-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '30', '-an']
FIT = "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,fps=30"
BASKET = "crop=830:1476:125:372,scale=1080:1920:flags=lanczos,setsar=1,fps=30"   # punch in on the basket
def run(a): subprocess.run(['ffmpeg', '-loglevel', 'error', '-y'] + a, check=True)
def ov(vf_in, name, fade_in=0.15):
    """filter_complex that overlays a text PNG with a quick fade-in"""
    return f"[0:v]{vf_in}[v];[1:v]format=rgba,fade=t=in:st=0:d={fade_in}:alpha=1[t];[v][t]overlay=0:0:shortest=0[o]"
def real(i, n, ss, t, text=None, speed=1.0, extra=''):
    src = f'{PX}/{rows[n]}.mp4'; out = f'{WD}/{i:02d}.mp4'
    vf = (f"setpts={1/speed}*PTS," if speed != 1 else '') + FIT + extra
    if text:
        run(['-ss', str(ss), '-t', str(t), '-i', src, '-loop', '1', '-t', str(t/speed), '-i', f'{OV}/{text}.png', '-filter_complex', ov(vf, text), '-map', '[o]', '-t', str(t/speed)] + ENC + [out])
    else:
        run(['-ss', str(ss), '-t', str(t), '-i', src, '-vf', vf] + ENC + [out])
    return out
def seg(i, name, text=None, t=None):
    src = f'{SEG}/{name}.mp4'; out = f'{WD}/{i:02d}.mp4'
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
    d = min(d, t) if t else d; tt = ['-t', str(d)]
    if text:
        run(tt + ['-i', src, '-loop', '1', '-t', str(d), '-i', f'{OV}/{text}.png', '-filter_complex', ov(BASKET, text, 0.25), '-map', '[o]', '-t', str(d)] + ENC + [out])
    else:
        run(tt + ['-i', src, '-vf', BASKET] + ENC + [out])
    return out
def still(i, path, crop, t, text):
    """made scene from an approved still: slow push-in"""
    out = f'{WD}/{i:02d}.mp4'; n = int(t*30)
    vf = f"crop={crop},scale=1620:2880:flags=lanczos,zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih*0.45-(ih/zoom*0.45)':d={n}:s=1080x1920:fps=30,setsar=1"
    run(['-i', path, '-loop', '1', '-t', str(t), '-i', f'{OV}/{text}.png', '-filter_complex', ov(vf, text), '-map', '[o]', '-t', str(t)] + ENC + [out])
    return out
clips = [
 real(1, 2, 0.45, 1.9, 'hook'),                    # model on the giant Lemongrass jar (real shoot)
 seg(2, 'seg0', 'empty', 1.3),                     # empty basket
 real(3, 24, 2.0, 1.5, 'body'),                    # model holding the Lemongrass jar (real shoot)
 seg(4, 'seg1'),                                   # monogram + Lemongrass boxes drop in
 real(5, 12, 24.0, 1.5, 'hair'),                   # Sleek Secret on hair (real UGC)
 seg(6, 'seg2'),                                   # Sleek Secret box
 still(7, f'{C}/images/amie-chocolate-bodyglow-closeup-a.jpg', '1152:2048:830:0', 1.5, 'glow'),  # made scene
 seg(8, 'seg3'),                                   # Body Glow box
 real(9, 25, 1.0, 1.4, 'lip'),                     # Lip Plump (real UGC)
 seg(10, 'seg4'),                                  # Lip Plump + Hand Cream boxes
 seg(11, 'seg5', 'ribbon'),                        # ribbon ties, light sweep
 real(12, 14, 7.0, 1.7),                           # real a'mie shopping bag
]
end = f'{WD}/13.mp4'                               # end card = the site hero loop (offer text + logo)
run(['-t', '3.2', '-i', f'{C}/hero/glow-friday-hero-mobile-9x16.mp4', '-vf', 'scale=1080:1920,setsar=1,fps=30'] + ENC + [end]); clips.append(end)
lst = f'{WD}/list.txt'; open(lst, 'w').write(''.join(f"file '{c}'\n" for c in clips))
run(['-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-crf', '20', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', OUT])
print('done', OUT)
