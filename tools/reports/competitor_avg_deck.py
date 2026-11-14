# a'mie: average competitor price and pack size per product (1280x720 slides, same design system as reports/market-deck).
# Usage: python3 -I competitor_avg_deck.py <out.html>   then: node render_deck.js <out.html> <out.pdf>
import sys, os, csv, html
OUT = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = ROOT + '/research/market-2026-11/'
A = ROOT + '/reports/market-deck/'
FONT = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/fonts/n/node_modules/@fontsource-variable'
S = list(csv.DictReader(open(R + '08-avg-price-size-summary.csv', encoding='utf-8-sig')))
ROWS = list(csv.DictReader(open(R + '08-avg-price-size-rows.csv', encoding='utf-8-sig')))
AR = {'Deep Tan': 'ديب تان (زيت تان)', 'Red Cherry': 'ريد تشيري (كريم تان)', 'Glittery Gold': 'قلتري قولد (جل تان)',
      'Body Glow': 'لمعة الجسم', 'Body Highlighter': 'هايلايتر الجسم (ستيك)', 'Hair Wax': 'واكس الشعر',
      'Sleek Secret': 'ماسكارا الشعر', 'Sleek Brush': 'فرشاة سليك', 'Sea Salt Scrub': 'سكراب ملح البحر',
      'Whipped Body Butter': 'زبدة الجسم المخفوقة', 'Foot Cream': 'كريم القدمين', 'Hand Cream': 'كريم اليدين',
      'Lip Plump': 'مرطب الشفاه', 'Flora / Natura': 'معطر الجسم فلورا / ناتورا', "a'musk": "مسك a'musk"}
def ar(p):
    for k, v in AR.items():
        if p.startswith(k): return v
    return p
UNIT = {'Foot Cream': 'مل/جم', 'Hair Wax': 'مل/جم', 'Sea Salt Scrub': 'مل/جم', 'Whipped Body Butter': 'مل/جم', 'Body Highlighter': 'جم'}
def unit(p):
    for k, v in UNIT.items():
        if p.startswith(k): return v
    return 'مل'
def chip(txt, c): return f'<span class="ix {c}">{txt}</span>'
def size_verdict(s):
    if not s['avg_size'] or not s['our_size']: return chip('—', 'w')
    a, o = float(s['avg_size_x']), float(s['our_size'])
    if abs(a - o) / o <= 0.15: return chip('قريب من حجمنا', 'g')
    return chip('أكبر من حجمنا', 'b') if a > o else chip('أصغر من حجمنا', 'w')
def price_verdict(s):
    a, o = float(s['avg_now_x']), float(s['our_price'])
    d = (o - a) / a * 100
    if abs(d) <= 10: return chip('قريب', 'g')
    return chip(f'أغلى {d:.0f}%', 'b') if d > 0 else chip(f'أرخص {-d:.0f}%', 'g')
WEAK = {'Red Cherry': 'كلهم Carrot Sun', 'Glittery Gold': '5 منافسين بس', 'Body Highlighter': 'ستيكات وش', 'Sleek Brush': 'فرشتين مستوردتين', 'Hand Cream': '3 منافسين بس', 'Lip Plump': 'منافسين اتنين بس', "a'musk": 'تلات زيوت مسك بس'}
def weak(p):
    for k, v in WEAK.items():
        if p.startswith(k): return f" <small>· {v}</small>"
    return ''

HDR = '<div class="hdr"><img src="../market-deck/a/logo_dark.png" class="lg"><i></i><span>Competitor Price &amp; Size</span><i></i><span>VOL 1.0</span><i></i><span>14 Nov 2026</span></div>'
pages = []
def slide(n, en, a, body, cls=''):
    pages.append(f'<section class="page {cls}">{HDR}<div class="body"><div class="ph"><span class="pnum">{n}</span><div><div class="pen">{en}</div><h2>{a}</h2></div></div>{body}</div><div class="ftr"><span>amie-sa.com · داخلي فقط</span><span>{len(pages)+1:02d}</span></div></section>')

# cover
pages.append('''<section class="page cover"><img class="cimg" src="../market-deck/a/cover_full.jpg"><div class="ctop"><img src="../market-deck/a/logo_dark.png" class="lgc"></div>
<div class="ctitle"><div class="cen">COMPETITOR PRICE &amp; SIZE <span>VOL 1.0</span></div><div class="cline"></div><h1>متوسط سعر وحجم المنافسين</h1><p>لكل منتج من منتجات a'mie · السوق السعودي · مراجعة ثانية على الويب يوم 14 نوفمبر 2026</p></div>
<div class="cfoot"><span>amie-sa.com</span><span>نوفمبر 2026 · داخلي فقط</span></div></section>''')

