"""New-year tag, page 2: re-flow the ORIGINAL outlined Arabic (Somar) into two lines + one line.
No font file is needed: the letter outlines are taken from the source PDF, moved and scaled uniformly.
Usage: python3 new_year_tag_relayout.py <source.pdf> <out.pdf>"""
import sys, pymupdf
SRC, OUT = sys.argv[1], sys.argv[2]
src = pymupdf.open(SRC); p = src[1]; PW = p.rect.width
dr = p.get_drawings()
INK = next(d['fill'] for d in dr if d['type'] == 's' or False) if False else None
text = [d for d in dr if d['type'] == 'f' and d['rect'].width < 150 and d['fill'] != (1.0, 1.0, 1.0)]   # 5 Arabic lines, top to bottom
assert len(text) == 5, len(text)
BASE = [54.0, 72.0, 90.0, 118.0, 136.0]      # baselines of the five original lines (pt)
SPACE = 3.4                                  # original word space (pt)
def contours(d):
    cs, cur, last = [], [], None
    for it in d['items']:
        a, b = it[1], it[-1]
        if last is not None and (abs(a.x-last.x) > 1e-3 or abs(a.y-last.y) > 1e-3): cs.append(cur); cur = []
        cur.append(it); last = b
    if cur: cs.append(cur)
    return cs
def xr(cs):
    xs = [q.x for c in cs for it in c for q in it[1:]]; return min(xs), max(xs)
L = [contours(d) for d in text]
def cx(c): a, b = xr([c]); return (a+b)/2
l2_right = [c for c in L[1] if cx(c) > 55.0]     # «صُمّمت هذه الهدية»
l2_left = [c for c in L[1] if cx(c) <= 55.0]     # «لتكون»
# each new line = pieces from right to left: (contours, original baseline)
NEW = [[(L[0], BASE[0]), (l2_right, BASE[1])],
       [(l2_left, BASE[1]), (L[2], BASE[2])],
       [(L[3], BASE[3]), (L[4], BASE[4])]]
def width(pieces): return sum(xr(c)[1]-xr(c)[0] for c, _ in pieces) + SPACE*(len(pieces)-1)
MAXW = 131.0
s = min(1.0, MAXW/max(width(pc) for pc in NEW))
RULE = 100.8
TARGET = [RULE - 10.8*s - 18.0*s, RULE - 10.8*s, RULE + 17.2*s]     # baselines of the new lines; the divider stays where it was
out = pymupdf.open(); out.insert_pdf(src, from_page=0, to_page=0)   # page 1 untouched
pg = out.new_page(width=PW, height=p.rect.height)
def redraw(d):
    sh = pg.new_shape()
    for it in d['items']:
        if it[0] == 'l': sh.draw_line(it[1], it[2])
        elif it[0] == 'c': sh.draw_bezier(it[1], it[2], it[3], it[4])
        elif it[0] == 're': sh.draw_rect(it[1])
        elif it[0] == 'qu': sh.draw_quad(it[1])
    if d['type'] == 's': sh.finish(color=d['color'], width=d['width'], closePath=False)
    else: sh.finish(fill=d['fill'], color=None, even_odd=d.get('even_odd', False), closePath=True, width=0)
    sh.commit()
for d in dr:
    if d not in text: redraw(d)                  # background, logo, divider: exactly as in the source
fill = text[0]['fill']
for pieces, ty in zip(NEW, TARGET):
    w = width(pieces)*s; right = PW/2 + w/2; sh = pg.new_shape()
    for cs, base in pieces:
        x0, x1 = xr(cs)
        T = lambda q: pymupdf.Point(right - (x1 - q.x)*s, ty + (q.y - base)*s)
        for c in cs:
            for it in c:
                if it[0] == 'l': sh.draw_line(T(it[1]), T(it[2]))
                else: sh.draw_bezier(T(it[1]), T(it[2]), T(it[3]), T(it[4]))
        right -= (x1 - x0)*s + SPACE*s
    sh.finish(fill=fill, color=None, even_odd=False, closePath=True, width=0); sh.commit()
out.insert_pdf(src, from_page=2, to_page=2)      # cut-line page untouched
out.save(OUT, garbage=3, deflate=True)
print('scale', round(s, 3), 'line widths', [round(width(pc)*s, 1) for pc in NEW], 'baselines', [round(t, 1) for t in TARGET])
