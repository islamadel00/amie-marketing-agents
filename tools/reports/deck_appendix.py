# Appendix of the market deck: competitor prices as references (verified 3 Nov 2026).
# exec()'d from market_deck.py (uses slide(), pic()). Reads research/market-2026-11/*.csv.
import csv, re, statistics, collections
RS = os.path.join(HERE, '..', '..', 'research', 'market-2026-11')
V = list(csv.DictReader(open(os.path.join(RS, '07-competitor-prices-verified.csv'), encoding='utf-8-sig')))
SA = list(csv.DictReader(open(os.path.join(RS, '06-saudi-competitors-social.csv'), encoding='utf-8-sig')))
MP = list(csv.DictReader(open(os.path.join(RS, '07-marketplaces-top5.csv'), encoding='utf-8-sig')))

def num(x):
    try: return float(str(x).replace(',', ''))
    except: return None
def size_ml(s):
    m = re.match(r'\s*([\d.]+)\s*(ml|g|مل|جم)\b', s or '', re.I)
    if m: return float(m.group(1))
    m = re.match(r'\s*([\d.]+)\s*kg', s or '', re.I)
    if m: return float(m.group(1)) * 1000
    m = re.match(r'\s*([\d.]+)\s*(fl oz|oz)', s or '', re.I)
    if m: return float(m.group(1)) * 29.57
    return None
def p(v):
    n = num(v)
    return f'{n:g}' if n is not None else '—'
def host(u):
    return u.split('/')[2].replace('www.', '').replace('en.', '') if u.startswith('http') else '—'
def status(m):
    if m == 'نعم': return '<span class="ix g">مطابق</span>'
    if m.startswith('لأ'): return '<span class="ix w">اتغيّر</span>'
    return '<span class="ix b">مش متأكد</span>'

CATS = [('التان', range(1, 17), "Deep Tan 159 / 150 مل (106 للـ 100) · Red Cherry 199 / 200 مل · Glittery Gold 149 / 120 مل"),
        ('اللمعة والهايلايتر', range(18, 30), 'Body Glow 176 · ستيك الهايلايتر 79 · مجموعات الهايلايتر 99'),
        ('الشعر', range(30, 39), 'واكس الشعر 129 / 30 مل · Sleek Secret 75 / 15 مل · فرشاة سليك 29 · Hair Set 282'),
        ('العناية بالجسم', range(41, 51), 'زبدة الليمون قراس 119 / 250 مل · سكراب الليمون قراس 119 / 300 مل'),
        ('القدمين واليدين والشفايف', range(51, 58), 'كريم القدمين 75 · Lip Plump 65 / 10 مل'),
        ('المعطرات والمسك', range(58, 71), "Flora / Natura Body Mist 129 · a'musk 99")]
EXCL = {49: 'سعر غلط في الصفحة (13 ريال)'}
for i, (cat, rng, ours) in enumerate(CATS):
    rows0 = [r for r in V if int(r['row_no']) in rng]
    rows = [r for r in rows0 if num(r['price_regular_verified']) or num(r['price_promo_verified'])]
    nop = ' · '.join(f"{r['brand']} {r['product'][:28]}" for r in rows0 if r not in rows)
    h = ('<table class="t sm ap"><tr><th>البراند</th><th>المنتج</th><th>الحجم</th><th>السعر العادي</th><th>سعر العرض</th>'
         '<th>للـ 100 مل/جم</th><th>اتباع فين</th><th>الحالة</th></tr>')
    h += f'<tr class="me"><td>a\'mie</td><td colspan="7">{ours}</td></tr>'
    for r in rows:
        rn = int(r['row_no'])
        reg, pro = num(r['price_regular_verified']), num(r['price_promo_verified'])
        sz = size_ml(r['size_verified'])
        eff = pro if pro else reg
        per = f'{eff/sz*100:.0f}' if (eff and sz) else '—'
        st = status(r['matches_list'])
        if rn in EXCL: st = f'<span class="ix b">مستبعد</span>'; per = '—'
        h += (f'<tr><td><b>{r["brand"]}</b></td><td><span class="ltr">{r["product"][:38]}</span></td><td class="nm">{r["size_verified"] if r["size_verified"] != "MISSING" else "—"}</td>'
              f'<td class="nm">{p(reg)}</td><td class="nm">{p(pro)}</td><td class="nm">{per}</td><td class="nm src">{host(r["url_opened"])}</td><td>{st}</td></tr>')
    h += '</table>'
    slide('11', f'APPENDIX · COMPETITOR PRICES {i+1}/{len(CATS)+3}', f'ملحق: أسعار المنافسين: {cat}',
          f'<div class="card">{h}</div><p class="note">' + (f'مافيش سعر على الصفحة: {nop}. ' if nop else '') + 'الأسعار بالريال شاملة الضريبة، زي ما ظهرت على الصفحة يوم 3 نوفمبر 2026. '
          '«اتغيّر» = السعر النهارده مختلف عن البحث الأول (غالباً عرض). «مش متأكد» = مافيش سعر على الصفحة. سعر الـ 100 محسوب على العرض لو موجود. الروابط في 07-competitor-prices-verified.csv.</p>')

