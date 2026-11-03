# a'mie market, pricing and 6-month performance deck (1280x720 slides, same design system as the product-tree deck).
# Usage: python3 -I market_deck.py <out.html>    (assets in reports/market-deck/)
import sys, os
OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv = sys.argv; sys.argv = ['x', '/dev/null']
import market_pricing_report as M  # reuse data + svg charts
sys.argv = _argv

# brand guidelines v1.0: Smoke White #F2F2F2, Cool Grey #D9D8D7, Black #191919, Nostalgia Rose #5E2E21, Red Dahlia #F2E4DF, Potent Purple #6B595C
M.INK, M.BROWN, M.GOLD, M.BLUE, M.GREY, M.LINE, M.RED, M.TXT = '#191919', '#5E2E21', '#C9A86A', '#6B595C', '#D9D8D7', '#E3E2E1', '#9E3B32', '#191919'
fmt = M.fmt

FONT = '/tmp/claude-0/-home-user/b736310d-3a65-5d5d-94b2-e1f479f6690e/scratchpad/fonts'
HDR = '<div class="hdr"><img src="a/logo_dark.png" class="lg"><i></i><span>Market &amp; Pricing</span><i></i><span>VOL 1.0</span><i></i><span>Nov 2026</span></div>'
pages = []
def slide(n, en, ar, body, cls=''):
    pages.append(f'<section class="page {cls}">{HDR}<div class="body"><div class="ph"><span class="pnum">{n}</span><div><div class="pen">{en}</div><h2>{ar}</h2></div></div>{body}</div><div class="ftr"><span>amie-sa.com</span><span>{len(pages)+1:02d}</span></div></section>')

IM = {'Summer Set': 'summer.jpg', 'Deep Tan': 'deeptan.jpg', 'Red Cherry': 'redcherry.jpg', 'Glittery Gold': 'glittery.jpg',
      'Body Glow': 'bodyglow.jpg', 'ستيك': 'hlm.png', 'مجموعات الهايلايتر': 'hlms.jpg', 'Into The Glow': 'itg.jpg', 'Glow Set': 'glowset.jpg',
      'واكس': 'wax.jpg', 'Sleek Secret': 'mascara.jpg', 'فرشاة': 'sleek.jpg', 'Hair Set': 'hairset.jpg', 'كريم القدمين': 'foot.jpg',
      'زبدة': 'lembutter.jpg', 'سكراب': 'lemscrub.jpg', 'Lip Plump': 'lip.jpg', 'Flora': 'flora.jpg', "a'musk": 'musk.jpg'}
def pic(name):
    for k, v in IM.items():
        if k in name: return f'<img class="th" src="img/{v}">'
    return '<span class="th"></span>'

def html_roas():
    rows = [('جوجل', 7.93, 5.13), ('سناب', 11.63, 2.24), ('ميتا', 7.73, 1.27), ('تيك توك', 10.02, 1.25)]
    h = '<div class="legend"><span><i style="background:#D9D8D7"></i>ROAS حسب المنصة نفسها</span><span><i style="background:#5E2E21"></i>ROAS حسب GA4 (الأقرب للحقيقة)</span></div>'
    for n, p, g in rows:
        h += f'<div class="rr"><span class="rn">{n}</span><div class="rb"><div class="ht"><i style="width:{p/12*100:.0f}%;background:#D9D8D7"></i></div><div class="ht"><i style="width:{g/12*100:.0f}%;background:{"#5E2E21" if g>=2 else "#9E3B32"}"></i></div></div><div class="rv"><span>{p:.1f}</span><b>{g:.2f}</b></div></div>'
    return h
def html_market():
    rows = [('العناية بالجسم', 835, 1215, 1800), ('المعطرات والمسك', 958, 1141, 1342), ('الهدايا والإكسسوارات', 50, 250, 790),
            ('تصفيف الشعر', 85, 160, 290), ('اللمعة والهايلايتر', 25, 60, 150), ('التان', 30, 60, 120)]
    h = ''
    for n, lo, mid, hi in rows:
        h += f'<div class="mr"><span class="rn">{n}</span><div class="mt"><i style="right:{lo/1800*100:.1f}%;width:{(hi-lo)/1800*100:.1f}%"></i><em style="right:{mid/1800*100:.1f}%"></em></div><b class="nm">{mid:,}M</b></div>'
    h += '<div class="mr ax"><span></span><div class="axl"><span>0</span><span>600</span><span>1,200</span><span>1,800</span></div><b></b></div>'
    return h

# ---------- cover ----------
pages.append('''<section class="page cover"><img class="cimg" src="a/cover_full.jpg"><div class="ctop"><img src="a/logo_dark.png" class="lgc"></div>
<div class="ctitle"><div class="cen">MARKET &amp; PRICING <span>VOL 1.0</span></div><div class="cline"></div><h1>السوق، والمنافسين، والتسعير</h1><p>وأداء آخر 6 شهور: صرفنا كام وجبنا كام (1 مايو – 30 أكتوبر 2026) · السوق السعودي</p></div>
<div class="cfoot"><span>amie-sa.com</span><span>نوفمبر 2026</span></div></section>''')

# ---------- agenda ----------
agenda = [('01', 'الملخص التنفيذي', 'Executive Summary'), ('02', 'آخر 6 شهور: صرفنا كام وجبنا كام', 'Performance'),
          ('03', 'القنوات والمنتجات: الفلوس راحت فين', 'Channels & Products'), ('04', 'حجم السوق السعودي لكل فئة', 'Market Size'),
          ('05', 'موقع a\'mie في السوق والمنافسين', 'Positioning'), ('06', 'التسعير: نطاق السعر لكل منتج', 'Pricing'),
          ('07', 'الخصومات: إمتى، وقد إيه، وعلى إيه', 'Discounts'), ('08', 'فين نصرف: نوفمبر – فبراير', 'Media Plan'),
          ('09', 'خطة التنفيذ وحدود البيانات', 'Roadmap'), ('10', 'الونرز: صيف وشتا، ومين قابل يبقى ونر', 'Winners'), ('11', 'ملحق: أسعار المنافسين بالمصادر', 'Appendix')]
rows = ''.join(f'<div class="tr"><span class="tn">{n}</span><span class="tar">{a}</span><span class="tdots"></span><span class="ten">{e}</span></div>' for n, a, e in agenda)
pages.append(f'<section class="page">{HDR}<div class="body"><div class="tocwrap"><div class="pen big">AGENDA</div>{rows}</div></div><div class="ftr"><span>amie-sa.com</span><span>02</span></div></section>')

