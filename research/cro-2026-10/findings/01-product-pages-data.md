# 01 — Product pages: data and cart-rate drivers

**Sources:** Zid store, read-only, pulled 2026-10-25: 41 published products, 539 approved reviews, Q&A and bundle offers. GA4 items cover Jul 20 – Oct 24. Sales cover May – Oct 24 (from `brand-study-2026-h2/data/`).
**Data file:** `data/zid_product_pages.csv`. **Status:** draft, not yet through amie-reviewer.

**Caveats**
- Stock is today's snapshot. Arabic word counts are estimates.
- Alt text was checked on 15 pages and was present on every image.
- Into The Glow (8,170 views) and Back to Routine (3,706 views) log **0 add-to-carts** but sold 319 and 70 units. They are variant products with a tracking gap, so they are excluded.
- There are no active bundle offers.

## 1. Attributes vs cart rate

Sample: 32 pages with ≥300 views. Cart rate is pooled (total adds ÷ total views).

| Attribute | With | Without |
|---|---|---|
| Set / bundle | **12.7%** (7 pages) | 22.0% |
| Price ≥150 SAR | **14.5%** (9) | 21.8% |
| Discount shown (all of these are sets) | **10.7%** (5) | 22.4% |
| 0 reviews | **13.3%** (8) | 19.0% |
| ≥10 reviews | 25.8% (8) | 15.8% |
| ≤2 images | **15.1%** (11) | 19.9% |
| ≥4 images | 22.3% (11) | 16.5% |
| Video in description | 23.8% (3) | 17.4% |
| Description <200 words (all accessories) | 16.6%, median **9.7%** (9) | 18.6% |

Per-page rank correlations are weak (|ρ| ≤ 0.19). The clearest pattern is that **high-priced sets on paid traffic convert worst**, and a 4–5% discount doesn't help. Reviews and images are the page levers that move with cart rate. Description length matters little now that 34 of 41 pages use the standard template. No page uses Zid's video field. Today's stock-outs (3 pages) came after the GA4 traffic, so they don't explain these rates.

## 2. Worst 10 pages by cart rate (>1,000 views)

| Page | Views | Cart | Price (SAR) | Missing |
|---|---|---|---|---|
| Lip Plump | 1,046 | 0.4% | 65 | **Out of stock.** 3 Q&A unanswered |
| Lemongrass Set | 9,549 | 6.9% | 227 | 1 review. The SEO title promises a dry brush the description doesn't list. Related products are empty |
| Mirror | 8,613 | 7.1% | 32 | 2 images, 0 reviews, ~130 words |
| **Summer Set (#1 revenue)** | 24,616 | 8.0% | 482 | **1 image.** 4 reviews. The EN short description describes a face cleanser. The SEO meta promises a fragrance that isn't in the set. Related products are empty |
| Brown bag | 2,422 | 9.4% | 69 | Legacy 35-word description, no template |
| Makeup brush | 2,499 | 9.7% | 39 | 1 image, 0 reviews |
| Chocolate Highlighter Set | 3,550 | 13.6% | 99 | 4 images, 3 reviews. The Marshmallow set (6 images) gets 36.9% |
| a'musk | 5,955 | 17.9% | 99 | 3 images. The slug says oil, the how-to says spray. Related products are empty |
| Hair Set (#3) | 8,756 | 18.2% | 268 | Product facts list 4 items. The page shows 2, and block 1 is titled mascara but describes wax. 2 reviews |
| Glow Set (#6) | 5,274 | 18.4% | 205 | 1 review, 3 images |

The best pages for comparison: Foot Cream 64.1% (23 reviews), Marshmallow highlighter 42.8% (with video), Natura/Flora 32–39% (14–17 reviews), Hair Wax 21.5% (176 reviews, with video).

## 3. Stock-outs on best sellers

Cover is in days, at October's sales pace.

| Rank | Product | Stock | Cover | Note |
|---|---|---|---|---|
| 2 | **Red Cherry cream** | **0** | 0 | Second stock-out this season (June also had 0 sales). The page still shows a "Selling fast" badge |
| 4 | **Hair Wax** | 89 | **~18** | #1 by orders. The Hair Set and Back to Routine also contain wax |
| 7 | Into The Glow | 279 (Marshmallow variant 41) | ~23 | Launched 22 Sep |
| 8 | Body Glow | 170 | ~40 | |
| 22 | Lavender Set | 131 | ~47 | |
| 24 | Lip Plump | 0 | — | |
| 29 | Dry brush | 14 | ~28 | |
| — | Hand Cream, Hand & Foot Set | 0 | — | No sales since May, despite 30 and 24 reviews |
| 34 | Gift box, 3 favor packs | 0 | — | Seasonal |

## 4. Other facts

- **Reviews**
  - Hair Wax holds 176 approved reviews (33% of all).
  - The top-3 revenue pages have only 4, 3 and 2.
  - 28 more reviews sit on unpublished legacy tan pages.
  - 173 reviews are pending moderation.
- **Q&A**
  - Only 5 pages have published Q&A, and it was all seeded by staff.
  - 23 questions are unanswered, including 14 staff drafts from 13 Oct.
- **Related products:** 6 pages are set to MANUAL with 0 items picked, including the Summer Set and Hair Wax. Check in the dashboard whether the block shows at all.
- **Badges don't match stock**
  - "Selling fast" shows on Red Cherry (out of stock) and on Lavender scrub (857 in stock).
  - "Limited Quantity" shows on Back to Routine (728 in stock).
- **Copy errors**
  - The Lavender scrub AR short description describes the set.
  - The Lavender butter EN short description describes the scrub.
  - The gift box page describes an empty box, though the product facts list what goes in it.
- **Claims for amie-reviewer**
  - The Red Cherry Q&A says "خالية من المواد الكيميائية".
  - The Hair Wax Q&A says "آمن على الأطفال".
  - The Glittery Gold copy says "بدون حروق", which is a sun-safety claim.
  - The dry brush copy claims it helps "circulation".
- The Marshmallow video embed has `sandbox=""` and may not play.

**Missing:** per-variant cart rate, GA4 data before Jul 20, and a reconciliation against Zid orders.
