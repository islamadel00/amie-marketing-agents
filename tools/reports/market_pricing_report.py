# Builds the a'mie market + pricing + 6-month performance report (HTML -> PDF).
import json, sys
SP = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad'
OUT = sys.argv[1]
F = SP + '/fonts'

INK, GOLD, BLUE, GREY, LINE, CREAM, RED = '#111111', '#A8834A', '#5F7A99', '#BDB9B2', '#E4E2DE', '#F6F5F3', '#A24B3B'

def fmt(x, d=0):
    return f"{x:,.{d}f}"

# ---------------- data ----------------
months = ['مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر']
orders = [1165, 1172, 1340, 856, 1069, 962]
items = [447483, 446532, 495128, 288652, 328516, 286138]
paid = [475521, 448194, 504140, 287790, 298983, 274450]
NET_TOTAL = 1847749
k = NET_TOTAL / sum(items)
net = [round(i * k) for i in items]
ads = {'سناب': [21064, 20160, 12008, 16095, 19526, 5711],
       'ميتا': [6954, 12694, 9595, 8061, 11143, 7653],
       'تيك توك': [392, 3796, 3750, 5068, 8392, 5225],
       'جوجل': [0, 0, 0, 3100, 5137, 7353]}
ads_m = [sum(v[i] for v in ads.values()) for i in range(6)]
inf_m = [3000, 65550, 3000, 21250, 24101, 34500]
coupon = [4.1, 48.2, 39.6, 62.1, 80.6, 71.1]
aov = [p / o for p, o in zip(paid, orders)]
mk_m = [a + b for a, b in zip(ads_m, inf_m)]
mk_pct = [m / n * 100 for m, n in zip(mk_m, net)]

# ---------------- svg helpers ----------------
def t(x, y, s, size=9, fill=INK, anchor='middle', w=400, fam="Readex Pro"):
    anchor = {'start': 'end', 'end': 'start'}.get(anchor, anchor)  # document is RTL: SVG anchors flip
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{w}" font-family="{fam}">{s}</text>'

def chart_monthly():
    W, H, L, R, T, B = 680, 300, 20, 60, 30, 46
    pw, ph = W - L - R, H - T - B
    mx = 420000
    g = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for v in range(0, mx + 1, 100000):
        y = T + ph - v / mx * ph
        g.append(f'<line x1="{L}" x2="{W-R}" y1="{y}" y2="{y}" stroke="{LINE}" stroke-width="1"/>')
        g.append(t(W - R + 6, y + 3, f'{v//1000}K' if v else '0', 8, '#777', 'start', fam='Montserrat'))
    bw = pw / 6
    for i in range(6):
        cx = W - R - bw * (i + 0.5)  # RTL: May on the right
        h = net[i] / mx * ph
        g.append(f'<rect x="{cx-26}" y="{T+ph-h}" width="24" height="{h}" fill="{INK}"/>')
        y0 = T + ph
        ha = ads_m[i] / mx * ph; hi = inf_m[i] / mx * ph
        g.append(f'<rect x="{cx+2}" y="{y0-ha}" width="24" height="{ha}" fill="{GOLD}"/>')
        g.append(f'<rect x="{cx+2}" y="{y0-ha-hi}" width="24" height="{hi}" fill="{BLUE}"/>')
        g.append(t(cx - 14, T + ph - h - 5, f'{net[i]/1000:.0f}K', 8, INK, fam='Montserrat', w=500))
        g.append(t(cx + 14, y0 - ha - hi - 5, f'{mk_m[i]/1000:.0f}K', 8, '#555', fam='Montserrat'))
        g.append(t(cx, H - B + 16, months[i], 9.5))
        g.append(t(cx, H - B + 31, f'{mk_pct[i]:.0f}٪ تسويق', 8, RED if mk_pct[i] > 20 else '#555'))
    lg = [(INK, 'صافي المبيعات (من غير ضريبة)'), (GOLD, 'إعلانات'), (BLUE, 'مؤثرين')]
    x = W - R
    for c, s in lg:
        g.append(f'<rect x="{x-10}" y="8" width="10" height="10" fill="{c}"/>')
        g.append(t(x - 14, 17, s, 8.5, '#333', 'end'))
        x -= 14 + len(s) * 5.2 + 22
    g.append('</svg>')
    return ''.join(g)

def chart_coupon():
    W, H, L, R, T, B = 680, 210, 46, 46, 26, 30
    pw, ph = W - L - R, H - T - B
    g = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for v in (0, 25, 50, 75, 100):
        y = T + ph - v / 100 * ph
        g.append(f'<line x1="{L}" x2="{W-R}" y1="{y}" y2="{y}" stroke="{LINE}"/>')
        g.append(t(W - R + 6, y + 3, f'{v}%', 8, '#777', 'start', fam='Montserrat'))
        g.append(t(L - 6, y + 3, f'{200 + v*2.4:.0f}', 8, '#777', 'end', fam='Montserrat'))
    bw = pw / 6
    pc, pa = [], []
    for i in range(6):
        cx = W - R - bw * (i + 0.5)
        yc = T + ph - coupon[i] / 100 * ph
        ya = T + ph - (aov[i] - 200) / 240 * ph
        pc.append(f'{cx},{yc}'); pa.append(f'{cx},{ya}')
        g.append(t(cx, H - 8, months[i], 9.5))
        g.append(t(cx, yc - 8, f'{coupon[i]:.0f}%', 8.5, RED, fam='Montserrat', w=500))
        g.append(t(cx, ya + 15, f'{aov[i]:.0f}', 8.5, INK, fam='Montserrat', w=500))
    g.append(f'<polyline points="{" ".join(pc)}" fill="none" stroke="{RED}" stroke-width="2.2"/>')
    g.append(f'<polyline points="{" ".join(pa)}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-dasharray="5 3"/>')
    for p in pc:
        x, y = p.split(','); g.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{RED}"/>')
    for p in pa:
        x, y = p.split(','); g.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{INK}"/>')
    g.append(t(W - R, 12, '— نسبة الطلبات بكوبون (يمين)', 8.5, RED, 'end'))
    g.append(t(L + 170, 12, '- - متوسط قيمة الطلب بالريال (شمال)', 8.5, INK, 'end'))
    g.append('</svg>')
    return ''.join(g)

def chart_roas():
    rows = [('جوجل', 7.93, 5.13), ('سناب', 11.63, 2.24), ('ميتا', 7.73, 1.27), ('تيك توك', 10.02, 1.25)]
    W, H = 680, 190
    L, R = 30, 110
    pw = W - L - R
    mx = 12
    g = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for i, (n, p, ga) in enumerate(rows):
        y = 26 + i * 40
        g.append(t(W - 8, y + 14, n, 10, INK, 'end', w=500))
        wp = p / mx * pw; wg = ga / mx * pw
        g.append(f'<rect x="{W-R-wp}" y="{y}" width="{wp}" height="13" fill="{GREY}"/>')
        g.append(f'<rect x="{W-R-wg}" y="{y+15}" width="{wg}" height="13" fill="{INK if ga >= 2 else RED}"/>')
        g.append(t(W - R - wp - 6, y + 10, f'{p:.1f}', 8.5, '#666', 'end', fam='Montserrat'))
        g.append(t(W - R - wg - 6, y + 25, f'{ga:.2f}', 9, INK, 'end', fam='Montserrat', w=600))
    g.append(f'<rect x="{W-R-10}" y="4" width="10" height="9" fill="{GREY}"/>' + t(W - R - 14, 12, 'ROAS حسب المنصة نفسها', 8.5, '#555', 'end'))
    g.append(f'<rect x="{W-R-190}" y="4" width="10" height="9" fill="{INK}"/>' + t(W - R - 194, 12, 'ROAS حسب GA4 (الأقرب للحقيقة)', 8.5, '#555', 'end'))
    g.append('</svg>')
    return ''.join(g)

