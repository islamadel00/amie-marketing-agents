# 02 — Web analytics (GA4, Search Console, Merchant Center)

**Period asked:** 2026-05-01 → 2026-10-24, monthly. **Pulled:** 2026-10-25 via Supermetrics, read-only.
**Data:** `data/web_*.csv`. Extends (does not repeat) `research/seo-audit-2026-10-22.md`.

> **GA4 coverage:** property "Ami" (471311593) has real data from **2026-07-20** (468 sessions, 14 purchases). May–June hold 18 stray sessions. GA4 figures cover **Jul 20 – Oct 24** (July = 12 days, October = 24). Revenue currency is unconfirmed.

---

## 1. Traffic & conversion trend (GA4)

| Month | Sessions | Users | New users | Engagement rate | Purchases | Revenue | Purchase CVR | Revenue/session | AOV |
|---|---|---|---|---|---|---|---|---|---|
| Jul (20–31) | 16,274 | 12,880 | 12,884 | 38.6% | 590 | 54,285 | **3.63%** | 3.34 | 92.0 |
| Aug | 52,980 | 41,016 | 39,571 | 26.2% | 713 | 63,537 | 1.35% | 1.20 | 89.1 |
| Sep | 65,082 | 50,060 | 49,330 | 29.4% | 930 | 69,748 | 1.43% | 1.07 | 75.0 |
| Oct (1–24) | 33,499 | 28,189 | 26,710 | 34.6% | 690 | 52,605 | 2.06% | 1.57 | 76.2 |

July→September: sessions rose 4×, purchases only 1.6×. Paid social drove the volume and CVR fell from 3.6% to 1.4%. In October, paid social halved and organic social tripled, and CVR recovered to 2.1%. AOV fell about 15 points in September and stayed down.

## 2. Channel quality (Jul 20 – Oct 24)

| Channel | Sessions | Share | Engagement | Purchases | CVR | Rev/session |
|---|---|---|---|---|---|---|
| Paid Social | 88,576 | 53% | 16.6% | 528 | **0.60%** | **0.48** |
| Direct | 34,367 | 20% | 35.6% | 789 | 2.30% | 1.88 |
| Organic Social | 17,945 | 11% | 43.1% | 366 | 2.04% | 1.59 |
| Referral | 8,660 | 5% | 73.4% | 581 | **6.71%** | **5.74** |
| Cross-network (PMax) | 7,238 | 4% | 49.5% | 189 | 2.61% | 2.10 |
| Organic Search | 7,118 | 4% | 59.2% | 358 | 5.03% | 4.27 |
| Paid Shopping | 993 | 0.6% | 59.9% | 48 | 4.83% | 3.28 |

**Source/medium findings** (`web_ga4_source_medium_top40.csv`):
- **Snapchat** is the largest source. CVR by medium: `paid` 0.31% (51,478 sessions), `cpc` 1.24%, `social` 2.42%, **`influencer` 3.24%** (103 purchases). Influencer traffic converts about 10× better than paid Snap.
- **TikTok:** `tiktok / paid` converts at 0.51% (14,801 sessions). `tiktok.com / referral` brought 2,883 sessions and **0 purchases** (probably untagged creator traffic).
- **Meta:** `meta / cpc` 1.35%, `ig / paid` 1.69%.
- **"Referral" is mostly owned traffic:** the bio-link card `amie-card.netlify.app` brought 6,050 sessions and 469 purchases (7.75% CVR).
- **Payment gateways show up as referrers** (`checkout.tabby.sa`, `noonpayments`, `sso.zid.store`). Each one breaks a session and steals credit for the purchase.
- AI Assistant: 95 sessions, 2 purchases.

**Device:** mobile is 97% of sessions and 99.4% of purchases (2.0% CVR). Desktop: 3,299 sessions, 18 purchases (0.55%). **Cities:** Riyadh 1.6% CVR. **Jeddah 2.3%** (as many purchases as Riyadh on 31% fewer sessions). Dammam 2.4%, Abha 3.2%. City `(not set)`: 21k sessions, 34 purchases.

