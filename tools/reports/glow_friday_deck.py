# Glow Friday 2026 strategy deck (1280x720, same design system as the product-tree / market deck).
# Usage: python3 -I glow_friday_deck.py <out.html>   (assets in reports/market-deck/)
import sys, os, re
OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'market_deck.py'), encoding='utf-8').read()
head = src[:src.index('# ---------- cover ----------')]
_orig_argv = list(sys.argv); sys.argv = ['x', '/dev/null']
exec(head)                                   # M, fmt, FONT, slide(), pic(), pages, html_roas()
sys.argv = _orig_argv
OUT = sys.argv[1]
css_src = src[src.index("css = f'''"):src.index("</style>'''") + len("</style>'''")]
exec(css_src)                                # css
HDR = '<div class="hdr"><img src="a/logo_dark.png" class="lg"><i></i><span>Glow Friday Strategy</span><i></i><span>VOL 1.0</span><i></i><span>Nov 2026</span></div>'
pages.clear()

def S(n, en, ar, body):
    pages.append(f'<section class="page">{HDR}<div class="body"><div class="ph"><span class="pnum">{n}</span><div><div class="pen">{en}</div><h2>{ar}</h2></div></div>{body}</div><div class="ftr"><span>amie-sa.com</span><span>{len(pages)+1:02d}</span></div></section>')

# ---------- cover ----------
pages.append('''<section class="page cover"><img class="cimg" src="a/cover_full.jpg"><div class="ctop"><img src="a/logo_dark.png" class="lgc"></div>
<div class="ctitle"><div class="cen">GLOW FRIDAY <span>STRATEGY 2026</span></div><div class="cline"></div><h1>استراتيجية Glow Friday</h1><p>عرض a'mie للجمعة البيضا · 25 نوفمبر – 1 ديسمبر 2026 · مبنية على أرقام آخر 6 شهور وموقع a'mie في السوق</p></div>
<div class="cfoot"><span>amie-sa.com</span><span>نوفمبر 2026</span></div></section>''')

agenda = [('01', 'الفكرة في صفحة واحدة', 'One-page summary'), ('02', 'إحنا فين دلوقتي: الأرقام والسوق', 'Where we start'),
          ('03', 'موقعنا: ليه مانكسرش السعر', 'Positioning'), ('04', 'العرض: 4 مجموعات بسعر ثابت', 'The offer'),
          ('05', 'الأهداف بالأرقام', 'Targets'), ('06', 'الجمهور والقنوات والميزانية', 'Audiences & media'),
          ('07', 'الجدول الزمني', 'Timeline'), ('08', 'القياس وقواعد القرار اليومي', 'Measurement'),
          ('09', 'المخاطر وقبل الإطلاق', 'Risks & checklist')]
rows = ''.join(f'<div class="tr"><span class="tn">{n}</span><span class="tar">{a}</span><span class="tdots"></span><span class="ten">{e}</span></div>' for n, a, e in agenda)
pages.append(f'<section class="page">{HDR}<div class="body"><div class="tocwrap"><div class="pen big">AGENDA</div>{rows}</div></div><div class="ftr"><span>amie-sa.com</span><span>02</span></div></section>')

