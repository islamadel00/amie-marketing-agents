"""Minimal Markdown -> RTL HTML page (headings, tables, lists, quotes, bold, code). Usage: md2html_ar.py in.md out.html title"""
import re,html,sys
md=open(sys.argv[1],encoding='utf-8').read(); title=sys.argv[3] if len(sys.argv)>3 else 'تقرير'
def inline(s):
  s=html.escape(s); s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s); s=re.sub(r'`(.+?)`',r'<code>\1</code>',s); return s
out=[];tbl=[];inlist=[None]
def flush():
  if tbl:
    rows=[r for r in tbl if not re.match(r'^\|[\s\-|]+\|$',r)]; h='<div class="wrap"><table>'
    for i,r in enumerate(rows):
      cells=[c.strip() for c in r.strip('|').split('|')]; t='th' if i==0 else 'td'
      h+='<tr>'+''.join(f'<{t}>{inline(c)}</{t}>' for c in cells)+'</tr>'
    out.append(h+'</table></div>'); tbl.clear()
def endlist():
  if inlist[0]: out.append(f'</{inlist[0]}>'); inlist[0]=None
for line in md.split('\n'):
  if line.startswith('|'): endlist(); tbl.append(line); continue
  flush()
  m=re.match(r'^(#{1,3}) (.*)',line)
  if m: endlist(); n=len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>')
  elif line.startswith('> '): endlist(); out.append(f'<div class="warn">{inline(line[2:])}</div>')
  elif re.match(r'^\d+\. ',line):
    if inlist[0]!='ol': endlist(); out.append('<ol>'); inlist[0]='ol'
    out.append(f'<li>{inline(re.sub(r"^\d+\. ","",line))}</li>')
  elif line.startswith('- '):
    if inlist[0]!='ul': endlist(); out.append('<ul>'); inlist[0]='ul'
    out.append(f'<li>{inline(line[2:])}</li>')
  elif line.strip()=='---': endlist(); out.append('<hr>')
  elif line.strip(): endlist(); out.append(f'<p>{inline(line)}</p>')
flush(); endlist()
css=""":root{--bg:#f7f5f2;--card:#fff;--ink:#1a1a1a;--mute:#6e6e6e;--line:#e6e2dc;--warn:#fff4e5;--warnb:#e0a040}
@media (prefers-color-scheme:dark){:root{--bg:#151515;--card:#1f1f1f;--ink:#eee;--mute:#aaa;--line:#333;--warn:#3a2c14;--warnb:#c08a30}}
body{margin:0;background:var(--bg);color:var(--ink);font-family:system-ui,"Segoe UI",Tahoma,sans-serif;padding:16px;max-width:980px;margin:auto;line-height:1.7}
h1{font-size:22px}h2{font-size:17px;margin-top:26px}h3{font-size:15px;margin-top:20px}.warn{background:var(--warn);border-right:4px solid var(--warnb);padding:10px 12px;border-radius:8px;margin:12px 0}
.wrap{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:10px;margin:10px 0}table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:right;vertical-align:top}th{color:var(--mute);font-weight:600}hr{border:0;border-top:1px solid var(--line);margin:22px 0}code{font-size:12px}"""
open(sys.argv[2],'w',encoding='utf-8').write(f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{css}</style></head><body>{"".join(out)}</body></html>')