# ---------- 01 summary ----------
ta, ti = sum(M.ads_m), 162669
kp = [('1,847,749', 'صافي المبيعات بالريال (من غير ضريبة وشحن)', ''), (fmt(sum(M.orders)), f'طلب · متوسط الطلب {sum(M.paid)/sum(M.orders):.0f} ريال', ''),
      (fmt(ta + ti), f'صرف تسويق: إعلانات {fmt(ta)} + مؤثرين {fmt(ti)}', ''), ('19.2%', 'التسويق ÷ المبيعات (7–9٪ في الموسم، و23–28٪ بعده)', 'w'),
      ('2.2×', 'العائد الحقيقي على الإعلانات حسب GA4 (المنصات بتقول 8–12×)', ''), ('47%', 'من الطلبات بكوبون، و81٪ في سبتمبر', 'w')]
kh = ''.join(f'<div class="kpi {c}"><b>{v}</b><span>{l}</span></div>' for v, l, c in kp)
dec = [('مانرفعش الأسعار المعلنة دلوقتي', 'أغلب منتجاتنا أغلى من المنافسين أصلاً، وأكتر من نص القطع بتتباع بكوبون.'),
       ('سقف للخصم وقواعد للكوبونات', '15٪ في 4 مواسم بس، وأكواد المؤثرين 10٪. لو القطع بكوبون نزلت من 50٪ لـ 35٪، السعر الفعلي يزيد 2.5–3٪.'),
       ('3 منتجات بس مرشحة للرفع', 'فرشاة سليك 29 ← 39–45، وSleek Secret 75 ← 79–85، وكريم القدمين اختبار لـ 79.'),
       ('نغير توزيع الصرف', 'نزوّد جوجل (5.1×)، ونقلل ميتا (1.27×)، ونثبت تيك توك 15٪. الشعر واللمعة في الشتا، والتان من مارس.'),
       ('المؤثرين بشروط', '46٪ من صرف التسويق، و9 تعاونات بس من 21 ليهم كود عليه مبيعات. أي تعاون جاي بكود أو رابط.')]
dh = ''.join(f'<div class="step"><span>{i+1}</span><h4>{t}</h4><p>{p}</p></div>' for i, (t, p) in enumerate(dec))
slide('01', 'EXECUTIVE SUMMARY', 'الملخص التنفيذي', f'''<p class="lede">a'mie باعت بـ <b>1.85 مليون ريال صافي</b> في 6 شهور وصرفت <b>355 ألف</b> على التسويق. التان شال نص المبيعات، وبعد الموسم المبيعات نزلت 40٪ والكوبونات وصلت 81٪. a'mie براند <b>بريميوم سعودي</b>، فمافيش مساحة نرفع الأسعار بشكل عام، والفلوس الحقيقية في تقليل الكوبونات.</p>
<div class="kpis">{kh}</div><div class="dec5">{dh}</div>''')

# ---------- 02 performance ----------
mt = '<table class="t sm"><tr><th>الشهر</th><th>الطلبات</th><th>صافي المبيعات</th><th>متوسط الطلب</th><th>إعلانات</th><th>مؤثرين</th><th>التسويق ÷ المبيعات</th><th>بكوبون</th></tr>'
for i in range(6):
    ix = 'b' if M.mk_pct[i] > 20 else 'g'
    mt += f'<tr><td>{M.months[i]}</td><td class="nm">{fmt(M.orders[i])}</td><td class="nm">{fmt(M.net[i])}</td><td class="nm">{M.aov[i]:.0f}</td><td class="nm">{fmt(M.ads_m[i])}</td><td class="nm">{fmt(M.inf_m[i])}</td><td><span class="ix {ix}">{M.mk_pct[i]:.1f}%</span></td><td class="nm">{M.coupon[i]:.0f}%</td></tr>'
mt += f'<tr class="tt"><td>الإجمالي</td><td class="nm">{fmt(sum(M.orders))}</td><td class="nm">{fmt(sum(M.net))}</td><td class="nm">{sum(M.paid)/sum(M.orders):.0f}</td><td class="nm">{fmt(ta)}</td><td class="nm">{fmt(ti)}*</td><td><span class="ix b">19.2%</span></td><td class="nm">47%</td></tr></table>'
slide('02', 'PERFORMANCE · 1/3', 'آخر 6 شهور: صرفنا كام وجبنا كام', f'''<p class="lede">المبيعات كانت 360–400 ألف في الشهر لحد يوليو، وبعدين نزلت لـ 230–265 ألف من أغسطس. والصرف على التسويق ماقلش، فنسبته من المبيعات طلعت من 7٪ لـ 26٪.</p><div class="chart grow big"><h4>صافي المبيعات (من غير ضريبة) قصاد صرف التسويق في الشهر</h4>{M.chart_monthly()}</div>''')
slide('02', 'PERFORMANCE · 2/3', 'بالأرقام: كل شهر', f'''<div class="card">{mt}<p class="note">* فيه حوالي 11 ألف مؤثرين من غير تاريخ نشر. صافي المبيعات من طلبات زد من غير الملغية، ومن غير ضريبة وشحن. متوسط الطلب شامل الضريبة والشحن. الكوبونات في أكتوبر لحد 24 أكتوبر.</p></div>
<div class="kpis k4"><div class="kpi"><b>1,847,749</b><span>صافي المبيعات</span></div><div class="kpi"><b>192,877</b><span>إعلانات: سناب 94.6K · ميتا 56.1K · تيك توك 26.6K · جوجل 15.6K</span></div><div class="kpi"><b>162,669</b><span>مؤثرين</span></div><div class="kpi w"><b>−30%</b><span>متوسط الطلب: 408 في مايو ← 285 في أكتوبر</span></div></div>''')
slide('02', 'PERFORMANCE · 3/3', 'إيه اللي حصل: 3 مراحل', f'''<div class="tl"><div class="on"><b>مايو – يوليو: موسم التان</b><span>360–400 ألف في الشهر. Summer Set لوحدها 36٪ من مبيعات الفترة. التسويق 7–9٪، إلا يونيو (65 ألف مؤثرين).</span></div>
<div><b>أغسطس: الموسم خلص</b><span>المبيعات نزلت 42٪ عن يوليو. Summer Set من 365 قطعة لـ 210، وفي أكتوبر 22 بس. والكوبونات 62٪.</span></div>
<div><b>سبتمبر – أكتوبر: كوبونات أكتر</b><span>أعلى صرف إعلانات (44 ألف) مع ND96 بخصم 20٪، و81٪ من الطلبات بكوبون. المبيعات زادت 14٪ بس.</span></div>
<div><b>النتيجة</b><span>متوسط الطلب نزل من 408 لـ 285 (−30٪)، والتسويق بقى ربع المبيعات.</span></div></div>
<div class="chart grow"><h4>كل ما الكوبونات زادت، متوسط قيمة الطلب نزل</h4>{M.chart_coupon()}</div>''')