# 01 summary
total = sum(int(s['n']) for s in S); sa = sum(int(s['n_saudi']) for s in S); w = sum(int(s['n_rechecked']) for s in S)
exp = [s for s in S if (float(s['our_price']) - float(s['avg_now_x'])) / float(s['avg_now_x']) > 0.10]
big = [s for s in S if s['avg_size_x'] and s['our_size'] and float(s['avg_size_x']) > float(s['our_size']) * 1.15]
old = sum(int(s['n_old']) for s in S)
kp = f'''<div class="kpis k4"><div class="kpi"><b>{len(S)}</b><span>منتج a'mie في المقارنة</span></div><div class="kpi"><b>{total}</b><span>منتج منافس محسوب</span></div>
<div class="kpi"><b>{sa}</b><span>منهم من براندات سعودية</span></div><div class="kpi"><b>{w}</b><span>منتج اتراجع أو اتضاف يوم 14 نوفمبر</span></div></div>'''
body = kp + f'''<div class="cols2"><div class="card"><h4>النتيجة</h4><ul class="pts">
<li>a'mie <b>أغلى من متوسط السوق في {len(exp)} منتج من {len(S)}</b>. الفرشاة أرخص، ومرطب الشفاه قريب (منافسين اتنين بس). زبدة الجسم أقرب منتج للمتوسط (أغلى 11%).</li>
<li>المنافسين <b>أحجامهم أكبر في {len(big)} منتجات</b>: التان بأنواعه، الواكس، السكراب، كريم القدمين وكريم اليدين. الحجم قريب من حجمنا في لمعة الجسم وزبدة الجسم ومعطر الجسم ومرطب الشفاه.</li>
<li>قدام <b>البراندات السعودية</b> الفرق أصغر في سعر العلبة: قريبين في زيت التان والسكراب والماسكارا ومرطب الشفاه، وأغلى في اللمعة والواكس والمسك والمعطرات. في سعر الـ100 مل a'mie أغلى في التان والسكراب، لأن عبواتهم أكبر.</li>
<li>كريم القدمين: المتوسط 47 ر.س لعلبة 108 مل/جم، يعني a'mie أغلى. ترشيح رفع سعره في التقرير الأول محتاج مراجعة.</li></ul></div>
<div class="card"><h4>الطريقة</h4><ul class="pts">
<li><b>سعر البيع</b> = اللي العميلة بتدفعه اليوم (سعر العرض لو فيه عرض).</li>
<li>المصادر: صفحات المنتجات عند المتاجر والبراندات، وأول نتايج نون وأمازون ونهدي والدواء وواتسونز وسيفورا.</li>
<li>كل منتج منافس محسوب مرة واحدة، والروايح والألوان من نفس المنتج متجمعة في صف واحد.</li>
<li>اتشالت: المجموعات، النتايج غير المطابقة، بخاخات العطر "أول أوفر"، ماسكات الشفاه، وسعرين شاذين (Tom Ford 502، Tree Hut 13).</li>
<li>متوسط الحجم محسوب على المنتجات اللي حجمها مكتوب بس.</li>
<li>أسعار a'mie من زد يوم 14 نوفمبر (زبدة الجسم 119، مرطب الشفاه 65، الهايلايتر 79).</li>
<li>{old} من {total} منتج لسه بسعر 3 نوفمبر. الأسعار زي ما هي معروضة، من غير الشحن.</li></ul></div></div>'''
slide('01', 'SUMMARY', 'الخلاصة', body, 's01')

# 02 main table
tr = ''
for s in S:
    p = s['product']; u = unit(p)
    osz = f"{s['our_size']} مل" if s['our_size'] else '—'
    asz = f"{s['avg_size']} {u}" if s['avg_size'] else '—'
    same = f"{s['n_same_size']} من {s['n_with_size']}" if s['n_with_size'] != '0' else '—'
    tr += f"<tr><td><b>{ar(p)}</b>{weak(p)}</td><td class='sz'>{osz}</td><td class='nm'>{s['our_price']}</td><td class='nm'>{s['n']}</td><td class='nm'><b>{s['avg_now']}</b></td><td class='nm'>{s['median_now']}</td><td class='nm'>{s['min_now']} – {s['max_now']}</td><td>{price_verdict(s)}</td><td class='sz'><b>{asz}</b></td><td class='sz'>{same}</td><td>{size_verdict(s)}</td></tr>"
