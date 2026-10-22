"""Build a'mie product descriptions in the standard template (same look as the lip balm / Into The Glow pages)."""
AR = '١٢٣٤٥٦٧٨٩'
DIV = '<p style="text-align: center; color: #aeb8c2; font-size: 10px; margin: {m};">✦ ✦ ✦</p>'
CARD = '''<div style="display: flex; background: #F5F6F7; border: 1px solid rgba(29, 29, 28, 0.08); border-radius: 16px; padding: 22px; margin-top: {mt};">
<div style="margin: 0 0 0 16px;">
<p style="font-size: 20px; color: #7d8d9d; line-height: 1; padding: 12px 16px; border: 1px solid rgba(125, 141, 157, 0.5); border-radius: 50%; margin: 0;">{n}</p>
</div>
<div>
<h4 style="font-size: clamp(16px, 4.3vw, 19px); color: #1b1b1c; margin: 2px 0 3px;">{t}</h4>
<p style="margin: 7px 0 0; color: #2b2b2b; font-size: clamp(12px, 3.3vw, 13.5px); line-height: 1.95;">{b}</p>
</div>
</div>'''
ING = '''<div style="background: #F5F6F7; border: 1px solid rgba(29, 29, 28, 0.08); border-radius: 16px; padding: 22px; margin-top: {mt};">
<h4 style="font-size: clamp(16px, 4.3vw, 19px); color: #1b1b1c; margin: 2px 0 3px;">{t}{en}</h4>
<p style="margin: 7px 0 0; color: #2b2b2b; font-size: clamp(12px, 3.3vw, 13.5px); line-height: 1.95;">{b}</p>
</div>'''
EN = ' <span style="color: #7d8d9d; font-size: clamp(12px, 3.3vw, 13.5px); font-weight: normal;">({})</span>'
H3 = '<h3 style="font-size: clamp(19px, 5vw, 24px); color: #1b1b1c; margin: 0 0 10px;">{}</h3>'

def cards(items):
    return '\n'.join(CARD.format(mt='26px' if i == 0 else '14px', n=AR[i], t=t, b=b) for i, (t, b) in enumerate(items))

def section(title, body, intro=None):
    i = f'\n<p style="color: #2b2b2b; margin: 0; font-size: clamp(12.5px, 3.4vw, 14px);">{intro}</p>' if intro else ''
    return f'<div style="padding: 32px 20px;">\n{H3.format(title)}{i}\n{body}\n</div>'

def build(title, sub, intro, sections, steps, video=None):
    """sections: list of (kind, title, items, intro) where kind is 'cards', 'ingredients' or 'text' (intro is the paragraph); empty en skips the English name."""
    out = ['<div style="text-align: right; max-width: 720px; margin: 0 auto; background: #ffffff; color: #1b1b1c;">',
           '<div style="text-align: center; padding: 48px 20px 32px; background: #f8f9fa; border-radius: 20px;">',
           f'<h2 style="font-size: clamp(21px, 5.4vw, 32px); line-height: 1.25; color: #1b1b1c; margin: 0;">{title}</h2>',
           f'<p style="font-size: clamp(13px, 3.6vw, 15px); color: #7d8d9d; margin: 11px 0 0;"><strong>{sub}</strong></p>',
           f'<p style="max-width: 580px; margin: 20px auto 0; color: #2b2b2b; font-size: clamp(12.5px, 3.4vw, 14px); line-height: 2.05;">{intro}</p>',
           '</div>']
    if video:
        out.append(f'<div style="padding: 24px 20px 0;">{video}</div>')
    first = True
    for kind, stitle, items, sintro in sections:
        out.append(DIV.format(m='24px 0 0' if first else '0'))
        first = False
        if kind == 'text':
            out.append(section(stitle, f'<p style="color: #2b2b2b; margin: 0; font-size: clamp(12.5px, 3.4vw, 14px); line-height: 1.95;">{sintro}</p>'))
            continue
        body = cards(items) if kind == 'cards' else '\n'.join(
            ING.format(mt='26px' if i == 0 else '14px', t=t, en=EN.format(en) if en else '', b=b) for i, (t, en, b) in enumerate(items))
        out.append(section(stitle, body, sintro))
    out.append(DIV.format(m='0'))
    st = '\n'.join(f'<p style="padding: 14px 0; margin: 0; color: #2b2b2b; font-size: clamp(12px, 3.3vw, 13.5px); line-height: 1.85;"><strong style="color: #7d8d9d; font-size: 16px;">{AR[i]} </strong> {s}</p>' for i, s in enumerate(steps))
    out.append(f'<div style="padding: 32px 20px;">\n<h3 style="font-size: clamp(18px, 4.6vw, 23px); color: #1b1b1c; margin: 0 0 12px;">طريقة الاستخدام</h3>\n{st}\n</div>')
    out.append('''<div style="padding: 0 20px 48px;">
<div style="background: #F5F6F7; border: 1px solid rgba(29, 29, 28, 0.07); border-radius: 20px; padding: 36px 24px; text-align: center;">
<h3 style="font-size: clamp(19px, 5vw, 24px); color: #1b1b1c; margin: 0 0 18px;">لماذا a'mie؟</h3>
<p style="font-size: clamp(12px, 3.3vw, 13.5px); color: #2b2b2b; margin: 0 0 8px;"><span style="color: #7d8d9d; font-size: 9px;">◆</span> منتجات مسجّلة لدى هيئة الغذاء والدواء.</p>
<p style="font-size: clamp(12px, 3.3vw, 13.5px); color: #2b2b2b; margin: 0 0 8px;"><span style="color: #7d8d9d; font-size: 9px;">◆</span> تركيبات مستوحاة من الطبيعة.</p>
<p style="font-size: clamp(12px, 3.3vw, 13.5px); color: #2b2b2b; margin: 0 0 8px;"><span style="color: #7d8d9d; font-size: 9px;">◆</span> خالية من التجارب على الحيوانات.</p>
<p style="font-size: clamp(12px, 3.3vw, 13.5px); color: #2b2b2b; margin: 0;"><span style="color: #7d8d9d; font-size: 9px;">◆</span> عبوات صديقة للبيئة.</p>
<p style="font-size: clamp(15px, 4.2vw, 18px); line-height: 1.7; color: #1b1b1c; max-width: 500px; margin: 24px auto 0;"><strong>لأننا نؤمن أن الجمال لا يُصنع، بل يُعتنى به حتى يتجلّى.</strong></p>
</div>
</div>
</div>''')
    return '\n'.join(out) + '\n'
