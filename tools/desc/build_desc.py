"""Build a'mie product-description HTML (template v2) from the copy .docx files.
The copy is used verbatim: only layout/markup is added. Run with: python3 -I build_desc.py <docx> <out_dir>"""
import sys, os, re, html, docx

C_TEXT = '#28272a'; C_BODY = '#4a4446'; C_MUTED = '#8a7a72'; C_ACC = '#5E2E21'; C_SOFT = '#EAE2D9'
AR_DIGITS = '٠١٢٣٤٥٦٧٨٩'

HEAD_AR = {'المكونات الأساسية وفوائدها', 'طريقة الاستخدام', 'المكونات', 'المكونات الرئيسية', 'مميزات الفرشاة', 'العناية بالفرشاة'}
HEAD_EN = {'key ingredients & benefits', 'key ingredients and benefits', 'how to use', 'ingredients', 'highlighted ingredients',
           'brush features', 'brush care'}


def esc(t):
    return html.escape(t, quote=False)


def is_heading(line, lang):
    t = line.strip().rstrip(':').strip()
    return (t in HEAD_AR) if lang == 'ar' else (t.lower() in HEAD_EN)


def split_langs(lines):
    """Arabic block first, English block second. English starts at the first line that is mostly Latin
    and is followed (within 2 lines) by the 'a’mie ...' name line."""
    for i, l in enumerate(lines):
        if i < 3:
            continue
        latin = sum(c.isascii() and c.isalpha() for c in l)
        arabic = sum('؀' <= c <= 'ۿ' for c in l)
        if latin > 3 and arabic == 0:
            return lines[:i], lines[i:]
    return lines, []


def parse(block, lang):
    """-> dict(title, name, tagline, intro[], sections[(heading, items[])], extras[])"""
    b = [l for l in block if l.strip()]
    notes = [l for l in b if l.startswith('Editorial note') or l.startswith('ملاحظة تحريرية') or (l.startswith('Note:') and 'INCI' in l)]
    b = [l for l in b if l not in notes]
    out = {'title': '', 'name': '', 'tagline': '', 'intro': [], 'sections': [], 'size': [], 'notes': notes}
    i = 0
    # title / name lines (EN may have "Hair Wax Stick" then "a’mie Hair Wax Stick", or start directly with "a’mie ...")
    if not b[0].lower().startswith('a’mie') and not b[0].lower().startswith("a'mie"):
        out['title'] = b[0]; i = 1
    if i < len(b) and (b[i].lower().startswith('a’mie') or b[i].lower().startswith("a'mie")):
        out['name'] = b[i]; i += 1
    out['tagline'] = b[i]; i += 1
    cur = None
    while i < len(b):
        l = b[i]
        if is_heading(l, lang):
            cur = (l.strip().rstrip(':').strip(), [])
            out['sections'].append(cur)
        elif cur is None:
            out['intro'].append(l)
        else:
            cur[1].append(l)
        i += 1
    # size lines live at the end of the last section ("الحجم: 30 مل", "75 مل", "Size: 30 ml", "Net Weight", "Set Includes", "محتويات المجموعة")
    size_re = re.compile(r'^(الحجم|Size|Net Weight|محتويات المجموعة|Set Includes)\s*:|^\d+\s*(مل|ml|mL|جم|g)$', re.I)
    for h, items in out['sections']:
        keep = []
        for it in items:
            (out['size'] if size_re.search(it.strip()) else keep).append(it)
        items[:] = keep
    # intro lines that look like "sub-product | size" headers (hand & foot set) become a section
    if any(' | ' in l for l in out['intro']):
        first = [l for l in out['intro']]
        intro, sub = [], []
        j = 0
        while j < len(first):
            if ' | ' in first[j]:
                sub.append((first[j], first[j + 1] if j + 1 < len(first) and ' | ' not in first[j + 1] else ''))
                j += 2 if sub[-1][1] else 1
            else:
                intro.append(first[j]); j += 1
        out['intro'] = intro
        out['subproducts'] = sub
    return out


def num(n, lang):
    s = str(n)
    return ''.join(AR_DIGITS[int(c)] for c in s) if lang == 'ar' else s


def card(n, title, body, lang):
    side = 'right' if lang == 'ar' else 'left'
    t = f'<h4 style="font-size:15.5px;color:{C_TEXT};margin:0;"><strong>{esc(title)}</strong></h4>' if title else ''
    bd = f'<p style="margin:{"6px" if title else "0"} 0 0;color:{C_BODY};font-size:13.5px;line-height:1.9;">{esc(body)}</p>' if body else ''
    return (f'<div style="background:#ffffff;border-radius:16px;padding:16px 18px;margin-top:10px;text-align:{side};">'
            f'{t}{bd}</div>')


def split_item(it):
    """'Name: desc' -> (name, desc); bullets '• x' -> ('', x)."""
    s = it.strip()
    if s.startswith('•'):
        return '', s.lstrip('•').strip()
    m = re.match(r'^([^:]{1,40}):\s*(.+)$', s)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return '', s


ACCORDION = True