tbl = f'''<table class="t sm pr"><tr><th>منتج a'mie</th><th>حجمنا</th><th>سعرنا</th><th>عدد المنافسين</th><th>متوسط سعر بيعهم</th><th>الوسيط</th><th>أقل – أعلى</th><th>سعرنا مقابل المتوسط</th><th>متوسط حجمهم</th><th>بنفس حجمنا</th><th>الحجم</th></tr>{tr}</table>
<p class="note">الأسعار بالريال السعودي. الوسيط = السعر اللي في النص، وبيتأثر أقل بالأسعار الشاذة. "قريب من حجمنا" = فرق 15% أو أقل. "بنفس حجمنا" = عدد المنتجات اللي فرق حجمها 10% أو أقل، من اللي حجمهم مكتوب.</p>'''
slide('02', 'PRICE & SIZE BY PRODUCT', 'لكل منتج: متوسط سعر بيع المنافسين ومتوسط الحجم', tbl, 'tight')

# 03 saudi + per 100
tr = ''
for s in S:
    p = s['product']; u = unit(p)
    if s['n_saudi'] == '0':
        sa_p = sa_s = '—'; v = chip('مفيش منافس سعودي', 'w')
    else:
        sa_p = s['saudi_avg_now']; sa_s = f"{s['saudi_avg_size']} {u}" if s['saudi_avg_size'] else 'غير مكتوب'
        d = (float(s['our_price']) - float(s['saudi_avg_now_x'])) / float(s['saudi_avg_now_x']) * 100
        v = chip('قريب', 'g') if abs(d) <= 10 else (chip(f'أغلى {d:.0f}%', 'b') if d > 0 else chip(f'أرخص {-d:.0f}%', 'g'))
    o100 = s['our_per100'] or '—'; a100 = s['avg_per100'] or '—'
    if p.startswith('Body Highlighter'): o100 = a100 = '—'; v100 = chip('—', 'w')
    elif s['our_per100'] and s['avg_per100']:
        r = float(s['our_per100']) / float(s['avg_per100'])
        v100 = chip(f'×{r:.1f}', 'b' if r > 1.1 else 'g')
    else: v100 = chip('—', 'w')
    tr += f"<tr><td><b>{ar(p)}</b></td><td class='nm'>{s['our_price']}</td><td class='nm'>{s['n_saudi']}</td><td class='nm'><b>{sa_p}</b></td><td class='sz'>{sa_s}</td><td>{v}</td><td class='nm'>{o100}</td><td class='nm'>{a100}</td><td>{v100}</td></tr>"
tbl = f'''<table class="t sm pr"><tr><th>منتج a'mie</th><th>سعرنا</th><th>عدد المنافسين السعوديين</th><th>متوسط سعر بيعهم</th><th>متوسط حجمهم</th><th>سعرنا مقابلهم</th><th>سعرنا لكل 100</th><th>متوسط السوق لكل 100</th><th>سعرنا كام مرة السوق</th></tr>{tr}</table>
<p class="note">البراندات السعودية: Surge، Waves، Besito، Ladeena، Jayla، Clara، Hearts، MZN، Cotton Skin، Clavar، Sunkissed، الماجد للعود. Hearts جنسيتها مش مؤكدة. "لكل 100" = سعر 100 مل أو 100 جم على المنتجات اللي حجمها مكتوب بس. الهايلايتر من غير مقارنة لأن المنافسين بالجرام. لما عدد المنافسين السعوديين 1 أو 2، المتوسط ضعيف.</p>'''
slide('03', 'SAUDI BRANDS & PRICE PER 100', 'قدام البراندات السعودية، وسعر الـ100 مل/جم', tbl, 'tight')

# 04 web re-check
ch = [r for r in ROWS if 'price changed' in r['flag']]
new = [r for r in ROWS if '; new' in r['flag']]
sz = [r for r in ROWS if 'size found' in r['flag']]
def tb(rows, cols, fn):
    return "<table class='t sm pr'><tr>" + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>' + ''.join('<tr>' + ''.join(f"<td class='{k}'>{v}</td>" for k, v in fn(r)) + '</tr>' for r in rows) + '</table>'
