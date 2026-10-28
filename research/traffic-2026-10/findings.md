# Product traffic and choice overload (GA4, 20 Jul – 27 Oct 2026)

Source: GA4 property 471311593 via Supermetrics (read-only). Item metrics grouped by Zid product ID, because GA4 logs the same product under several names (Arabic, English, old names, variants). Purchases are GA4 units (GA4 records ~88–90% of Zid orders). Revenue in USD as GA4 reports it. `data/ga4_items_2026-07-20_2026-10-27.csv` holds the grouped numbers.

## 1. Highlighter / glow family: 7 products for one job

| Product | Price (SAR) | Views | Add to cart | Units | View → unit |
|---|---|---|---|---|---|
| Into The Glow collection (2 shades) | 294 | 8,657 | 1,791 | 294 | 3.4% |
| Glow Set (gel set) | 205 | 5,427 | 997 | 204 | 3.8% |
| Body Glow gel | 176 | 5,129 | 1,245 | 234 | 4.6% |
| Marshmello highlighter **set** | 99 | 3,376 | 1,233 | 247 | 7.3% |
| Chocolate highlighter **set** | 99 | 3,629 | 491 | 117 | 3.2% |
| Marshmello highlighter single | 79 | 1,867 | 786 | 123 | 6.6% |
| Chocolate highlighter single | 79 | 2,109 | 428 | 74 | 3.5% |
| **Family total** | | **30,194** | | **1,293** | 4.3% |

- Shade × format × bundle = 7 choices. A single and its set differ by 20 SAR (the set adds the makeup brush).
- Sets outsell singles: 364 vs 197 units. Singles take 13% of family views and 15% of units.
- Marshmello beats Chocolate in every format: 370 vs 191 units (set + single).
- Last 30 days: Into The Glow had 8,128 views (most-viewed product in the store) and 277 units. Marshmello single: 448 add-to-carts but only 54 units (12%), so many people add it and then don't buy it.

## 2. Other families

| Family | Product | Views | Units | View → unit |
|---|---|---|---|---|
| Hair | Hair wax 129 | 10,960 | 547 | 5.0% |
| | Hair set 268 | 9,116 | 355 | 3.9% |
| | Mascara 75 | 3,006 | 156 | 5.2% |
| | Sleek brush 29 | 2,515 | 220 | 8.7% |
| Lemongrass | **Set 227** | 9,727 | 141 | **1.4%** |
| | Scrub 119 | 2,935 | 111 | 3.8% |
| | Butter | 1,633 | 60 | 3.7% |
| Lavender | Set | 1,357 | 69 | 5.1% |
| | Scrub / butter | 1,017 | 26 | 2.6% |
| Accessories | **Mirror 32** | 8,698 | 88 | **1.0%** |
| Tan (seasonal) | Summer Set | 24,734 | 441 | 1.8% |

Hair works: the set and the singles both sell, with no sign of confusion. Lemongrass set and the mirror pull a lot of traffic that barely converts.

## 3. Products with views and (almost) no add-to-cart
Hand cream 49 (669 views, 0 adds), Hand & foot set 124 (238, 0), Lip balm (1,060, 4), Gift box (198, 0), mini-favor packs (0 adds). All are published on Zid. Likely out of stock or no buy button; to check in the dashboard.

## 4. URL problems that leak traffic
| Page type | Views | Engaged sessions | Add-to-cart / view |
|---|---|---|---|
| `/products/<slug>` (normal) | 121,614 | 30% | 9.5% |
| `/products/<slug>/` (trailing slash) | 13,338 | 18% | 1.4% |
| Country prefixes `/ar-eg/`, `/ar-us/`, `/en-sa/`… | 11,359 | 55% of sessions | 1.8% |

Same traffic source, different URL: Snapchat cpc to slash pages 6,568 views → 149 adds (2.3%) vs to normal pages 5,478 → 841 (15.4%). TikTok paid: slash 4,501 → 30 (0.7%) vs normal 1,072 → 236 (22%). Ad links with a trailing slash (several Snap/TikTok ads) land on pages that barely convert or don't fire add-to-cart. Needs a manual check of one slash URL in the dashboard.

## 5. Tracking gap
`select_item` is not tracked (0 clicks from every list), so we can't measure which product cards get clicked on category pages. Fix in the GA4 / Zid integration.

## Decisions to take
1. Highlighter family: cut from 7 to ~4 choices. Option A: drop the two singles and keep the 99 SAR sets. Option B: keep singles, sell the brush as a one-tap add-on, drop the sets. Data favours A (sets sell 1.8× singles). Show Marshmello first.
2. One "glow" category page with a short chooser (stick vs gel vs full collection) instead of 7 cards side by side.
3. Remove trailing slashes and country prefixes from all ad links; redirect slash URLs if Zid allows.
4. Stop sending paid traffic to the Lemongrass set and the mirror until their pages convert; move it to wax / hair set / Marshmello set.
5. Check stock for hand cream, hand & foot set, lip balm, gift box; hide or restock.