def chart_position():
    # unit prices in SAR (verified 3 Nov where available)
    rows = [
        ('زيت تان', 45, [156.5, 195, 150], [80.5, 92], 159),
        ('لمعة الجسم', 56, [96, 160], [160, 129.95], 176),
        ('هايلايتر ستيك', 47, [35.7], [], 79),
        ('واكس الشعر', 25, [94], [110], 129),
        ('ماسكارا الشعر', 40, [83], [87, 73], 75),
        ('زبدة الجسم', 29, [128.7, 100, 85], [74], 119),
        ('سكراب الجسم', 43, [128.7, 150, 90], [], 119),
        ('كريم القدمين', 35, [], [47.94, 164], 75),
        ('بودي مست', 25, [55, 70, 150], [50, 73], 129),
    ]
    W, L, R, T = 680, 18, 110, 34
    rh = 25
    H = T + rh * len(rows) + 28
    pw = W - L - R
    mx = 200
    X = lambda v: W - R - v / mx * pw
    g = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for v in range(0, mx + 1, 50):
        g.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="{T-6}" y2="{H-24}" stroke="{LINE}"/>')
        g.append(t(X(v), H - 10, f'{v}', 8, '#777', fam='Montserrat'))
    for i, (n, mkt, sa, intl, am) in enumerate(rows):
        y = T + i * rh + 10
        g.append(t(W - 8, y + 4, n, 9.5, INK, 'end', w=500))
        allv = [mkt] + sa + intl + [am]
        g.append(f'<line x1="{X(min(allv))}" x2="{X(max(allv))}" y1="{y}" y2="{y}" stroke="#D5D2CC" stroke-width="1.2"/>')
        g.append(f'<rect x="{X(mkt)-4.5}" y="{y-4.5}" width="9" height="9" fill="{GREY}"/>')
        for v in sa: g.append(f'<circle cx="{X(v)}" cy="{y}" r="4.6" fill="{GOLD}"/>')
        for v in intl: g.append(f'<path d="M{X(v)} {y-5.5} L{X(v)+5.5} {y} L{X(v)} {y+5.5} L{X(v)-5.5} {y} Z" fill="{BLUE}"/>')
        g.append(f'<circle cx="{X(am)}" cy="{y}" r="7" fill="{INK}"/>')
        g.append(t(X(am), y - 10, f'{am:g}', 8, INK, fam='Montserrat', w=600))
    lg = [('sq', GREY, 'وسيط نون/أمازون/الصيدليات'), ('c', GOLD, 'براندات سعودية'), ('d', BLUE, 'براندات عالمية (بعد الخصم)'), ('a', INK, "a'mie")]
    x = W - 8
    for kind, c, s in lg:
        if kind == 'sq': g.append(f'<rect x="{x-9}" y="7" width="9" height="9" fill="{c}"/>')
        elif kind == 'd': g.append(f'<path d="M{x-5} 6 L{x} 11.5 L{x-5} 17 L{x-10} 11.5 Z" fill="{c}"/>')
        else: g.append(f'<circle cx="{x-5}" cy="11.5" r="{6 if kind=="a" else 4.6}" fill="{c}"/>')
        g.append(t(x - 14, 15, s, 8.3, '#333', 'end'))
        x -= 14 + len(s) * 4.9 + 24
    g.append('</svg>')
    return ''.join(g)