def szar(r): return f"{r['size']} {'مل' if r['unit']=='ml' else 'جم'}" if r['size'] != 'MISSING' else 'غير مكتوب'
nmp = lambda r: f"{html.escape(r['brand'])} · {html.escape(r['product'])}"
c1 = tb(ch, ['المنتج', 'اليوم', '3 نوفمبر'], lambda r: [('nm', nmp(r)), ('nm', f"<b>{r['price_now_sar']}</b>"), ('nm', r['flag'].split('was ')[1].rstrip(')').replace(' on promo', ''))])
c2 = tb(new, ['المنتج', 'السعر', 'الحجم'], lambda r: [('nm', nmp(r)), ('nm', f"<b>{r['price_now_sar']}</b>"), ('sz', szar(r))])
c3 = tb(sz, ['المنتج', 'السعر', 'الحجم'], lambda r: [('nm', nmp(r)), ('nm', r['price_now_sar']), ('sz', f"<b>{szar(r)}</b>")])
body = f'''<div class="cols3 wb"><div><h4>أسعار اتغيرت من 3 نوفمبر</h4>{c1}
<p class="note">Besito نزّل السعر (المشطوب 150 و160). The Body Shop رجع للسعر العادي بعد عرض 74. Carrot Sun في نهدي طلع من 80.50.</p>
<h4 style="margin-top:14px">ما اتغيرش</h4><p style="font-size:12px;direction:ltr;text-align:right;font-family:Montserrat">Slick Hair 110 / 87 · Clara 94 / 83 / 47 · Surge 195 · Waves 128.70 / 156.52 · Puravie 164 · Laneige 135 · Sol de Janeiro 125 · Beesline 83.95 / 109 · Almajed 59.01</p></div>
<div><h4>منافسين جداد اتضافوا</h4>{c2}</div>
<div><h4>أحجام كانت ناقصة ولقيناها</h4>{c3}</div></div>'''
slide('04', 'WEB RE-CHECK · 14 NOV', 'المراجعة الثانية على الويب: إيه اللي اتغير', body)

# 05-06 saudi rows detail
sr = [r for r in ROWS if 'saudi' in r['flag']]
def det(rows):
    t = ''; last = ''
    for r in rows:
        if r['amie_product'] != last:
            t += f"<tr class='cat'><td colspan='5'>{ar(r['amie_product'])}</td></tr>"; last = r['amie_product']
        size = f"{r['size']} {'مل' if r['unit']=='ml' else 'جم'}" if r['size'] != 'MISSING' else 'غير مكتوب'
        reg = r['price_regular_sar'] if r['price_regular_sar'] != r['price_now_sar'] else '—'
        p100 = r['price_per_100_now'] if r['price_per_100_now'] != 'MISSING' else '—'
        t += f"<tr><td class='nm'>{html.escape(r['brand'])}</td><td class='nm'>{html.escape(r['product'])}</td><td class='sz'>{size}</td><td class='nm'><b>{r['price_now_sar']}</b></td><td class='nm'>{reg}</td></tr>"
    return f"<table class='t sm pr'><tr><th>البراند</th><th>المنتج</th><th>الحجم</th><th>سعر البيع</th><th>السعر قبل العرض</th></tr>{t}</table>"
prods = []
for r in sr:
    if r['amie_product'] not in prods: prods.append(r['amie_product'])
tot = len(sr) + len(prods); parts = [[]]; acc = 0
for pr in prods:
    grp = [r for r in sr if r['amie_product'] == pr]
    if acc + len(grp) + 1 > tot / 4 + 2 and len(parts) < 4: parts.append([]); acc = 0
    parts[-1] += grp; acc += len(grp) + 1
while len(parts) < 4: parts.append([])
slide('05', 'SAUDI BRANDS · DETAIL 1/2', 'المنافسين السعوديين بالتفصيل (1 من 2)', f"<div class='cols2'>{det(parts[0])}{det(parts[1])}</div>", 's05')
slide('06', 'SAUDI BRANDS · DETAIL 2/2', 'المنافسين السعوديين بالتفصيل (2 من 2)', f"<div class='cols2'>{det(parts[2])}{det(parts[3]) if parts[3] else ''}</div>", 's05')

