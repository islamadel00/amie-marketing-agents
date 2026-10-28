# a'mie traffic: full report and decisions (20 Jul – 27 Oct 2026)

Sources: GA4 (471311593), Search Console (sc-domain:amie-sa.com), Merchant Center (5512193053), all via Supermetrics, read-only. Raw files in `data/` (ga4_*, gsc_*, gmc_*). Zid store analytics returned "no analytics access is configured" for every report, so there is no Zid funnel here. GA4 revenue is USD. The Supermetrics trial ends 29 Oct 2026. See also `findings.md` (first pass on product families and URLs).

## Headline
171.7k sessions, 2,998 purchases, $246k, conversion 1.75%. Since 12 Oct: ~4.6k sessions and ~60 purchases a week.

## 1. Where buyers come from
| Channel | Sessions | Conversion | Revenue/session |
|---|---|---|---|
| Referral (mostly the link card amie-card.netlify.app) | 9.2k | 6.48% | $5.55 |
| Organic Search | 7.3k | 4.91% | $4.16 |
| Paid Shopping (Google) | 1.1k | 4.74% | |
| Direct | 35k | 2.30% | |
| Organic Social | 18k | 2.02% | |
| **Paid Social** | **89.6k (52%)** | **0.60%** | **$0.49** |

- The link card alone: 481 purchases, $41k, 7.69% conversion. It is the best-converting entry point.
- Snapchat paid: 51.8k sessions at 0.31%; one UUID-named campaign has 48.6k sessions at 0.19%. TikTok paid 0.53%. tiktok.com referral: 3k sessions, 0 purchases.
- Snapchat influencer traffic converts at 3.2%; the 6–7 Oct influencer spike brought 12.8k sessions and 415 purchases.
- Returning visitors: 12% of sessions, 37% of revenue (5.34% conversion vs 1.45% for new).

## 2. Devices and cities
- 97% mobile. Desktop converts at 0.54%; tablet 0 of 800. Android Chrome 0.14% vs iOS Safari 1.91%.
- Jeddah converts better than Riyadh (2.34% vs 1.65%). Abha 3.15%, Doha 3.70%. Buraydah 0.57%, Makkah 0.75%.

## 3. Landing pages
- Best: homepage (18k sessions, 5.37%), `/products` (5.48%), body-products category (4.4%).
- Worst: Summer Set `amie-glow-skincare-set` (17.8k sessions, 0.75%, the main paid landing page), lemongrass set (8.1k, 0.12%), mirror (6.9k, 0.04%), sleek brush (0%), makeup brush (0.05%), bag (0.15%), mascara page (0.16%).

## 4. Products (detail in findings.md)
- Most units: hair wax (547). Into The Glow (launched Sep) grew the whole glow family: 252 units in Sep → 654 in Oct. Marshmello takes ~85% of Into The Glow adds.
- Tan line and Summer Set down 81–95% (season over). Lavender line started selling in October (95 units).
- Paid Social sends 54% of item views at 1.14% view→unit; Organic Search 13.3%, Referral 12.9%.
- Zero add-to-cart despite views: hand cream, hand & foot set, gift box, mini favors.

## 5. Funnel and tracking
- view_item → add_to_cart 16.1% → begin_checkout 48.8% → add_payment_info 98% → purchase 25.6%.
- The 74% drop after "payment info" is partly a tracking artefact: add_payment_info fires on page load, and add_shipping_info fires more than once per checkout.
- Sessions break when shoppers return from Tabby, Tamara, noonpayments and sso.zid.store (they show up as referrals and as landings on /checkout and /cart). Add these domains to GA4 unwanted referrals.
- Junk traffic: UAE with no city 18.8k sessions / 1 purchase; US data-centre cities; "(not set)" visitors 19.4k at 5% engaged.
- UTMs broken: unfilled `{{campaign.name}}` and `__CAMPAIGN_NAME__`, Snapchat medium tagged paid / cpc / CPC, campaigns named by UUID.
- Product-list clicks (select_item) not tracked at all.
- URL variants: trailing-slash product URLs (from Snap/TikTok ads) convert at 1.4% add-to-cart vs 11.6% on the clean URL for the same page and source. `/ar-eg/` 2.7% vs 5.1%.

## 6. Google search
- Clicks −46% (8,201 → 4,438) while impressions rose 157k → 225k.
- Brand clicks −55% (5,818 → 2,623, counting the old "a'mi" spellings). "ايمي" CTR 9.1% → 4.95% at the same position; "amie" fell from position 7.1 to 10.5 and Google shows `/en/` for it.
- Non-branded is tiny (172 clicks). Quick wins at position 4–15: تان (10.4k impressions), كريم تان, واكس للشعر / واكس شعر (6.6k combined), لمعة جسم (3.6k), العناية بالجسم.
- Low CTR, high impressions: tanning category (21.7k, 1.2%), hair wax (16.8k, 1.4%), glow set (7.8k), curly-hair blog (7.4k, 0.2%).
- 400 of the top 500 pages in Search are locale copies (/ar-eg/, /ar-us/, /en-qa/…), 41.6k impressions.

## 7. Merchant Center
- 552.6k impressions, 3,777 clicks, 0 conversions (conversion tracking not connected).
- مسك ايمي: 49.8k impressions at 0.35% CTR.
- Disapproved: Back-to-Routine set ("tobacco policy", likely false positive, appeal). Marshmello highlighter image blocked on Demand Gen / Discover.
- Duplicate product entries under extra IDs.

## On-site search
Rarely used (396 searches). Top terms: واكس, كريم, تان, مسك, عطر, كريم التان, كريم القدمين, مقشر.

## Decisions, by impact
1. **Paid Social:** cut the Snapchat UUID campaign (48.6k sessions, 0.19%) and the paid landing on Summer Set; move budget to influencer + Google Shopping/PMax, which convert 5–10× better.
2. **Ad links:** clean URLs only (no trailing slash, no country prefix), fixed UTMs (one medium per platform, real campaign names).
3. **Link card:** it is the best-converting door. Put it in every bio and influencer brief, keep UTMs on it.
4. **Returning customers:** 37% of revenue from 12% of sessions. Start win-back / replenishment (WhatsApp, email) for wax, tan, glow buyers.
5. **Search:** fix titles/meta for tanning category, hair wax, glow set; target تان / واكس شعر / لمعة جسم; stop locale copies being indexed (canonical / hreflang settings in Zid).
6. **Tracking (one sprint):** unwanted referrals for Tabby/Tamara/noon/Zid SSO, bot filter, fix add_payment_info / add_shipping_info, add select_item, connect Merchant Center conversions.
7. **Catalogue:** fix or hide zero-cart products; keep Marshmello first in glow; lemongrass set and mirror off paid traffic.
8. **Merchant Center:** appeal the Back-to-Routine disapproval, replace the Marshmello image, merge duplicate IDs.
9. **Zid analytics:** enable store analytics access so the Zid funnel and abandoned carts can be pulled.
