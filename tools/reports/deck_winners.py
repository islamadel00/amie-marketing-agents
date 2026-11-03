# Section 10 of the market deck: summer vs winter winners + potential winners.
# exec()'d from market_deck.py (uses its slide() helper).
# Units per month, Apr..Oct 2026 (Oct to the 30th), from Zid orders (cancelled excluded, variants merged).
SEAS = [('Summer Set', 'summer.jpg', [147, 362, 372, 365, 210, 152, 22]),
        ('Red Cherry', 'redcherry.jpg', [145, 423, 0, 308, 95, 46, 20]),
        ('Deep Tan', 'deeptan.jpg', [43, 128, 129, 163, 193, 42, 8]),
        ('Glittery Gold', 'glittery.jpg', [9, 43, 60, 122, 61, 22, 1]),
        ('واكس الشعر', 'wax.jpg', [139, 111, 152, 157, 156, 295, 144]),
        ('Hair Set', 'hairset.jpg', [81, 115, 119, 153, 96, 171, 82]),
        ('Into The Glow', 'itg.jpg', [0, 0, 0, 0, 0, 25, 330]),
        ('Marshmallow Set', 'hlms.jpg', [280, 101, 164, 80, 41, 66, 132]),
        ('Body Glow', 'bodyglow.jpg', [97, 105, 111, 92, 40, 60, 106]),
        ('Glow Set', 'glowset.jpg', [53, 87, 115, 94, 54, 63, 74]),
        ('Chocolate Set', 'hlcs.jpg', [188, 72, 169, 57, 36, 31, 33]),
        ('Lavender Set', 'lavset.png', [0, 0, 1, 0, 0, 0, 87]),
        ('Lip Plump', 'lip.jpg', [102, 82, 67, 23, 3, 0, 68]),
        ('كريم القدمين', 'foot.jpg', [56, 57, 88, 59, 37, 127, 66]),
        ("a'musk", 'musk.jpg', [74, 56, 102, 74, 53, 127, 64]),
        ('Natura', 'natura.jpg', [50, 51, 51, 87, 55, 97, 43]),
        ('Flora', 'flora.jpg', [34, 31, 52, 72, 50, 101, 28]),
        ('Sleek Secret', 'mascara.jpg', [45, 52, 73, 55, 22, 92, 46]),
        ('فرشاة سليك', 'sleek.jpg', [54, 33, 74, 47, 62, 116, 65]),
        ('Lemongrass Set', 'lemset.png', [46, 61, 54, 48, 27, 83, 34])]
MON = ['أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر']

def wcard(name, im, big, lab, note, tag=''):
    return (f'<div class="wc"><div class="wi"><img src="img/{im}">{tag}</div><div class="wt"><h5>{name}</h5>'
            f'<div class="wn"><b>{big}</b><span>{lab}</span></div><p>{note}</p></div></div>')

summer = ''.join([
    wcard('Summer Set', 'summer.jpg', '327', 'قطعة في الشهر (مايو–أغسطس)', '36٪ من مبيعات الفترة. في أكتوبر 22 بس.'),
    wcard('Red Cherry', 'redcherry.jpg', '207', 'قطعة في الشهر', 'أعلى شهر 423 في مايو. يونيو صفر (مخزون).'),
    wcard('Deep Tan', 'deeptan.jpg', '153', 'قطعة في الشهر', 'بيكبر لآخر الصيف: 193 في أغسطس.'),
    wcard('Glittery Gold', 'glittery.jpg', '72', 'قطعة في الشهر', 'ذروته يوليو (122)، وفي أكتوبر 1.')])
winter = ''.join([
    wcard('Into The Glow', 'itg.jpg', '330', 'قطعة في أكتوبر', 'نزلت آخر سبتمبر وبقت أكبر منتج في أكتوبر.', '<span class="nw">جديد</span>'),
    wcard('Marshmallow Set', 'hlms.jpg', '132', 'قطعة في أكتوبر', 'أعلى من متوسط الصيف (97)، و280 في أبريل (موسم مناسبات).'),
    wcard('Body Glow', 'bodyglow.jpg', '106', 'قطعة في أكتوبر', 'رجعت لمستوى الصيف بعد ما نزلت لـ 40 في أغسطس.'),
    wcard('Glow Set', 'glowset.jpg', '74', 'قطعة في أكتوبر', 'ثابتة تقريباً طول السنة (54–115).')])
allyear = ''.join([
    wcard('واكس الشعر', 'wax.jpg', '295', 'قطعة في سبتمبر', 'أعلى منتج في سبتمبر، و144 في أكتوبر.'),
    wcard('Hair Set', 'hairset.jpg', '171', 'قطعة في سبتمبر', '82–171 في الشهر من أبريل لأكتوبر.')])