# ---------- 03 channels ----------
gt = '''<table class="t"><tr><th>المنصة</th><th>الصرف</th><th>مشتريات المنصة</th><th>مشتريات GA4</th><th>إيراد GA4</th><th>ROAS GA4</th><th>المنصة بتكبّر</th></tr>
<tr><td>جوجل</td><td class="nm">15,590</td><td class="nm">419</td><td class="nm">276</td><td class="nm">80,037</td><td><span class="ix g">5.13</span></td><td class="nm">1.5×</td></tr>
<tr><td>سناب</td><td class="nm">45,982</td><td class="nm">1,760</td><td class="nm">334</td><td class="nm">102,924</td><td><span class="ix w">2.24</span></td><td class="nm">5.3×</td></tr>
<tr><td>ميتا</td><td class="nm">30,571</td><td class="nm">763</td><td class="nm">133</td><td class="nm">38,914</td><td><span class="ix b">1.27</span></td><td class="nm">5.7×</td></tr>
<tr><td>تيك توك</td><td class="nm">20,137</td><td class="nm">649</td><td class="nm">81</td><td class="nm">25,116</td><td><span class="ix b">1.25</span></td><td class="nm">8.0×</td></tr></table>'''
slide('03', 'CHANNELS · 1/2', 'القنوات: المنصة بتقول إيه، وGA4 بيقول إيه', f'''<p class="lede">كل منصة بتحسب نفس الطلب لنفسها، فمجموع اللي المنصات بتقول إنها جابته (2.0 مليون) قريب من كل مبيعات المتجر. GA4 بيحسب الطلب مرة واحدة، فهو الأقرب للحقيقة.</p>
<div class="cols2 w2"><div class="chart"><h4>ROAS: المنصة قصاد GA4</h4>{html_roas()}</div><div class="card"><h4>20 يوليو – 30 أكتوبر</h4>{gt}<p class="note">GA4 بدأ يسجل المشتريات صح من 20 يوليو. وهو بيحسب آخر ضغطة، فممكن يظلم سناب وتيك توك اللي بيعرّفوا العميلة على البراند.</p></div></div>''')

ct = '''<table class="t sm"><tr><th>الفئة</th><th>صافي المبيعات</th><th>النصيب</th><th>إعلانات</th><th>مؤثرين</th><th>التسويق ÷ المبيعات</th></tr>
<tr><td>التان</td><td class="nm">935,386</td><td class="nm">50.6%</td><td class="nm">88,255</td><td class="nm">44,091</td><td><span class="ix g">14.1%</span></td></tr>
<tr><td>اللمعة والهايلايتر</td><td class="nm">331,883</td><td class="nm">18.0%</td><td class="nm">47,282</td><td class="nm">61,274</td><td><span class="ix b">32.7%</span></td></tr>
<tr><td>الشعر</td><td class="nm">275,568</td><td class="nm">14.9%</td><td class="nm">32,757</td><td class="nm">41,954</td><td><span class="ix b">27.1%</span></td></tr>
<tr><td>العناية بالجسم</td><td class="nm">166,892</td><td class="nm">8.8%</td><td class="nm">15,313</td><td class="nm">9,107</td><td><span class="ix g">14.6%</span></td></tr>
<tr><td>المعطرات والمسك</td><td class="nm">109,629</td><td class="nm">5.9%</td><td class="nm">4,852</td><td class="nm">5,057</td><td><span class="ix g">9.0%</span></td></tr></table>'''
pt = '<table class="t sm"><tr><th></th><th>المنتج</th><th>القطع</th><th>صافي المبيعات</th><th>التسويق ÷ المبيعات</th><th>بكوبون</th></tr>'
for n, s, u, m, p, c in M.prod_rows[:8]:
    ix = 'b' if p > 30 else ('g' if p < 12 else 'w')
    pt += f'<tr><td class="pi">{pic(n)}</td><td>{n}</td><td class="nm">{fmt(u)}</td><td class="nm">{fmt(s)}</td><td><span class="ix {ix}">{p:.1f}%</span></td><td class="nm">{c:.0f}%</td></tr>'
pt += '</table>'
slide('03', 'PRODUCTS · 2/2', 'الفئات والمنتجات: مين بيجيب ومين بيصرف', f'''<div class="cols2"><div class="col"><div class="card"><h4>الفئات</h4>{ct}</div>
<div class="callout"><b>أول حاجة نوقفها:</b> ستيك Chocolate صرفنا عليه إعلانات أكتر من مبيعاته (134٪)، ومجموعة Chocolate 58٪. <b>Into The Glow</b> 47٪ تسويق و74٪ بكوبون. <b>Hair Set</b> 32٪، أغلبه مؤثرين. أما المعطرات وكريم القدمين وGlow Set فبتتباع بتسويق قليل (5–12٪).</div></div>
<div class="card"><h4>أعلى 8 منتجات</h4>{pt}</div></div>''')