# ---------- 01 summary ----------
S('01', 'ONE-PAGE SUMMARY', 'الفكرة في صفحة واحدة', '''<p class="lede">Glow Friday هي جمعة a'mie البيضا، بس بطريقتنا: <b>مجموعات مختارة بسعر ثابت لمدة 7 أيام</b>، من غير كوبونات ومن غير خصم على المتجر كله. الهدف إننا نكبّر قيمة الطلب ونحرّك مجموعات الشتا، من غير ما نعلّم العميلة تستنى الكوبون تاني.</p>
<div class="kpis k4"><div class="kpi"><b>4</b><span>مجموعات بسعر ثابت (الشعر، الليمون قراس، سهرة تشوكلت، ثلاثي العطور)</span></div><div class="kpi"><b>7</b><span>أيام بس: 25 نوفمبر – 1 ديسمبر، ودخول مبكر للعميلات يوم 24</span></div><div class="kpi"><b>~100K</b><span>ريال صافي في الأسبوع (حوالي ضعف الأسبوع العادي)</span></div><div class="kpi"><b>320+</b><span>متوسط قيمة الطلب المستهدف (كان 285 في أكتوبر)</span></div></div>
<div class="dec5"><div class="step"><span>1</span><h4>مانكسرش السعر</h4><p>a'mie بريميوم سعودي. المنافسين بيخصموا 25–50٪، وإحنا ندخل بمجموعات بقيمة واضحة.</p></div>
<div class="step"><span>2</span><h4>المجموعات بدل الكوبون</h4><p>العرض على 4 مجموعات بس، وأي كود مايشتغلش معاها. Into The Glow ومارشميلو برا العرض لإنهم بيبيعوا لوحدهم.</p></div>
<div class="step"><span>3</span><h4>سناب الأول</h4><p>الحصة الأكبر (35–40٪) لسناب: وصول وإعادة استهداف. عائد جوجل (5.1×) كان عالي بسبب أيام المؤثرين، فجوجل 30٪ للبحث على «سكراب» و«هدايا» و«مسك».</p></div>
<div class="step"><span>4</span><h4>العميلات القدام الأول</h4><p>دخول مبكر يوم 24 برسالة. أرخص طلبات، ومن غير ما نصرف إعلانات.</p></div>
<div class="step"><span>5</span><h4>بعدها نرجع للسعر</h4><p>يوم 2 ديسمبر الأسعار ترجع زي ما هي، ومن غير تمديد. ده اللي هيحمي البراند بعد الحملة.</p></div></div>''')

# ---------- 02 where we start ----------
S('02', 'WHERE WE START', 'إحنا فين دلوقتي: الأرقام والسوق', f'''<div class="cols2"><div class="card"><h4>أرقامنا (مايو – أكتوبر 2026)</h4>
<table class="t sm"><tr><th>المؤشر</th><th>الرقم</th><th>يعني إيه للحملة</th></tr>
<tr><td>صافي المبيعات في أكتوبر</td><td class="nm">230,632</td><td>حوالي 7.7 ألف في اليوم: ده الأساس اللي هنقيس عليه</td></tr>
<tr><td>متوسط قيمة الطلب</td><td class="nm">408 ← 285</td><td>نزل 30٪ مع الكوبونات: الحملة لازم ترفعه</td></tr>
<tr><td>طلبات بكوبون في سبتمبر</td><td><span class="ix b">81%</span></td><td>ND96 فضل 40 يوم بخصم 20٪: مانكررهاش</td></tr>
<tr><td>التسويق ÷ المبيعات</td><td class="nm">19.2%</td><td>كان 7٪ في الموسم و26٪ بعده: سقف الحملة 20٪</td></tr>
<tr><td>ROAS حقيقي (GA4)</td><td class="nm">جوجل 5.1 · سناب 2.2 · ميتا 1.3 · تيك توك 1.25</td><td>عائد جوجل كان عالي بسبب أيام المؤثرين: سناب ياخد الحصة الأكبر</td></tr></table></div>
<div class="col"><div class="card"><h4>الونرز بتوع الشتا (أكتوبر)</h4><table class="t sm"><tr><th></th><th>المنتج</th><th>قطع في أكتوبر</th><th>في العرض؟</th></tr>
<tr><td class="pi">{pic('Into The Glow')}</td><td>Into The Glow</td><td class="nm">330</td><td>لأ: بيبيع لوحده</td></tr>
<tr><td class="pi"><img class="th" src="img/hlms.jpg"></td><td>Marshmallow Set</td><td class="nm">132</td><td>لأ: بيبيع لوحده</td></tr>
<tr><td class="pi">{pic('واكس')}</td><td>واكس الشعر</td><td class="nm">144</td><td>جوه مجموعة الشعر</td></tr>
<tr><td class="pi">{pic('Body Glow')}</td><td>Body Glow</td><td class="nm">106</td><td>جوه سهرة تشوكلت</td></tr>
<tr><td class="pi">{pic('Hair Set')}</td><td>Hair Set</td><td class="nm">82</td><td><span class="ix g">239</span></td></tr></table></div>
<div class="callout"><b>السوق:</b> المنافسين داخلين بخصومات كبيرة: Hearts معلنة Black Friday، وClara مخصّمة على كل حاجة، وCarrot Sun وBeesline بنص السعر. لو دخلنا حرب سعر هنخسر، فنكسب بالمجموعة والقيمة والتغليف.</div></div></div>''')

