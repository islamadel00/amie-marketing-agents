# a'mie ads performance report, March to October 2026 (1280x720 slides, same design system as reports/market-deck).
# Numbers are as supplied by the team from each platform's Ads Manager.
# Usage: python3 -I ads_report_deck.py <out.html>   then: node render_deck.js <out.html> <out.pdf>
import sys
OUT = sys.argv[1]
FONT = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/fonts/n/node_modules/@fontsource-variable'
M = ['مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر']
D = {  # platform: [(spend, orders, revenue) per month]
 'سناب شات': [(5037.49,191,103039.69),(10034.70,516,156921.00),(21064.73,558,209719.05),(20158.31,638,239706.75),(12009.38,692,247853.74),(16094.93,507,166555.13),(19525.16,652,179650.24),(5878.95,369,102434.70)],
 'ميتا': [(1236.30,45,22890.15),(1804.88,69,21736.73),(6954.26,177,71758.16),(12693.83,287,117748.05),(9594.75,359,130181.55),(8060.96,180,60596.06),(11143.16,337,92682.68),(7832.06,111,34069.91)],
 'تيك توك': [(1360.13,25,15511.95),(0,0,0),(450.42,0,0),(4365.85,135,53864.24),(4312.26,147,57037.54),(5827.99,152,54739.83),(9651.12,291,82442.94),(6138.34,152,43384.79)],
 'جوجل': [(0,0,0)]*5 + [(3100.12,78,23212.07),(5137.46,172,50740.67),(7581.19,189,56698.89)],
}
SUB = {'سناب شات': 'حساب: Amie Self Service · العملة الأصلية: دولار', 'ميتا': "حساب: A'MI 96 · العملة الأصلية: دولار",
       'تيك توك': 'حساب: Ami TikTok Ads · العملة: ريال · الصرف بعد الضريبة 15%', 'جوجل': 'حساب: Ami · العملة: ريال · مفيش صرف من مارس ليوليو'}
EXPECT = {'سناب شات': (109803.64, 4123, 1405880.29), 'ميتا': (59320.20, 1565, 551663.29), 'تيك توك': (32106.11, 902, 306981.28), 'جوجل': (15818.77, 439, 130651.63)}
def tot(rows): return (sum(r[0] for r in rows), sum(r[1] for r in rows), sum(r[2] for r in rows))
for k, v in D.items():
    t = tot(v); e = EXPECT[k]
    assert abs(t[0]-e[0]) < 0.06 and t[1] == e[1] and abs(t[2]-e[2]) < 0.06, (k, t, e)
ALL = [tuple(sum(D[k][i][j] for k in D) for j in range(3)) for i in range(8)]
GT = tot(ALL); GT0 = (217048.72, 7029, 2395176.49); assert abs(GT[0]-217048.72) < 0.1 and GT[1] == 7029 and abs(GT[2]-2395176.49) < 0.1, GT

GT = GT0  # totals as reported (the cent-level float drift is dropped)
def n2(x): return f'{x:,.2f}'
def roas(s, r): return f'{r/s:.2f}' if s else '—'
def aov(o, r): return f'{r/o:.2f}' if o else '—'
def bar(s, r, mx=21):
    if not s: return ''
    v = r / s
    return f'<div class="mini"><i style="width:{min(v/mx,1)*100:.0f}%"></i></div>'
def table(rows, labels, total=True, big=False, tsum=None):
    h = '<table class="t sm ad"><tr><th>' + ('المنصة' if big else 'الشهر') + '</th><th>الصرف</th><th>الطلبات</th><th>العائد</th><th>ROAS</th><th></th><th>متوسط السلة</th></tr>'
    for lab, (s, o, r) in zip(labels, rows):
        if not big and s == 0 and o == 0 and lab not in ('أبريل',) and len(rows) == 8 and r == 0 and rows is D['جوجل']: continue
        h += f"<tr><td><b>{lab}</b></td><td class='nm'>{n2(s)}</td><td class='nm'>{o:,}</td><td class='nm'>{n2(r)}</td><td class='nm'><b>{roas(s,r) if (s or o) else '—'}</b></td><td>{bar(s,r)}</td><td class='nm'>{aov(o,r)}</td></tr>"
    if total:
        s, o, r = tsum or tot(rows)
        h += f"<tr class='tt'><td>الإجمالي</td><td class='nm'>{n2(s)}</td><td class='nm'>{o:,}</td><td class='nm'>{n2(r)}</td><td class='nm'>{roas(s,r)}</td><td>{bar(s,r)}</td><td class='nm'>{aov(o,r)}</td></tr>"
    return h + '</table>'

