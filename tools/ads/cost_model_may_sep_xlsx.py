"""Write the May-Sep cost model workbook from v2's layout and cost_model_may_sep.py output.
Usage: python3 -I cost_model_may_sep_xlsx.py <v2.xlsx> <data.json> <out.xlsx>"""
import json, sys
from copy import copy
import openpyxl
V2, DATA, OUT = sys.argv[1:4]
d = json.load(open(DATA, encoding='utf-8')); wb = openpyxl.load_workbook(V2)

def restyle(ws, src_row, dst_row, ncol):
    for c in range(1, ncol + 1):
        s, t = ws.cell(src_row, c), ws.cell(dst_row, c)
        t.font, t.fill, t.border, t.alignment, t.number_format = copy(s.font), copy(s.fill), copy(s.border), copy(s.alignment), s.number_format

# ---------- المنتجات ----------
ws = wb['المنتجات']
body = [copy(ws.cell(2, c)._style) for c in range(1, 15)]; tot = [copy(ws.cell(44, c)._style) for c in range(1, 15)]
ws.delete_rows(2, ws.max_row)
rows = d['rows']; n = len(rows); last = n + 1; T = n + 2
for i, r in enumerate(rows, start=2):
    vals = r + [None, f'=C{i}*K{i}', f'=D{i}-H{i}-L{i}', f'=IFERROR(M{i}/D{i},"")']
    for c, v in enumerate(vals, start=1):
        cell = ws.cell(i, c, v); cell._style = copy(body[c - 1])
ws.cell(T, 1, 'الإجمالي')
for c, col in enumerate('BCDEFGH', start=2): ws.cell(T, c, f'=SUM({col}2:{col}{last})')
ws.cell(T, 9, f'=H{T}/D{T}'); ws.cell(T, 12, f'=SUM(L2:L{last})'); ws.cell(T, 13, f'=SUM(M2:M{last})'); ws.cell(T, 14, f'=IFERROR(M{T}/D{T},"")')
for c in range(1, 15): ws.cell(T, c)._style = copy(tot[c - 1])

# ---------- حسبة البراند ----------
b = wb['حسبة البراند']
b['B2'] = '1 مايو – 30 سبتمبر 2026 (من غير أكتوبر)'
b['B3'] = d['orders']; b['C3'] = 'طلبات زد الصالحة (من غير الملغي)'
b['B4'] = f"='المنتجات'!D{T}"
b['B5'] = round(145660 / 6564 * d['orders']); b['C5'] = 'تقدير: متوسط الشحن لكل طلب من حسبة 25 أكتوبر × عدد الطلبات. عدّله لو الرقم الفعلي عندك'
b['B7'] = f"='المنتجات'!L{T}"
b['B13'] = f"='المنتجات'!E{T}+'المنتجات'!F{T}"; b['B14'] = f"='المنتجات'!G{T}"
b['A19'] = 'المصاريف الثابتة للفترة (5 شهور)'; b['B19'] = '=B18*5'

# ---------- الكوبونات ----------
c = wb['الكوبونات']
hs = [copy(c.cell(1, i)._style) for i in range(1, 12)]; bs = [copy(c.cell(2, i)._style) for i in range(1, 12)]
c.delete_rows(1, c.max_row)
head = ['ID', 'الكود', 'الاسم', 'طلبات (مايو – سبتمبر)', 'مبيعات (شامل ضريبة وشحن)', 'الخصم %', 'البداية', 'النهاية']
for i, h in enumerate(head, 1): c.cell(1, i, h)._style = copy(hs[i - 1])
for j, r in enumerate(d['coupons'], start=2):
    for i, v in enumerate(r, 1): c.cell(j, i, v)._style = copy(bs[i - 1] if i < 4 else bs[[0, 1, 2, 3, 4, 8, 9, 10][i - 1]])

# ---------- المنصات قصاد GA4 ----------
p = wb['المنصات قصاد GA4']
for j, k in enumerate(['Snap', 'Meta', 'TikTok', 'Google'], start=2):
    sp, pp, pv, gs, gp, gv = d['platforms'][k]
    vals = [k, sp, pp, pv, round(pv / sp, 2), gs, gp, gv, round(gv / sp, 2), round(pv / gv, 1) if gv else None]
    for i, v in enumerate(vals, 1): p.cell(j, i, v)
p.cell(7, 1, 'الفترة: 20 يوليو (أول يوم في داتا GA4) – 30 سبتمبر 2026. صرف يوليو محسوب 12/31 من الشهر.')

# ---------- drop item-level GA4 (no monthly split available) ----------
del wb['المنتج قصاد GA4']

# ---------- text sheets ----------
ins = wb['تعليمات المحاسب']
ins['A10'] = 'المصادر: مبيعات زد الفعلية (1 مايو – 30 سبتمبر 2026، من غير أكتوبر)، الصرف الفعلي على إعلانات سناب وميتا وتيك توك وجوجل في نفس الفترة، وتكلفة المؤثرين. تفاصيل الحساب في شيت «طريقة الحساب».'
m = wb['طريقة الحساب']
txt = ['طريقة الحساب',
       f"1. الفترة: 1 مايو – 30 سبتمبر 2026، وشهر أكتوبر متشال بالكامل. المبيعات من طلبات زد الفعلية ({d['orders']:,} طلب صالح، من غير الملغي)، والعملات التانية اتحولت لريال.",
       '2. صافي المبيعات = إجمالي سعر المنتجات × (1 − نسبة الخصم التقديرية للمنتج من حسبة 25 أكتوبر) ÷ 1.15.',
       '3. الإعلانات: الصرف الفعلي لكل إعلان من مايو لسبتمبر (سناب وميتا وتيك توك وجوجل)، متربط بالمنتج من رابط الإعلان أو صورته. ميتا وسناب بالدولار × 3.75. إعلانات الكتالوج في ميتا متوزعة على المنتجات بنفس نسب ملف الكتالوج.',
       f"4. الإعلانات اللي فيها أكتر من منتج: صرفها متقسم بالتساوي. الكتالوج والإعلانات العامة وجوجل غير المنسوب والإعلانات غير المعروفة ({d['pool']:,} ريال) متوزعة حسب نسبة مبيعات كل منتج.",
       '5. المؤثرين: من حسبة 25 أكتوبر، ومشال منها الاتفاقات اللي اتنشرت في أكتوبر: نجلاء (5 أكتوبر، 30,000 ريال من غير ضريبة، متشالة بنفس توزيعها على المنتجات) وغدي البارقي (27 أكتوبر، 9,500 ريال).',
       '6. الكوبونات: الطلبات والمبيعات من 1 مايو لـ 30 سبتمبر بس، من ربط الكوبون بالطلبات. كوبون LULU مسجّل عليه استخدامات أكتر من الطلبات المربوطة، فمبيعاته أقل من الحقيقة.',
       '7. GA4: من 20 يوليو (أول يوم فيه داتا) لـ 30 سبتمبر. شيت «المنتج قصاد GA4» اتشال لإن داتا المنتجات في GA4 مش متقسمة بالشهر، فمانقدرش نشيل منها أكتوبر.',
       '8. الخانة الصفرا (تكلفة القطعة) مدخل: أول ما تتملا، الربح والهامش بيتحسبوا أوتوماتيك.']
m.delete_rows(1, m.max_row)
for i, t in enumerate(txt, 1): m.cell(i, 1, t)
m['A1'].font = copy(ins['A1'].font)
wb.save(OUT); print('saved', OUT, 'products', n, 'total row', T)
