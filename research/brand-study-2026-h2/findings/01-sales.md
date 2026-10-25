# 01 · Sales: a'mie store, May 1 to Oct 24, 2026

Source: Zid Orders API (read-only), all 7,407 orders from Apr 1 to Oct 24, 2026. This matches the API's own total. April is included as a baseline. Times are Riyadh time. Amounts are SAR including VAT, with non-SAR orders (5%) converted. "Valid" means not cancelled and paid total > 0. October covers 24 days. The CSVs are in `../data/sales_*.csv`.

## Headline KPIs (May 1 to Oct 24)

| KPI | Value |
|---|---|
| Valid paid orders | 6,400 (cancelled: 28 of 6,441 = 0.43%) |
| Gross revenue (list value of lines) | 2,250,454 |
| Discounts (estimated) | 170,400 (7.6% of gross) |
| Net revenue (after discounts, excl. shipping) | 2,080,054 |
| Shipping charged | 163,333 |
| Net AOV | 325 |
| Units / units per order | 11,764 / 1.84 |
| Orders using any coupon | 48.5% |
| Unique customers | 5,869 |

## Monthly trend

| Month | Orders | Orders/day | Gross | Net | Net AOV | Discount % | Coupon orders % |
|---|---|---|---|---|---|---|---|
| Apr (baseline) | 957 | 31.9 | 292,795 | 287,386 | 300 | 1.8 | 8 |
| May | 1,162 | 37.5 | 444,781 | 441,989 | 380 | 0.6 | 4 |
| Jun | 1,174 | 39.1 | 449,593 | 420,962 | 359 | 6.4 | 48 |
| Jul | 1,341 | 43.3 | 495,116 | 469,295 | 350 | 5.2 | 40 |
| Aug | 861 | 27.8 | 290,337 | 265,365 | 308 | 8.6 | 62 |
| Sep | 1,066 | 35.5 | 327,731 | 274,043 | 257 | 16.4 | 81 |
| Oct (1–24) | 796 | 33.2 | 242,896 | 208,401 | 262 | 14.2 | 71 |

- Net revenue per day fell **39%** from May–Jul (14,481) to Aug–Oct (8,798). Orders per day fell only 20%. The rest came from lower AOV (380 to about 260) and deeper discounts (about 6% of gross in Jun–Jul, 14–16% in Sep–Oct).
- Status: 98.6% delivered, 1.0% in progress, 0.4% cancelled.

## Products (product family = variants merged)

| # | Family | Units | Gross revenue | Share | Bought alone | Daily units, Aug–Oct vs May–Jul |
|---|---|---|---|---|---|---|
| 1 | Summer Set (tan trio) | 1,483 | 805,635 | 35.8% | 66% | −62% |
| 2 | Red Cherry tan cream | 891 | 177,264 | 7.9% | 59% | −76% |
| 3 | Hair Set | 723 | 173,052 | 7.7% | 49% | −7% |
| 4 | Hair Wax 30 ml | 991 | 127,846 | 5.7% | 41% | **+48%** |
| 5 | Deep Tan oil | 665 | 105,735 | 4.7% | 35% | −38% |
| 6 | Glow Set | 479 | 96,068 | 4.3% | 25% | −33% |
| 7 | Into The Glow Collection | 319 | 93,792 | 4.2% | 76% | new (Sep/Oct) |
| 8 | Body Glow | 509 | 89,581 | 4.0% | 21% | −29% |
| 9 | Lemongrass Set | 299 | 67,869 | 3.0% | 23% | −10% |
| 10 | Marshmello Highlighter Set | 564 | 55,838 | 2.5% | 34% | −32% |

- **Tanning is 50.4% of gross** (Summer Set plus three single tan products) and is fading with the season.
- **Growing:** Hair Wax (+48%), Sleek Brush (+63%), mirror (+80%), Flora mist (+23%), Foot Cream (+14%). Into The Glow sold 319 units in 5 weeks (from Sep 22).
- **Bottom:** Lip Plump fell 98% from August, which looks like a stock-out (stock data MISSING). Lavender scrub and butter sold 26 units against 370 for Lemongrass. Favors and gift box sold fewer than 15 units each.
- Accessories (brushes, mirror, bags) are bought alone in only 0–7% of their orders.

## Basket

| Units per order | 1 | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|---|
| Share of orders | 53.5% | 26.6% | 11.1% | 4.9% | 2.0% | 2.0% |

| Top co-purchase pairs | Orders | Support | Lift |
|---|---|---|---|
| Hair Wax + Sleek Brush | 249 | 3.9% | 5.0 (69% of brush orders include wax) |
| Deep Tan + Red Cherry | 150 | 2.3% | 2.0 |
| Deep Tan + Glittery Gold | 106 | 1.7% | 3.7 |
| Body Glow + Marshmello Set | 92 | 1.4% | 2.3 |
| Flora mist + a'musk | 88 | 1.4% | 5.6 |
| Flora mist + Natura mist | 87 | 1.4% | 7.3 |

Sets and bundles made up 50–70% of monthly revenue, peaking in Jun (70%) and Oct (69%). 58% of orders contain only one product.

## Customers

