# a'mie site organisation plan, combined draft (for amie-reviewer)

Inputs: 01-product-scorecard-summary.md (+ product_scorecard.csv, homepage_ranking.csv), 02-pricing-bundles.md, 03-cro-merchandising.md, 04-voice-of-customer.md, 05-seo-architecture.md, ../full-report.md, ../findings.md. Period 20 Jul–27 Oct 2026 (GA4), Zid units May–Oct.

## A. What confuses or stops shoppers (diagnosis)
1. Glow family: 7 options, price steps 79 / 99 / 176 / 205 / 294. Into The Glow (294) saves 0 vs its parts and is 19 SAR dearer than Body Glow + Highlighter Set (275, bought together in 92 orders). Into The Glow cart→unit 16.4% (z −3.8). Marshmello = 85% of its adds, stock 41 vs Chocolate 238. Same Arabic name "مجموعة لمعة الجسم" used for Glow Set and Into The Glow. Body Glow named "جلّ" but is an oily liquid.
2. Singles vs sets 20 SAR apart: Marshmello single 448 adds / 54 units last 30 days; sets outsell singles ~2:1.
3. Scrub/butter: Lemongrass Set (227) vs Lavender Set (199.75) same format; Lemongrass set cart rate 6.9% vs Lavender 20.5%; cluster flat while Lavender cannibalises Lemongrass.
4. Sets save only 4–5% (strike-through), coupons on 48.5–80% of orders → shoppers build their own baskets.
5. Pages with wrong or missing content: Summer Set (EN text describes a face cleanser, 1 image, meta promises fragrance), Lemongrass Set (title promises dry brush), Hair Set (shows 2 of 4 items), Into The Glow (no shade guide, 0 reviews shown, contents unconfirmed).
6. Products with views and no buy path: hand cream, hand & foot set, lip balm, gift box, favors (out of stock / no add-to-cart).
7. False scarcity badges: "يباع سريعًا" on out-of-stock Red Cherry; "كمية محدودة" on items with 700+ in stock.
8. Paid traffic lands on pages that don't sell (mirror 0.15%, Lemongrass Set 0.41%, Summer Set 0.58% on Paid Social) and on duplicate URLs (trailing slash 1.4% add-to-cart vs 11.6% clean; country prefixes 1.8%).

## B. Homepage (top to bottom, mobile)
1. Announcement bar: صنع في السعودية · مسجّلة لدى هيئة الغذاء والدواء.
2. Hero: Into The Glow → CTA to the لمعة الجسم chooser. Precondition: restock Marshmello (41 units). If not restocked, hero = واكس الشعر.
3. الأكثر مبيعاً (4): واكس الشعر · مجموعة مارشميلو هايلايتر الجسم · لمعة الجسم · مجموعة الشعر.
4. Shop by routine tiles: لمعة الجسم · العناية بالشعر · العناية بالجسم · العطور · الهدايا · التان (last).
5. Winter banner (replaces Deep Tan, −93%): كريم القدمين (non-paid view→unit ~19–20%) + مجموعة اللافندر (views up sharply, 4.97★).
6. Small add-ons: فرشاة سليك · عطر ناتورا · عطر فلورا · ماسكارا الشعر · مسك ايمي.
7. Reviews block (wax, foot cream, Body Glow).
Remove: "احدث المنتجات" tab, mirror and Lemongrass Set from featured spots, false scarcity badges, chat bubble overlapping cards. Max 2–3 glow products on the page.

## C. Categories (no renames; order and contents only)
Menu order: منتجات التان (last on homepage, kept in menu for search) / لمعة الجسم / العناية بالشعر / العناية بالجسم / العطور / مجموعة الهدايا والعروض / المجموعات / الأكثر مبيعاً. (SEO and CRO disagree on tan's menu position; see open items.)
- لمعة الجسم: chooser of 3 tiles (ستيك للمناطق المحددة = 99 sets · لمعة لكل الجسم = Body Glow / Glow Set · المجموعة الكاملة = Into The Glow), Marshmello first; singles and makeup brush out of the grid but still reachable.
- الأكثر مبيعاً: 8 products by last-30-day units; no tan, no out-of-stock.
- العناية بالجسم 8, العناية بالشعر 4, العطور 4, التان 4.
- Hide (not delete) duplicate / legacy lists and categories; merge اللمعة والإشراقة into لمعة الجسم.

## D. Prices and bundles (COGS missing; confirm against margin)
- Make current sale prices the list prices; show saving only if ≥ 8% as "وفّري X ر.س".
- Into The Glow: give it a real saving (e.g. 269, needs +9.3% units to hold revenue) or add value at 294.
- Cart offers: wax + sleek brush; fragrance trio (Flora + Natura + a'musk); Body Glow + Marshmello set as "complete the look".
- Confirm price conflicts: Lemongrass butter 119 vs sheet 199; A'mi Bag 69 vs sheet 49.

## E. Product page content fixes (top 8)
Summer Set contents/images/EN text; Into The Glow contents + shade guide + publish reviews; "what's the difference" block on glow pages; Lemongrass Set contents (drop dry-brush promise); Hair Set all 4 items; answer 23 open questions and remove forbidden phrases in answers; tan trio comparison (remove "بدون حروق"); one highlighter spelling + separate shade videos.

## F. Technical (needed for the above to work and be measured)
Disable unused markets (keep SA AR+EN), canonical/hreflang, clean ad URLs (no trailing slash, no prefix), GA4 unwanted referrals (Tabby, Tamara, noon, Zid SSO), select_item tracking, fix add_payment_info / add_shipping_info, connect GMC conversions, enable Zid store analytics.

## G. Tests (≈4.6k sessions, ≈60 purchases/week; main metric add-to-cart / units per view)
Glow chooser vs grid (≥6 weeks); Into The Glow page upgrade (5–6 weeks); wax + brush add-on (4 weeks); winter vs Deep Tan banner (6–8 weeks, directional).

## Open items / conflicts for the team
- لمعة الجسم category ID: GA4 path shows 1759672, SEO draft says 1756504. Confirm.
- Into The Glow contents (pricing draft: Body Glow + stick + brush).
- a'musk: oil or spray. Body Glow: gel or oil.
- Free-shipping threshold and order-value histogram.
- COGS per product.
