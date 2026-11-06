"""Product cost model for 1 May - 30 Sep 2026 (October removed), same method as v2.
Usage: python3 -I cost_model_may_sep.py <orders_dir> <repo_root> [check]
  check: also rebuild ad spend for May-Oct and compare with the v2 per-product file.
Sales: stripped Zid order dumps (no PII). Ads: monthly per-ad exports + ad->product maps (USD x3.75).
Influencers: v2 allocation minus deals dated in October (NAJLA 5 Oct, Ghadi Albarqi 27 Oct)."""
import csv, json, glob, sys, collections
S, ROOT = sys.argv[1], sys.argv[2]
R = ROOT + '/research/ads-by-product'
FXR = 3.75
f = lambda x: float(str(x).replace('%', '').replace(',', '') or 0)
rd = lambda p: list(csv.DictReader(open(R + '/' + p, encoding='utf-8-sig')))
norm = lambda s: (s or '').replace('’', "'").replace('‘', "'").strip()
clean = lambda p: norm((p or '').replace('(غير مؤكد)', '')) or 'غير معروف'
MONTHS = ['2026-05', '2026-06', '2026-07', '2026-08', '2026-09']
UN = {'كتالوج/عام', 'جوجل PMax غير منسوب لمنتج', 'غير معروف', 'براند (جوجل)', 'غير مؤكد'}

# ---------- ad spend per product ----------
def ad_spend(months):
    W = {m: 1 for m in months}; A = collections.defaultdict(float)
    smap = {r['ad_id']: clean(r['product']) for r in rd('snap/snap-ad-product-map.csv')}
    for r in rd('snap/snap-ads-Amie-Self-Service-monthly.csv'):
        A[smap.get(r['Ad ID'], 'غير معروف')] += f(r['Spend']) * W.get(r['Month'], 0) * FXR
    mmap = {r['ad_id']: clean(r['product']) for r in rd('meta/meta-ad-product-map.csv')}
    cat_ids = {'6809724209279', '6913438158479'}; catw = 0
    for r in rd('meta/meta-ads-AMI_96-monthly.csv'):
        s = f(r['Amount spent (USD)']) * W.get(r['Month'], 0) * FXR
        if r['Ad ID'] in cat_ids: catw += s
        else: A[mmap.get(r['Ad ID'], 'غير معروف')] += s
    cb = rd('meta/meta-catalog-by-product-AMI_96.csv'); cbt = sum(f(r['Amount spent']) for r in cb)
    for r in cb:   # catalog spend has no monthly split per product: spread the period's catalog spend by all-time shares
        n = clean(r['Zid product name']); n = 'غير معروف' if n.startswith('غير معروف') else n
        if n == 'مرآة ايمى': n = "a'mie Fluid-Shaped Luxury Mirror"
        A[n] += f(r['Amount spent']) / cbt * catw
    for r in rd('tiktok/tiktok-ads-Ami-TikTok-Ads-monthly.csv'):
        p = clean(r['Product']); p = {'Sleek Secret Hair Mascara': 'Sleek Secret Hair Mascara 15ml'}.get(p, p)
        A[p] += f(r['Cost (SAR)']) * W.get(r['Month'], 0)
    # Google: PMax item spend per month; the rest of each month's Google spend (search, brand) is unattributed
    gmap = {}
    for r in rd('google/google-product-map.csv'):
        z = clean(r['zid_product'])
        if not r['product_title'].startswith('توزيعات') and 'كيس' not in z and not z.startswith('غير معروف'): gmap[r['item_id'].strip()] = z
    gitem = 0
    for r in rd('google/google-products-monthly.csv'):
        if r['month'] not in W: continue
        c = f(r['cost_sar']); gitem += c
        A[gmap.get(r['item_id'].strip(), 'جوجل PMax غير منسوب لمنتج')] += c
    gall = sum(f(r['cost_sar']) for r in rd('google/google-campaigns-monthly.csv') if r['month'] in W)
    A['جوجل PMax غير منسوب لمنتج'] += gall - gitem
    A['غير معروف'] += A.pop('غير مؤكد', 0)
    return A