| Metric | Value |
|---|---|
| Orders from new customers, May–Oct | 3,712 (58%); Oct reached 68% |
| Repeat rate inside window (≥2 orders Apr–Oct) | 10.0% |
| Repeat rate incl. pre-April history (Zid lifetime count) | 40.1% |
| New customers (first order since Apr 1) placing a 2nd order | 6.0% (250 of 4,143) |
| Median days from 1st to 2nd order | 25 (29 excluding same-day) |
| Top cities (orders) | Riyadh 54.6%, Jeddah 21.0%, Dammam 3.9%, Khobar 3.3%, Dhahran 1.7%, Makkah 1.7% |
| Outside KSA | 3.4% (Qatar 1.6%, UAE 0.9%, Kuwait 0.6%) |

Cohorts are weak: in any later month, no more than 3.3% of a first-order cohort ordered again.

## Coupons and influencer codes

| Code | Orders | Net revenue | Discount | Net AOV | % new customers | Active |
|---|---|---|---|---|---|---|
| Summer26 (15%) | 1,178 | 384,443 | 66,755 | 326 | 49% | Jun 2–Sep 29 |
| ND96 (20%) | 970 | 238,461 | 60,919 | 246 | 57% | Sep 3–Oct 10 |
| NAJLA (20%) | 374 | 88,909 | 22,175 | 238 | 77% | Oct 6–20 |
| Y10 | 192 | 39,726 | 4,392 | 207 | 72% | Jun 27–Aug 21 |
| LULU | 187 | 70,043 | 7,495 | 375 | 41% | mainly Jul 26–27 |
| FTD | 85 | 15,794 | 1,678 | 186 | 73% | Jun 27–Jul 25 |
| aya | 41 | 16,803 | 1,761 | 410 | 59% | May |
| Sh10 / SH | 33 / 21 | 6,914 / 7,552 | 768 / 580 | 210 / 360 | 82% / 71% | Jun–Oct |
| RGD20 / HS15 | 12 / 11 | 2,081 / 2,001 | 621 / 353 | 173 / 182 | 83% / 73% | Sep–Oct |
| Loyal (25%, non-influencer) | 60 | 17,071 | 5,531 | 285 | 7% | Apr–May |

- Influencer-flagged codes (the brief's list, including Summer26 and ND96) account for **48.3% of orders and 41.8% of net revenue**, reaching 80% of orders in September.
- Each code pulls different products: NAJLA drove Into The Glow (216 units), Y10 and FTD drove highlighters and Deep Tan, ND96 drove Hair Wax, LULU drove tan.
- Daily spikes match code launches: Oct 7 (339 orders, 260 NAJLA), Jun 27–28 (Y10 + FTD), Aug 3 (Y10), Sep 4 (ND96), Jul 26–27 (LULU), Jun 2 (Summer26). The median day is 30 orders.

## Time and payment

- Hours: peaks at 14:00–16:00 and 22:00–23:00. 00:00–01:00 still brings 10% of orders. The low is 05:00–08:00.
- Weekday: Wednesday leads (17%), but only because of Oct 7. Other days range from 12.6% to 15%.
- Payment: Apple Pay 73.5%, Tamara 11.9%, Tabby 11.6%, cards 3.0%.

## Anomalies

1. **October collapse:** after ND96 expired on Oct 10, orders fell to **6–16 a day** for Oct 11–24, against a median of 30. Apr 1–10 looked the same (3–14 a day). With no code live, demand seems to sit around 10 orders a day.
2. A **70,600 SAR zero-paid order** (400 tan units, May 25) and 16 other zero-value orders (gifting or internal, including code 00002) are left out of revenue.
3. Apr 30: 18 POS orders (an in-person event, code Stc). This is the only POS activity.
4. Summer Set became a single SKU in July, replacing the Natora and Flora variants, so variant-level growth figures for it are an artefact. Use the family file.

## Data gaps

- **MISSING:** returns and refunds. The API shows 0 reversed orders and refunds were not pulled.
- **MISSING:** exact discount and shipping per order. Discount is estimated from each coupon's % and the flat 33.35 SAR shipping fee. 37 orders had an unattributed discount (wallet or cashback).
- **MISSING:** attribution for codes with 8 or fewer uses. G10 has 0 uses (created Oct 22). RGD10 and "END…" are not in Zid's coupon list.
- **MISSING:** stock and price history, traffic and conversion, UTMs (only on the single-order view), and a Zid sales report to reconcile revenue (only order counts were checked).
- New vs returning uses Zid's lifetime order count, which may include cancelled orders.

## What stands out

- Tanning made the summer: half of gross revenue, now fading fast. Q4 revenue depends on Hair (wax, Hair Set) and Glow (Into The Glow, Body Glow, highlighters).
- Influencer and seasonal codes now drive most orders. When none is live, orders fall to about a third of normal.
- Discounts went from about 6% of gross to 14–16% while net AOV fell 32% (380 to about 260).
- Retention is thin: only 6% of new buyers come back within the window, and a typical second order takes about 25 days.
- Hair Wax + Sleek Brush (lift 5) and the mist + a'musk combos are the strongest natural bundles.