# ---------- 03 positioning ----------
S('03', 'POSITIONING', 'موقعنا: ليه مانكسرش السعر', '''<div class="cols3"><div class="card"><h4>إحنا مين في السوق</h4><p>a'mie أغلى من البراندات السعودية والماركت بليس بـ 2–5 مرات، وفي مستوى العالمية أو أعلى. العميلة بتشتري البراند والتجربة والتغليف اللي يصلح هدية.</p></div>
<div class="card warn"><h4>الخطر لو خصمنا على كله</h4><ul><li>متوسط الطلب ينزل أكتر (حصل في سبتمبر).</li><li>العميلة تتعود ماتشتريش من غير كود.</li><li>بعد الحملة المبيعات تقع لحد الكود الجاي.</li></ul></div>
<div class="card good"><h4>اللي هنعمله</h4><ul><li>«Glow Friday»: مناسبتنا إحنا، مش «بلاك فرايدي» زي الكل.</li><li>مجموعات بسعر ثابت، قيمتها واضحة.</li><li>كلام هادي وواثق: «اكتشفي مجموعاتنا لفترة محدودة».</li><li>المنتجات اللي بتبيع لوحدها تفضل بسعرها.</li></ul></div></div>
<div class="callout">الرسالة الأساسية: <b>«لمعتك كاملة، بسعر أخف»</b>، وجنبها جمل الإعلانات المعتمدة: «لمعة جسمك في دقايق» و«شعر مرتب لساعات» و«روتين شعرك في شنطة وحدة».</div>''')

# ---------- 04 offer ----------
offer = [('Hair Set', 'hairset.jpg', 'مجموعة الشعر', 'واكس + Sleek Secret + فرشاة + شنطة', '282', '239', 'بطل الحملة', 'بيتباع طول السنة، وتاني أعلى بحث على جوجل. Clara أقوى منافس هنا (189 بعد الخصم).'),
         ('Chocolate', 'hlcs.jpg', 'مجموعة سهرة تشوكلت (جديدة)', 'Body Glow + ستيك تشوكلت + الفرشاة', '275*', '219', 'للسهرات', 'بتحرّك مجموعة تشوكلت الضعيفة عن طريق Body Glow. مارشميلو برا.'),
         ('Lemongrass', 'lemset.png', 'مجموعة الليمون قراس', 'سكراب + زبدة', '238', '199', 'سعر الدخول', '«سكراب» أعلى كلمة بحث عندنا (74 ألف في الشهر). واللافندر بنفس السعر لو المخزون يسمح.'),
         ('Trio', 'flora.jpg', 'ثلاثي العطور (جديدة)', 'فلورا + ناتورا + مسك a\'mie', '357*', '285', 'للهدايا', '«هدايا» 60 ألف و«مسك» 50 ألف بحث في الشهر. 3 قطع في طلب واحد، بشحن مرة واحدة.')]