if len(sys.argv) > 3 and sys.argv[3] == 'check':
    full = ad_spend(MONTHS + ['2026-10'])
    v2 = {norm(r['product']): f(r['total_sar']) for r in rd('ads-spend-by-product-all-platforms-SAR.csv')}
    print('check May-Oct: rebuilt', round(sum(full.values())), 'v2', round(sum(v2.values())))
    for p in sorted(set(full) | set(v2), key=lambda p: -v2.get(p, 0))[:20]:
        print(f'  {p[:45]:45} {round(full.get(p, 0)):7} {round(v2.get(p, 0)):7}')

ads = ad_spend(MONTHS)

# ---------- Zid sales per product, 1 May - 30 Sep ----------
FX = {'SAR': 1, 'QAR': 1.03, 'AED': 1.021, 'KWD': 12.2, 'USD': 3.75, 'EGP': 0.077, 'EUR': 4.05, 'BHD': 9.95, 'GBP': 4.75, 'MAD': 0.38,
      'CAD': 2.7, 'IQD': 0.00286, 'OMR': 9.74, 'TRY': 0.1}
od = {}
for fn in glob.glob(S + '/orders_*.json'):
    for o in json.load(open(fn)): od[o['id']] = o
win = lambda o: '2026-05-01' <= o['created_at'][:10] <= '2026-09-30'
valid = lambda o: o.get('status') != 'cancelled' and float(o.get('order_total') or 0) > 0
orders = [o for o in od.values() if win(o) and valid(o)]
cm = json.load(open(ROOT + '/research/brand-study-2026-h2/data/cost_allocation_by_product.json'))
known = {r['product'] for r in cm['rows']}; disc = {r['product']: r['discount_pct'] / 100 for r in cm['rows']}
names = collections.defaultdict(collections.Counter)
for o in orders:
    for p in o['products']: names[p['pid']][p['name'].strip()] += 1
def base(n):
    b = n.split(' - ')[0].strip(); return b if b in known else n
canon_c = {}
def canon(pid):
    if pid in canon_c: return canon_c[pid]
    c = collections.Counter()
    for n, k in names[pid].items(): c[base(n)] += k
    r = next((n for n, _ in c.most_common() if n in known), c.most_common(1)[0][0]); canon_c[pid] = r; return r
P = collections.defaultdict(lambda: {'orders': set(), 'units': 0.0, 'gross': 0.0})
mon = collections.defaultdict(lambda: [0, 0.0])
for o in orders:
    fx = FX.get(o.get('currency', 'SAR'), 1); m = mon[o['created_at'][:7]]; m[0] += 1; m[1] += float(o['order_total']) * fx
    for p in o['products']:
        a = P[norm(canon(p['pid']))]; a['orders'].add(o['id']); a['units'] += p['qty']; a['gross'] += p['total'] * fx
net = {n: a['gross'] * (1 - disc.get(n, 0.054)) / 1.15 for n, a in P.items()}
tot_net = sum(net.values())

# ---------- influencers: v2 allocation minus October deals ----------
v2m = {norm(r['product']): r for r in rd('product-marketing-cost-2026-05-01_2026-10-30.csv')}
inf = {p: f(r['influencer_sar']) for p, r in v2m.items()}
inf["a'mie Into The Glow Collection"] -= 9500          # Ghadi Albarqi, 27 Oct
# NAJLA (posted 5 Oct, 30,000 ex VAT) was spread over the products sold with her code: take the same share back out
co = json.load(open(S + '/coupon_orders.json'))
nj = collections.defaultdict(float)
for i in co.get('6641301', []):
    o = od.get(i)
    if not o or not valid(o) or not ('2026-05-01' <= o['created_at'][:10] <= '2026-10-30'): continue
    for p in o['products']: nj[norm(canon(p['pid']))] += p['total'] * FX.get(o.get('currency', 'SAR'), 1)
njt = sum(nj.values())
for p, v in nj.items(): inf[p] = max(0, inf.get(p, 0) - 30000 * v / njt)

# ---------- product table ----------
pool = 0; direct = collections.defaultdict(float)
for p, t in ads.items():
    if p in UN: pool += t; continue
    parts = [norm(x) for x in p.split(' + ')]
    for x in parts: direct[x] += t / len(parts)
