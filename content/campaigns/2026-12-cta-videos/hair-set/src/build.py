import subprocess,sys
O='../orig'; W='.'
ENC=['-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-r','30','-an']
LOOK="eq=contrast=1.04:saturation=1.03:gamma=0.99,unsharp=5:5:0.4"
def run(a): subprocess.run(['ffmpeg','-loglevel','error','-y']+a,check=True)
def shot(i,n,ss,d,cap,speed=1.0,z=1.0,yoff=0.5,xoff=0.5):
    o=f'{W}/s{i}.mp4'; src=d*speed
    vf=(f"setpts=PTS/{speed},fps=30,scale=1080*{z}:1920*{z}:force_original_aspect_ratio=increase:flags=lanczos,"
        f"crop=1080:1920:(iw-1080)*{xoff}:(ih-1920)*{yoff},setsar=1,{LOOK}[v];"
        f"[1]format=rgba,fade=t=in:st=0.1:d=0.18:alpha=1[c];[v][c]overlay=0:0")
    run(['-ss',str(ss),'-t',str(src+0.1),'-i',f'{O}/{n}.mov','-loop','1','-t',str(d),'-i',f'{cap}.png','-filter_complex',vf,'-t',str(d)]+ENC+[o]); return o
def end(i,d):
    o=f'{W}/s{i}.mp4'
    run(['-loop','1','-t',str(d),'-i','end.png','-vf',f"scale=2160:3840,zoompan=z='1+0.035*on/({d}*30)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,fade=t=in:st=0:d=0.25",'-t',str(d)]+ENC+[o]); return o
S=[shot(1,51,0.4,1.9,'c1'),
   shot(2,12,3.2,2.4,'c2',speed=1.25),
   shot(3,12,9.8,2.2,'c3'),
   shot(4,148,5.5,2.5,'c4',z=1.25,yoff=0.22),
   shot(5,12,30.6,1.9,'c5'),
   end(6,4.0)]
open('list.txt','w').write(''.join(f"file '{s}'\n" for s in S))
run(['-f','concat','-safe','0','-i','list.txt','-c:v','libx264','-crf','18','-preset','slow','-pix_fmt','yuv420p','-movflags','+faststart','-an',sys.argv[1]])