oc = ''.join(f'''<div class="rz"><div class="rzi"><img src="img/{im}"></div><span class="role" style="background:#F2E4DF;color:#5E2E21">{tag}</span><h4>{name}</h4><p class="sub">{items}</p>
<div class="big2"><div><b>{was.rstrip('*')}</b><span>{'سعرها دلوقتي' if not was.endswith('*') else 'قيمة القطع منفصلة'}</span></div><div><b class="to">{now}</b><span>Glow Friday</span></div></div><p class="note">{why}</p></div>''' for _, im, name, items, was, now, tag, why in offer)
S('04', 'THE OFFER', 'العرض: 4 مجموعات بسعر ثابت', f'''<div class="cols4 rzs">{oc}</div>
<p class="note">القواعد: مافيش كود يتجمع مع العرض · Into The Glow ومارشميلو بسعرهم · الأسعار ترجع يوم 2 ديسمبر · «قيمة القطع منفصلة» للمجموعات الجديدة بدل السعر المشطوب (قواعد وزارة التجارة).</p>''')

# ---------- 05 targets ----------
S('05', 'TARGETS', 'الأهداف بالأرقام', '''<div class="cols2"><div class="card"><h4>الهدف لأسبوع العرض (25 نوفمبر – 1 ديسمبر)</h4><table class="t"><tr><th>المؤشر</th><th>الأساس (أسبوع عادي في أكتوبر)</th><th>الهدف</th></tr>
<tr><td>صافي المبيعات</td><td class="nm">~54,000</td><td class="nm"><b>~100,000</b></td></tr>
<tr><td>متوسط قيمة الطلب</td><td class="nm">285</td><td class="nm"><b>320+</b></td></tr>
<tr><td>الطلبات</td><td class="nm">~225</td><td class="nm"><b>~350</b></td></tr>
<tr><td>طلبات بكوبون</td><td class="nm">71%</td><td class="nm"><b>أقل من 35%</b></td></tr>
<tr><td>التسويق ÷ المبيعات</td><td class="nm">26%</td><td class="nm"><b>20% بحد أقصى</b></td></tr>
<tr><td>ROAS حسب GA4 (كل القنوات)</td><td class="nm">2.2</td><td class="nm"><b>3+</b></td></tr></table>
<p class="note">تقديرات مبنية على أكتوبر. مبيعات نوفمبر اللي فات (البرومبت 34) هتظبطها.</p></div>
<div class="card"><h4>القطع المستهدفة من كل مجموعة</h4><table class="t"><tr><th>المجموعة</th><th>قطع</th><th>المبيعات (شامل الضريبة)</th></tr>
<tr><td>مجموعة الشعر · 239</td><td class="nm">120</td><td class="nm">28,680</td></tr>
<tr><td>سهرة تشوكلت · 219</td><td class="nm">100</td><td class="nm">21,900</td></tr>
<tr><td>الليمون قراس · 199</td><td class="nm">100</td><td class="nm">19,900</td></tr>
<tr><td>ثلاثي العطور · 285</td><td class="nm">80</td><td class="nm">22,800</td></tr>
<tr class="tt"><td>الإجمالي</td><td class="nm">400</td><td class="nm">93,280</td></tr></table>
<p class="note">والباقي من المنتجات اللي بسعرها الكامل (Into The Glow، مارشميلو، الواكس) اللي بتتضاف للسلة.</p></div></div>''')

