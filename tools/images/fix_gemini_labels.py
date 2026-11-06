import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
P='/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e'
G=np.asarray(Image.open(P+'/images/107.webp').convert('RGB')).astype(np.float32)
ref=Image.open(P+'/scratchpad/body-glow-reference.jpg').convert('RGB')
blur=lambda a,r: np.asarray(Image.fromarray(np.clip(a,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r))).astype(np.float32)
def erase_dark(x0,y0,x1,y1,thr=14,bright=150):
    R=G[y0:y1,x0:x1].copy()
    Rm=np.asarray(Image.fromarray(R.mean(-1).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))).astype(np.float32)
    C=np.asarray(Image.fromarray(R.astype(np.uint8)).filter(ImageFilter.MaxFilter(11)).filter(ImageFilter.GaussianBlur(5))).astype(np.float32)
    dk=np.clip(((C-R).sum(-1)-thr)/36,0,1)*(Rm>bright)*(R.mean(-1)>bright-70)   # only on the white bottle, never on skin
    dk=blur(dk*255,1.2)[...]/255
    fe=np.ones(dk.shape,np.float32); fe[:3]=fe[-3:]=0; fe[:,:3]=fe[:,-3:]=0; fe=blur(fe*255,2)/255
    k=(dk*fe)[...,None]; G[y0:y1,x0:x1]=R*(1-k)+C*k
def paste_ref(box,scale,px,py,col,ang=0,op=0.85,thr=28):
    r=ref.crop(box); Rf=np.asarray(r).astype(np.float32); bot=np.percentile(Rf,85,axis=0)[None]
    al=np.clip(((bot-Rf).sum(-1)-thr)/60,0,1); al[:2]=al[-2:]=0; al[:,:2]=al[:,-2:]=0
    A=Image.fromarray((al*255).astype(np.uint8)).resize((int(r.width*scale),int(r.height*scale)),Image.LANCZOS)
    if ang: A=A.rotate(ang,expand=True,resample=Image.BICUBIC)
    A=blur(np.asarray(A).astype(np.float32),0.45)/255*op; h,w=A.shape
    sub=G[py:py+h,px:px+w]; sh=np.clip(sub.mean(-1,keepdims=True)/215,0.7,1.1)
    # only on bottle pixels (keep fingers on top)
    onb=(sub.mean(-1,keepdims=True)>150)&(np.abs(sub[...,:1]-sub[...,2:3])<35)
    A=A[...,None]*onb; G[py:py+h,px:px+w]=sub*(1-A)+np.array(col,np.float32)*sh*A
# Body Glow: wordmark, the half-hidden line, logo
erase_dark(570,515,668,545); erase_dark(566,552,650,582); erase_dark(578,735,668,770)
paste_ref((640,795,772,826),0.70,574,518,(176,118,104))      # BODY GLOW
paste_ref((660,1115,760,1160),0.72,586,738,(214,150,140),op=0.9,thr=20)   # a'mie logo
# Chocolate stick label (light text on brown)
x0,y0,x1,y1=462,388,530,426; R=G[y0:y1,x0:x1].copy()
C=np.asarray(Image.fromarray(R.astype(np.uint8)).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(4))).astype(np.float32)
lt=np.clip(((R-C).sum(-1)-20)/50,0,1); lt=blur(np.asarray(Image.fromarray((lt*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))),1.2)/255
fe=np.ones(lt.shape,np.float32); fe[:3]=fe[-3:]=0; fe[:,:3]=fe[:,-3:]=0; fe=blur(fe*255,2)/255
k=(lt*fe)[...,None]; G[y0:y1,x0:x1]=R*(1-k)+C*k
S=4; L=Image.new('L',(80*S,30*S),0); d=ImageDraw.Draw(L)
d.text((2*S,1*S),'Chocolate',font=ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',14*S),fill=255)
d.text((4*S,18*S),'BODY HIGHLIGHTER STICK',font=ImageFont.truetype(P+'/scratchpad/fonts/Montserrat-Regular.ttf',int(3.0*S)),fill=170)
L=L.resize((80,30),Image.LANCZOS).rotate(-5,expand=True,resample=Image.BICUBIC)
A=blur(np.asarray(L).astype(np.float32),0.35)/255*0.85; h,w=A.shape; px,py=466,388
sub=G[py:py+h,px:px+w]; G[py:py+h,px:px+w]=sub*(1-A[...,None])+np.array([230,214,200],np.float32)*A[...,None]
Image.fromarray(np.clip(G,0,255).astype(np.uint8)).save(P+'/scratchpad/swap/g107fix.jpg',quality=95)