## 3. Funnel leaks (event counts)

| Step | Jul | Aug | Sep | Oct | Total |
|---|---|---|---|---|---|
| view_item → add_to_cart | 27.5% | 12.7% | 13.7% | 20.6% | **16.1%** |
| add_to_cart → begin_checkout | 50.5% | 50.8% | 48.2% | 47.1% | 48.9% |
| begin_checkout → add_payment_info | 104.8% | 92.9% | 98.6% | 97.9% | 98.0% |
| add_payment_info → purchase | 28.9% | 25.9% | 24.1% | 24.2% | **25.4%** |
| view_item → purchase | 4.2% | 1.6% | 1.6% | 2.3% | 2.0% |

- **Biggest drop by volume: view → cart.** 84% of product views never add to cart, and it is worst in the paid-social months.
- **Most suspicious drop: payment → purchase.** 3 of 4 shoppers who enter payment info don't complete. Possible causes: payment failures, redirects losing the session, or `purchase` under-firing. `/checkout` and `/cart` as landing pages (2,593 sessions, 257 purchases) plus the gateway referrers point to session breaks. Reconcile with Zid orders (MISSING).
- `begin_checkout` ≈ `add_payment_info` (>100% in July). They probably fire together in Zid's checkout.
- **Mobile vs desktop:** view→cart 16.2% vs 11.6%; checkout→payment 98% vs **67%**; view→purchase 2.0% vs 0.8%. Desktop is too small to prioritise.

## 4. Product page performance (Jul–Oct, ≥1,000 item views)

| Product | Views | Cart rate | Purchase/view | Read |
|---|---|---|---|---|
| مجموعة الصيف (Summer Set) | 23,408 | **7.7%** | 1.6% | #1 revenue (52.4k) despite the low cart rate. Paid-traffic destination. Test price/bundle framing |
| مجموعة الليمون قراس | 9,301 | **6.6%** | 1.3% | Landing page brought 8,071 sessions and 9 purchases (12% engagement). Ad→page mismatch |
| مرآة ايمى (mirror) | 8,478 | **7.1%** | 1.0% | 6,915 landing sessions, 3 purchases. A traffic magnet that doesn't convert |
| شنطة ايمي بني / فرشاة الميك اب | 2.3–2.4k | 8–9% | ~2% | Low-intent accessories |
| مجموعة تشوكلت هايلايتر | 3,419 | 12.6% | 3.2% | Marshmallow set gets 36% on similar traffic |
| مسك ايمي | 5,795 | 17.4% | 3.4% | Also the #1 Shopping impression item |
| Benchmarks: كريم القدمين 62.6% · مارشميلو هايلايتر 46.7% · Flora/Natura mists 33% · ريد تشيري 25% (6.1% purchase/view, the best seller) |

**Tracking gap:** several items have views but **0 add-to-carts**: مجموعة لمعة الجسم من a'mie (8,026 views), مجموعة العودة للروتين (3,600), Into The Glow, gift box, favor packs and hand cream. Lip Plump has 4 adds. Yet the glow-set landing page brought 133 purchases, so bundles are probably sent to GA4 under their component names. **Per-product CVR for sets is unreliable.**

## 5. Search trends (Search Console)

| Month | Clicks | Impressions | CTR | Position | Branded clicks (CTR, pos) | Non-branded named clicks / impr | Anonymised clicks |
|---|---|---|---|---|---|---|---|
| May | 2,384 | 26,013 | 9.2% | 12.8 | 1,713 (15.0%, 5.0) | 14 / 4.4k | 618 |
| Jun | 2,910 | 44,823 | 6.5% | 10.8 | 2,026 (13.6%, 5.2) | 24 / 9.5k | 810 |
| Jul | 2,962 | 56,214 | 5.3% | 12.0 | 2,061 (14.1%, 6.0) | 46 / 18.2k | 809 |
| Aug | 1,843 | 66,783 | 2.8% | 11.3 | 1,176 (8.5%, 7.4) | 66 / 24.4k | 578 |
| Sep | 1,639 | 55,966 | 2.9% | 11.7 | 971 (7.6%, 9.5) | 50 / 17.4k | 599 |
| Oct (1–24) | **461** | 52,482 | **0.9%** | 11.7 | **178 (2.0%, 9.7)** | 31 / 15.8k | 248 |