# ---------- 06 media ----------
S('06', 'AUDIENCES & MEDIA', 'الجمهور والقنوات والميزانية', '''<div class="cols3"><div class="card"><h4>الجمهور بالترتيب</h4><ol><li><b>العميلات القدام:</b> رسالة واتساب يوم 24 فيها رابط المجموعات قبل الإعلانات.</li><li><b>اللي زاروا الموقع أو سابوا السلة</b> (آخر 60 يوم): سناب وميتا.</li><li><b>اللي بيدوروا على جوجل:</b> «سكراب» و«هدايا» و«مسك» و«واكس للشعر» و«لمعة جسم».</li><li><b>جمهور جديد:</b> تيك توك وسناب بمحتوى UGC وفيديوهات الحركة.</li></ol></div>
<div class="chart"><h4>الميزانية: 12–15 ألف ريال للأسبوعين</h4>
<div class="hb"><span>سناب</span><div class="ht"><i style="width:40%;background:#5E2E21"></i></div><span class="hv">35–40%</span><span class="hn">وصول + إعادة استهداف</span></div>
<div class="hb"><span>جوجل</span><div class="ht"><i style="width:30%;background:#5E2E21"></i></div><span class="hv">30%</span><span class="hn">بحث وPMax</span></div>
<div class="hb"><span>ميتا</span><div class="ht"><i style="width:15%;background:#6B595C"></i></div><span class="hv">15%</span><span class="hn">ريلز + كتالوج</span></div>
<div class="hb"><span>تيك توك</span><div class="ht"><i style="width:15%;background:#6B595C"></i></div><span class="hv">15%</span><span class="hn">UGC</span></div>
<p class="note">حسب المرحلة: 20٪ تشويق (18–23) · 70٪ أسبوع العرض · 10٪ آخر فرصة (30 نوفمبر – 1 ديسمبر).</p></div>
<div class="card"><h4>المؤثرين</h4><ul><li>2–3 بس، ومحتواهم لمعة وهدايا وشعر.</li><li>من غير كود خصم (العرض مايتجمعش مع الأكواد). كل واحدة ليها رابط UTM.</li><li>نختار من اللي جابوا مبيعات قبل كده (زي NAJLA وLULU)، ونقيس تكلفة كل تعاون باللي جابه.</li></ul></div></div>''')

# ---------- 07 timeline ----------
S('07', 'TIMELINE', 'الجدول الزمني', '''<div class="cal six"><div><b>لحد 17 نوفمبر · تجهيز</b><span>المخزون (تشوكلت، المعطرات، المسك) · منتجات المجموعات الجديدة على زد (بعد الموافقة) · صفحة الحملة · الكريتيفز.</span><small>الفريق + المتجر</small></div>
<div><b>18 – 23 نوفمبر · تشويق</b><span>«Glow Friday قرّبت». فيديوهات من غير سعر، وقايمة انتظار، ونجمع جمهور لإعادة الاستهداف. 20٪ من الميزانية.</span><small>الإعلانات</small></div>
<div><b>24 نوفمبر · دخول مبكر</b><span>المجموعات تتنشر، ورسالة واتساب للعميلات القدام بالرابط. مافيش إعلانات لسه.</span><small>المتجر + الواتساب</small></div>
<div><b>25 – 29 نوفمبر · العرض</b><span>كل القنوات شغالة. كل يوم نراجع الأرقام وننقل الصرف للي بيجيب. 70٪ من الميزانية.</span><small>الإعلانات</small></div>
<div><b>30 نوفمبر – 1 ديسمبر · آخر فرصة</b><span>«آخر يوم». إعادة استهداف للي زاروا ومااشتروش، ورسالة آخر فرصة. 10٪ من الميزانية.</span><small>الإعلانات + الواتساب</small></div>
<div><b>2 – 8 ديسمبر · بعد الحملة</b><span>الأسعار ترجع. رسالة شكر من غير خصم، ونقترح المنتجات اللي بسعرها (Into The Glow، مارشميلو). نراجع النتايج.</span><small>الفريق</small></div></div>''')