# 06 limits
body = '''<div class="cols2"><div class="card"><h4>حدود الأرقام</h4><ul class="pts">
<li><b>المتوسط بيخلط الرخيص بالغالي:</b> براندات صيدليات بـ15–30 ر.س مع براندات فاخرة. للمقارنة المباشرة، جدول البراندات السعودية أدق.</li>
<li><b>أحجام ناقصة:</b> Clara وBesito وMZN وClavar وSunkissed مش كاتبين الحجم، وHearts كاتبة حجم البودي جلو بس. في الواكس 4 من 10 حجمهم معروف، وفي الماسكارا 3 من 8.</li>
<li><b>مقارنات ضعيفة:</b> كريم التان (كل المنافسين Carrot Sun)، جل التان (5 منافسين)، الهايلايتر (ستيكات وش بالجرام)، الفرشاة، كريم اليدين، مرطب الشفاه، والمسك (2 أو 3 منافسين لكل واحد).</li>
<li><b>مل وجرام:</b> السكراب والزبدة والواكس عندنا بالمل، وأغلب المنافسين بالجرام. المقارنة تقريبية.</li>
<li><b>أسعار بالدولار:</b> Clara وJayla عرضوا السعر بالدولار، واتحوّل بسعر 3.75. النتيجة طابقت أسعار 3 نوفمبر بالريال.</li>
<li><b>Waves:</b> أسعارها على الأغلب من غير الضريبة. مع الضريبة تبقى 180 بدل 156.52، و148 بدل 128.70، و78 بدل 67.83. استخدمنا السعر الظاهر.</li></ul></div>
<div class="card"><h4>صفحات ما اتفتحتش يوم 14 نوفمبر</h4><ul class="pts">
<li>نون، الدواء، Desertcart، ليمون، Beauty Bay، كارفور، سنتربوينت، FirstCry: الموقع رفض الفتح الآلي. أسعارهم فضلت بتاريخ 3 نوفمبر.</li>
<li>Hearts وMZN: المتجر ما عرضش المنتجات المطلوبة، فأسعارهم بتاريخ 3 نوفمبر.</li></ul>
<h4 style="margin-top:14px">الخطوة الجاية المقترحة</h4><ul class="pts">
<li>نسأل Clara وHearts وBesito عن الحجم، أو نشتري عينة.</li>
<li>نعيد الفحص بعد الجمعة البيضاء، لأن الأسعار بتتحرك دلوقتي.</li>
<li>الملفات الكاملة: <span class="nm">research/market-2026-11/08-avg-price-size-rows.csv</span></li></ul></div></div>'''
slide('07', 'LIMITS', 'حدود الأرقام واللي ما قدرناش نتأكد منه', body)

css = f'''@font-face{{font-family:"Readex Pro";src:url("file://{FONT}/readex-pro/files/readex-pro-arabic-wght-normal.woff2");font-weight:160 700;unicode-range:U+0600-06FF,U+0750-077F,U+FB50-FDFF,U+FE70-FEFF,U+200C-200F}}
@font-face{{font-family:"Readex Pro";src:url("file://{FONT}/readex-pro/files/readex-pro-latin-wght-normal.woff2");font-weight:160 700}}
@font-face{{font-family:"Montserrat";src:url("file://{FONT}/montserrat/files/montserrat-latin-wght-normal.woff2");font-weight:100 900}}
table.t.sm{{font-size:12px}} table.t.sm th{{white-space:normal;padding:6px 8px;line-height:1.35}} table.t.sm td{{padding:4.5px 8px}}
table.t.pr small.d{{display:block;font-size:9.5px;color:#6B595C;line-height:1.3}}
table.t tr.cat td{{background:#F2E4DF;color:#5E2E21;font-weight:500;font-size:11px;padding:3px 10px}}
.kpis.k4{{grid-template-columns:repeat(4,1fr)}} .ix{{white-space:nowrap;direction:rtl;font-family:'Readex Pro';font-weight:400;font-size:11px}} td.sz{{white-space:nowrap}}
.tight table.t.sm{{font-size:11.5px}} .tight table.t.sm td{{padding:3.2px 8px}} .tight .note{{margin-top:2px;font-size:10.5px}} .tight .ph{{padding-bottom:6px}} .tight .body{{gap:8px}} .cols2{{align-items:start}} .cols3{{align-items:start}}
.s01 .pts{{font-size:12.5px}} .s01 .kpi{{padding:9px 14px}} .s01 .kpi b{{font-size:23px}} .s01 .card{{padding:13px 16px}}
.wb table.t.sm{{font-size:11px}} .wb table.t.sm td{{padding:4px 8px}} .wb td.nm{{text-align:left}} .wb th:first-child{{text-align:left}}
.s05 table.t.sm{{font-size:11.5px}} .s05 table.t.sm td{{padding:4px 8px}}'''
doc = f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>a\'mie · Competitor Price &amp; Size</title><link rel="stylesheet" href="../market-deck/base.css"><link rel="stylesheet" href="../market-deck/extra.css"><style>{css}</style></head><body>' + ''.join(pages) + '</body></html>'
open(OUT, 'w', encoding='utf-8').write(doc)
print('pages', len(pages))