HDR = '<div class="hdr"><img src="../market-deck/a/logo_dark.png" class="lg"><i></i><span>Ads Performance</span><i></i><span>Mar – Oct 2026</span><i></i><span>16 Nov 2026</span></div>'
pages = []
def slide(n, en, a, body, cls=''):
    pages.append(f'<section class="page {cls}">{HDR}<div class="body"><div class="ph"><span class="pnum">{n}</span><div><div class="pen">{en}</div><h2>{a}</h2></div></div>{body}</div><div class="ftr"><span>amie-sa.com · داخلي فقط</span><span>{len(pages)+1:02d}</span></div></section>')

pages.append('''<section class="page cover"><img class="cimg" src="../market-deck/a/cover_full.jpg"><div class="ctop"><img src="../market-deck/a/logo_dark.png" class="lgc"></div>
<div class="ctitle"><div class="cen">ADS PERFORMANCE <span>MAR – OCT 2026</span></div><div class="cline"></div><h1>تقرير أداء الإعلانات</h1><p>مارس – أكتوبر 2026 · سناب شات، ميتا، تيك توك، جوجل</p></div>
<div class="cfoot"><span>amie-sa.com</span><span>تاريخ التقرير: 16 نوفمبر 2026 · داخلي فقط</span></div></section>''')

# 01 summary
kp = f'''<div class="kpis k5"><div class="kpi"><b>{GT[0]:,.0f}</b><span>إجمالي الصرف (ريال)</span></div><div class="kpi"><b>{GT[1]:,}</b><span>الطلبات المنسوبة للإعلانات</span></div>
<div class="kpi"><b>{GT[2]:,.0f}</b><span>العائد المنسوب (ريال)</span></div><div class="kpi"><b>{GT[2]/GT[0]:.2f}</b><span>ROAS الإجمالي</span></div><div class="kpi"><b>{GT[2]/GT[1]:.2f}</b><span>متوسط السلة (ريال)</span></div></div>'''
plat = table([EXPECT[k] for k in D], list(D), big=True, tsum=GT)
defs = '''<div class="card"><h4>المقاييس</h4><ul class="pts" style="font-size:12.5px">
<li><b>الصرف:</b> المبلغ اللي اتصرف على الإعلانات.</li><li><b>الطلبات:</b> عدد عمليات الشراء اللي المنصة نسبتها لإعلاناتها.</li>
<li><b>العائد:</b> قيمة المبيعات اللي المنصة نسبتها لإعلاناتها.</li><li><b>ROAS</b> = العائد ÷ الصرف.</li><li><b>متوسط السلة</b> = العائد ÷ عدد الطلبات.</li></ul>
<p class="note">كل المبالغ بالريال السعودي. ميتا وسناب شات اتحولوا من الدولار بسعر 3.75. صرف تيك توك محسوب بعد ضريبة القيمة المضافة 15%.</p></div>'''
slide('01', 'SUMMARY', 'ملخص المنصات', kp + f'<div class="cols2 r">{plat}{defs}</div>')

# 02 monthly all
slide('02', 'ALL PLATFORMS · MONTH BY MONTH', 'كل المنصات شهر بشهر', table(ALL, M, tsum=GT))

# 03-04 snap, meta
for n, k, en in (('03', 'سناب شات', 'SNAPCHAT'), ('04', 'ميتا', 'META')):
    slide(n, en, k, f'<p class="lede">{SUB[k]}</p>' + table(D[k], M, tsum=EXPECT[k]))

# 05 tiktok + google
tk = f'<div><h4>تيك توك</h4><p class="sub">{SUB["تيك توك"]}</p>{table(D["تيك توك"], M, tsum=EXPECT["تيك توك"])}<p class="note">تيك توك: الوحيدة اللي عليها ضريبة 15%، وإجماليها 4,187.75 ريال.</p></div>'
gg = f'<div><h4>جوجل</h4><p class="sub">{SUB["جوجل"]}</p>{table(D["جوجل"][5:], M[5:], tsum=EXPECT["جوجل"])}</div>'
slide('05', 'TIKTOK & GOOGLE', 'تيك توك وجوجل', f'<div class="cols2 two">{tk}{gg}</div>', 'two')

