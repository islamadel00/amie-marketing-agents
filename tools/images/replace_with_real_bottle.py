import numpy as np, sys
from PIL import Image, ImageFilter
P='/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e'
M=np.asarray(Image.open('m103.jpg').convert('RGB')).astype(np.float32)
O=np.asarray(Image.open(P+'/images/103.jpg').convert('RGB')).astype(np.float32)
fit=[[0.94,-3.132],[0.88,-7.491],[0.861,-13.192]]
R=np.stack([O[...,c]*fit[c][0]+fit[c][1] for c in range(3)],-1)
u8=lambda a: Image.fromarray(np.clip(a,0,255).astype(np.uint8))
L,Rt,BOT=[int(x) for x in sys.argv[1:4]]
ref=Image.open(P+'/scratchpad/body-glow-reference.jpg').convert('RGB')
rd=np.abs(np.asarray(ref).astype(int)-np.array([234,225,216])).sum(-1)
x0,x1,y0,y1=612,815,455,1250; m=np.zeros((y1-y0,x1-x0),bool)
for y in range(y0,y1):
    xs=np.where(rd[y,616:812]>10)[0]
    if len(xs)>2: m[y-y0,616-x0+xs.min():616-x0+xs.max()+1]=True
b=np.asarray(ref.crop((x0,y0,x1,y1))).astype(np.float32)
sc=(Rt-L)/192; W,H=int((x1-x0)*sc),int((y1-y0)*sc)
b=np.asarray(u8(b).resize((W,H),Image.LANCZOS)).astype(np.float32)
mm=np.asarray(u8(m*255).resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.7))).astype(np.float32)/255
px=L-int((616-x0)*sc); py=BOT-int((1245-y0)*sc)
# shade like the Gemini bottle: per-column luminance ratio over the body band
band=slice(BOT-int(0.55*(BOT-py)),BOT-10)
gcol=M[band,px:px+W].mean(-1).mean(0); rcol=b[int(H*0.55):H-10].mean(-1).mean(0)
ratio=np.clip(gcol/np.maximum(rcol,1),0.6,1.35); ratio=np.convolve(ratio,np.ones(9)/9,'same')
inside=mm[int(H*0.6)].astype(bool) if False else None
b=b*ratio[None,:,None]*np.array([1.02,1.0,0.97])
out=M.copy()
# restore original (toned) where the Gemini bottle/nozzle was, then paste real bottle
gx0,gy0,gx1,gy1=[int(x) for x in sys.argv[4:8]]
fe=np.zeros(M.shape[:2],np.float32); fe[gy0:gy1,gx0:gx1]=1; fe=np.asarray(u8(fe*255).filter(ImageFilter.GaussianBlur(4))).astype(np.float32)[...,None]/255
# only restore where Gemini pixels are bottle-white (keep fingers/hair from Gemini)
white=((M.min(-1)>150)&(np.abs(M[...,0]-M[...,2])<40)).astype(np.float32)
white=np.asarray(u8(white*255).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32)[...,None]/255
k=(fe*white)[...,0]
# fill the old nozzle with the surrounding wall/hair (normalized blur of non-bottle pixels)
keep=(1-np.clip(k*3,0,1))
num=np.stack([np.asarray(Image.fromarray(np.clip(M[...,c]*keep,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(30))).astype(np.float32) for c in range(3)],-1)
den=np.asarray(Image.fromarray((keep*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(30))).astype(np.float32)[...,None]/255
fill=num/np.maximum(den,1e-3)
out=out*(1-k[...,None])+fill*k[...,None]
sub=out[py:py+H,px:px+W]; A=mm[...,None]; out[py:py+H,px:px+W]=sub*(1-A)+b*A
# fingertip back on top
fx0,fy0,fx1,fy1=[int(x) for x in sys.argv[8:12]]
ycc=np.asarray(u8(M).convert('YCbCr')).astype(np.float32); sk=((ycc[...,2]>138)&(ycc[...,1]<125)&(ycc[...,0]>70)).astype(np.float32)
fm=np.zeros(sk.shape,np.float32); fm[fy0:fy1,fx0:fx1]=sk[fy0:fy1,fx0:fx1]
fm=np.asarray(u8(fm*255).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)[...,None]/255
out=out*(1-fm)+M*fm
u8(out).save('m103b.jpg',quality=95); print(px,py,W,H)