# ---------- 04 market ----------
mk = '''<table class="t sm"><tr><th>الفئة</th><th>حجم السوق (منخفض · متوسط · عالي)</th><th>الثقة</th><th>من مبيعاتنا</th><th>حصتنا</th><th>بحث جوجل</th></tr>
<tr><td>التان</td><td class="nm">30 · 60 · 120M</td><td>منخفضة</td><td class="nm">50.6%</td><td class="nm">≈2%</td><td class="nm">31,328</td></tr>
<tr><td>اللمعة والهايلايتر</td><td class="nm">25 · 60 · 150M</td><td>منخفضة</td><td class="nm">18.0%</td><td class="nm">≈1%</td><td class="nm">11,009</td></tr>
<tr><td>تصفيف الشعر</td><td class="nm">85 · 160 · 290M</td><td>منخفضة–متوسطة</td><td class="nm">14.9%</td><td class="nm">≈0.3%</td><td class="nm">23,657</td></tr>
<tr><td>العناية بالجسم</td><td class="nm">835 · 1,215 · 1,800M</td><td>منخفضة–متوسطة</td><td class="nm">8.8%</td><td class="nm">≈0.03%</td><td class="nm">5,985</td></tr>
<tr><td>المعطرات والمسك</td><td class="nm">958 · 1,141 · 1,342M</td><td>منخفضة</td><td class="nm">5.9%</td><td class="nm">≈0.02%</td><td class="nm">1,460</td></tr>
<tr><td>الهدايا والإكسسوارات</td><td class="nm">50 · 250 · 790M</td><td>منخفضة جداً</td><td class="nm">1.7%</td><td>—</td><td>—</td></tr></table>'''
slide('04', 'MARKET SIZE · 1/2', 'حجم السوق السعودي لكل فئة (ريال في السنة)', f'''<p class="lede">فئاتنا الأقوى (التان، واللمعة، والشعر) أسواق متخصصة وصغيرة، وحصتنا فيها 0.3–2٪. والأسواق الكبيرة (العناية بالجسم والمعطرات) حصتنا فيها أقل من 0.05٪، والمنافسة فيها على السعر.</p>
<div class="cols2 w2"><div class="chart"><h4>حجم السوق بالمليون ريال (منخفض ← عالي، والخط = المتوسط)</h4>{html_market()}<p class="note">الشريط من التقدير المنخفض للعالي، والخط هو المتوسط.</p></div><div class="card">{mk}<p class="note">الحصة على تقدير مبيعات سنوية 2.8–3.9 مليون. بحث جوجل = مرات الظهور في بحث مش باسم البراند (Search Console، 6 شهور)، ونسبة الضغط أقل من 0.3٪.</p></div></div>''')
slide('04', 'MARKET SIZE · 2/2', 'الأرقام دي جاية منين، ويهمنا منها إيه', '''<div class="cols3"><div class="card good"><h4>مؤكد من مصدره (3 نوفمبر)</h4><ul><li>سكان السعودية 35.3 مليون، والسعوديات 9.8 مليون، 36٪ منهم 15–34 سنة.</li><li>الجمال والعناية الشخصية 4.8 مليار دولار (2025، IMARC).</li><li>العناية بالشعر 765–884 مليون دولار (TechSci وIMARC).</li><li>العناية من الشمس 137 مليون دولار (IMARC).</li><li>الأونلاين 15–20٪ من سوق الجمال (ECDB).</li></ul></div>
<div class="card warn"><h4>حدود الأرقام</h4><ul><li>مافيش رقم منشور للسعودية لزيت التان، ولا هايلايتر الجسم، ولا واكس الشعر للستات: محسوبة من تحت (عدد العميلات × متوسط الصرف).</li><li>أرقام Statista ورا paywall، ومنها رقم المعطرات.</li><li>الأرقام <b>اتجاه</b> مش نهائية، وKeyword Planner (البرومبت 30) هيدي حجم البحث الحقيقي.</li></ul></div>
<div class="card"><h4>يهمنا منها إيه</h4><ul><li>النمو مش هييجي من حصة كبيرة في سوق صغير.</li><li>نكبر في الفئات المتخصصة اللي فيها طلب على جوجل وترتيبنا ضعيف (SEO وGoogle Search).</li><li>الشعر بيتباع طول السنة، فيغطي على موسمية التان.</li><li>العناية بالجسم والمعطرات إضافة للسلة، مش حرب أسعار.</li></ul></div></div>''')

# ---------- 05 positioning ----------
lad = '''<div class="lad"><div><span class="role" style="background:#D9D8D7;color:#191919">1</span><b>الماركت بليس</b><p>نون، أمازون، الصيدليات. وسيط 25–56 ريال. a'mie مش بتنافس هنا.</p></div>
<div><span class="role" style="background:#C9A86A;color:#191919">2</span><b>براندات سعودية</b><p>Clara، Hearts، Surge، Jayla، Ladeena، MZN. 35–195 ريال، وعروض طول الوقت.</p></div>
<div class="me"><span class="role" style="background:#5E2E21;color:#fff">3</span><b>a'mie</b><p>65–482 ريال. براند سعودي، تغليف يصلح هدية، ومجموعات روتين كاملة.</p></div>
<div><span class="role" style="background:#6B595C;color:#fff">4</span><b>براندات عالمية</b><p>Sol de Janeiro، Tan-Luxe، Slick، Carrot Sun، Eucerin. 48–164، وكتير منها بخصم 25–50٪.</p></div></div>'''
slide('05', 'POSITIONING · 1/2', "a'mie في أنهي شريحة؟ البريميوم السعودي", f'''<div class="cols2 r"><div class="chart"><h4>سعر القطعة بالريال (3 نوفمبر)</h4>{M.chart_position()}<p class="note">الأحجام مختلفة، فده موقع السعر في عين العميلة، مش سعر المل.</p></div>
<div class="col">{lad}<div class="callout">في كل فئة تقريباً، سعرنا أعلى من الماركت بليس 2–5 مرات، وأعلى من أغلب البراندات السعودية، وفي مستوى العالمية أو أعلى بعد خصوماتها. العميلة بتدفع عشان البراند والتغليف والتجربة، مش عشان السعر.</div></div></div>''')
comp = [('الشعر', 'Clara', 'سعودي · 282 ألف على تيك توك · في الدواء · خصم على كل المنتجات', 'واكس 94 قصاد 129 · ماسكارا 83 قصاد 75 · فرشاة 47 قصاد 29', 'wax.jpg'),
        ('اللمعة', 'Hearts', 'سعودي · 69.5 ألف على تيك توك · عند موزعين كتير', 'Body Glow 96 قصاد 176 · ستيك 42 (35.70 بعد الخصم) قصاد 79', 'bodyglow.jpg'),
        ('التان', 'Surge + Carrot Sun / Beesline', 'Surge تقييم 4.98 · العالميين بخصم 50٪ في نهدي', '0.78 ريال للمل قصاد 1.06 · Carrot Sun 80.5 لـ 200 مل', 'deeptan.jpg'),
        ('العناية بالجسم', 'Ladeena · Waves · MZN', 'براندات سعودية في نفس الشريحة تقريباً', 'زبدة 85–129 قصاد 119 (في النص)', 'lembutter.jpg'),
        ('المعطرات', "Jayla · Victoria's Secret", 'Jayla 80.6 ألف متابع ومؤثرات', 'بودي مست 50–73 قصاد 129 · مسك 75–80 قصاد 99', 'flora.jpg')]
cc = ''.join(f'<div class="comp"><div class="cimgw"><img src="img/{im}"></div><div><span class="sub">{c}</span><h4>{n}</h4><p>{w}</p><p class="vs">{v}</p></div></div>' for c, n, w, v, im in comp)
slide('05', 'COMPETITORS · 2/2', 'المنافسين الحقيقيين في كل فئة', f'''<div class="comps">{cc}</div><p class="note">من 70 سعر منافس: 23 اتطابق مع البحث، و35 اختلف (أغلبهم نزل بخصم)، و11 ماقدرناش نتأكد منهم. الكوبونات والعروض منتشرة عند كل المنافسين.</p>''')

