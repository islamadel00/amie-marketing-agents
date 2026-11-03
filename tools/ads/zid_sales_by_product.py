"""Zid sales per product + coupon sales, 1 May - 30 Oct 2026, from stripped order dumps (no PII).
Usage: python3 -I zid_sales_by_product.py <orders_dir> <repo_root>"""
import json,glob,sys,collections,csv,datetime as dt
S,ROOT=sys.argv[1],sys.argv[2]
FX={'SAR':1,'QAR':1.03,'AED':1.021,'KWD':12.2,'USD':3.75,'EGP':0.077,'EUR':4.05,'BHD':9.95,'GBP':4.75,'MAD':0.38,'CAD':2.7,'IQD':0.00286,'OMR':9.74,'TRY':0.1}
od={}
for f in glob.glob(S+'/orders_*.json'):
  for o in json.load(open(f)): od[o['id']]=o
for o in json.load(open(S+'/late_2026-10-24_30.json')):   # list API times are UTC -> Riyadh
  o=dict(o); o['created_at']=(dt.datetime.fromisoformat(o['created_at'])+dt.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'); od.setdefault(o['id'],o)
win=lambda o:'2026-05-01'<=o['created_at'][:10]<='2026-10-30'
valid=lambda o:o.get('status')!='cancelled' and float(o.get('order_total') or 0)>0
orders=[o for o in od.values() if win(o) and valid(o)]
# canonical name per pid
cm=json.load(open(ROOT+'/research/brand-study-2026-h2/data/cost_allocation_by_product.json'))
known={r['product'] for r in cm['rows']}; disc={r['product']:r['discount_pct']/100 for r in cm['rows']}
names=collections.defaultdict(collections.Counter)
for o in orders:
  for p in o['products']: names[p['pid']][p['name'].strip()]+=1
def base(n):
  b=n.split(' - ')[0].strip()
  return b if b in known else n
def canon(pid):
  c=collections.Counter()
  for n,k in names[pid].items(): c[base(n)]+=k
  names[pid]=c
  for n,_ in c.most_common():
    if n in known: return n
  return c.most_common(1)[0][0]
P=collections.defaultdict(lambda:{'orders':set(),'units':0.0,'gross':0.0})
mon=collections.defaultdict(float)
for o in orders:
  fx=FX.get(o.get('currency','SAR'),1)
  mon[o['created_at'][:7]]+=float(o['order_total'])*fx
  for p in o['products']:
    n=canon(p['pid']); a=P[n]; a['orders'].add(o['id']); a['units']+=p['qty']; a['gross']+=p['total']*fx
rows=[]
for n,a in P.items():
  d=disc.get(n,0.054); net=a['gross']*(1-d)/1.15
  rows.append([n,len(a['orders']),round(a['units']),round(a['gross'],2),round(d*100,1),round(net,2)])
rows.sort(key=lambda r:-r[5])
out=ROOT+'/research/ads-by-product/zid'; import os; os.makedirs(out,exist_ok=True)
with open(out+'/zid-sales-by-product-2026-05-01_2026-10-30.csv','w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f); w.writerow(['product','orders','units','gross_incl_vat_sar','discount_pct_est','net_ex_vat_sar']); w.writerows(rows)
print('valid orders',len(orders),'order totals SAR',round(sum(mon.values())),'products net',round(sum(r[5] for r in rows)))
print({k:round(v) for k,v in sorted(mon.items())})
for r in rows[:12]: print(r)
# coupons
co=json.load(open(S+'/coupon_orders.json')); cl={c['id']:c for c in json.load(open(S+'/coupons_list_p1.json'))}
C=[]
for cid,ids in co.items():
  oo=[od[i] for i in ids if i in od and win(od[i]) and valid(od[i])]
  sales=sum(float(o['order_total'])*FX.get(o.get('currency','SAR'),1) for o in oo)
  c=cl.get(cid,{}); new=max(0,int(c.get('total_usage') or 0)-len(ids)) if c.get('date_end','')>='2026-10-25' else 0
  avg=sales/len(oo) if oo else 0
  C.append([cid,c.get('code',''),c.get('name',''),len(oo),round(sales),new,round(new*avg),round(sales+new*avg),c.get('discount',''),c.get('date_start',''),c.get('date_end','')])
C.sort(key=lambda r:-r[7])
with open(out+'/zid-coupon-sales-2026-05-01_2026-10-30.csv','w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f); w.writerow(['coupon_id','code','name','orders_to_oct24','sales_to_oct24_sar_incl_vat_ship','new_uses_oct25_30','est_sales_oct25_30','est_total_sales_sar','discount','start','end']); w.writerows(C)
for r in C: print(r)
