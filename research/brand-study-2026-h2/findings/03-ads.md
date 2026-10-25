# 03 · Paid media performance (1 May to 24 Oct 2026)

**Sources:** Supermetrics, read-only: Meta (A'MI 96), Google Ads (Ami), Snapchat (Amie Self Service), TikTok (A'mi0618 + Ami TikTok Ads). Zid order counts were read for a cross-check. **Currency:** Meta and Snapchat accounts are billed in **USD** and were converted at ×3.75. Google and TikTok are in **SAR**. Every figure below is in SAR. October covers only the 1st to the 24th. Revenue, purchases and ROAS are **as each platform reports them** (each platform's default attribution window), and the platforms double-count each other (see §6). CSVs are in `../data/ads_*.csv`.

## 1. Spend mix and blended totals

| Platform | Spend | Share | Platform purchases | Platform revenue | ROAS | CPA |
|---|---|---|---|---|---|---|
| Snapchat | 93,779 | 50% | 3,337 | 1,131,869 | 12.1 | 28 |
| Meta (IG only in practice) | 54,007 | 29% | 1,417 | 497,239 | 9.2 | 38 |
| TikTok | 25,614 | 14% | 836 | 280,099 | 10.9 | 31 |
| Google (from Aug) | 13,643 | 7% | 368 | 109,275 | 8.0 | 37 |
| **Total** | **187,042** | | **5,958** | **2,018,483** | **10.8** | **31** |

**Monthly, cross-platform** (spend / platform revenue):

| Month | Meta | Google | Snapchat | TikTok | Total spend | Σ platform purchases | Zid orders (all channels) | Spend per Zid order |
|---|---|---|---|---|---|---|---|---|
| May | 6,954 / 71,758 | – | 21,065 / 206,664 | 392 / 0 | 28,411 | 715 | 1,171 | 24.3 |
| Jun | 12,694 / 117,748 | – | 20,158 / 238,883 | 3,796 / 53,864 | 36,649 | 1,058 | 1,181 | 31.0 |
| Jul | 9,595 / 130,182 | – | 12,009 / 259,481 | 3,750 / 57,038 | 25,354 | 1,225 | 1,350 | **18.8** |
| Aug | 8,061 / 60,596 | 3,100 / 23,212 | 16,095 / 157,947 | 5,068 / 54,740 | 32,324 | 892 | 872 | 37.1 |
| Sep | 11,143 / 92,683 | 5,137 / 49,249 | 19,525 / 185,659 | 8,392 / 82,443 | **44,198** | 1,462 | 1,070 | **41.3** |
| Oct* | 5,560 / 24,273 | 5,405 / 36,815 | 4,926 / 83,235 | 4,216 / 32,015 | 20,107 | 606 | 797 | 25.2 |

July had the lowest spend after October and the most store orders. September had the highest spend (+74% vs July) and 21% fewer orders. Paid spend and store orders do not move together.

## 2. Efficiency trends by platform

| Platform | CTR | CPC | CPM | Trend |
|---|---|---|---|---|
| Meta | 0.7–1.8% (link) | 2.9 → 4.9 | 26 (Jun) → 58 (Sep) | CPC is up 72% from May to Sep. ROAS fell from 13.6 (Jul) to 4.4 (Oct), and October CPA (72) is nearly double the period average. **This platform is getting worse.** |
| Snapchat | 0.8% → 3.0% (swipe) | 2.9 → 0.5 | 22 → 10 | Swipes quadrupled in Aug–Sep (catalog ads), yet purchases stayed flat (482–666). The extra traffic is cheap and converts poorly. |
| TikTok | 1.5% → 0.9% | 0.6 → 1.8 | 10 → 17 | Spend grew more than 2× from Jun to Sep while ROAS fell from 15.2 to 9.8 and CPA rose from 26 to 38. A typical pattern as scale increases. |
| Google | 2.8% → 1.4% | 0.9 → 3.2 | 24 → 43 | PMax does the heavy lifting. CPC nearly quadrupled by October. |

Reach (monthly, deduplicated): Meta 32k–157k. TikTok 84k–159k (summed across 2 accounts). Snapchat: **MISSING** (the API refuses monthly reach).

## 3. Best and worst campaigns (whole period)

**Top by spend:** Meta *ACQ-Sales-Catalog* (26,888 · ROAS 10.7 · CPA 34), Snap *ACQ-Sales-Conversion* (26,522 · 12.7 · 27), Meta *ACQ-Sales-Conversion* (25,692 · 8.1 · 41), TikTok *ACQ-Con-Sales* (21,402 · 10.5 · 31), Snap *ACQ-Sales-Catalog* (19,701 · 11.3 · 25), Google *PMax* (10,083 · 8.8 · 35).

**Best efficiency at meaningful spend:** Snap *New Summer Colle 17/6* (ROAS 17.1, CPA 21), TikTok *Sales Plog 7/6* (17.1, CPA 22), Snap *Amr Scalling LLA* (13.6) and *Summer New Test Cap* (13.5).

**Worst:** Meta *Sales 2 Vids 20/4* (757 · ROAS 1.6 · CPA 252), Meta *Retention-Conversion-Sales* (548 · 2.4 · CPA 110), Meta *Testing* (122 · 0.9), TikTok *Sales Smart 13/5* (392 · 0 purchases; the pixel was not recording purchases in May), Google *Search-Brand* (195 · 0.7), Snap *New Data 27/4* and *Eid 20/5* (CPA 61–63). Google Shopping (3,365 · ROAS 6.1) trails PMax (8.8).

All campaigns are Sales/Conversion objectives. No awareness or consideration campaigns ran in the period.

## 4. Creatives

- **Meta:** one catalog carousel (DPA) took **50% of Meta spend** (26,888 · ROAS 10.7). The best video, *"2"* (7,651 · ROAS 11.3, 3-sec hook rate 18%), does as well as the carousel. *SingleVideo-07* has the best hook (41%) and the best CTR (1.8%) but only 6.6 ROAS. It earns attention without converting. The *"1"* and *"3"* videos (ROAS 2.5) are clear losers. No Meta ad names show a UGC or creator signal.
- **Snapchat:** static/catalog "Frame" and "Collection" ads lead on spend (CTR 4–4.5%, ROAS 11–12). The highest ROAS comes from *SingleImage-06-PDP* (7,152 · 18.9). The only sizeable UGC ad, *SingleVideo-UGC-02-PDP*, returned 12.6 ROAS at 2,607 spend. Snap video completion is tiny (1–18% of impressions get a view).
- **TikTok:** **every top-10 ad is creator, UGC or Spark content.** The leader is a creator's "it was sold out, now it's back" tan post (4,548 · ROAS 14.5 · 2-sec hook 36% · CTR 1.9%). Creator tan posts by Arwa (15.0) and shuroq (11.7) also do well, as does the summer26-code post (17.8). Hair-wax creator posts land at ROAS 9–10. A discount-code National Day hair post had a strong hook (32%) but weak ROAS (6.7). The best non-UGC ad is a before/after tan image (ROAS 16.3, CTR 5.9%).

## 5. Audience insights (Meta)

- **Women 25–44 take 81% of spend and 86% of purchases.** 25–34 F: ROAS 9.9, CPA 35. 35–44 F: ROAS 9.7, CPA 37.
- 45–54 F has a higher CTR but ROAS 6.5 and CPA 56. 18–24 F reaches cheaply (ROAS 8.9).
- Men took 3.1k SAR (6%) at ROAS 1.3–7.0. That is waste on a women's brand.
- **Placement:** 99.98% Instagram. Feed 52% of spend (ROAS 8.8), Stories 27% (CTR 2.8%, ROAS 9.1), Reels 20% (9.6). Explore is tiny but has the best ROAS (28.7). Facebook gets effectively zero.
- **Region:** Riyadh 56%, Makkah 27% and Eastern 13% take 96% of spend. Purchases by region are **MISSING** (Meta does not return them).

## 6. Google detail

PMax: 10,083 SAR, 290 conversions, ROAS 8.8. Shopping: 3,365 SAR, ROAS 6.1. Search-Brand: 195 SAR in August, then stopped. Only the "Purchase" action counts as a conversion (add-to-cart, checkout and page view are secondary), which is good. Among Shopping search terms, the converting ones are mostly **brand terms and misspellings** (amie, ايمي, a mi, ami تان, aime tan: 758 SAR → 26.6 conv → 8,107 SAR in the top-50 sample). Competitor terms (surge/سيرج, audela, jayla/جيلا, ladeena) take impressions and some spend (361 SAR → 5 conv). PMax search terms are **MISSING** (not exposed).

## 7. Tracking caveats

- **Over-attribution is certain.** The platforms claim 5,958 purchases, which is **92.5% of all 6,441 Zid orders** (organic, direct, referral and influencer-code orders included). In **August (892 vs 872) and September (1,462 vs 1,070), the platforms claim more purchases than the store took in total.**
- **GA4 comparison (Jul–Oct):** the social platforms (Meta+Snap+TikTok) claim 3,817 purchases. GA4 credits Paid Social with 528, so the platforms claim **6–11× more**. The platforms reported 96.6k clicks/swipes against 88.6k GA4 Paid Social sessions, so click volume roughly matches. Conversion is where they diverge: **platform click-to-purchase rate ~4.0% vs GA4 Paid Social session CVR 0.57%**. Google is closer: 368 platform conversions vs ~238 in GA4 Paid Shopping + Cross-network (PMax), about 1.5×.
- Snapchat's default window is 28-day swipe + **1-day view**. 40% of Snap purchases (1,320) are view-through, so its 12.1 ROAS is the least reliable. Meta and TikTok defaults also include view-through.
- GA4 only started tracking in July, so May–June cannot be cross-checked.
- Meta campaign-level `website_purchase_roas` returned inconsistent values (e.g. 56.7). ROAS here is recomputed as value ÷ spend.

## 8. Data gaps (MISSING)

Snapchat reach. Meta purchases by region. PMax search terms and asset-group creative. Meta and Snap thumb-stop rates beyond what the platforms expose (Snap gives video views only, TikTok uses 2-sec views as the hook). **Zid net revenue for the period, so blended MER/ROAS on real revenue is not computed.** Incrementality or holdout tests. Snap/TikTok audience breakdowns (not pulled). Two other Meta accounts (Ami Ads, A'MI Read-Only) returned no data for the period.

## What stands out

- **Snapchat takes half the budget on the weakest evidence.** 40% of its purchases are view-through, and its August–September swipe surge (CPC down to 0.58) brought traffic that GA4 shows converting at about 0.5%.
- **Spend went up while orders went down.** September's 44k SAR (the period peak) produced 1,070 orders. July's 25k produced 1,350. Paid cost per store order more than doubled (18.8 → 41.3).
- **Meta efficiency is decaying.** CPC rose 72% from May to September and ROAS fell to 4.4 in October (CPA 72). One catalog carousel carries half of Meta spend, and Facebook placements are effectively unused.
- **Creator content wins on TikTok.** Every top TikTok ad is a creator, UGC or Spark post, led by tan "back in stock" content (ROAS 14–18). Meta runs almost no UGC, which leaves an obvious test.
- **Platform ROAS (~10.8 blended) cannot be used for budget decisions.** The platforms claim more purchases than the store made in two months. A store-revenue MER and a geo or holdout test are needed before scaling.