# ---------- 06 pricing ----------
def ptable(cats):
    h = '<table class="t sm pr"><tr><th></th><th>المنتج</th><th>السعر</th><th>بكوبون</th><th>أقرب منافسين (ريال)</th><th>القرار</th><th>النطاق</th><th>أقصى خصم</th></tr>'
    for cat, rows in M.price_rows:
        if cat not in cats: continue
        h += f'<tr class="cat"><td colspan="8">{cat}</td></tr>'
        for r in rows:
            up = 'لـ' in r[5]
            h += f'<tr><td class="pi">{pic(r[0])}</td><td><b>{r[0]}</b><small class="d">{r[7]}</small></td><td class="nm">{r[1]}</td><td class="nm">{r[2]}</td><td><small>{r[3]}</small></td><td>{r[4]}</td><td>{"<span class=\"ix w\">"+r[5]+"</span>" if up else "<span class=\"nm\">"+r[5]+"</span>"}</td><td><small>{r[6]}</small></td></tr>'
    return h + '</table>'
rule = '<p class="note">«تثبيت» = الحد الأقصى هو السعر الحالي. أقصى خصم: 15٪ للمجموعات ومنتجات الموسم في موسمها بس، و10٪ للمنتجات اللي بتتباع لوحدها أو نسبة الكوبون فيها قليلة، و0٪ وقت اختبار الرفع. القاعدة: مانرفعش سعر أي منتج قبل ما نسبة قطعه بكوبون تنزل تحت 50٪.</p>'
slide('06', 'PRICING · 1/4', 'التسعير: التان والمعطرات', ptable(['التان', 'المعطرات']) + rule)
slide('06', 'PRICING · 2/4', 'التسعير: اللمعة والهايلايتر', ptable(['اللمعة والهايلايتر']) + rule)
slide('06', 'PRICING · 3/4', 'التسعير: الشعر والعناية بالجسم', ptable(['الشعر', 'العناية بالجسم']) + '<p class="note">باقي المنتجات (Lemongrass Set، اللافندر، Back to Routine، كريم اليدين، الإكسسوارات): تثبيت، وأقصى خصم 10٪.</p>')
be = [('فرشاة سليك', 'sleek.jpg', '29', '39 – 45', '397', '26–36٪', '3,452 – 5,523', 'فرشاة Clara بـ 47 (كانت 59). أصغر خطر، وتبدأ الأول في ديسمبر.'),
      ('Sleek Secret', 'mascara.jpg', '75', '79 – 85', '340', '5–12٪', '1,183 – 2,957', 'سعر المل 5 ريال قصاد 7.3–8.7 عند Slick وSmooth. يناير.'),
      ('كريم القدمين', 'foot.jpg', '75', '79', '434', '5٪', '1,510', 'Eucerin بـ 48 بعد الخصم في نهدي، فالاختبار صغير. فبراير.')]
bh = ''.join(f'''<div class="rz"><div class="rzi"><img src="img/{im}"></div><h4>{n}</h4><div class="big2"><div><b>{a}</b><span>دلوقتي</span></div><div><b class="to">{b}</b><span>المقترح</span></div></div>
<div class="rzm"><div><span>قطع في 6 شهور</span><b>{u}</b></div><div><span>الإيراد يفضل زي ما هو لو المبيعات نزلت لحد</span><b>{d}</b></div><div><span>إيراد إضافي لو المبيعات ماقلتش (ريال)</span><b>{x}</b></div></div><p class="note">{note}</p></div>''' for n, im, a, b, u, d, x, note in be)
slide('06', 'PRICING · 4/4', 'المرشحين للرفع، وإزاي نختبر', f'''<div class="cols4 rzs">{bh}<div class="card"><h4>طريقة الاختبار</h4><ul><li>منتج واحد كل مرة، لمدة 4 أسابيع، ومن غير أي كوبون عليه.</li><li>نقارن القطع في الأسبوع بمتوسط آخر 8 أسابيع، من غير أسابيع الجمعة البيضا ولا الطلبات اللي كان فيها كوبون.</li><li>لو النزول أقل من الرقم، نثبت السعر الجديد. لو أكتر، نرجع للقديم.</li><li>الإيراد الإضافي من الـ 3 مع بعض حوالي 6–10 آلاف في 6 شهور، قصاد 45–55 ألف من تقليل الكوبونات.</li></ul></div></div>''')