- **Branded clicks fell off a cliff around 23 Sep.** Daily clicks were ~62 (Sep 10–22), then ~19 (Sep 23 – Oct 24), while impressions held at ~2,000/day. "ايمي" still ranks ~4–5, but its clicks fell from ~300/month to 35. The homepage went from 682 clicks (Sep) to 123 (Oct). GA4 Organic Search confirms it (2,330 → 655 sessions). Likely cause: a SERP or snippet change. **New since the 22 Oct audit; needs a manual SERP check.**
- Branded impressions are also falling (≈14.6k/month in Jul → ≈11k/month pace in Oct).
- Non-branded traffic is negligible: 231 named clicks in six months. Top terms: لمعة جسم (22 clicks, pos 5.8), تان (20 clicks / 14.5k impressions, pos 7.6).
- The brand regex misses some variants (aime, a’mi, a.mi, اىمي, آمي, اماي, emie), worth 4–50 clicks/month. They are tagged separately in the CSV.
- **Locale-duplicate URLs** (`/en-xx/`, `/ar-xx/`) take **25–30% of impressions every month**. URLs with impressions grew from 508 (May) to 1,196 (Oct). In October they took 16.5% of clicks.

## 6. Merchant Center

| Month | Shopping-ads impressions | Clicks | CTR | Free-listing impressions | Conversions |
|---|---|---|---|---|---|
| Aug | 192,174 | 1,011 | 0.53% | 782 | 0 |
| Sep | 209,196 | 1,850 | 0.88% | 362 | 0 |
| Oct | 140,269 | 785 | 0.56% | 131 | 0 |

- Most impressions: مسك ايمي (48.6k, 0.35% CTR). **Best CTR: مجموعة الصيف at 2.1%** (661 clicks).
- **New issue:** "مجموعة العودة للروتين" is **DISAPPROVED in SA for `tobacco_policy_violation`** on Shopping, free listings, Demand Gen and Video. The Marshmallow highlighter is still disapproved for Demand Gen (image).
- Free listings are almost invisible (131 impressions in Oct).

## 7. Data gaps (MISSING)

- **GA4 before Jul 20**: no tracking. Search Console is the only source for May–Jul.
- **Revenue currency**: decimal values suggest conversion. Confirm the property currency. MISSING.
- **GA4 purchases vs Zid orders**: not reconciled. MISSING.
- Bundle-item ecommerce (0 adds on sets). Checkout events fire together.
- Merchant Center conversions = 0 (not linked).
- `(not set)`: city 21k sessions, landing page 1,156, source 3,219. Payment gateways are not excluded as referrers.
- GSC: 3,662 clicks (≈26%) are anonymised queries and can't be classed.

---

## What stands out

- **Branded Google clicks collapsed ~70% starting 23 Sep**, while impressions and ranking position barely moved. a'mie is losing clicks on its own name. This is the most urgent web issue, and the 22 Oct audit did not catch it.
- **Paid social buys volume, not buyers.** It is 53% of sessions and 18% of purchases, at 0.48 revenue/session. Organic search earns 4.27 and the bio link earns 5.74. Snapchat influencer traffic converts 10× better than Snapchat paid.
- **Three of four shoppers who enter payment info don't finish.** Either checkout or payment is failing, or tracking is losing the purchase. Reconcile with Zid orders before spending more on top-of-funnel.
- **Ad destinations leak:** the Lemongrass set page (8k sessions, 9 sales) and the mirror page (6.9k sessions, 3 sales) absorb paid clicks. Foot cream, highlighters and mists show the cart rates good pages achieve (33–63%).
- **Measurement debt hides product truth.** Sets report 0 carts, MC shows 0 conversions, gateways steal attribution, and a top bundle is disapproved for "tobacco". Fixing these is a prerequisite for any product-level decision.