# 06 notes
notes = [('الـ ROAS بينزل من الصيف.', 'الـ ROAS الإجمالي نزل من 16.8 في يوليو لحوالي 8.6 في أكتوبر، ومتوسط السلة نزل من حوالي 390 لحوالي 285 ريال.'),
 ('ميتا أكتر منصة بتضعف.', 'الـ ROAS بتاعها نزل من 18.5 في مارس لـ 4.35 في أكتوبر.'),
 ('سناب شات هي الأكبر،', 'بس أرقامها غالبًا متضخمة، لأنها بتحسب أي شراء حصل لحد 28 يوم بعد الضغط على الإعلان.'),
 ('أرقام جوجل محتاجة مراجعة.', 'متوسط السلة ثابت تقريبًا على 300 ريال كل شهر، وده غالبًا معناه إن تاج الشراء بيبعت قيمة ثابتة، فالعائد والـ ROAS هناك مش دقيقين.'),
 ('العائد الإجمالي أعلى من المبيعات الفعلية،', 'لأن كل منصة بتحسب نفس الطلب لنفسها. المقياس الحقيقي هو إجمالي الصرف مقارنةً بمبيعات المتجر.')]
steps = ''.join(f'<div class="step"><span>{i+1}</span><p><b>{a}</b> {b}</p></div>' for i, (a, b) in enumerate(notes))
src = '''<div class="card"><h4>مصادر الأرقام</h4><ul class="pts" style="font-size:12.5px">
<li>الأرقام مأخوذة من Ads Manager في كل منصة، على مستوى الحساب كله.</li>
<li>نوافذ الإسناد (Attribution): ميتا 7 أيام بعد الضغط ويوم بعد المشاهدة، وسناب شات 28 يوم بعد الضغط ويوم بعد المشاهدة.</li>
<li>صرف سناب شات في Ads Manager (29,280.97 دولار) أعلى بحوالي 2.3% من المخصوم من الكارت (28,622.99 دولار).</li></ul></div>'''
slide('06', 'KEY NOTES & SOURCES', 'أهم الملاحظات ومصادر الأرقام', f'<div class="steps n5">{steps}</div>{src}', 'notes')

css = f'''@font-face{{font-family:"Readex Pro";src:url("file://{FONT}/readex-pro/files/readex-pro-arabic-wght-normal.woff2");font-weight:160 700;unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}}
@font-face{{font-family:"Readex Pro";src:url("file://{FONT}/readex-pro/files/readex-pro-latin-wght-normal.woff2");font-weight:160 700}}
@font-face{{font-family:"Montserrat";src:url("file://{FONT}/montserrat/files/montserrat-latin-wght-normal.woff2");font-weight:100 900}}
table.t.ad{{font-size:14px}} table.t.ad th{{padding:9px 14px;font-size:12px}} table.t.ad td{{padding:9px 14px}}
table.t .tt td{{font-weight:500;border-top:1px solid #191919;background:#F2E4DF;color:#5E2E21}}
.kpis.k5{{grid-template-columns:repeat(5,1fr)}} .kpi b{{font-size:25px}}
.cols2{{align-items:start}} .mini{{width:120px;height:10px}} .mini i{{background:#5E2E21}}
.two table.t.ad{{font-size:12px}} .two table.t.ad th,.two table.t.ad td{{padding:6px 8px}} .two .mini{{width:60px}}
.cols2.r table.t.ad{{font-size:13px}} .cols2.r table.t.ad th,.cols2.r table.t.ad td{{padding:8px 10px}} .cols2.r .mini{{width:70px}}
.steps.n5{{grid-template-columns:repeat(5,1fr);gap:12px;align-items:stretch}} .notes .body{{gap:18px}} .steps.n5 .step{{padding:14px}} .steps.n5 .step p{{font-size:12.5px;line-height:1.7}}
.lede{{margin-top:-4px}}'''
doc = f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>a\'mie · Ads Performance</title><link rel="stylesheet" href="../market-deck/base.css"><link rel="stylesheet" href="../market-deck/extra.css"><style>{css}</style></head><body>' + ''.join(pages) + '</body></html>'
open(OUT, 'w', encoding='utf-8').write(doc)
print('pages', len(pages), 'totals ok')
