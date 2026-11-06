"""Merge a same-framing Gemini edit back into the full-res original:
skin tone matched by regression, changed product/hand area pasted from Gemini.
Usage: merge.py orig gem out x0 y0 x1 y1   (box in ORIGINAL pixel coords)"""
import sys, numpy as np
from PIL import Image, ImageFilter
o=Image.open(sys.argv[1]).convert('RGB'); g=Image.open(sys.argv[2]).convert('RGB').resize(o.size, Image.LANCZOS)
O=np.asarray(o).astype(np.float32); Gm=np.asarray(g).astype(np.float32)
x0,y0,x1,y1=map(int,sys.argv[4:8])
ycc=np.asarray(o.convert('YCbCr')).astype(np.float32); Y,Cb,Cr=ycc[...,0],ycc[...,1],ycc[...,2]
skin=(Cr>135)&(Cr<180)&(Cb>80)&(Cb<128)&(Y>40)
outbox=np.ones(skin.shape,bool); outbox[y0:y1,x0:x1]=False
sel=skin&outbox
# per-channel affine fit original->gemini on skin
M=np.zeros((3,2))
for c in range(3):
    M[c]=np.polyfit(O[...,c][sel][::7],Gm[...,c][sel][::7],1)
T=np.stack([O[...,c]*M[c,0]+M[c,1] for c in range(3)],-1)
sm=np.asarray(Image.fromarray((skin*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32)[...,None]/255
R=O*(1-sm)+np.clip(T,0,255)*sm
# changed area from Gemini, only inside the box
d=np.abs(Gm-R).sum(-1); ch=(d>60).astype(np.uint8)*255
box=np.zeros(ch.shape,np.uint8); box[y0:y1,x0:x1]=255
ch=np.minimum(ch,box)
m=Image.fromarray(ch).filter(ImageFilter.MedianFilter(7)).filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(8))
m=np.minimum(np.asarray(m).astype(np.float32), np.asarray(Image.fromarray(box).filter(ImageFilter.GaussianBlur(10))).astype(np.float32))[...,None]/255
res=R*(1-m)+Gm*m
Image.fromarray(np.clip(res,0,255).astype(np.uint8)).save(sys.argv[3],quality=95)
Image.fromarray((m[...,0]*255).astype(np.uint8)).save(sys.argv[3].replace('.jpg','-mask.png'))
print('fit',M.round(3).tolist())