# ---------- 07 discounts ----------
slide('07', 'DISCOUNTS · 1/2', 'الخصومات: سقف واضح ومواسم محددة', '''<p class="lede">47٪ من الطلبات كانت بكوبون، و81٪ في سبتمبر. Summer26 جاب 1,178 طلب، وND96 جاب 970. لما الكوبون بيبقى موجود طول الوقت، العميلة بتتعود ماتشتريش من غيره.</p>
<div class="rules4"><div><span>15%</span><p><b>بحد أقصى في المواسم بس</b>، وكل منتج مايعديش الحد بتاعه في جدول التسعير.</p></div><div><span>10%</span><p><b>أكواد المؤثرين</b>، وكود العميلة الراجعة لمرة واحدة. دول بس المسموحين بره المواسم، وكل كود ليه تاريخ نهاية.</p></div><div><span>0%</span><p>على أي منتج <b>وقت اختبار الرفع</b>، وعلى فرشاة سليك لوحدها (جوه المجموعات عادي).</p></div><div><span>1×</span><p><b>الخصومات ماتتجمعش:</b> الكوبون مايشتغلش مع عرض تاني.</p></div></div>
<div class="cal"><div><b>الجمعة البيضا</b><span>نوفمبر · اللمعة والهدايا</span></div><div><b>رمضان والعيد</b><span>من حوالي 8 فبراير · الهدايا والتوزيعات</span></div><div><b>بداية الصيف</b><span>مايو – يونيو · التان</span></div><div><b>اليوم الوطني</b><span>سبتمبر · المتجر كله</span></div><div><b>مدة كل موسم</b><span>أسبوع لأسبوعين بالكتير. Summer26 فضل 4 شهور، وND96 فضل 40 يوم بخصم 20٪.</span></div></div>''')
slide('07', 'DISCOUNTS · 2/2', 'بدل الخصم، والأثر المتوقع', '''<div class="cols2"><div class="card"><h4>إزاي نبيع من غير ما نكسر السعر</h4><table class="t sm"><tr><th>بدل</th><th>مثال</th><th>ليه أحسن</th></tr>
<tr><td>مجموعات بسعر أحسن</td><td>Hair Set سعرها 282 = نفس مجموع القطع بالظبط. نخليها أقل بوضوح، ونراجعها لو رفعنا الفرشاة</td><td>متوسط الطلب يعلى، وسعر كل منتج يفضل زي ما هو</td></tr>
<tr><td>هدية مع حد أدنى</td><td>ستيك هايلايتر أو Lip Plump (بعد ما نتأكد من المخزون) فوق 400 ريال</td><td>تكلفة الهدية أقل من خصم 15٪ على الطلب كله</td></tr>
<tr><td>شحن مجاني</td><td>فوق 300–350 ريال (أعلى من متوسط الطلب، حوالي 260 من غير الشحن)</td><td>بيرفع الطلب. لو الحد أقل من المتوسط، نخسر إيراد الشحن (163 ألف في 6 شهور)</td></tr>
<tr><td>العميلة الراجعة</td><td>كود لمرة واحدة بعد أول طلب بـ 30 يوم</td><td>بيكافئ الولاء، مش أي حد</td></tr></table></div>
<div class="col"><div class="card"><h4>الأثر المتوقع</h4><div class="formula">السعر الفعلي = السعر المعلن × (1 − نسبة القطع بكوبون × متوسط الخصم)</div><div class="big2"><div><b>92%</b><span>العميلة بتدفع دلوقتي من السعر المعلن</span></div><div><b>94.5%</b><span>لو الكوبونات نزلت لـ 35٪ بسقف 15٪</span></div><div><b>45–55K</b><span>ريال في 6 شهور لو عدد الطلبات فضل زي ما هو</span></div></div><p class="note">متوسط الخصم حوالي 16٪، و49٪ من القطع بكوبون. ده تقدير لازم يتختبر، لإن جزء من العميلات ممكن ماتشتريش من غير كوبون.</p></div>
<div class="card"><h4>الخصم اللي عنده الربح صفر (لما المحاسب يملا تكلفة القطعة)</h4><div class="formula">1 − (تكلفة القطعة + الشحن والدفع + التسويق للقطعة) × 1.15 ÷ السعر المعلن</div><p class="note">جاهزة في شيت الحسبة. التسويق للقطعة: Summer Set 59 · Hair Set 61 · الواكس 26 · كريم القدمين 4 ريال.</p></div></div></div>''')

# ---------- 08 media ----------
slide('08', 'MEDIA PLAN', 'فين نصرف: نوفمبر 2026 – فبراير 2027', '''<p class="lede">نفس الميزانية تقريباً (حوالي 30 ألف إعلانات في الشهر)، متوزعة على اللي بيجيب فعلاً حسب GA4. كل شهر ننقل 10 نقط من القناة الأضعف للأقوى، ومافيش قناة تعدي 50٪. وROAS جوجل محسوب على 15.6 ألف صرف بس، فممكن ينزل لما نزود.</p>
<div class="cols3"><div class="chart"><h4>حسب القناة</h4>
<div class="hb"><span>جوجل</span><div class="ht"><i style="width:8%;background:#D9D8D7"></i></div><span class="hv">8%</span><span class="hn">قبل</span></div><div class="hb"><span></span><div class="ht"><i style="width:40%;background:#5E2E21"></i></div><span class="hv">35–40%</span><span class="hn">بعد</span></div>
<div class="hb"><span>سناب</span><div class="ht"><i style="width:49%;background:#D9D8D7"></i></div><span class="hv">49%</span><span class="hn">قبل</span></div><div class="hb"><span></span><div class="ht"><i style="width:30%;background:#5E2E21"></i></div><span class="hv">30%</span><span class="hn">بعد</span></div>
<div class="hb"><span>ميتا</span><div class="ht"><i style="width:29%;background:#D9D8D7"></i></div><span class="hv">29%</span><span class="hn">قبل</span></div><div class="hb"><span></span><div class="ht"><i style="width:15%;background:#5E2E21"></i></div><span class="hv">15%</span><span class="hn">بعد</span></div>
<div class="hb"><span>تيك توك</span><div class="ht"><i style="width:14%;background:#D9D8D7"></i></div><span class="hv">14%</span><span class="hn">قبل</span></div><div class="hb"><span></span><div class="ht"><i style="width:15%;background:#5E2E21"></i></div><span class="hv">15%</span><span class="hn">بعد</span></div>
<p class="note">جوجل 5.1× · سناب 2.2× وأكتر قناة بتجيب زيارات (68 ألف جلسة) · ميتا 1.27×: نختبر إعلانات جديدة · تيك توك 1.25×: للمحتوى، وClara قوية هناك.</p></div>
<div class="chart"><h4>حسب الفئة</h4>
<div class="hb"><span>الشعر</span><div class="ht"><i style="width:35%;background:#5E2E21"></i></div><span class="hv">35%</span><span class="hn"></span></div>
<div class="hb"><span>اللمعة والهايلايتر</span><div class="ht"><i style="width:35%;background:#5E2E21"></i></div><span class="hv">35%</span><span class="hn"></span></div>
<div class="hb"><span>العناية بالجسم</span><div class="ht"><i style="width:15%;background:#6B595C"></i></div><span class="hv">15%</span><span class="hn"></span></div>
<div class="hb"><span>براند وكتالوج</span><div class="ht"><i style="width:10%;background:#6B595C"></i></div><span class="hv">10%</span><span class="hn"></span></div>
<div class="hb"><span>المعطرات</span><div class="ht"><i style="width:5%;background:#C9A86A"></i></div><span class="hv">5%</span><span class="hn"></span></div>
<div class="hb"><span>التان</span><div class="ht"><i style="width:0%"></i></div><span class="hv">0%</span><span class="hn">لحد مارس</span></div>
<p class="note">الشعر بيتباع طول السنة · اللمعة للجمعة البيضا ومناسبات الشتا · التان نجهز حملاته على جوجل في فبراير ونبدأ مارس · رمضان (حوالي 8 فبراير): نحجز جزء من فبراير للهدايا.</p></div>
<div class="card"><h4>قواعد الصرف</h4><ul><li>أي منتج التسويق بتاعه أكتر من 30٪ من مبيعاته لمدة شهر، إعلاناته تتوقف أو تتغير (زي ستيك Chocolate).</li><li>نقيس بـ GA4 مش بأرقام المنصة، وكل الإعلانات عليها UTM.</li><li>المؤثرين: ميزانية لوحدها، وكل تعاون بكود أو رابط، ونقارن تكلفته باللي جابه قبل ما نجدد.</li><li>SEO على الكلمات اللي بنظهر فيها بنسبة ضغط أقل من 0.3٪: تان، واكس للشعر، لمعة جسم.</li></ul></div></div>''')