def section(title, inner, lang):
    side = 'right' if lang == 'ar' else 'left'
    if ACCORDION:
        # <details>: closed by default; the customer taps the title to open it. Works without JS.
        push = 'margin-right:auto' if lang == 'ar' else 'margin-left:auto'
        return (f'<details class="amie-acc" style="padding:4px 0;text-align:{side};">'
                f'<summary style="display:flex;padding:16px 0;font-size:17px;color:{C_TEXT};">'
                f'<strong>{esc(title)}</strong><span class="amie-acc-sign" style="{push};font-size:20px;color:{C_ACC};line-height:1;">+</span></summary>'
                f'<div style="padding:0 0 18px;">{inner}</div></details>'
                f'<div style="height:1px;background:rgba(94,46,33,.35);margin:0;"></div>')
    return (f'<div style="padding:26px 0 2px;text-align:{side};">'
            f'<h3 style="font-size:19px;color:{C_TEXT};margin:0 0 4px;font-weight:700;">{esc(title)}</h3>{inner}</div>')


def render(d, lang):
    dirn = 'rtl' if lang == 'ar' else 'ltr'
    side = 'right' if lang == 'ar' else 'left'
    parts = []
    head = d['title'] or d['name']
    sub = d['name'] if d['title'] else ''
    parts.append(f'<div style="padding:6px 0 20px;text-align:{side};">')
    if sub:
        parts.append(f'<p style="margin:0 0 6px;color:{C_ACC};font-size:12px;"><strong>{esc(sub)}</strong></p>')
    parts.append(f'<h2 style="font-size:23px;line-height:1.35;color:{C_TEXT};margin:0;"><strong>{esc(head)}</strong></h2>')
    parts.append(f'<p style="font-size:15px;color:{C_TEXT};margin:8px 0 0;line-height:1.8;"><strong>{esc(d["tagline"])}</strong></p>')
    for p in d['intro']:
        parts.append(f'<p style="margin:10px 0 0;color:{C_BODY};font-size:13.5px;line-height:2;">{esc(p)}</p>')
    parts.append('</div>')
    parts.append('<div style="height:1px;background:rgba(94,46,33,.15);margin:0;"></div>')
    if d.get('subproducts'):
        inner = ''.join(card(i + 1, t, b, lang) for i, (t, b) in enumerate(d['subproducts']))
        parts.append(f'<div style="padding:16px 0 10px;">{inner}</div>')
    for h, items in d['sections']:
        low = h.lower()
        plain_ingredients = low in ('المكونات', 'المكونات الرئيسية', 'ingredients', 'highlighted ingredients')
        how = low in ('طريقة الاستخدام', 'how to use', 'العناية بالفرشاة', 'brush care')
        if plain_ingredients:
            inner = ''.join(f'<p style="margin:8px 0 0;color:{C_BODY};font-size:13.5px;line-height:1.9;">{esc(x)}</p>' for x in items)
            inner = f'<div style="background:#ffffff;border-radius:16px;padding:14px 18px;margin-top:10px;">{inner}</div>'
        elif how:
            rows = []
            for k, x in enumerate(items, 1):
                rows.append(f'<div style="padding:10px 0;">'
                            f'<p style="margin:0;color:{C_BODY};font-size:13.5px;line-height:1.9;">{esc(x)}</p></div>'
                            + (f'<div style="height:1px;background:rgba(94,46,33,.12);margin:0;"></div>' if k < len(items) else ''))
            inner = f'<div style="margin-top:6px;">{"".join(rows)}</div>'
        else:
            inner = ''.join(card(k, *split_item(x), lang) for k, x in enumerate(items, 1))
        parts.append(section(h, inner, lang))
    if d['size']:
        chips = ''.join(f'<span style="display:inline-block;background:{C_SOFT};color:{C_ACC};border-radius:999px;padding:6px 14px;margin:4px;font-size:13px;"><strong>{esc(s)}</strong></span>' for s in d['size'])
        parts.append(f'<div style="padding:22px 0 8px;text-align:{side};">{chips}</div>')
    return f'<div style="text-align:{side};direction:{dirn};max-width:720px;margin:0 auto;color:{C_TEXT};">' + ''.join(parts) + '</div>'


def main(src, out_dir):
    lines = [p.text.strip() for p in docx.Document(src).paragraphs if p.text.strip()]
    # document letterhead ('a’mie  |  PRODUCT CONTENT'), not product copy
    lines = [l for l in lines if 'PRODUCT CONTENT' not in l]
    ar, en = split_langs(lines)
    base = os.path.splitext(os.path.basename(src))[0]
    res = {}
    for lang, block in (('ar', ar), ('en', en)):
        if not block:
            continue
        d = parse(block, lang)
        open(os.path.join(out_dir, f'{base}.{lang}.html'), 'w').write(render(d, lang))
        res[lang] = d
    return res


if __name__ == '__main__':
    import json
    r = main(sys.argv[1], sys.argv[2])
    print(json.dumps({k: {'title': v['title'], 'name': v['name'], 'sections': [h for h, _ in v['sections']], 'size': v['size'], 'notes': v['notes'], 'sub': v.get('subproducts')} for k, v in r.items()}, ensure_ascii=False))
