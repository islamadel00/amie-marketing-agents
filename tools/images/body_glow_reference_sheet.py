import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
P='/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad'
F=P+'/fonts/'; ML=lambda s: ImageFont.truetype(F+'Montserrat-Light.ttf',s); MR=lambda s: ImageFont.truetype(F+'Montserrat-Regular.ttf',s)
BG=(244,239,234); INK=(25,25,25); ROSE=(94,46,33); GREY=(133,117,110)
W,H=2400,1500; S=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(S)
def rows_mask(a,bg,thr,x0=0):
    dd=np.abs(a.astype(int)-np.array(bg)).sum(-1); m=np.zeros(dd.shape,bool)
    for y in range(dd.shape[0]):
        xs=np.where(dd[y]>thr)[0]
        if len(xs)>3: m[y,xs.min():xs.max()+1]=True
    return Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
# cutouts
ref=Image.open(P+'/body-glow-reference.jpg').convert('RGB').crop((612,455,815,1250))
pm=rows_mask(np.asarray(ref),(234,225,216),10)
itg=Image.open(P+'/swap/itg_rot.jpg').convert('RGB')
cap=itg.crop((512,300,752,1145)); cm=rows_mask(np.asarray(cap),(255,255,255),16)
stk=Image.open(P+'/swap/stick_up.jpg').convert('RGB').crop((232,125,460,590)); sm=rows_mask(np.asarray(stk),(250,249,246),55)
def place(img,m,h,x,ybottom):
    h=int(h); k=h/img.height; im=img.resize((int(img.width*k),h),Image.LANCZOS); mm=m.resize(im.size,Image.LANCZOS)
    S.paste(im,(x,ybottom-h),mm); return im.width
def label(x,y,t,sub=None):
    d.text((x,y),t,font=MR(26),fill=INK)
    if sub: d.text((x,y+38),sub,font=ML(21),fill=GREY)
# header
d.text((80,60),"a'mie  BODY GLOW  120 ML",font=MR(44),fill=ROSE)
d.text((80,118),"Product reference for image edits: exact shape, proportions, label and scale",font=ML(26),fill=GREY)
base=1300
# 1 front pump
label(80,230,'1  FRONT · PUMP','matte white cylinder, white pump')
place(ref,pm,980,140,base)
# 2 with cap
label(560,230,'2  WITH CAP ON','cap is the same width as the body')
place(cap,cm,980*825/906,600,base)
# 3 true scale
label(1010,230,'3  TRUE SCALE vs. HIGHLIGHTER STICK','same width · bottle ≈ 2× the stick height')
sh=480; bh=int(sh*906/445)     # measured from one photo of both products
wb=place(ref,pm,bh,1090,base); ws=place(stk,sm,sh,1090+wb+70,base)
xs=1090+wb+70+ws+40
for (yt,hh,txt) in [(base-bh,bh,'≈ 2× H'),(base-sh,sh,'H')]:
    xx=xs if hh==sh else 1090-40
    d.line((xx,yt,xx,base),fill=ROSE,width=3); d.line((xx-12,yt,xx+12,yt),fill=ROSE,width=3); d.line((xx-12,base,xx+12,base),fill=ROSE,width=3)
    tw=d.textlength(txt,font=MR(24)); d.text((xx+18 if hh==sh else xx-tw-18,yt+hh/2-14),txt,font=MR(24),fill=ROSE)
d.line((1060,base+6,xs+30,base+6),fill=GREY,width=2)
d.text((1090,base+24),'Body Glow',font=ML(22),fill=GREY); d.text((1090+wb+70,base+24),'stick (Chocolate = same size)',font=ML(22),fill=GREY)
# 4 in hand
label(1830,230,'4  IN HAND · REAL SIZE','fits in one hand, held around the body')
ih=Image.open(P+'/swap/inhand.jpg'); ih=ih.resize((500,int(500*ih.height/ih.width))); ih=ih.crop((0,0,500,min(ih.height,900)))
S.paste(ih,(1830,base-ih.height))
# label text strip
d.text((80,base+80),'LABEL (rose, exact):  BODY GLOW  ·  LIGHTWEIGHT BODY SHIMMER / WATER-LIKE GLOW, / SILKY, LUMINOUS, / SMOOTH SKIN / WITH PERFUME  ·  a\'mie logo  ·  120ML',font=ML(23),fill=INK)
S.save('/home/user/amie-marketing-agents/content/campaigns/2026-11-glow-friday/images/body-glow-reference-sheet.jpg',quality=95)