# ---------- 09 roadmap ----------
slide('09', 'ROADMAP · 1/2', 'خطة التنفيذ', '''<div class="cal six"><div><b>الأسبوع ده</b><span>نوقف أو نغير إعلانات ستيك ومجموعة Chocolate. ونقفل أو نقصّر Y10 وSh10 (لحد يونيو) وHS15 (15٪ لحد مايو)، وأكواد المؤثرين 10٪. كود 00002 (UGC بره السعودية) يفضل.</span><small>الإعلانات</small></div>
<div><b>نوفمبر</b><span>نطبق سقف الخصم (15٪ / 10٪) قبل الجمعة البيضا، ونعمل مجموعة للشعر ومجموعة للهدايا بدل الخصم.</span><small>التسويق + المتجر</small></div>
<div><b>نوفمبر</b><span>المحاسب يملا تكلفة القطعة في شيت الحسبة، عشان نحسب الخصم اللي عنده الربح صفر لكل منتج.</span><small>المحاسب</small></div>
<div><b>ديسمبر</b><span>اختبار رفع فرشاة سليك لـ 39 لمدة 4 أسابيع.</span><small>المتجر</small></div>
<div><b>يناير – فبراير</b><span>اختبار Sleek Secret لـ 79 (4 أسابيع)، وبعده كريم القدمين لـ 79 (4 أسابيع).</span><small>المتجر</small></div>
<div><b>فبراير</b><span>نجهز حملات التان على جوجل، ونقرر سعر موسم 2027، ونحجز ميزانية رمضان.</span><small>الإعلانات</small></div></div>
<div class="callout">أي تغيير في الأسعار أو الكوبونات على زد بيتعمل بعد موافقة الفريق، وبعد ما ناخد نسخة من الأسعار الحالية.</div>''')
slide('09', 'DATA NOTES · 2/2', 'حدود البيانات', '''<div class="cols2"><div class="card"><h4>الأرقام جاية منين</h4><ul><li><b>المبيعات:</b> طلبات زد (6,564 طلب من غير الملغية). صافي = من غير ضريبة 15٪ وشحن، وبعد الخصومات.</li><li><b>GA4:</b> المشتريات صح من 20 يوليو، والعملة دولار (× 3.75). لو الإيراد شامل الضريبة، يبقى ROAS الحقيقي حوالي 1.9 مش 2.2.</li><li><b>المؤثرين:</b> من شيت المؤثرين، وفيه أرقام شاملة الضريبة. 12 من 21 تعاون مالهمش كود. الأكواد اللي عليها مبيعات في زد 9، والشيت مسجل 6 بس، فلازم نوحّد المصدرين.</li><li><b>أسعار المنافسين</b> يوم 3 نوفمبر، وبتتغير مع العروض.</li><li><b>حجم السوق</b> تقديرات، وثقتها منخفضة في الفئات المتخصصة.</li></ul></div>
<div class="card warn"><h4>مستني يتأكد</h4><ul><li>سعر Summer Set: 482 ولا 582؟</li><li>سعر Hair Set: 282 ولا 268؟</li><li>زبدة الليمون قراس: زد بيبيعها بـ 119، والشيت بيقول 199.</li><li>تكلفة القطعة من المحاسب: كل الحسابات هنا على الإيراد، مش الربح.</li><li>مخزون Lip Plump قبل ما نستخدمه هدية.</li><li>Keyword Planner (البرومبت 30) لحجم البحث الحقيقي.</li></ul>
<p class="note">المصادر: زد · Snapchat Ads · Meta Ads · TikTok Ads · Google Ads · GA4 · Search Console · صفحات المنافسين (سيفورا، نهدي، واتسونز، كارفور، نون، أمازون، سلة، زد، تيك توك) · الهيئة العامة للإحصاء · IMARC · TechSci · ECDB.</p></div></div>''')

exec(open(os.path.join(HERE, 'deck_winners.py'), encoding='utf-8').read())
exec(open(os.path.join(HERE, 'deck_appendix.py'), encoding='utf-8').read())

# ---------- end ----------
pages.append('''<section class="page cover end"><img class="cimg" src="a/cover_full.jpg"><div class="ctitle"><div class="cen">THANK YOU</div><div class="cline"></div><p>«الجمال لا يُصنع... بل يُعتنى به حتى يتجلّى»</p><img src="a/logo_dark.png" class="lgend"></div>
<div class="cfoot"><span>amie-sa.com</span><span>a'mie · Market &amp; Pricing</span></div></section>''')