slide('10', 'WINNERS · 1/3', 'الونرز: الصيف قصاد الشتا',
      '<div class="wcols">'
      '<div class="wcol sum"><div class="wh"><span class="role" style="background:#C9A86A;color:#191919">الصيف · مايو – أغسطس</span>'
      '<p>التان. بيشيل نص المبيعات، وبيقف تقريباً من أكتوبر.</p></div><div class="wgrid">' + summer + '</div></div>'
      '<div class="wcol win"><div class="wh"><span class="role" style="background:#5E2E21;color:#fff">الشتا · من أكتوبر</span>'
      '<p>اللمعة والهايلايتر: سهرات ومناسبات وهدايا.</p></div><div class="wgrid">' + winter + '</div></div></div>'
      '<div class="wall"><span class="role" style="background:#6B595C;color:#fff">طول السنة</span>' + allyear +
      '<p class="note">الشتا هنا مبني على أكتوبر وأبريل بس، لإن الطلبات اللي عندنا من أبريل لأكتوبر. '
      'سبتمبر عالي في كل المنتجات بسبب ND96 (خصم 20٪)، فمش مقياس للموسم.</p></div>')

def heat(items):
    h = '<table class="t sm heat"><tr><th></th><th>المنتج</th>' + ''.join(f'<th>{m}</th>' for m in MON) + '<th>الموسم</th></tr>'
    for n, im, u in items:
        mx = max(u) or 1
        summ = sum(u[1:5]) / 4
        r = u[6] / summ if summ else 9
        if n in ('Into The Glow', 'Lavender Set'): tag = '<span class="ix g">جديد</span>'
        elif n == 'Lip Plump': tag = '<span class="ix w">مخزون</span>'
        elif r < 0.4: tag = '<span class="ix b">صيف</span>'
        elif r > 1.15: tag = '<span class="ix g">شتا ↑</span>'
        else: tag = '<span class="ix w">طول السنة</span>'
        cells = ''.join(f'<td class="hc" style="background:rgba(94,46,33,{v/mx*0.85:.2f});color:{"#fff" if v/mx > 0.55 else "#191919"}">{v:g}</td>' for v in u)
        h += f'<tr><td class="pi"><img class="th" src="img/{im}"></td><td>{n}</td>{cells}<td>{tag}</td></tr>'
    return h + '</table>'

slide('10', 'WINNERS · 2/3', 'كل منتج بيتباع إمتى (قطع في الشهر)',
      '<div class="cols2"><div class="card">' + heat(SEAS[:10]) + '</div><div class="card">' + heat(SEAS[10:]) + '</div></div><div>' + '<p class="note">اللون الأغمق = أعلى شهر للمنتج نفسه. أكتوبر لحد يوم 30. '
      'Red Cherry في يونيو، وLip Plump في أغسطس وسبتمبر: الصفر من المخزون مش من الطلب. '
      'الموسم = أكتوبر مقارنة بمتوسط مايو–أغسطس.</p></div>')

cand = [('Lavender Set', 'lavset.png', '87 قطعة في أكتوبر (أول شهر)', [1, 1, 1, 0], 'ترطيب وروتين قبل النوم. نحطها في حملات الشتا والهدايا.'),
        ('Lip Plump', 'lip.jpg', '68–102 في الشهر لما بيبقى متوفر · تسويق 5.5٪', [1, 1, 1, 0], 'كان أعلى من 100 في أبريل، ووقف شهرين من المخزون. نأمّن المخزون قبل الشتا.'),
        ('كريم القدمين', 'foot.jpg', '127 في سبتمبر · تسويق 7.6٪', [1, 1, 1, 0], 'جفاف الشتا. حملة شتوية صغيرة، ومعاه مجموعة اليدين والقدمين اللي كانت بتتباع في ديسمبر اللي فات.'),
        ("a'musk", 'musk.jpg', '127 في سبتمبر · تسويق 13.8٪', [1, 1, 1, 0], 'هدية ورمضان. نربطه بالهدايا والتوزيعات، مش حملة لوحده.'),
        ('Sleek Secret + فرشاة سليك', 'mascara.jpg', '92 و116 في سبتمبر · تسويق 11–17٪', [1, 1, 0, 1], 'بيتباعوا مع الواكس. إضافة للسلة جنب الواكس وHair Set.'),
        ('Back to Routine', 'bts.jpg', '29 و26 في سبتمبر وأكتوبر', [0, 0, 1, 0], 'جديد. نستنى شهرين قبل ما نحكم عليه.')]
crit = ['بيتباع بتسويق قليل', 'بيكبر لما نزقه', 'مناسب للشتا', 'سعره قريب من المنافسين']
rows = ''
for n, im, ev, sc, act in cand:
    marks = ''.join(f'<td class="mk">{"●" if x else "○"}</td>' for x in sc)
    rows += f'<tr><td class="pi"><img class="th" src="img/{im}"></td><td><b>{n}</b><small class="d">{ev}</small></td>{marks}<td><small>{act}</small></td></tr>'
slide('10', 'WINNERS · 3/3', 'مين قابل يبقى ونر؟',
      '<p class="lede">الونر عندنا = منتج بيتباع كتير من غير ما نصرف عليه كتير، وبيكبر لما نزقه. '
      'دول المرشحين للشتا الجاي، من مبيعاتهم ونسبة التسويق منها.</p>'
      '<div class="card"><table class="t sm cand"><tr><th></th><th>المنتج</th>' + ''.join(f'<th>{c}</th>' for c in crit) +
      '<th>نعمل إيه</th></tr>' + rows + '</table></div>'
      '<div class="callout"><b>محتاجين نتأكد:</b> مبيعات نوفمبر 2025 – مارس 2026 (الشتا اللي فات) عشان نعرف الونرز الحقيقيين للشتا. '
      'ده في البرومبت 34، وبعده نحدّث القسم ده.</div>')
