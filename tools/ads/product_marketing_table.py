"""Per product: Zid net sales (1 May-30 Oct) + actual ad spend (Snap/Meta/TikTok/Google) + influencer cost.
Unattributed ad spend (catalog/general/PMax/brand/unknown) is spread by net-sales share; multi-product ads split equally."""
import csv,json,sys,collections
ROOT=sys.argv[1]; R=ROOT+'/research/ads-by-product'
f=lambda x:float(x or 0); norm=lambda s:s.replace('’',"'").replace('‘',"'").strip()
sales={norm(r['product']):r for r in csv.DictReader(open(R+'/zid/zid-sales-by-product-2026-05-01_2026-10-30.csv',encoding='utf-8-sig'))}
ads=collections.defaultdict(float); pool=0
UN={'كتالوج/عام','جوجل PMax غير منسوب لمنتج','غير معروف','براند (جوجل)','غير مؤكد'}
for r in csv.DictReader(open(R+'/ads-spend-by-product-all-platforms-SAR.csv',encoding='utf-8-sig')):
  t=f(r['total_sar']); p=norm(r['product'])
  if p in UN: pool+=t; continue
  parts=[norm(x) for x in p.split(' + ')]
  for x in parts: ads[x]+=t/len(parts)
alias={"a'mie Fluid-Shaped Luxury Mirror":"a'mie Fluid-Shaped Luxury Mirror","Sleek Secret Hair Mascara 15ml":"Sleek Secret Hair Mascara 15ml"}
cm=json.load(open(ROOT+'/research/brand-study-2026-h2/data/cost_allocation_by_product.json'))
inf={norm(r['product']):r['influencer_cost'] for r in cm['rows']}
inf["a'mie Into The Glow Collection"]=inf.get("a'mie Into The Glow Collection",0)+9500  # Ghadi Albarqi, 27 Oct (in period now)
tot_net=sum(f(r['net_ex_vat_sar']) for r in sales.values())
rows=[]; unmatched={}
for p in set(sales)|set(ads)|set(inf):
  s=sales.get(p); net=f(s['net_ex_vat_sar']) if s else 0
  if not s and ads.get(p,0)>0: unmatched[p]=ads[p]
  direct=ads.get(p,0); alloc=pool*net/tot_net; i=inf.get(p,0); m=direct+alloc+i
  if net==0 and m==0: continue
  rows.append([p,int(f(s['orders'])) if s else 0,int(f(s['units'])) if s else 0,round(net),round(direct),round(alloc),round(i),round(m),round(m/net*100,1) if net else '',round(m/f(s['units']),1) if s and f(s['units']) else ''])
rows.sort(key=lambda r:-r[3])
with open(R+'/product-marketing-cost-2026-05-01_2026-10-30.csv','w',newline='',encoding='utf-8-sig') as o:
  w=csv.writer(o); w.writerow(['product','orders','units','net_sales_ex_vat_sar','ads_direct_sar','ads_allocated_sar','influencer_sar','marketing_total_sar','marketing_pct_of_net','marketing_per_unit_sar']); w.writerows(rows)
T=[sum(r[i] for r in rows) for i in (3,4,5,6,7)]
print('net',T[0],'ads direct',T[1],'allocated',T[2],'(pool',round(pool),') influencer',T[3],'marketing',T[4],'pct',round(T[4]/T[0]*100,1))
print('ads not matched to a Zid product:',{k:round(v) for k,v in unmatched.items()})
for r in rows[:18]: print(r)