css = f'''<link rel="stylesheet" href="base.css"><link rel="stylesheet" href="extra.css"><style>
@font-face{{font-family:"Readex Pro";src:url("file://{FONT}/ReadexPro-VF.ttf");font-weight:160 700}}
@font-face{{font-family:"Montserrat";src:url("file://{FONT}/Montserrat-Light.ttf");font-weight:200 300}}
@font-face{{font-family:"Montserrat";src:url("file://{FONT}/Montserrat-Regular.ttf");font-weight:400 700}}
.kpis{{grid-template-columns:repeat(6,1fr)}}
.kpi.w b{{color:#9E3B32}}
.dec5{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;flex:1;min-height:0}}
.dec5 .step{{padding:14px 16px}}.dec5 .step p{{font-size:12.5px;color:#191919}}.dec5 h4{{font-size:14px}}
.col{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.chart svg{{display:block;max-height:330px;width:100%}}
.cols2.w2{{grid-template-columns:.85fr 1.15fr}}
table.t.sm{{font-size:11.5px}} table.t.sm th{{white-space:normal;padding:6px 8px}} table.t.sm td{{padding:4px 8px}}
.chart.grow{{flex:1;justify-content:center}} .chart.big svg{{max-height:440px}} .kpis.k4{{grid-template-columns:repeat(4,1fr)}} table.t{{font-size:13px}} .chart.grow svg{{max-height:290px}}
table.t .tt td{{font-weight:500;border-top:1px solid #191919}}
table.t td.pi{{width:46px;padding:3px 6px}}
.th{{width:38px;height:38px;object-fit:contain;display:block;background:#fff;border-radius:8px}}
table.t.pr td{{padding:4px 8px}} table.t.pr small.d{{display:block;font-size:9.5px;color:#6B595C;line-height:1.35}}
table.t tr.cat td{{background:#F2E4DF;color:#5E2E21;font-weight:500;font-size:11.5px;padding:4px 12px}}
.lad{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.lad div{{background:#fff;border:1px solid #E3E2E1;border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:4px}}
.lad div.me{{background:#F2E4DF;border-color:#5E2E21}}
.lad b{{font-weight:500}}.lad p{{font-size:12px;color:#6B595C}}
.comps{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;flex:1;min-height:0}}
.comp{{background:#fff;border:1px solid #E3E2E1;border-radius:14px;overflow:hidden;display:flex;flex-direction:column}}
.comp>div:last-child{{padding:12px 14px;display:flex;flex-direction:column;gap:6px}}
.cimgw{{height:190px;background:#fff;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #F0EFEE}}
.cimgw img{{max-height:170px;max-width:85%;object-fit:contain}}
.comp h4{{margin:0;font-size:16px}}.comp p{{font-size:12.5px}}.comp .vs{{background:#F2F2F2;border-radius:8px;padding:6px 8px;font-size:12px}}
.rzs{{grid-template-columns:1fr 1fr 1fr 1.1fr}}
.rz{{background:#fff;border:1px solid #E3E2E1;border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}}
.rzi{{height:120px;display:flex;align-items:center;justify-content:center}}.rzi img{{max-height:116px;max-width:80%;object-fit:contain}}
.rz h4{{margin:0;font-size:16px}}
.big2 b.to{{color:#5E2E21}}
.rzm{{display:grid;gap:4px}}.rzm div{{display:flex;justify-content:space-between;gap:8px;font-size:11.5px;border-top:1px solid #F0EFEE;padding-top:4px}}
.rzm span{{color:#6B595C}}.rzm b{{font-family:Montserrat;font-weight:500;direction:ltr;white-space:nowrap}}
.rules4{{flex:none}}
.rules4 div{{padding:16px 18px}}.rules4 p{{font-size:13px}}
.cal.six{{grid-template-columns:repeat(3,1fr);flex:1}}
.cal.six div{{padding:16px 18px;gap:6px}}.cal.six span{{font-size:13px}}.cal.six small{{margin-top:auto;color:#5E2E21}}
.formula{{border:1px dashed #5E2E21;border-radius:10px;padding:8px 12px;text-align:center;font-size:13px;margin:4px 0 8px}}
.big2{{flex-wrap:wrap}}
.hb{{grid-template-columns:110px 1fr 58px 44px}}
.wcols{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.wcol{{background:#fff;border:1px solid #E3E2E1;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}}
.wcol.win{{background:#F2E4DF;border-color:#E8CFC6}}
.wh{{display:flex;align-items:center;gap:10px}}.wh p{{font-size:12px;color:#6B595C}}
.wgrid{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
.wc{{background:#fff;border:1px solid #EEEDEC;border-radius:12px;overflow:hidden;display:flex;flex-direction:column}}
.wi{{height:92px;display:flex;align-items:center;justify-content:center;position:relative;background:#fff;flex:none}}.wi img{{max-height:86px;max-width:90%;object-fit:contain}}
.nw{{position:absolute;top:6px;left:6px;font-size:10px;background:#5E2E21;color:#fff;border-radius:999px;padding:1px 7px}}
.wt{{padding:6px 9px 8px;display:flex;flex-direction:column;gap:2px}}.wt h5{{margin:0;font-weight:500;font-size:12.5px}}
.wn{{display:flex;align-items:baseline;gap:5px}}.wn b{{font-family:Montserrat;font-weight:300;font-size:22px;color:#5E2E21}}.wn span{{font-size:9.5px;color:#6B595C;line-height:1.2}}
.wt p{{font-size:10.5px;color:#191919;line-height:1.45}}
.wall{{display:grid;grid-template-columns:auto 230px 230px 1fr;gap:12px;align-items:center;background:#fff;border:1px solid #E3E2E1;border-radius:14px;padding:10px 14px}}
.wall .wc{{flex-direction:row}}.wall .wi{{width:70px;height:84px}}.wall .wi img{{max-height:76px}}
.wall .note{{margin:0}}
table.heat td.hc{{text-align:center;font-family:Montserrat;font-size:11px;padding:1px 4px;border-bottom:2px solid #fff}}
table.heat td{{padding:1px 8px}} table.heat th{{text-align:center}} table.heat td.pi{{width:30px}} table.heat .th{{width:22px;height:22px}}
table.cand td.mk{{text-align:center;color:#5E2E21;font-size:16px}} table.cand th{{white-space:normal;text-align:center}}
table.mpt td{{padding:11px 12px;font-size:13.5px}} table.ap{{font-size:10.5px;line-height:1.35}} table.ap td{{padding:2px 7px}} table.ap th{{padding:4px 7px}} table.ap tr.me td{{background:#F2E4DF;color:#5E2E21;font-weight:500}} table.ap td.src{{font-size:10px;color:#6B595C}} table.ap .ix{{white-space:nowrap;font-size:10px}}
table.cand small.d{{display:block;font-size:10.5px;color:#6B595C}} table.cand .th{{width:40px;height:40px}} table.cand td{{padding:3px 8px}} table.heat{{font-size:11px}} table.heat .ix{{white-space:nowrap;font-size:10px;padding:0 6px}} table.heat td:nth-child(2){{white-space:nowrap}} table.heat .th{{width:28px;height:28px}} table.heat td.hc{{padding:4px 2px}} table.heat th{{padding:5px 3px}}
.rr{{display:grid;grid-template-columns:70px 1fr 70px;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid #F0EFEE}}
.rn{{font-size:13px;font-weight:400}}.rb{{display:flex;flex-direction:column;gap:5px}}.rb .ht{{height:14px}}
.rv{{display:flex;flex-direction:column;font-family:Montserrat;direction:ltr;text-align:left;line-height:1.3}}.rv span{{font-size:11px;color:#6B595C}}.rv b{{font-size:16px;font-weight:500;color:#5E2E21}}
.mr{{display:grid;grid-template-columns:120px 1fr 70px;gap:12px;align-items:center;padding:9px 0}}
.mt{{position:relative;height:16px;background:#F2F2F2;border-radius:8px}}.mt i{{position:absolute;top:0;bottom:0;background:#D9C2B8;border-radius:8px}}
.mt em{{position:absolute;top:-4px;bottom:-4px;width:3px;background:#5E2E21;border-radius:2px}}
.mr b{{font-size:13px;font-weight:500}}
.axl{{display:flex;justify-content:space-between;font-family:Montserrat;font-size:10px;color:#9A9897}}
.chart .note{{margin-top:auto}}
.card h4{{margin-bottom:8px}}
</style>'''
html = f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>a\'mie · Market &amp; Pricing</title>{css}</head><body>{"".join(pages)}</body></html>'
open(OUT, 'w', encoding='utf-8').write(html)
print('slides', len(pages))