# Saudi brands (Salla / Zid / TikTok inventory)
sa = [r for r in SA if num(r['السعر العادي'])]
def sa_table(rows):
    h = ('<table class="t sm ap"><tr><th>البراند</th><th>الفئة</th><th>تيك توك</th><th>المنصة</th><th>المنتج</th><th>الحجم</th>'
         '<th>السعر</th><th>العرض</th><th>كوبونات وعروض ظاهرة</th></tr>')
    for r in rows:
        h += (f'<tr><td><b>{r["البراند"]}</b></td><td>{r["الفئة"]}</td><td class="nm">{r["متابعين تيك توك"].replace("MISSING", "—")}</td>'
              f'<td>{r["المنصة"].replace("MISSING", "—")}</td><td>{r["أهم منتج منافس"][:34]}</td><td class="nm">{r["الحجم"].split(" (")[0].replace("MISSING", "—")}</td>'
              f'<td class="nm">{p(r["السعر العادي"])}</td><td class="nm">{p(r["سعر العرض"])}</td><td><small>{r["كوبونات/عروض ظاهرة"].replace("MISSING", "—")[:36]}</small></td></tr>')
    return h + '</table>'
half = (len(sa) + 1) // 2
for j, part in enumerate([sa[:half], sa[half:]]):
    slide('11', f'APPENDIX · COMPETITOR PRICES {len(CATS)+j+1}/{len(CATS)+3}', f'ملحق: البراندات السعودية على سلة وزد وتيك توك ({j+1}/2)',
          f'<div class="card">{sa_table(part)}</div><p class="note">من جرد 3 نوفمبر 2026 بالمتصفح على متاجر البراندات وحساباتهم على تيك توك. '
          'إنستجرام كان طالب تسجيل دخول، فالمتابعين على تيك توك بس. البراندات اللي ماظهرلهاش سعر مش في الجدول. الروابط في 06-saudi-competitors-social.csv.</p>')

# Marketplaces
g = collections.defaultdict(list); sites = collections.defaultdict(set)
for r in MP:
    if 'غير مطابق' in r['notes']: continue
    v = num(r['price'])
    if v: g[r['keyword']].append(v); sites[r['keyword']].add(r['site'])
ours = {'زيت تان': 'Deep Tan 159', 'كريم تان': 'Red Cherry 199', 'بودي جلو / زيت لمعة الجسم': 'Body Glow 176', 'هايلايتر الجسم': 'ستيك 79',
        'واكس شعر ستيك': 'واكس 129', 'ماسكارا الشعر المتطاير': 'Sleek Secret 75', 'زبدة الجسم': 'زبدة 119', 'سكراب الجسم': 'سكراب 119',
        'كريم القدمين': 'كريم القدمين 75', 'بودي مست': 'بودي مست 129'}
h = '<table class="t mpt"><tr><th>كلمة البحث</th><th>عدد النتايج</th><th>الوسيط</th><th>أقل سعر</th><th>أعلى سعر</th><th>المواقع</th><th>a\'mie</th></tr>'
for k, v in g.items():
    h += (f'<tr><td><b>{k}</b></td><td class="nm">{len(v)}</td><td class="nm"><b>{statistics.median(v):.0f}</b></td><td class="nm">{min(v):.0f}</td>'
          f'<td class="nm">{max(v):.0f}</td><td><small>{" · ".join(sorted(sites[k]))}</small></td><td>{ours.get(k, "—")}</td></tr>')
h += '</table>'
slide('11', f'APPENDIX · COMPETITOR PRICES {len(CATS)+3}/{len(CATS)+3}', 'ملحق: الماركت بليس والصيدليات',
      f'<div class="card">{h}</div><p class="note">أعلى 5 نتايج لكل كلمة على نون وأمازون ونهدي والدواء وواتسونز وسيفورا يوم 3 نوفمبر 2026 ({len(MP)} نتيجة). '
      'شلنا النتايج اللي مش من نفس الفئة (زي ماسكارا الرموش في بحث ماسكارا الشعر). الروابط في 07-marketplaces-top5.csv.</p>')