def chart_market():
    rows = [('العناية بالجسم', 835, 1215, 1800, 'منخفضة–متوسطة'), ('المعطرات والمسك', 958, 1141, 1342, 'منخفضة'),
            ('الهدايا والإكسسوارات', 50, 250, 790, 'منخفضة جداً'), ('تصفيف الشعر (للستات)', 85, 160, 290, 'منخفضة–متوسطة'),
            ('اللمعة والهايلايتر', 25, 60, 150, 'منخفضة'), ('التان', 30, 60, 120, 'منخفضة')]
    W, L, R, T, rh = 680, 70, 150, 22, 30
    H = T + rh * len(rows) + 24
    pw = W - L - R
    mx = 1800
    X = lambda v: W - R - v / mx * pw
    g = [f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg">']
    for v in range(0, mx + 1, 300):
        g.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="{T-8}" y2="{H-22}" stroke="{LINE}"/>')
        g.append(t(X(v), H - 8, f'{v:,}', 8, '#777', fam='Montserrat'))
    for i, (n, lo, mid, hi, c) in enumerate(rows):
        y = T + i * rh + 6
        g.append(t(W - 8, y + 4, n, 9.5, INK, 'end', w=500))
        g.append(f'<rect x="{X(hi)}" y="{y-6}" width="{X(lo)-X(hi)}" height="12" fill="#D9D5CE"/>')
        g.append(f'<rect x="{X(mid)-1.5}" y="{y-9}" width="3" height="18" fill="{INK}"/>')
        g.append(t(X(hi) - 6, y + 4, f'{mid:,} مليون', 8.3, INK, 'end', w=500))
    g.append('</svg>')
    return ''.join(g)

# ---------------- tables ----------------
def monthly_table():
    h = '<table><thead><tr><th>الشهر</th><th>الطلبات</th><th>صافي المبيعات</th><th>متوسط الطلب</th><th>إعلانات</th><th>مؤثرين</th><th>إجمالي التسويق</th><th>التسويق ÷ المبيعات</th><th>طلبات بكوبون</th></tr></thead><tbody>'
    for i in range(6):
        cls = ' class="bad"' if mk_pct[i] > 20 else ''
        h += f'<tr><td>{months[i]}</td><td class="num">{fmt(orders[i])}</td><td class="num">{fmt(net[i])}</td><td class="num">{aov[i]:.0f}</td><td class="num">{fmt(ads_m[i])}</td><td class="num">{fmt(inf_m[i])}</td><td class="num">{fmt(mk_m[i])}</td><td class="num"{cls}>{mk_pct[i]:.1f}٪</td><td class="num">{coupon[i]:.0f}٪</td></tr>'
    to, tn = sum(orders), sum(net)
    ta, ti = sum(ads_m), 162669
    h += f'<tr class="tot"><td>الإجمالي</td><td class="num">{fmt(to)}</td><td class="num">{fmt(tn)}</td><td class="num">{sum(paid)/to:.0f}</td><td class="num">{fmt(ta)}</td><td class="num">{fmt(ti)}*</td><td class="num">{fmt(ta+ti)}</td><td class="num">{(ta+ti)/tn*100:.1f}٪</td><td class="num">47٪</td></tr>'
    return h + '</tbody></table>'

prod_rows = [
    # name, net, units, mk total, mk%, coupon%
    ('Summer Set', 662612, 1483, 87606, 13.2, 36.7),
    ('Red Cherry كريم تان', 149517, 892, 16251, 10.9, 27.9),
    ('Hair Set', 139108, 736, 45115, 32.4, 53.0),
    ('واكس الشعر', 107727, 1015, 25921, 24.1, 57.3),
    ('Deep Tan زيت تان', 85970, 663, 20455, 23.8, 51.8),
    ('Glow Set', 78228, 487, 9273, 11.9, 47.6),
    ('Into The Glow', 75789, 355, 35654, 47.0, 74.4),
    ('Body Glow', 71251, 514, 9866, 13.8, 52.7),
    ('Lemongrass Set', 54381, 307, 8240, 15.2, 57.7),
    ('Marshmallow Set', 45689, 584, 16048, 35.1, 54.1),
    ('Natura Body Mist', 38684, 384, 2931, 7.6, 55.2),
    ("a'musk", 37352, 476, 5157, 13.8, 49.6),
    ('Glittery Gold جل تان', 37287, 309, 8035, 21.5, 55.7),
    ('Flora Body Mist', 33593, 334, 1821, 5.4, 53.3),
    ('Chocolate Set', 31813, 398, 18407, 57.9, 51.0),
    ('كريم القدمين', 25448, 434, 1925, 7.6, 54.8),
    ('سكراب الليمون قراس', 21066, 229, 4144, 19.7, 64.7),
    ('Sleek Secret', 19905, 340, 2140, 10.8, 60.9),
    ('ستيك Chocolate', 10792, 166, 14454, 133.9, 52.4),
    ('فرشاة سليك', 8828, 397, 1535, 17.4, 61.5),
]

def product_table():
    h = '<table><thead><tr><th>المنتج</th><th>القطع</th><th>صافي المبيعات</th><th>تسويق (إعلانات + مؤثرين)</th><th>التسويق ÷ المبيعات</th><th>قطع بكوبون</th></tr></thead><tbody>'
    for n, s, u, m, p, c in prod_rows:
        cls = ' class="bad"' if p > 30 else (' class="good"' if p < 12 else '')
        h += f'<tr><td>{n}</td><td class="num">{fmt(u)}</td><td class="num">{fmt(s)}</td><td class="num">{fmt(m)}</td><td class="num"{cls}>{p:.1f}٪</td><td class="num">{c:.0f}٪</td></tr>'
    return h + '</tbody></table>'

# name, price, coupon%, competitor ref, decision, range, cap, note
price_rows = [
    ('التان', [
        ('Summer Set', '482', '37٪', 'مالوش مجموعة منافسة مباشرة', 'تثبيت', '482', '15٪ في الموسم بس', 'أكبر منتج (36٪ من المبيعات). نتأكد من سعره (وسيط القطعة في الطلبات 582)'),
        ('Deep Tan زيت 150 مل', '159', '52٪', 'Surge 195/250 مل · Waves 156.5 · Carrot Sun 80.5 (بعد خصم 50٪)', 'تثبيت + كوبونات أقل', '159', '15٪', 'أغلى في سعر المل من كل المنافسين اللي نعرف حجمهم'),
        ('Red Cherry كريم 200 مل', '199', '28٪', 'Surge زيت 195/250 مل · Beesline 184 قبل الخصم (92 دلوقتي)', 'تثبيت', '199', '10٪', 'من أغلى منتجات الفئة'),
        ('Glittery Gold جل 120 مل', '149', '56٪', 'Surge Glitter Tan 207', 'تثبيت + كوبونات أقل', '149', '15٪', 'نسبة الكوبون عالية (56٪)، فنثبت السعر ونقلل الكوبونات الأول'),
    ]),
    ('اللمعة والهايلايتر', [
        ('Body Glow', '176', '53٪', 'Sol de Janeiro 160 · Tan-Luxe 130 · Hearts 96', 'تثبيت + كوبونات أقل', '176', '15٪', 'أغلى من المنافسين المباشرين (Sol de Janeiro وTan-Luxe وHearts)'),
        ('ستيك الهايلايتر', '79', '52–59٪', 'Hearts 42 (35.70 بعد الخصم)', 'تثبيت', '79', '10٪', 'حوالي ضعف Hearts'),
        ('مجموعات الهايلايتر', '99', '51–54٪', 'Hearts / Besito', 'تثبيت', '99', '15٪', ''),
        ('Into The Glow', '294', '74٪', 'مالوش مقابل مباشر', 'كوبونات أقل أولاً', '294', '15٪', 'أعلى اعتماد على الكوبون في المتجر'),
        ('Glow Set', '199', '48٪', '—', 'تثبيت', '199', '15٪', ''),
    ]),
    ('الشعر', [
        ('واكس الشعر 30 مل', '129', '57٪', 'Clara 94 · Slick Wax Stick 110/50 جم', 'تثبيت (مانرفعش)', '129', '10٪', 'Clara أرخص بـ 35 ريال؛ نبرر السعر بالمحتوى'),
        ('Sleek Secret 15 مل', '75', '61٪', 'Clara 83 · Slick Stick 87/10 مل · Smooth 73/10 مل', 'رفع بعد ظبط الكوبونات', 'من 79 لـ 85', '10٪ (0٪ وقت الاختبار)', 'سعر المل 5 ريال قصاد 7.3–8.7'),
        ('فرشاة سليك', '29', '62٪', 'فرشاة Clara 47 (كانت 59)', 'رفع بعد ظبط الكوبونات', 'من 39 لـ 45', '0٪ (منتج إضافة للسلة)', 'أرخص منتج تقريباً، والخصم عليه مالوش لازمة'),
        ('Hair Set', '282 (زد)', '53٪', 'مجموعة Clara 189 (كانت 304)', 'تثبيت + نتأكد من السعر', '282', '15٪', 'وسيط القطعة في الطلبات 226'),
    ]),
    ('العناية بالجسم', [
        ('كريم القدمين', '75', '55٪', 'Eucerin 47.94 (نهدي، بعد الخصم) · Puravie 164', 'اختبار صغير', 'لـ 79 بس (اختبار)', '10٪ (0٪ وقت الاختبار)', 'نراقب المبيعات 4 أسابيع'),
        ('زبدة الليمون قراس 250 مل', '119', '63٪', 'Waves 128.7 · Ladeena 100 · MZN 85 · Body Shop 74', 'تثبيت', '119', '10٪', 'في نص السوق'),
        ('سكراب الليمون قراس 300 مل', '119', '65٪', 'Waves 128.7/400 مل · Ladeena 150 · MZN 90', 'تثبيت + كوبونات أقل', '119', '10٪', ''),
        ('Lip Plump', '65', '56٪', '—', 'تثبيت', '65', '10٪', ''),
    ]),
    ('المعطرات', [
        ('Flora / Natura Body Mist', '129', '53–55٪', 'MZN 55 · Jayla 70 · VS 50–73', 'تثبيت + كوبونات أقل', '129', '10٪ لوحدها، و15٪ لو جوه مجموعة في الموسم', 'أغلى من أغلب السوق'),
        ("a'musk", '99', '50٪', 'Jayla 80 · Ladeena 75', 'تثبيت', '99', '10٪', ''),
    ]),
]

def price_table():
    h = '<table class="price"><thead><tr><th style="width:17%">المنتج</th><th>السعر الحالي</th><th>قطع بكوبون</th><th style="width:24%">أقرب منافسين (ريال)</th><th>القرار</th><th>النطاق المقترح</th><th>أقصى خصم</th><th style="width:19%">ملاحظة</th></tr></thead><tbody>'
    for cat, rows in price_rows:
        h += f'<tr class="cat"><td colspan="8">{cat}</td></tr>'
        for r in rows:
            up = 'لـ' in r[5]
            h += f'<tr><td>{r[0]}</td><td class="num">{r[1]}</td><td class="num">{r[2]}</td><td class="small">{r[3]}</td><td>{r[4]}</td><td class="num{" up" if up else ""}">{r[5]}</td><td class="small">{r[6]}</td><td class="small">{r[7]}</td></tr>'
    return h + '</tbody></table>'

def breakeven_table():
    rows = [('فرشاة سليك', 29, 39, 397), ('فرشاة سليك', 29, 45, 397), ('Sleek Secret', 75, 79, 340), ('Sleek Secret', 75, 85, 340), ('كريم القدمين', 75, 79, 434)]
    h = '<table><thead><tr><th>المنتج</th><th>من</th><th>لـ</th><th>الزيادة</th><th>القطع في 6 شهور</th><th>الإيراد يفضل زي ما هو لو المبيعات نزلت لحد</th><th>الإيراد الإضافي في 6 شهور لو المبيعات ماقلتش (من غير ضريبة)</th></tr></thead><tbody>'
    for n, a, b, u in rows:
        h += f'<tr><td>{n}</td><td class="num">{a}</td><td class="num">{b}</td><td class="num">+{(b/a-1)*100:.0f}٪</td><td class="num">{u}</td><td class="num">{(1-a/b)*100:.0f}٪</td><td class="num">{fmt(u*(b-a)/1.15)} ريال</td></tr>'
    return h + '</tbody></table>'

# ---------------- html ----------------
css = f"""
@font-face {{ font-family: 'Readex Pro'; src: url('file://{F}/ReadexPro-AR-Regular.ttf'); font-weight: 300 500; }}
@font-face {{ font-family: 'Readex Pro'; src: url('file://{F}/ReadexPro-AR-Bold.ttf'); font-weight: 600 800; }}
@font-face {{ font-family: 'Montserrat'; src: url('file://{F}/Montserrat-Regular.ttf'); font-weight: 400 800; }}
@page {{ size: A4; margin: 15mm 13mm 17mm 13mm; }}
@page :first {{ margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Readex Pro', sans-serif; color: {INK}; font-size: 9.6pt; line-height: 1.7; background: #fff; }}
.cover {{ height: 297mm; background: {INK}; color: {CREAM}; padding: 30mm 22mm 20mm; display: flex; flex-direction: column; break-after: page; }}
.cover img {{ width: 46mm; filter: invert(1); align-self: flex-start; }}
.cover .kicker {{ margin-top: auto; color: {GOLD}; font-size: 10pt; letter-spacing: .5px; }}
.cover h1 {{ font-size: 28pt; font-weight: 600; line-height: 1.35; margin: 6mm 0 6mm; }}
.cover .sub {{ font-size: 12pt; color: #CFCBC4; max-width: 140mm; }}
.cover .meta {{ margin-top: 18mm; border-top: 1px solid #333; padding-top: 6mm; font-size: 9pt; color: #9C9890; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4mm; }}
.cover .meta b {{ display: block; color: {CREAM}; font-weight: 500; font-size: 10pt; }}
h2 {{ font-size: 16pt; font-weight: 600; margin: 0 0 3mm; padding-top: 1mm; break-after: avoid; }}
h2 .no {{ color: {GOLD}; font-family: 'Montserrat'; margin-left: 6px; }}
h3 {{ font-size: 11pt; font-weight: 600; margin: 6mm 0 2mm; break-after: avoid; }}
.sec {{ break-before: page; }}
.lead {{ font-size: 10.6pt; color: #333; border-right: 3px solid {GOLD}; padding: 1mm 4mm 1mm 0; margin: 0 0 5mm; }}
p {{ margin: 0 0 2.5mm; }}
.kpis {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; margin: 4mm 0 5mm; }}
.kpi {{ background: {CREAM}; padding: 3.5mm 4mm; border-top: 2px solid {INK}; }}
.kpi .v {{ font-family: 'Montserrat'; font-size: 17pt; font-weight: 600; direction: ltr; text-align: right; line-height: 1.3; }}
.kpi .l {{ font-size: 8.4pt; color: #555; line-height: 1.45; }}
.kpi.warn {{ border-top-color: {RED}; }}
.kpi.warn .v {{ color: {RED}; }}
.decisions {{ counter-reset: d; margin: 2mm 0; padding: 0; }}
.decisions li {{ list-style: none; position: relative; padding: 2.5mm 11mm 2.5mm 0; border-bottom: 1px solid {LINE}; }}
.decisions li::before {{ counter-increment: d; content: counter(d); position: absolute; right: 0; top: 2.4mm; width: 7mm; height: 7mm; background: {INK}; color: #fff; font-family: 'Montserrat'; font-weight: 600; font-size: 9pt; text-align: center; line-height: 7mm; }}
table {{ width: 100%; border-collapse: collapse; margin: 2mm 0 2mm; font-size: 8.5pt; line-height: 1.5; }}
th {{ background: {INK}; color: #fff; font-weight: 500; text-align: right; padding: 2mm 2mm; vertical-align: bottom; }}
td {{ padding: 1.7mm 2mm; border-bottom: 1px solid {LINE}; text-align: right; vertical-align: top; }}
tr {{ break-inside: avoid; }}
tbody tr:nth-child(even) td {{ background: #FAF9F7; }}
td.num {{ font-family: 'Montserrat'; white-space: nowrap; font-size: 8.3pt; }}
td.bad {{ color: {RED}; font-weight: 600; }}
td.good {{ color: #3D6B4A; font-weight: 600; }}
td.up {{ color: {GOLD}; font-weight: 700; }}
td.small {{ font-size: 7.9pt; color: #444; }}
tr.tot td {{ border-top: 1.5px solid {INK}; font-weight: 600; background: #fff !important; }}
tr.cat td {{ background: {CREAM} !important; font-weight: 600; color: {GOLD}; padding-top: 2.4mm; }}
table.price td {{ padding: 1.5mm 1.6mm; }}
.fig {{ margin: 3mm 0 1mm; break-inside: avoid; }}
.cap {{ font-size: 8pt; color: #666; margin: 1mm 0 4mm; }}
.box {{ background: {CREAM}; padding: 4mm 5mm; margin: 4mm 0; break-inside: avoid; }}
.box h4 {{ margin: 0 0 1.5mm; font-size: 10pt; font-weight: 600; }}
.box.dark {{ background: {INK}; color: {CREAM}; }}
.box.dark h4 {{ color: {GOLD}; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 5mm; }}
ul {{ margin: 1mm 0 3mm; padding: 0 5mm 0 0; }}
li {{ margin-bottom: 1.4mm; }}
.phase {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; margin: 3mm 0 4mm; }}
.phase div {{ border-top: 2px solid {GOLD}; padding: 2.5mm 0 0; font-size: 8.8pt; }}
.phase b {{ display: block; font-size: 10pt; margin-bottom: 1mm; }}
.tag {{ display: inline-block; font-size: 7.6pt; padding: 0 2mm; background: #EDEAE4; margin-left: 1mm; }}
.src {{ font-size: 7.8pt; color: #777; }}
.ladder {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin: 4mm 0; }}
.ladder div {{ padding: 3mm 3mm; font-size: 8.4pt; line-height: 1.5; border-left: 1px solid #fff; }}
.ladder div b {{ display: block; font-size: 9.6pt; margin-bottom: 1mm; }}
.formula {{ font-family: 'Readex Pro'; background: #fff; border: 1px dashed {GOLD}; padding: 2.5mm 4mm; margin: 2mm 0; text-align: center; font-size: 9.6pt; }}
"""

logo = SP + '/brand/logo.png'
ta, ti = sum(ads_m), 162669
tn = sum(net)

html = f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>a'mie — السوق والتسعير والأداء</title><style>{css}</style></head><body>

<section class="cover">
  <img src="file://{logo}" alt="a'mie">
  <div class="kicker">تقرير داخلي · السوق السعودي</div>
  <h1>السوق، والمنافسين، والتسعير،<br>وأداء آخر 6 شهور</h1>
  <div class="sub">حجم السوق لكل فئة، وموقع a'mie وسط المنافسين، ونطاق السعر المسموح لكل منتج، وحدود الخصم، وصرفنا كام وجبنا كام من مايو لأكتوبر 2026.</div>
  <div class="meta">
    <div><b>الفترة</b>1 مايو – 30 أكتوبر 2026</div>
    <div><b>تاريخ التقرير</b>3 نوفمبر 2026</div>
    <div><b>السوق</b>السعودية (الخليج لاحقاً)</div>
  </div>
</section>

<section>
<h2><span class="no">01</span>الملخص التنفيذي</h2>
<p class="lead">a'mie باعت بـ <b>1.85 مليون ريال صافي</b> في 6 شهور، وصرفت على التسويق <b>355 ألف ريال</b> (19٪ من المبيعات). التان شال نص المبيعات، وبعد ما موسمه خلص في أغسطس، المبيعات نزلت حوالي 40٪، والطلبات بكوبون طلعت لـ 81٪، والتسويق بقى ربع المبيعات. a'mie براند <b>بريميوم سعودي</b>: أغلى من البراندات السعودية والماركت بليس، وفي مستوى البراندات العالمية أو أعلى. <b>يعني مافيش مساحة نرفع الأسعار بشكل عام،</b> والفلوس الحقيقية في إننا نقلل الكوبونات.</p>

<div class="kpis">
  <div class="kpi"><div class="v">1,847,749</div><div class="l">صافي المبيعات بالريال (من غير ضريبة وشحن)</div></div>
  <div class="kpi"><div class="v">{fmt(sum(orders))}</div><div class="l">طلب · متوسط الطلب {sum(paid)/sum(orders):.0f} ريال شامل الضريبة والشحن</div></div>
  <div class="kpi"><div class="v">{fmt(ta+ti)}</div><div class="l">صرف تسويق: إعلانات {fmt(ta)} + مؤثرين {fmt(ti)}</div></div>
  <div class="kpi warn"><div class="v">19.2%</div><div class="l">التسويق ÷ المبيعات (كان 7–9٪ في مايو ويوليو، و23–28٪ في يونيو ومن أغسطس لأكتوبر)</div></div>
  <div class="kpi"><div class="v">2.2×</div><div class="l">العائد الحقيقي على الإعلانات حسب GA4 (المنصات بتقول 8–12×)</div></div>
  <div class="kpi"><div class="v">5.1×</div><div class="l">جوجل: أحسن قناة حسب GA4</div></div>
  <div class="kpi warn"><div class="v">47%</div><div class="l">من الطلبات بكوبون في الفترة كلها، و81٪ في سبتمبر</div></div>
  <div class="kpi warn"><div class="v">−30%</div><div class="l">متوسط قيمة الطلب: من 408 في مايو لـ 285 في أكتوبر</div></div>
</div>

<h3>القرارات اللي بنقترحها</h3>
<ol class="decisions">
  <li><b>مانرفعش الأسعار المعلنة دلوقتي.</b> أغلب منتجاتنا أغلى من المنافسين أصلاً، وأكتر من نص القطع بتتباع بكوبون، فرفع السعر هيخلي العميلة تستنى الكوبون.</li>
  <li><b>نحط سقف للخصم وقواعد للكوبونات</b> (القسم 07): 15٪ بحد أقصى، في 4 مواسم بس، وأكواد المؤثرين 10٪. لو نسبة القطع اللي بتتباع بكوبون نزلت من حوالي 50٪ لـ 35٪، السعر اللي العميلة بتدفعه فعلاً يزيد حوالي 2.5–3٪ من غير ما نغير السعر المعلن.</li>
  <li><b>3 منتجات بس مرشحة للرفع بعد ظبط الكوبونات:</b> فرشاة سليك من 29 لـ 39–45، وSleek Secret من 75 لـ 79–85، وكريم القدمين اختبار من 75 لـ 79.</li>
  <li><b>نغير توزيع الصرف:</b> نزوّد جوجل (5.1×)، ونقلل ميتا (1.27×)، ونثبّت تيك توك على حوالي 15٪ (1.25×) لحد ما يثبتوا نفسهم. ونصرف على الشعر واللمعة في الشتا، ونأجل التان لمارس.</li>
  <li><b>نشغل المؤثرين بشروط:</b> 46٪ من صرف التسويق كان على المؤثرين، ومن 21 تعاون، 9 بس ليهم كود عليه مبيعات في زد (أكبرهم NAJLA وLULU، 172 ألف ريال مع بعض شامل الضريبة والشحن)، والباقي مالوش كود ولا رابط، فمانقدرش نقيسه. أي تعاون جاي لازم يبقى بكود أو رابط UTM.</li>
</ol>
</section>

<section class="sec">
<h2><span class="no">02</span>آخر 6 شهور: صرفنا كام وجبنا كام</h2>
<p class="lead">المبيعات كانت ثابتة حوالي 360–400 ألف في الشهر لحد يوليو، وبعدين نزلت لحوالي 230–265 ألف من أغسطس. ومع النزول ده، الصرف على التسويق ماقلش، فنسبته من المبيعات طلعت من 7٪ لـ 26٪.</p>
<div class="fig">{chart_monthly()}</div>
<div class="cap">صافي المبيعات من غير ضريبة وشحن (من طلبات زد، من غير الملغية). الإعلانات: سناب وميتا وتيك توك وجوجل. المؤثرين حسب تاريخ النشر.</div>
{monthly_table()}
<div class="cap">* إجمالي المؤثرين 162,669 فيه حوالي 11 ألف تعاون من غير تاريخ نشر، فمش ظاهرين في الشهور. متوسط الطلب = اللي العميلة دفعته (بالضريبة والشحن) ÷ عدد الطلبات. نسبة الكوبونات في أكتوبر لحد 24 أكتوبر.</div>

<h3>إيه اللي حصل: 3 مراحل</h3>
<div class="phase">
  <div><b>مايو–يوليو: موسم التان</b>مبيعات 360–400 ألف في الشهر، وSummer Set لوحدها 36٪ من مبيعات الفترة. تسويق قليل (7–9٪) إلا يونيو، اللي صرفنا فيه 65 ألف على المؤثرين.</div>
  <div><b>أغسطس: الموسم خلص</b>المبيعات نزلت 42٪ عن يوليو. Summer Set من 365 قطعة في يوليو لـ 210، وفي أكتوبر 22 بس. والطلبات بكوبون طلعت لـ 62٪.</div>
  <div><b>سبتمبر–أكتوبر: كوبونات أكتر، وعائد أقل</b>أعلى صرف إعلانات (44 ألف في سبتمبر) مع ND96 (خصم 20٪)، و81٪ من الطلبات بكوبون. المبيعات زادت 14٪ بس، ومتوسط الطلب نزل لـ 280.</div>
</div>
<div class="fig">{chart_coupon()}</div>
<div class="cap">كل ما الكوبونات زادت، متوسط قيمة الطلب نزل. يعني الكوبون بقى بيجيب طلبات أصغر، مش عميلات جداد بس.</div>
</section>

<section class="sec">
<h2><span class="no">03</span>القنوات والمنتجات: الفلوس راحت فين</h2>
<p class="lead">كل منصة بتحسب نفس الطلب لنفسها، فمجموع اللي المنصات بتقول إنها جابته (2.0 مليون) قريب من كل مبيعات المتجر. GA4 بيحسب الطلب مرة واحدة، فهو الأقرب للحقيقة.</p>
<div class="fig">{chart_roas()}</div>
<div class="cap">من 20 يوليو لـ 30 أكتوبر، لإن GA4 بدأ يسجل المشتريات صح من 20 يوليو. GA4 بيحسب آخر ضغطة، فممكن يظلم القنوات اللي بتعرّف العميلة على البراند (سناب وتيك توك).</div>
<table><thead><tr><th>المنصة</th><th>الصرف (20 يوليو – 30 أكتوبر)</th><th>المشتريات حسب المنصة</th><th>المشتريات حسب GA4</th><th>إيراد GA4</th><th>ROAS حسب GA4</th><th>المنصة بتكبّر الرقم</th></tr></thead><tbody>
<tr><td>جوجل</td><td class="num">15,590</td><td class="num">419</td><td class="num">276</td><td class="num">80,037</td><td class="num good">5.13</td><td class="num">1.5×</td></tr>
<tr><td>سناب</td><td class="num">45,982</td><td class="num">1,760</td><td class="num">334</td><td class="num">102,924</td><td class="num">2.24</td><td class="num">5.3×</td></tr>
<tr><td>ميتا</td><td class="num">30,571</td><td class="num">763</td><td class="num">133</td><td class="num">38,914</td><td class="num bad">1.27</td><td class="num">5.7×</td></tr>
<tr><td>تيك توك</td><td class="num">20,137</td><td class="num">649</td><td class="num">81</td><td class="num">25,116</td><td class="num bad">1.25</td><td class="num">8.0×</td></tr>
</tbody></table>

<h3>الفئات: مين بيجيب ومين بيصرف</h3>
<table><thead><tr><th>الفئة</th><th>صافي المبيعات</th><th>من المبيعات</th><th>إعلانات</th><th>مؤثرين</th><th>التسويق ÷ المبيعات</th></tr></thead><tbody>
<tr><td>التان</td><td class="num">935,386</td><td class="num">50.6٪</td><td class="num">88,255</td><td class="num">44,091</td><td class="num">14.1٪</td></tr>
<tr><td>اللمعة والهايلايتر</td><td class="num">331,883</td><td class="num">18.0٪</td><td class="num">47,282</td><td class="num">61,274</td><td class="num bad">32.7٪</td></tr>
<tr><td>الشعر</td><td class="num">275,568</td><td class="num">14.9٪</td><td class="num">32,757</td><td class="num">41,954</td><td class="num bad">27.1٪</td></tr>
<tr><td>العناية بالجسم</td><td class="num">166,892</td><td class="num">8.8٪</td><td class="num">15,313</td><td class="num">9,107</td><td class="num">14.6٪</td></tr>
<tr><td>المعطرات والمسك</td><td class="num">109,629</td><td class="num">5.9٪</td><td class="num">4,852</td><td class="num">5,057</td><td class="num good">9.0٪</td></tr>
</tbody></table>

<h3>أعلى 20 منتج</h3>
{product_table()}
<div class="cap">الإعلانات اللي مش لمنتج معين (كتالوج/عام، حوالي 41 ألف) اتوزعت على المنتجات حسب نصيب كل منتج من المبيعات. التسويق ÷ المبيعات: الأحمر أكتر من 30٪، والأخضر أقل من 12٪.</div>
<div class="box"><h4>أكتر حاجة بتقولها الأرقام دي</h4>
<ul>
<li><b>ستيك Chocolate</b> صرفنا عليه إعلانات أكتر من مبيعاته (134٪)، و<b>مجموعة Chocolate</b> 58٪. دول أول حاجة نوقفها أو نغير إعلاناتها.</li>
<li><b>Into The Glow</b> (47٪ تسويق، و74٪ من قطعها بكوبون) باعت في أكتوبر بس، وأغلب مبيعاتها جت من المؤثرين والكوبونات.</li>
<li><b>Hair Set</b> صرفنا عليها 32٪ من مبيعاتها، أغلبه مؤثرين (30 ألف).</li>
<li><b>المعطرات وكريم القدمين وGlow Set</b> بتتباع بتسويق قليل (5–12٪). دي منتجات بتتباع لوحدها، ونستخدمها كإضافة في السلة.</li>
</ul></div>
</section>

<section class="sec">
<h2><span class="no">04</span>حجم السوق السعودي لكل فئة</h2>
<p class="lead">الفئات اللي a'mie أقوى فيها (التان، واللمعة، والشعر) أسواق متخصصة وصغيرة (60–160 مليون ريال في السنة)، وحصتنا فيها 0.3–2٪. الأسواق الكبيرة (العناية بالجسم والمعطرات، أكتر من مليار) حصتنا فيها أقل من 0.05٪، والمنافسة فيها على السعر.</p>
<div class="fig">{chart_market()}</div>
<div class="cap">حجم السوق في السنة بالمليون ريال. الشريط من التقدير المنخفض للعالي، والخط في النص هو التقدير المتوسط.</div>
<table><thead><tr><th>الفئة</th><th>حجم السوق (منخفض · متوسط · عالي)</th><th>الثقة</th><th>من مبيعات a'mie</th><th>حصة a'mie</th><th>الطلب على جوجل (ظهور، 6 شهور)</th></tr></thead><tbody>
<tr><td>التان</td><td class="num">30 · 60 · 120 مليون</td><td>منخفضة</td><td class="num">50.6٪</td><td class="num">≈ 2٪</td><td class="num">31,328</td></tr>
<tr><td>اللمعة والهايلايتر</td><td class="num">25 · 60 · 150 مليون</td><td>منخفضة</td><td class="num">18.0٪</td><td class="num">≈ 1٪</td><td class="num">11,009</td></tr>
<tr><td>تصفيف الشعر (للستات)</td><td class="num">85 · 160 · 290 مليون</td><td>منخفضة–متوسطة</td><td class="num">14.9٪</td><td class="num">≈ 0.3٪</td><td class="num">23,657</td></tr>
<tr><td>العناية بالجسم</td><td class="num">835 · 1,215 · 1,800 مليون</td><td>منخفضة–متوسطة</td><td class="num">8.8٪</td><td class="num">≈ 0.03٪</td><td class="num">5,985</td></tr>
<tr><td>المعطرات والمسك</td><td class="num">958 · 1,141 · 1,342 مليون</td><td>منخفضة</td><td class="num">5.9٪</td><td class="num">≈ 0.02٪</td><td class="num">1,460</td></tr>
<tr><td>الهدايا والإكسسوارات</td><td class="num">50 · 250 · 790 مليون</td><td>منخفضة جداً</td><td class="num">1.7٪</td><td>—</td><td>—</td></tr>
</tbody></table>
<div class="cap">الحصة محسوبة على تقدير مبيعات a'mie في السنة (2.8–3.9 مليون ريال)، لإن عندنا بيانات 6 شهور بس. الطلب على جوجل من Search Console: مرات ظهور a'mie في بحث مش باسم البراند، ونسبة الضغط أقل من 0.3٪.</div>

<div class="two">
<div class="box"><h4>الأرقام المؤكدة من مصادرها (اتفتحت يوم 3 نوفمبر)</h4>
<ul>
<li>سكان السعودية 35.3 مليون (منتصف 2024)، والسعوديات 9.8 مليون، 36٪ منهم من 15 لـ 34 سنة (الهيئة العامة للإحصاء).</li>
<li>الجمال والعناية الشخصية 4.8 مليار دولار في 2025 (IMARC).</li>
<li>العناية بالشعر 765–884 مليون دولار في 2025 (TechSci وIMARC).</li>
<li>العناية من الشمس 137 مليون دولار في 2025 (IMARC).</li>
<li>الأونلاين 15–20٪ من سوق الجمال (ECDB).</li>
</ul></div>
<div class="box"><h4>حدود الأرقام دي</h4>
<ul>
<li>مافيش رقم منشور للسعودية لزيت التان، ولا لهايلايتر الجسم، ولا لواكس الشعر للستات. التقديرات دي محسوبة من تحت: عدد العميلات × متوسط الصرف.</li>
<li>أرقام Statista ورا paywall، ومنها رقم المعطرات، فثقته منخفضة.</li>
<li>يعني الأرقام دي <b>اتجاه</b>، مش أرقام نهائية. وحجم البحث الحقيقي هيجي من Keyword Planner (البرومبت 30).</li>
</ul></div>
</div>
<p><b>اللي يهمنا من حجم السوق:</b> النمو مش هييجي من إننا ناخد حصة كبيرة من سوق صغير، لكن من 3 حاجات: نكبر في الفئات المتخصصة اللي فيها طلب على جوجل وترتيبنا ضعيف (SEO وGoogle Search)، والشعر بيتباع طول السنة فيغطي على موسمية التان، والعناية بالجسم والمعطرات نستخدمهم كإضافة للسلة، مش ندخل بيهم حرب أسعار.</p>
</section>

<section class="sec">
<h2><span class="no">05</span>موقع a'mie في السوق: إحنا في أنهي فئة؟</h2>
<p class="lead">في كل فئة تقريباً، سعر a'mie أعلى من الماركت بليس بـ 2–5 مرات، وأعلى من أغلب البراندات السعودية، وفي مستوى البراندات العالمية أو أعلى منها بعد خصوماتها. يعني a'mie في شريحة <b>البريميوم السعودي</b>، والعميلة بتدفع زيادة عشان البراند والتغليف والتجربة، مش عشان السعر.</p>
<div class="ladder">
  <div style="background:#ECEAE6"><b>1. الماركت بليس</b>نون، أمازون، الصيدليات. وسيط 25–56 ريال. منتجات رخيصة ومن غير براند. <b style="display:inline;font-size:8.4pt">a'mie مش بتنافس هنا.</b></div>
  <div style="background:#E7DCC9"><b>2. براندات سعودية</b>Clara، Hearts، Surge، Jayla، Ladeena، MZN. 35–195 ريال، وعندهم عروض وخصومات طول الوقت.</div>
  <div style="background:{INK};color:{CREAM}"><b style="color:{GOLD}">3. a'mie</b>65–482 ريال (من غير الإكسسوارات). براند سعودي، تغليف يصلح هدية، ومجموعات روتين كاملة.</div>
  <div style="background:#DCE2EA"><b>4. براندات عالمية</b>Sol de Janeiro، Tan-Luxe، Slick، Carrot Sun، Beesline، Eucerin. 48–164 ريال، وكتير منها بخصم 25–50٪ دلوقتي.</div>
</div>
<div class="fig">{chart_position()}</div>
<div class="cap">سعر القطعة بالريال يوم 3 نوفمبر (من صفحات المنافسين). الأحجام مختلفة، فده موقع السعر في عين العميلة، مش سعر المل. الماركت بليس = وسيط أعلى 5 نتايج على نون وأمازون والصيدليات.</div>

<h3>المنافسين الحقيقيين في كل فئة</h3>
<table><thead><tr><th>الفئة</th><th>أخطر منافس</th><th>ليه</th><th>سعرهم قصادنا</th></tr></thead><tbody>
<tr><td>الشعر</td><td><b>Clara</b> (سعودي)</td><td>282 ألف متابع على تيك توك، وموجود في صيدليات الدواء، وعنده خصم على كل المنتجات</td><td>واكس 94 قصاد 129 · ماسكارا 83 قصاد 75 · فرشاة 47 قصاد 29</td></tr>
<tr><td>اللمعة</td><td><b>Hearts</b> (سعودي)</td><td>69.5 ألف على تيك توك، وموجود عند موزعين كتير</td><td>Body Glow 96 قصاد 176 · ستيك 35.70 قصاد 79</td></tr>
<tr><td>التان</td><td><b>Surge</b> (سعودي) + Carrot Sun وBeesline</td><td>Surge تقييمه 4.98، والعالميين بخصم 50٪ في نهدي</td><td>0.78 ريال للمل قصاد 1.06 · Carrot Sun 80.5 لـ 200 مل</td></tr>
<tr><td>العناية بالجسم</td><td><b>Ladeena، Waves، MZN</b></td><td>براندات سعودية في نفس الشريحة تقريباً</td><td>زبدة 85–129 قصاد 119 (في النص)</td></tr>
<tr><td>المعطرات</td><td><b>Jayla، Victoria's Secret</b></td><td>Jayla عندها 80.6 ألف متابع ومؤثرات</td><td>بودي مست 50–73 قصاد 129 · مسك 75–80 قصاد 99</td></tr>
</tbody></table>
<div class="cap">من 70 سعر منافس: 23 اتطابق مع البحث، و35 اختلف (أغلبهم نزل بخصم)، و11 ماقدرناش نتأكد منهم. الكوبونات والعروض منتشرة عند كل المنافسين.</div>
</section>

<section class="sec">
<h2><span class="no">06</span>التسعير: نطاق السعر لكل منتج</h2>
<p class="lead">لكل منتج: السعر الحالي، ونسبة القطع اللي بتتباع بكوبون، وأقرب منافس، والقرار، ونطاق السعر المسموح (من–لـ)، وأقصى خصم نسمح بيه. <b>القاعدة:</b> أي منتج أكتر من نص قطعه بتتباع بكوبون، مانرفعش سعره قبل ما نسبة قطعه بكوبون تنزل تحت 50٪.</p>
{price_table()}
<div class="cap">الأسعار شاملة الضريبة زي ما هي على المتجر. «تثبيت» يعني الحد الأقصى هو السعر الحالي. اللون الدهبي = منتج مرشح للرفع. أقصى خصم: 15٪ للمجموعات ومنتجات الموسم في موسمها بس، و10٪ للمنتجات اللي بتتباع لوحدها أو اللي نسبة الكوبون فيها قليلة (زي Red Cherry 28٪)، و0٪ للمنتجات اللي في اختبار رفع. نسبة الكوبون للنسخة الأساسية من المنتج. باقي المنتجات (Lemongrass Set، اللافندر، Back to Routine، كريم اليدين، الإكسسوارات): تثبيت، وأقصى خصم 10٪.</div>

<h3>لو رفعنا: المبيعات ممكن تنزل لحد فين؟</h3>
<p>الجدول ده بيقول المبيعات ممكن تنزل لحد فين والإيراد يفضل زي ما هو. لو المبيعات نزلت أقل من كده، الرفع كسبان. (لما المحاسب يملا تكلفة القطعة، الحسبة هتبقى على الربح، والمساحة هتبقى أكبر.)</p>
{breakeven_table()}
<div class="box"><h4>طريقة اختبار الرفع</h4>
<ul>
<li>نرفع منتج واحد بس كل مرة، ولمدة 4 أسابيع، ومن غير ما يدخل عليه أي كوبون في الفترة دي.</li>
<li>نقارن القطع في الأسبوع بمتوسط آخر 8 أسابيع من غير أسابيع الجمعة البيضا، ومن غير الطلبات اللي كان فيها كوبون. لو النزول أقل من رقم الجدول، نثبت السعر الجديد. لو أكتر، نرجع للسعر القديم.</li>
<li>نبدأ بفرشاة سليك (أصغر خطر، ومنتج إضافة للسلة)، وبعدها Sleek Secret، وبعدها كريم القدمين.</li>
</ul></div>
</section>

<section class="sec">
<h2><span class="no">07</span>الخصومات: إمتى، وقد إيه، وعلى إيه</h2>
<p class="lead">47٪ من الطلبات كانت بكوبون، وفي سبتمبر وصلت 81٪. Summer26 لوحده جاب 1,178 طلب، وND96 جاب 970. لما الكوبون بيبقى موجود طول الوقت، العميلة بتتعود ماتشتريش من غيره، والسعر المعلن بيبقى مجرد رقم.</p>

<div class="two">
<div class="box dark"><h4>سقف الخصم</h4>
<ul>
<li><b>15٪ بحد أقصى</b> في المواسم بس، وكل منتج مايعديش الحد بتاعه في جدول القسم 06.</li>
<li><b>10٪</b> لأكواد المؤثرين، وكود العميلة الراجعة 10٪ لمرة واحدة. دول بس اللي مسموحين بره المواسم، وكل كود ليه تاريخ نهاية.</li>
<li><b>0٪</b> على أي منتج وقت اختبار الرفع، وعلى فرشاة سليك لوحدها (جوه المجموعات عادي).</li>
<li>الخصومات ماتتجمعش: الكوبون مايشتغلش مع عرض تاني.</li>
</ul></div>
<div class="box"><h4>4 مواسم بس للخصم</h4>
<ul>
<li><b>الجمعة البيضا</b> (نوفمبر): اللمعة والهدايا.</li>
<li><b>رمضان والعيد</b>: الهدايا والتوزيعات.</li>
<li><b>بداية الصيف</b> (مايو–يونيو): التان.</li>
<li><b>اليوم الوطني</b> (سبتمبر): المتجر كله.</li>
<li>كل موسم من أسبوع لأسبوعين بالكتير (Summer26 فضل 4 شهور، وND96 فضل 40 يوم بخصم 20٪، وده اللي وصّل الكوبونات لـ 81٪).</li><li>بره المواسم دي: مجموعات وهدية مع الطلب بدل الخصم.</li>
</ul></div>
</div>

<h3>بدل الخصم: إزاي نبيع من غير ما نكسر السعر</h3>
<table><thead><tr><th>بدل</th><th>مثال</th><th>ليه أحسن</th></tr></thead><tbody>
<tr><td>مجموعات بسعر أحسن</td><td>Hair Set (واكس + Sleek Secret + فرشاة + شنطة) سعرها دلوقتي 282، يعني نفس مجموع القطع بالظبط. نخليها أقل من مجموع القطع بشكل واضح، ونراجعها لو رفعنا الفرشاة</td><td>متوسط الطلب يعلى، والسعر المعلن لكل منتج يفضل زي ما هو</td></tr>
<tr><td>هدية مع حد أدنى للطلب</td><td>ستيك هايلايتر أو Lip Plump (بعد ما نتأكد من المخزون) هدية فوق 400 ريال</td><td>تكلفة الهدية أقل من خصم 15٪ على الطلب كله (نتأكد بتكلفة القطعة)</td></tr>
<tr><td>شحن مجاني فوق حد معين</td><td>فوق 300–350 ريال (أعلى من متوسط الطلب الحالي، حوالي 260 من غير الشحن)</td><td>بيرفع متوسط الطلب، اللي نزل 30٪. لو الحد أقل من متوسط الطلب، هنخسر إيراد الشحن (163 ألف في 6 شهور) من غير ما الطلب يكبر</td></tr>
<tr><td>خصم العميلة الراجعة</td><td>كود لمرة واحدة بعد أول طلب بـ 30 يوم</td><td>بيكافئ الولاء، مش أي حد</td></tr>
</tbody></table>

<h3>الأثر المتوقع</h3>
<div class="formula">السعر اللي العميلة بتدفعه = السعر المعلن × (1 − نسبة القطع بكوبون × متوسط الخصم)</div>
<p>متوسط الخصم في الكوبونات حوالي 16٪ (Summer26 15٪، وND96 وNAJLA 20٪، وأغلب أكواد المؤثرين 10٪)، وحوالي 49٪ من القطع في الـ 6 شهور اتباعت بكوبون. يعني العميلة دفعت حوالي 92٪ من السعر المعلن، وده نفس اللي بتقوله خصومات زد (170 ألف من 2.25 مليون). لو نسبة القطع بكوبون نزلت لـ 35٪ والخصم بقى 15٪ بحد أقصى، السعر اللي العميلة بتدفعه يطلع لحوالي 94.5٪ من السعر المعلن، يعني <b>حوالي 2.5–3٪ زيادة</b> من غير ما نغير ولا سعر. على مبيعات 6 شهور، ده حوالي <b>45–55 ألف ريال</b> لو عدد الطلبات فضل زي ما هو. وللمقارنة، رفع أسعار المنتجات التلاتة مع بعض هيجيب حوالي 6–10 آلاف بس، فالكوبونات الأول. ده تقدير ولازم نختبره، لإن جزء من العميلات ممكن ماتشتريش من غير كوبون.</p>

<h3>الخصم اللي عنده الربح صفر (لما المحاسب يملا تكلفة القطعة)</h3>
<div class="formula">خصم الربح صفر = 1 − (تكلفة القطعة + الشحن والدفع للقطعة + التسويق للقطعة) × 1.15 ÷ السعر المعلن</div>
<p>الحسبة دي جاهزة في شيت الحسبة (amie-product-cost-model-v2) أول ما المحاسب يملا عمود تكلفة القطعة. التسويق للقطعة معروف دلوقتي، مثلاً: Summer Set 59 ريال، وHair Set 61، وواكس الشعر 26، وكريم القدمين 4.</p>
</section>

<section class="sec">
<h2><span class="no">08</span>فين نصرف: نوفمبر 2026 – فبراير 2027</h2>
<p class="lead">نفس الميزانية تقريباً (حوالي 30 ألف ريال إعلانات في الشهر)، بس متوزعة على القنوات والفئات اللي بتجيب فعلاً حسب GA4. ده مقترح لازم يتختبر: كل شهر ننقل 10 نقط من القناة الأضعف في GA4 للأقوى، ومافيش قناة تعدي 50٪ من الميزانية. وROAS جوجل محسوب على 15.6 ألف صرف بس، فممكن ينزل لما نزود.</p>
<div class="two">
<div>
<h3>حسب القناة</h3>
<table><thead><tr><th>القناة</th><th>متوسط آخر 6 شهور</th><th>المقترح</th><th>ليه</th></tr></thead><tbody>
<tr><td>جوجل</td><td class="num">8٪</td><td class="num up">35–40٪</td><td>أحسن ROAS (5.1×)، وعندنا طلب على كلمات بنظهر فيها بالفعل</td></tr>
<tr><td>سناب</td><td class="num">49٪</td><td class="num">30٪</td><td>2.2×، وأكتر قناة بتجيب زيارات (68 ألف جلسة في GA4)</td></tr>
<tr><td>ميتا</td><td class="num">29٪</td><td class="num">15٪</td><td>1.27×: نختبر إعلانات جديدة الأول</td></tr>
<tr><td>تيك توك</td><td class="num">14٪</td><td class="num">15٪</td><td>1.25×: نثبّته عشان المحتوى، ولإن Clara قوية هناك (282 ألف متابع)</td></tr>
</tbody></table>
</div>
<div>
<h3>حسب الفئة</h3>
<table><thead><tr><th>الفئة</th><th>المقترح</th><th>ليه</th></tr></thead><tbody>
<tr><td>الشعر</td><td class="num up">35٪</td><td>بيتباع طول السنة، وتاني أعلى طلب على جوجل</td></tr>
<tr><td>اللمعة والهايلايتر</td><td class="num up">35٪</td><td>الجمعة البيضا ومناسبات الشتا</td></tr>
<tr><td>العناية بالجسم</td><td class="num">15٪</td><td>كريم القدمين والزبدة وLip Plump في الشتا</td></tr>
<tr><td>براند وكتالوج</td><td class="num">10٪</td><td>إعادة استهداف</td></tr>
<tr><td>المعطرات</td><td class="num">5٪</td><td>اختبار صغير (Natura مع Body Glow)</td></tr>
<tr><td>التان</td><td class="num">0٪ لحد مارس</td><td>نجهز حملات جوجل في فبراير ونبدأ مارس</td></tr><tr><td colspan="3" class="small">رمضان بيبدأ حوالي 8 فبراير 2027، فنحجز جزء من ميزانية فبراير للهدايا والتوزيعات. وميزانية المؤثرين تتحدد لوحدها، بنفس قاعدة الكود أو الرابط.</td></tr>
</tbody></table>
</div>
</div>
<div class="box"><h4>قواعد الصرف</h4>
<ul>
<li>أي منتج التسويق بتاعه أكتر من 30٪ من مبيعاته لمدة شهر، إعلاناته تتوقف أو تتغير (زي ستيك Chocolate).</li>
<li>نقيس بـ GA4 مش بأرقام المنصة، ونتأكد إن كل الإعلانات عليها UTM.</li>
<li>المؤثرين: بكود أو رابط لكل واحدة، ونقارن تكلفة كل تعاون باللي جابه قبل ما نجدد معاها.</li>
<li>SEO على الكلمات اللي بنظهر فيها بنسبة ضغط أقل من 0.3٪: تان، واكس للشعر، لمعة جسم.</li>
</ul></div>
</section>

<section class="sec">
<h2><span class="no">09</span>خطة التنفيذ، وحدود البيانات</h2>
<table><thead><tr><th>إمتى</th><th>إيه</th><th>مين</th></tr></thead><tbody>
<tr><td>الأسبوع ده</td><td>نوقف أو نغير إعلانات ستيك ومجموعة Chocolate. ونقفل أو نقصّر الأكواد اللي شغالة لحد 2027 (Y10 وSh10 لحد يونيو، وHS15 بخصم 15٪ لحد مايو)، ونخلي أكواد المؤثرين 10٪. كود 00002 (لطلبات UGC بره السعودية) يفضل.</td><td>الإعلانات</td></tr>
<tr><td>نوفمبر</td><td>نطبق سقف الخصم (15٪ / 10٪) قبل الجمعة البيضا، ونعمل مجموعة للشعر ومجموعة للهدايا بدل الخصم.</td><td>التسويق + المتجر</td></tr>
<tr><td>نوفمبر</td><td>المحاسب يملا تكلفة القطعة في شيت الحسبة، عشان نحسب أقصى خصم لكل منتج.</td><td>المحاسب</td></tr>
<tr><td>ديسمبر</td><td>اختبار رفع فرشاة سليك لـ 39 لمدة 4 أسابيع.</td><td>المتجر</td></tr>
<tr><td>يناير – فبراير</td><td>اختبار Sleek Secret لـ 79 (4 أسابيع)، وبعده كريم القدمين لـ 79 (4 أسابيع).</td><td>المتجر</td></tr>
<tr><td>فبراير</td><td>نجهز حملات التان على جوجل، ونقرر سعر موسم 2027.</td><td>الإعلانات</td></tr>
</tbody></table>
<div class="cap">أي تغيير في الأسعار أو الكوبونات على زد بيتعمل بعد موافقة الفريق، وبعد ما ناخد نسخة من الأسعار الحالية.</div>

<h3>حدود البيانات</h3>
<ul>
<li><b>المبيعات</b> من طلبات زد (6,564 طلب، من غير الملغية). صافي المبيعات من غير ضريبة 15٪ وشحن، وبعد الخصومات.</li>
<li><b>GA4</b> بدأ يسجل المشتريات صح من 20 يوليو، والعملة فيه دولار (حولناها × 3.75). ولو الإيراد فيه شامل الضريبة، يبقى ROAS الحقيقي حوالي 1.9 مش 2.2.</li>
<li><b>المؤثرين:</b> التكلفة من شيت المؤثرين، وفيها أرقام شاملة الضريبة. و12 من 21 تعاون مالهمش كود. الأكواد اللي عليها مبيعات في زد 9، بس شيت المؤثرين مسجل مبيعات لـ 6 بس، فلازم نوحّد المصدرين قبل ما نحكم على أي تعاون.</li>
<li><b>أسعار المنافسين</b> اتأكدنا منها يوم 3 نوفمبر، وبتتغير مع العروض. و11 منتج ماقدرناش نتأكد منهم.</li>
<li><b>حجم السوق</b> تقديرات، وثقتها منخفضة في الفئات المتخصصة. Keyword Planner (البرومبت 30) هيدي حجم البحث الحقيقي.</li>
<li><b>مستني يتأكد:</b> سعر Summer Set (482 ولا 582)، وسعر Hair Set (282 ولا 268)، وسعر زبدة الليمون قراس (زد بيبيعها بـ 119، والشيت بيقول 199).</li>
<li><b>تكلفة القطعة</b> مش موجودة لسه، فكل الحسابات هنا على الإيراد، مش على الربح.</li>
</ul>
<p class="src">المصادر: طلبات زد · Snapchat Ads · Meta Ads · TikTok Ads · Google Ads · GA4 · Google Search Console · صفحات المنافسين (سيفورا، نهدي، واتسونز، كارفور، نون، أمازون، سلة، زد، تيك توك) · الهيئة العامة للإحصاء · IMARC · TechSci · ECDB.</p>
</section>
</body></html>"""

open(OUT, 'w', encoding='utf-8').write(html)
print('ok', round(tn), ta, [round(x, 1) for x in mk_pct], [round(a) for a in aov])