# ---------- 08 measurement ----------
S('08', 'MEASUREMENT', 'القياس وقواعد القرار اليومي', '''<div class="cols2"><div class="card"><h4>نتابع كل يوم الساعة 10 الصبح</h4><table class="t"><tr><th>المؤشر</th><th>المصدر</th><th>لو أقل من كده</th></tr>
<tr><td>صافي المبيعات اليومي</td><td>زد</td><td>أقل من 12 ألف يومين ورا بعض: نزوّد إعادة الاستهداف</td></tr>
<tr><td>متوسط قيمة الطلب</td><td>زد</td><td>أقل من 300: نبرز المجموعات أكتر في الصفحة الرئيسية</td></tr>
<tr><td>قطع كل مجموعة</td><td>زد</td><td>مجموعة أقل من نص هدفها: نغير الكريتيف بتاعها</td></tr>
<tr><td>ROAS لكل منصة</td><td>GA4</td><td>أقل من 1 يومين: نقلل صرفها 50٪</td></tr>
<tr><td>طلبات بكوبون</td><td>زد</td><td>أكتر من 35٪: نشوف الأكواد المفتوحة ونقفلها</td></tr></table></div>
<div class="col"><div class="card"><h4>قواعد ثابتة</h4><ul><li>نقيس بـ GA4 مش بأرقام المنصة، وكل رابط عليه UTM.</li><li>مافيش قناة تعدي 50٪ من الميزانية.</li><li>ماحدش يمدّ العرض بعد 1 ديسمبر.</li></ul></div>
<div class="callout"><b>بعد الحملة بأسبوعين:</b> هل المبيعات رجعت لمستواها العادي ولا وقعت؟ ده المقياس الحقيقي إن الحملة ماعلّمتش العميلة تستنى الخصم.</div></div></div>''')

# ---------- 09 risks ----------
S('09', 'RISKS & CHECKLIST', 'المخاطر وقبل الإطلاق', '''<div class="cols2"><div class="card warn"><h4>المخاطر</h4><table class="t sm"><tr><th>الخطر</th><th>نعمل إيه</th></tr>
<tr><td>سهرة تشوكلت (219) تاكل من Into The Glow (294) لإن فيها نفس القطع تقريباً</td><td>قرار: نعرض Into The Glow نفسها بـ 219 بدل مجموعة جديدة، أو نخلي الفرق واضح في الكريتيف</td></tr>
<tr><td>المخزون يخلص في نص العرض</td><td>نعدّ المخزون قبل 17 نوفمبر، ونحدد كمية لكل مجموعة</td></tr>
<tr><td>السعر المرجعي</td><td>«قيمة القطع منفصلة» للمجموعات الجديدة بدل السعر المشطوب</td></tr>
<tr><td>الشحن يتأخر من الضغط</td><td>نأكد مع Isnaad على عدد الطلبات المتوقع</td></tr>
<tr><td>المبيعات تقع بعد الحملة</td><td>مافيش تمديد، ورسالة شكر من غير خصم</td></tr></table></div>
<div class="card"><h4>قبل الإطلاق (لازم كلها ✓)</h4><ul class="check"><li>أسامي المجموعات الجديدة متوافق عليها</li><li>المنتجات الجديدة على زد (بعد الموافقة) وصفحة الحملة</li><li>المخزون متعدّ</li><li>الأكواد القديمة مقفولة (Y10، Sh10، HS15)</li><li>الكريتيفز والنصوص متوافق عليها</li><li>UTM على كل الروابط</li></ul></div></div>''')

pages.append('''<section class="page cover end"><img class="cimg" src="a/cover_full.jpg"><div class="ctitle"><div class="cen">THANK YOU</div><div class="cline"></div><p>«الجمال لا يُصنع... بل يُعتنى به حتى يتجلّى»</p><img src="a/logo_dark.png" class="lgend"></div>
<div class="cfoot"><span>amie-sa.com</span><span>a'mie · Glow Friday Strategy</span></div></section>''')

css += '<style>.check li{list-style:none}.check li::before{content:"☐ ";color:#5E2E21}.rz .sub{font-size:11.5px;color:#6B595C}.rz .role{align-self:flex-start}</style>'
html = f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>a\'mie · Glow Friday Strategy</title>{css}</head><body>{"".join(pages)}</body></html>'
open(OUT, 'w', encoding='utf-8').write(html)
print('slides', len(pages))
