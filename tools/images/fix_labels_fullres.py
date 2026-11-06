import numpy as np
from PIL import Image, ImageFilter
P='/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e'
G=np.asarray(Image.open('m104.jpg').convert('RGB')).astype(np.float32)
O=np.asarray(Image.open(P+'/images/104.jpg').convert('RGB')).astype(np.float32)
ref=Image.open(P+'/scratchpad/body-glow-reference.jpg').convert('RGB')
u8=lambda a: Image.fromarray(np.clip(a,0,255).astype(np.uint8))
blur=lambda a,r: np.asarray(u8(a).filter(ImageFilter.GaussianBlur(r))).astype(np.float32)
def feather(h,w,b=3):
    fe=np.ones((h,w),np.float32); fe[:b]=fe[-b:]=0; fe[:,:b]=fe[:,-b:]=0; return blur(fe*255,2)/255
def erase(x0,y0,x1,y1,light):
    R=G[y0:y1,x0:x1].copy(); f=ImageFilter.MinFilter(9) if light else ImageFilter.MaxFilter(11)
    C=np.asarray(u8(R).filter(f).filter(ImageFilter.GaussianBlur(4))).astype(np.float32)
    d=(R-C).sum(-1) if light else (C-R).sum(-1)
    k=np.clip((d-16)/40,0,1); k=blur(np.asarray(u8(k*255).filter(ImageFilter.MaxFilter(5))),1.2)/255
    if not light:
        Rm=np.asarray(u8(R.mean(-1)).filter(ImageFilter.MaxFilter(9))).astype(np.float32); k*=(Rm>150)
    k=(k*feather(y1-y0,x1-x0))[...,None]; G[y0:y1,x0:x1]=R*(1-k)+C*k
def light_text_from_orig(x0,y0,x1,y1,dx,dy,sc=1.0,op=0.9):
    R=O[y0:y1,x0:x1]; C=np.asarray(u8(R).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(4))).astype(np.float32)
    al=np.clip(((R-C).sum(-1)-30)/80,0,1)*feather(y1-y0,x1-x0,2); col=R
    A=u8(al*255).resize((int((x1-x0)*sc),int((y1-y0)*sc)),Image.LANCZOS); Cc=u8(col).resize(A.size,Image.LANCZOS)
    A=np.asarray(A).astype(np.float32)[...,None]/255*op; Cc=np.asarray(Cc).astype(np.float32); h,w=A.shape[:2]
    px,py=x0+dx,y0+dy; sub=G[py:py+h,px:px+w]; G[py:py+h,px:px+w]=sub*(1-A)+Cc*A
def paste_ref(box,scale,px,py,col,op=0.85,thr=28):
    r=ref.crop(box); Rf=np.asarray(r).astype(np.float32); bot=np.percentile(Rf,85,axis=0)[None]
    al=np.clip(((bot-Rf).sum(-1)-thr)/60,0,1)*feather(r.height,r.width,2)
    A=u8(al*255).resize((int(r.width*scale),int(r.height*scale)),Image.LANCZOS)
    A=blur(np.asarray(A).astype(np.float32),0.4)/255*op; h,w=A.shape
    sub=G[py:py+h,px:px+w]; sh=np.clip(sub.mean(-1,keepdims=True)/215,0.7,1.1)
    onb=((sub.mean(-1,keepdims=True)>150)&(np.abs(sub[...,:1]-sub[...,2:3])<35)).astype(np.float32)
    A=A[...,None]*onb; G[py:py+h,px:px+w]=sub*(1-A)+np.array(col,np.float32)*sh*A
import sys
bx,by,sc=int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3])
# Chocolate stick: label + logo from the original photo
Os=np.asarray(u8(O).resize((int(2000*1.06),int(1500*1.06)),Image.LANCZOS)).astype(np.float32)
def patch(x0,y0,x1,y1,dx=-8,dy=-8,s=1.06):
    X0,Y0=int(x0*s)-dx,int(y0*s)-dy; p=Os[Y0:Y0+(y1-y0),X0:X0+(x1-x0)].copy(); g=G[y0:y1,x0:x1]
    p=p-p.reshape(-1,3).mean(0)+g.reshape(-1,3).mean(0)          # match local tone
    k=feather(y1-y0,x1-x0,5)[...,None]; G[y0:y1,x0:x1]=g*(1-k)+p*k
patch(1076,612,1142,664); patch(1060,672,1124,716)
# Body Glow: wordmark + small text block from the product photo
x0,y0,x1,y1=bx-3,by-22,bx+int(152*sc)+6,by+int(135*sc)+6
R=G[y0:y1,x0:x1].copy(); prof=np.percentile(R,80,axis=0); prof=blur(prof[None],2)[0] if False else prof
C=np.repeat(prof[None],y1-y0,0)
Rm=np.asarray(u8(R.mean(-1)).filter(ImageFilter.MaxFilter(9))).astype(np.float32)
k=np.clip(((C-R).sum(-1)-12)/36,0,1)*(Rm>150); k=blur(np.asarray(u8(k*255).filter(ImageFilter.MaxFilter(5))),1.2)/255
k=(k*feather(y1-y0,x1-x0,4))[...,None]; G[y0:y1,x0:x1]=R*(1-k)+C*k
paste_ref((628,792,780,927),sc,bx,by,(176,118,104))
u8(G).save(P+'/scratchpad/swap/m104fix.jpg',quality=95)
