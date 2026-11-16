"""Convert a simple Arabic Markdown file (headings, bullets, tables, bold) to a right-to-left Word file.
Usage: python3 md_to_docx_ar.py in.md out.docx"""
import sys, re
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SRC, OUT = sys.argv[1], sys.argv[2]
FONT = 'Arial'
BROWN = RGBColor(0x5E, 0x2E, 0x21)

def rtl_par(p):
    pPr = p._p.get_or_add_pPr()
    bidi = OxmlElement('w:bidi'); bidi.set(qn('w:val'), '1'); pPr.append(bidi)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT  # with bidi on, "left" renders as right

def add_runs(p, text, size=11, bold=False, color=None):
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if not part: continue
        r = p.add_run(part)
        r.bold = bold or i % 2 == 1
        r.font.size = Pt(size); r.font.name = FONT
        if color: r.font.color.rgb = color
        rPr = r._r.get_or_add_rPr()
        rf = rPr.find(qn('w:rFonts'))
        if rf is None: rf = OxmlElement('w:rFonts'); rPr.append(rf)
        rf.set(qn('w:cs'), FONT); rf.set(qn('w:ascii'), FONT); rf.set(qn('w:hAnsi'), FONT)
        rtl = OxmlElement('w:rtl'); rtl.set(qn('w:val'), '1'); rPr.append(rtl)
        szcs = OxmlElement('w:szCs'); szcs.set(qn('w:val'), str(size * 2)); rPr.append(szcs)
        if r.bold:
            bcs = OxmlElement('w:bCs'); rPr.append(bcs)

def shade(cell, hexcol):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcol)
    tcPr.append(shd)

doc = Document()
sec = doc.sections[0]
sp = sec._sectPr; b = OxmlElement('w:bidi'); sp.append(b)
lines = open(SRC, encoding='utf-8').read().split('\n')
i = 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c) for c in cells): rows.append(cells)
            i += 1
        t = doc.add_table(rows=len(rows), cols=len(rows[0])); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = t._tbl.tblPr; bv = OxmlElement('w:bidiVisual'); tblPr.append(bv)
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                c = t.cell(ri, ci); p = c.paragraphs[0]; rtl_par(p)
                add_runs(p, val, size=10, bold=(ri == 0), color=BROWN if ri == 0 else None)
                if ri == 0: shade(c, 'F2E4DF')
        doc.add_paragraph()
        continue
    if ln.startswith('# '):
        p = doc.add_paragraph(); rtl_par(p); add_runs(p, ln[2:], size=18, bold=True, color=BROWN)
    elif ln.startswith('## '):
        p = doc.add_paragraph(); rtl_par(p); p.paragraph_format.space_before = Pt(14); add_runs(p, ln[3:], size=14, bold=True, color=BROWN)
    elif ln.startswith('- '):
        p = doc.add_paragraph(style='List Bullet'); rtl_par(p); add_runs(p, ln[2:])
    elif ln.strip():
        p = doc.add_paragraph(); rtl_par(p); add_runs(p, ln)
    i += 1
doc.save(OUT)
print('saved', OUT)