rows = []
for p in set(net) | set(direct) | {k for k, v in inf.items() if v > 0.5}:
    n = net.get(p, 0); d = direct.get(p, 0); al = pool * n / tot_net; i = inf.get(p, 0); m = d + al + i
    a = P.get(p)
    if n == 0 and m < 0.5: continue
    u = round(a['units']) if a else 0
    rows.append([p, len(a['orders']) if a else 0, u, round(n), round(d), round(al), round(i), round(m), round(m / n, 3) if n else None, round(m / u, 1) if u else None])
rows.sort(key=lambda r: -r[3])

# ---------- coupons, 1 May - 30 Sep ----------
cl = {c['id']: c for c in json.load(open(S + '/coupons_list_p1.json'))}
C = []
for cid, ids in co.items():
    oo = [od[i] for i in ids if i in od and win(od[i]) and valid(od[i])]
    if not oo: continue
    c = cl.get(cid, {}); sales = sum(float(o['order_total']) * FX.get(o.get('currency', 'SAR'), 1) for o in oo)
    C.append([cid, c.get('code', ''), c.get('name', ''), len(oo), round(sales), c.get('discount', ''), c.get('date_start', ''), c.get('date_end', '')])
C.sort(key=lambda r: -r[4])

# ---------- platforms vs GA4, 20 Jul - 30 Sep (July prorated 12/31; GA4 starts 20 Jul) ----------
G = {'2026-07': 12 / 31, '2026-08': 1, '2026-09': 1}
plat = {k: [0.0, 0.0, 0.0] for k in ('Snap', 'Meta', 'TikTok', 'Google')}
for r in rd('snap/snap-ads-Amie-Self-Service-monthly.csv'):
    w = G.get(r['Month'], 0); a = plat['Snap']; a[0] += f(r['Spend']) * w * FXR; a[1] += f(r['Purchases']) * w; a[2] += f(r['Purchase Value']) * w * FXR
for r in rd('meta/meta-ads-AMI_96-monthly.csv'):
    w = G.get(r['Month'], 0); a = plat['Meta']; a[0] += f(r['Amount spent (USD)']) * w * FXR; a[1] += f(r['Purchases']) * w; a[2] += f(r['Purchases conversion value']) * w * FXR
for r in rd('tiktok/tiktok-ads-Ami-TikTok-Ads-monthly.csv'):
    w = G.get(r['Month'], 0); a = plat['TikTok']; a[0] += f(r['Cost (SAR)']) * w; a[1] += f(r['Purchases']) * w; a[2] += f(r['Purchase value (SAR)']) * w
for r in rd('google/google-campaigns-monthly.csv'):
    w = G.get(r['month'], 0); a = plat['Google']; a[0] += f(r['cost_sar']) * w; a[1] += f(r['conversions']) * w; a[2] += f(r['conv_value_sar']) * w
def ga4_platform(src):   # paid source/medium only (same split as v2: organic, social and influencer links excluded)
    s, _, m = src.lower().partition(' / ')
    if m not in ('paid', 'cpc'): return None
    return {'snapchat': 'Snap', 'tiktok': 'TikTok', 'meta': 'Meta', 'ig': 'Meta', 'facebook': 'Meta', 'google': 'Google'}.get(s)
g4 = {k: [0.0, 0.0, 0.0] for k in plat}
for r in rd('ga4/ga4-campaigns-monthly.csv'):
    if r['month'] not in G: continue   # GA4 monthly already starts 20 Jul
    k = ga4_platform(r['session_source_medium'])
    if k: a = g4[k]; a[0] += f(r['sessions']); a[1] += f(r['ecommerce_purchases']); a[2] += f(r['purchase_revenue_usd']) * FXR

out = {'rows': rows, 'coupons': C, 'months': {k: [v[0], round(v[1])] for k, v in sorted(mon.items())}, 'orders': len(orders),
       'platforms': {k: [round(plat[k][0]), round(plat[k][1]), round(plat[k][2]), round(g4[k][0]), round(g4[k][1]), round(g4[k][2])] for k in plat},
       'pool': round(pool), 'inf_total': round(sum(r[6] for r in rows))}
json.dump(out, open(sys.argv[4] if len(sys.argv) > 4 else '/dev/stdout', 'w'), ensure_ascii=False)
