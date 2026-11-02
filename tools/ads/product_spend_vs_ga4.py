"""Ad spend per product (Snap+Meta+TikTok+Google) vs GA4 item revenue, 20 Jul - 30 Oct 2026.
Usage: python3 tools/ads/product_spend_vs_ga4.py research/ads-by-product
July spend is prorated 12/31 because GA4 data starts 20 Jul. USD x3.75 -> SAR."""
import csv,sys,collections
R=sys.argv[1]; f=lambda x:float(str(x).replace('%','').replace(',','') or 0)
rd=lambda p:list(csv.DictReader(open(R+'/'+p,encoding='utf-8-sig')))
W={'2026-07':12/31,'2026-08':1,'2026-09':1,'2026-10':1}; FX=3.75
clean=lambda p:(p or '').replace('(غير مؤكد)','').strip() or 'غير معروف'
idn={}
for r in rd('meta/meta-catalog-by-product-AMI_96.csv'):
  n=clean(r['Zid product name'])
  if not n.startswith('غير معروف'): idn[r['Product ID'].strip()]=n
for r in rd('google/google-product-map.csv'):
  z=clean(r['zid_product'])
  if r['product_title'].startswith('توزيعات') or 'كيس' in z: z=r['product_title'].strip()
  idn.setdefault(r['item_id'].strip(),z)
idn.update({'afeb1392-f7f3-4a22-8dd7-828b841fe460':'Summer Set','a3bccdee-4b74-4ef9-bc32-9918950728f2':"a'mie Fluid-Shaped Luxury Mirror",'d1aeadb7-b224-4dab-8bd8-db1acaeae741':'Lip Plump Balm 10ml'})
S=collections.defaultdict(float)
smap={r['ad_id']:clean(r['product']) for r in rd('snap/snap-ad-product-map.csv')}
for r in rd('snap/snap-ads-Amie-Self-Service-monthly.csv'): S[smap.get(r['Ad ID'],'غير معروف')]+=f(r['Spend'])*W.get(r['Month'],0)*FX
mmap={r['ad_id']:clean(r['product']) for r in rd('meta/meta-ad-product-map.csv')}
cat_ids={'6809724209279','6913438158479'}; catw=0
for r in rd('meta/meta-ads-AMI_96-monthly.csv'):
  s=f(r['Amount spent (USD)'])*W.get(r['Month'],0)*FX
  if r['Ad ID'] in cat_ids: catw+=s
  else: S[mmap.get(r['Ad ID'],'غير معروف')]+=s
cb=rd('meta/meta-catalog-by-product-AMI_96.csv'); cbt=sum(f(r['Amount spent']) for r in cb)
for r in cb:
  n=clean(r['Zid product name']); n='غير معروف' if n.startswith('غير معروف') else n
  if n=='مرآة ايمى': n="a'mie Fluid-Shaped Luxury Mirror"
  S[n]+=f(r['Amount spent'])/cbt*catw
for r in rd('tiktok/tiktok-ads-Ami-TikTok-Ads-monthly.csv'):
  p=clean(r['Product']); p={'Sleek Secret Hair Mascara':'Sleek Secret Hair Mascara 15ml'}.get(p,p)
  S[p]+=f(r['Cost (SAR)'])*W.get(r['Month'],0)
for r in rd('google/google-spend-by-product.csv'): S[r['product']]+=f(r['cost_sar'])
S['غير معروف']+=S.pop('غير مؤكد',0)
paidG={'Paid Social','Cross-network','Paid Shopping','Paid Search','Paid Other'}
V=collections.defaultdict(lambda:[0.0,0.0,0.0]); miss=collections.defaultdict(float)
for r in rd('ga4/ga4-items-by-channel.csv'):
  iid=r['item_id'].strip().split('|')[0]; n=idn.get(iid)
  if not n: miss[r['item_name']]+=f(r['item_revenue_usd']); n=r['item_name'].strip()
  rev=f(r['item_revenue_usd'])*FX; a=V[n]; a[1]+=rev; a[2]+=f(r['items_purchased'])
  if r['session_primary_channel_group'] in paidG: a[0]+=rev
rows=[]
for p in set(S)|set(V):
  s=S.get(p,0); pv,tv,u=V[p] if p in V else (0,0,0)
  rows.append([p,round(s),round(pv),round(tv),round(u),round(pv/s,2) if s>300 else '',round(s/tv*100,1) if tv else ''])
rows.sort(key=lambda r:-r[1])
with open(R+'/product-spend-vs-ga4-2026-07-20_2026-10-30.csv','w',newline='',encoding='utf-8-sig') as o:
  w=csv.writer(o); w.writerow(['product','ad_spend_sar','ga4_paid_item_revenue_sar','ga4_all_item_revenue_sar','ga4_units','ga4_paid_roas','ad_spend_pct_of_all_item_revenue']); w.writerows(rows)
for r in rows[:26]: print(f"{r[0][:38]:38} {r[1]:7} {r[2]:8} {r[3]:8} {r[4]:5} {str(r[5]):>6} {str(r[6]):>5}")
print('spend',sum(r[1] for r in rows),'paid rev',sum(r[2] for r in rows),'all',sum(r[3] for r in rows),'unmapped $',round(sum(miss.values())),list(miss)[:6])
