"""Per product: units, avg realised unit price (SAR incl VAT, pre-coupon), share of units sold in coupon orders, monthly units.
Usage: python3 -I price_sensitivity.py <orders_dir> <repo_root>"""
import json,glob,sys,collections,csv,statistics,datetime as dt
S,ROOT=sys.argv[1],sys.argv[2]
FX={'SAR':1,'QAR':1.03,'AED':1.021,'KWD':12.2,'USD':3.75,'EGP':0.077,'EUR':4.05,'BHD':9.95,'GBP':4.75,'MAD':0.38,'CAD':2.7,'IQD':0.00286,'OMR':9.74,'TRY':0.1}
od={}
for f in glob.glob(S+'/orders_*.json'):
  for o in json.load(open(f)): od[o['id']]=o
for o in json.load(open(S+'/late_2026-10-24_30.json')):
  o=dict(o); o['created_at']=(dt.datetime.fromisoformat(o['created_at'])+dt.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S'); od.setdefault(o['id'],o)
orders=[o for o in od.values() if '2026-05-01'<=o['created_at'][:10]<='2026-10-30' and o.get('status')!='cancelled' and float(o.get('order_total') or 0)>0]
co=json.load(open(S+'/coupon_orders.json')); coupon_ids={i for v in co.values() for i in v}
cm=json.load(open(ROOT+'/research/brand-study-2026-h2/data/cost_allocation_by_product.json')); known={r['product'] for r in cm['rows']}
norm=lambda n:n.replace('’',"'").strip()
def base(n):
  b=norm(n.split(' - ')[0]); return b if b in {norm(k) for k in known} else norm(n)
P=collections.defaultdict(lambda:{'u':0,'uc':0,'prices':[],'m':collections.Counter(),'sa':0})
for o in orders:
  fx=FX.get(o.get('currency','SAR'),1); c=o['id'] in coupon_ids
  for p in o['products']:
    a=P[base(p['name'])]; a['u']+=p['qty']; a['uc']+=p['qty'] if c else 0; a['prices'].append(p['price']*fx); a['m'][o['created_at'][:7]]+=p['qty']
    if o.get('currency','SAR')=='SAR': a['sa']+=p['qty']
rows=[]
for n,a in P.items():
  if a['u']<20: continue
  pr=a['prices']; rows.append([n,int(a['u']),round(statistics.median(pr),1),round(min(pr),1),round(max(pr),1),round(a['uc']/a['u']*100,1),round(a['sa']/a['u']*100,1)]+[int(a['m'][m]) for m in ['2026-05','2026-06','2026-07','2026-08','2026-09','2026-10']])
rows.sort(key=lambda r:-r[1])
import os; os.makedirs(ROOT+'/research/market-2026-11',exist_ok=True)
with open(ROOT+'/research/market-2026-11/03-own-price-and-coupon-dependence.csv','w',newline='',encoding='utf-8-sig') as f:
  w=csv.writer(f); w.writerow(['product','units','median_unit_price_sar','min_price','max_price','pct_units_in_coupon_orders','pct_units_saudi_sar_orders','may','jun','jul','aug','sep','oct']); w.writerows(rows)
print('orders',len(orders),'coupon orders in window',sum(o['id'] in coupon_ids for o in orders))
for r in rows[:25]: print(r)
