import subprocess,sys
O='../orig'
ENC=['-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-r','30','-an']
def run(a): subprocess.run(['ffmpeg','-loglevel','error','-y']+a,check=True)
def shot(i,n,ss,d,bg,crop,speed=1.0):
    o=f's{i}.mp4'; w,h,x,y=crop
    fc=(f"[0]setpts=PTS/{speed},fps=30,crop={w}:{h}:{x}:{y},scale=860:1290:flags=lanczos,unsharp=5:5:0.6,eq=contrast=1.03:saturation=1.04,format=rgba[v];"
        f"[2]format=gray[m];[v][m]alphamerge[vm];[1][vm]overlay=110:380:shortest=0[o]")
    run(['-ss',str(ss),'-t',str(d*speed+0.1),'-i',f'{O}/{n}.mov','-loop','1','-t',str(d),'-i',f'{bg}.png','-loop','1','-t',str(d),'-i','m.png','-filter_complex',fc,'-map','[o]','-t',str(d)]+ENC+[o]); return o
def end(i,d):
    o=f's{i}.mp4'
    run(['-framerate','30','-loop','1','-t',str(d),'-i','end.png','-vf',f"scale=2160:3840,zoompan=z='1+0.035*on/({d}*30)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30",'-t',str(d)]+ENC+[o]); return o
S=[shot(1,79,0.0,2.8,'b1',(373,560,53,0)),
   shot(2,44,0.0,2.4,'b2',(415,622,30,230)),
   shot(3,66,1.5,2.8,'b3',(425,637,27,215)),
   shot(4,86,0.0,1.4,'b4',(368,552,56,300)),
   end(5,3.6)]
open('list.txt','w').write(''.join(f"file '{s}'\n" for s in S))
run(['-f','concat','-safe','0','-i','list.txt','-c:v','libx264','-crf','18','-preset','slow','-pix_fmt','yuv420p','-movflags','+faststart','-an',sys.argv[1]])
