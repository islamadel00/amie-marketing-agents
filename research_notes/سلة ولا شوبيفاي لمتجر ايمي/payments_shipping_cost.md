# Payments, shipping, pricing and compliance: Salla vs Shopify (Zid baseline), KSA, 2026

Research date: 2026-10-29. USD converted at 3.75 SAR. All figures exclude 15% VAT unless stated.

**Method caveat (read first):** in this session WebFetch could not reach salla.com, zid.sa or shopify.com (DNS blocked by the session's network allowlist). Every figure below comes from search-result snippets, including snippets of official pages (salla.com/en-sa/plans, zid.sa pricing / payments / ZidPay terms, help.salla.sa, apps.salla.sa) plus third-party 2025–2026 blogs. Official-page snippets are marked **[official]**; everything else is **[3rd-party]**. Before any decision, someone should open the official pricing pages and confirm. Allowing salla.com, zid.sa and shopify.com in the session's network settings would let a re-run verify directly.

## 1. Payments: methods, fees, payouts, prepaid-only

### Takeaway
Salla and Zid bundle a native gateway (Salla Payments / Zid Pay) with mada, Apple Pay, cards, and Tabby/Tamara built in, with mada around 1% + SAR 1. Shopify Payments is not available to Saudi merchants, so a Shopify store must use a third-party gateway (Moyasar, Tap, HyperPay, PayTabs) and pays Shopify's extra third-party fee of 2% / 1% / 0.6% (Basic / Grow / Advanced) on top of the gateway's fee. That surcharge is the biggest structural cost difference.

### Cited findings

**Comparison table: payment fees (dated where the source dates them)**

| Item | Salla (Salla Payments) | Zid (Zid Pay), current baseline | Shopify in KSA (3rd-party gateway) |
|---|---|---|---|
| Native gateway | Yes. Mada, Tabby, Tamara native — [isnaad.ai](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison) [3rd-party] | Yes, Zid Pay — [zid.sa payments](https://zid.sa/en/solutions/payments/) [official] | No. Shopify Payments not available / "not fully available" for Saudi merchants as of 2026 — [easyappsecom](https://easyappsecom.com/guides/selling-on-shopify-saudi-arabia), [truescho](https://truescho.com/en/blog/best-ecommerce-platforms-saudi-arabia) [3rd-party] |
| mada | No official Salla Payments rate card found. One older comparison (about 688 days old, so ~late 2024) gives a flat "2.9% + SAR 0.5" for both Salla and Zid — [isnaad.ai](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison) (stale, conflicts with Zid's own page) | Growth plan tiers: 1% + SAR 1, 2.3% + SAR 1, 3.3% + SAR 1, excl. VAT (method not labelled in snippet; 1% + 1 is almost certainly mada) — [zid.sa payments](https://zid.sa/en/solutions/payments/) [official]; mada capped at SAR 200 per transaction, fees depend on subscription package — [ZidPay T&Cs](https://zid.sa/en/legal/zidpay-terms-conditions-sa/) [official] | Gateway rate + Shopify surcharge. Moyasar: 1% + SAR 1 for mada — [twlm.sa / Arabic guide snippet](https://twlm.sa/tools/%D8%AD%D8%A7%D8%B3%D8%A8%D8%A9-%D8%B1%D8%B3%D9%88%D9%85-%D8%A7%D9%84%D8%AF%D9%81%D8%B9-%D8%A7%D9%84%D8%A5%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/) [3rd-party]; Tap: 1% with SAR 200 cap (Tap blog, 2023) — [Tap blog](https://blog.tap.company/new-mada-fees-saudi/) |
| Visa / Mastercard | Not found officially | Third-party: 2.5–2.75% + SAR 1 — [ijjad](https://www.ijjad.com/payment-gateway-fees-saudi-arabia-2026) [3rd-party]; official page shows 2.3% + 1 / 3.3% + 1 tiers (likely local vs international cards — unverified) | Moyasar 2.5% + SAR 1 (Arabic guide snippet, see above); Tap ~2.85% + SAR 0.30 — [cmarix](https://www.cmarix.com/blog/best-payment-gateways-in-saudi-arabia/), [startupik](https://startupik.com/saudi-payment-gateway-fees-startups-2026/); PayTabs ~2.7% + small fixed fee [3rd-party]. Moyasar's own site says rates come from sales — [Moyasar FAQ](https://www.moyasar.com/en/resources/faqs) |
| Apple Pay | Supported | Supported | Supported via gateway. Charged at the rate of the underlying card (mada card = mada rate) — [ksatools calculator](https://ksatools.com/tools/payment-gateway-calculator) [3rd-party] |
| STC Pay | Not confirmed in search results | Not confirmed | Tap lists STC Pay, Tabby, Tamara, Apple Pay, SADAD as supported — [logiolegion](https://logiolegion.com/blogs/tap-payments-vs-hyperpay-vs-moyasar-saudi-arabia-2026) [3rd-party]; no fee found (only figure: 0.90% on Telr, a different gateway) |
| Tabby / Tamara | Native — [isnaad.ai](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison); activation guides for all three platforms — [mt-themes](https://mt-themes.com/en/blog/tabby-tamara-activation-strategies-for-salla-zid) | Native | Via Tabby/Tamara apps or Tap. Merchant rates are not published; set per contract, estimated 2–3% of order value plus a fixed fee — [watily](https://watily.com/blog/en/bnpl-installment-payment-saudi-online-store-2026/), [paymentreview](https://paymentreview.com/comparisons/tabby-vs-tamara/) [3rd-party]. Whether Shopify's surcharge applies to BNPL depends on how it is installed (unverified) |
| Shopify third-party fee | n/a | n/a | 2.0% Basic, 1.0% Grow, 0.6% Advanced, 0.2% Plus — [qualimero (2026)](https://qualimero.com/en/blog/shopify-transaction-fees), [flatlineagency (Sep 2026)](https://www.flatlineagency.com/blog/shopify-payments-vs-third-party-psps); outlier: Advanced 0.5%, Plus 0.15–0.3% — [profitcalcu](https://profitcalcu.com/blog/shopify-transaction-fees-2026/) |
| Payout | Not found | Sun/Tue/Thu once balance ≥ SAR 100; SAR 3 per deposit except into Al Rajhi — [ijjad](https://www.ijjad.com/payment-gateway-fees-saudi-arabia-2026) [3rd-party] | Gateway-dependent. General KSA guide: mada T+1 to T+3, credit cards T+7 to T+14 (2025) — [raghdan.sa](https://raghdan.sa/en/news/payment-gateways-in-saudi-arabia-guide-2025-requirements-fees-registration-steps-and-comprehensive-comparison/) |
| BNPL payouts | Weekly (Tabby Mondays, Tamara Tuesdays); SAR 25 fee on weekly payouts under SAR 2,500 — [paymentreview](https://paymentreview.com/comparisons/tabby-vs-tamara/); Tamara default waits for SAR 2,500 balance — [paymentreview Tamara](https://paymentreview.com/reviews/tamara/) | same | same |

- Integration build for Tap on Shopify (one vendor, ECOSIRE): one-time USD 249 (SAR 934), no cut of transactions; Tap fees under the merchant's own contract — [ECOSIRE](https://ecosire.com/apps/shopify/payment-tap). Tap also has a native Shopify app per one guide — [velvetica](https://velvetica.studio/best-payment-gateways-shopify-bahrain-uae-saudi-arabia/).
- Mada cap conflict: Tap (2023) announced a SAR 200 cap on mada fees; a later analysis says the SAMA/mada rulebook text does not contain a cap — [Tap blog](https://blog.tap.company/new-mada-fees-saudi/) vs [ijjad](https://www.ijjad.com/payment-gateway-fees-saudi-arabia-2026). Zid's own T&Cs do state a SAR 200 cap for Zid Pay.

**Prepaid-only (disable COD)**
- Salla: COD can be switched on/off from the Shipping Rates tab or Shipping & Delivery > More > Settings > Cash on delivery; specific products/categories can be excluded. With Salla shipping labels, COD is capped at SAR 1,000 per order and hidden below SAR 20 cart value — [Salla help](https://help.salla.sa/en/article/enabling-and-managing-cash-on-delivery-with-salla-shipping-labels/koda8pykc6pdhylg7zb2iu0g) [official].
- Shopify: COD is a manual payment method you simply do not add (general Shopify knowledge, not sourced in this session — flag).
- Zid: not found in search; a'mie already runs on Zid and can check the current setting in the dashboard.

### Inferences
- Worked example per SAR 1,000 of card/mada sales, mada at 1% + SAR 1 per order and average order SAR 250 (4 orders): ~SAR 14 on Zid/Salla. On Shopify Basic with Moyasar: the same ~SAR 14 plus 2% Shopify surcharge = SAR 20 extra, i.e. ~SAR 34, more than double. On Grow, +SAR 10; on Advanced, +SAR 6. For a mada-heavy Saudi basket, the surcharge often costs more than the gateway itself.
- For a'mie's current setup the cheapest payment stack is native (Zid Pay or Salla Payments). Shopify only closes the gap at Advanced or Plus volumes.

### Gaps
- No official Salla Payments rate card, payout schedule or STC Pay support was found (salla.com unreachable).
- Zid Pay's per-method labels and whether rates change by plan beyond "Growth" were not visible.
- Moyasar, HyperPay, Checkout.com and PayTabs official rate cards are not published (sales-quoted); figures above are third-party.
- Whether Shopify charges its third-party fee on Tabby/Tamara orders: not verified.

## 2. Shipping in KSA

### Takeaway
Salla and Zid both have built-in shipping aggregators (Salla shipping labels / ZidShip) with pre-negotiated carrier rates around SAR 25–30 for a domestic parcel; Shopify relies on carrier or aggregator apps. Published rates on the Salla app store: SMSA SAR 25 (first 15 kg) and Aramex SAR 27 (first 15 kg).

### Cited findings

| Carrier / route | Rate found | Platform / source |
|---|---|---|
| SMSA via Salla | SAR 25 first 15 kg, +SAR 1 per extra kg, +15% VAT | [Salla App Store – SMSA](https://apps.salla.sa/en/app/1683195908) [official listing, undated]; SMSA on fixed rates since 15 Mar 2025, excluded from tiered pricing — Salla help (via search snippet) |
| SMSA via Salla (another reading) | SAR 25.65 first 15 kg (cited to Salla SMSA docs, April 2026) | [sellershipment](https://sellershipment.pages.dev/ae-en/ecommerce-shipping-cost/smsa-express-shipping-rates/) [3rd-party] |
| SMSA international GCC (UAE, Bahrain, Kuwait) | SAR 44.6 first 2 kg | [Salla help – SMSA GCC](https://help.salla.sa/en/article/integrating-smsa-international-shipping-gcc/g0y774eifh9rwajiul70376j) [official] |
| Aramex via Salla | SAR 27 first 15 kg, +SAR 2 per extra kg | [Salla App Store – Aramex](https://apps.salla.sa/en/app/1311345502) [official listing, undated] |
| Aramex retail (not merchant) | SAR 110, 1 kg overnight Riyadh–Jeddah | [Qoyod](https://www.qoyod.com/en/blog/online-stores/shipping-companies-in-saudi-arabia/) [3rd-party] |
| SPL (Saudi Post) | SAR 29.95/shipment (Start-up bundle) down to SAR 20 (250-shipment bundle), parcels to 20 kg; listed in Zid's shipping solutions | [Qoyod](https://www.qoyod.com/en/blog/online-stores/shipping-companies-in-saudi-arabia/) [3rd-party] |
| Last Point via Salla | Riyadh SAR 25 (first 5 kg) +SAR 4/kg; other cities SAR 30 +SAR 4/kg, excl. VAT | [Salla help – Last Point](https://help.salla.sa/en/article/connect-last-point-shipping/scnq5sx8j682o7oc0b94xt8f) [official] |
| Salla shipping labels | Discounted labels, discount tied to paid plan | [Salla plans](https://salla.com/en-sa/plans) [official snippet] |
| ZidShip | Zid charges logistics apps SAR 0.70/transaction (shipping apps), SAR 0.50 (fulfilment apps), SAR 0.30 for apps integrated with ZidShip, from 1 Jan 2025 (partner-side fee, not merchant price) | [Zid partner help](https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure) [official] |
| J&T, Naqel, Redbox lockers | No rates found | — |

- Salla supports adding your own delivery rep / shipping company and a shipping-management app API for partners — [Salla help](https://help.salla.sa/en/article/add-delivery-rep-shipping-company/j738mx9fmezq1whaaonz2g3l), [Salla docs](https://docs.salla.dev/422996m0).
- Shipping-cost reduction guide covering all three platforms — [mt-themes](https://mt-themes.com/en/blog/shipping-costs-strategies-to-reduce-them-in-salla-zid).

### Inferences
- For a light beauty/fashion parcel, built-in rates on Salla (SAR 25–27 first 15 kg) are comparable to what Zid merchants report. A Shopify store would need to negotiate its own carrier contracts or use an aggregator app; there is no evidence of a Shopify-side discount for KSA carriers.
- Label printing and tracking come with the native aggregators on Salla/Zid. On Shopify they depend on the chosen app.

### Gaps
- ZidShip merchant rates, J&T, Naqel and Redbox locker pricing: not found.
- Returns workflows (reverse pickup pricing) on each platform: not found.
- National Address / Arabic address-field handling on Shopify checkout vs Salla/Zid: not found in sources this session (unverified; generally Shopify needs apps or checkout customisation for National Address short codes).

## 3. Platform pricing and total cost

### Takeaway
Salla Plus is about SAR 99/month or SAR 990/year, and Pro about SAR 249–299/month or SAR 2,990/year. Zid's comparable tiers are about SAR 99 (Rise) and SAR 299 (Growth) per month. Shopify is USD-priced with no evidence of a Saudi regional discount: Basic $39 (SAR 146) monthly or $29 (SAR 109) annual billing, plus apps that the Saudi platforms include, mainly ZATCA invoicing and Arabic.

### Cited findings

**Plan table (prices as reported, accessed 2026-10-29)**

| Platform / plan | Monthly | Annual | Source |
|---|---|---|---|
| Salla Basic | Free | — | [softwares.com](https://www.softwares.com/compare/salla-vs-searchspring) [3rd-party, flagged unverified by the site itself] |
| Salla Plus | SAR 99 | SAR 990/yr (official snippet; annual shown as 16% off) | [Salla plans](https://salla.com/en-sa/plans) [official]; monthly from [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/) |
| Salla Pro | SAR 249 or SAR 299 (sources conflict) | SAR 2,990/yr | [Salla plans](https://salla.com/en-sa/plans) [official]; monthly: [truescho](https://truescho.com/en/blog/best-ecommerce-platforms-saudi-arabia) (249) vs [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/) (299) |
| Salla Special | Custom / on request | — | [truescho](https://truescho.com/en/blog/best-ecommerce-platforms-saudi-arabia) |
| Salla (UAE page) | "from AED 99/month" | — | [salla.com vs Shopify page](https://salla.com/en-ae/salla-vs-shopify) [official marketing] |
| Zid Rise | SAR 99 | not found | [zid.sa pricing (older cached)](https://zid.sa/en/pricing/), [redrock](https://www.redrock.com.sa/blog/salla-vs-zid-vs-shopify-saudi-arabia/) |
| Zid Growth | SAR 299 (an older 2025 source said SAR 460, likely outdated) | not found | same; [takteek](https://takteek.net/salla-vs-zid-which-is-better/) |
| Zid Professional / Enterprise | By negotiation (one source: SAR 799, conflicts) | — | [redrock](https://www.redrock.com.sa/blog/salla-vs-zid-vs-shopify-saudi-arabia/), [snaabble](https://snaabble.com/en/blog/custom-store-vs-platforms) |
| Shopify Basic | USD 39 = SAR 146.25 | USD 29/mo = SAR 108.75/mo (SAR 1,305/yr) | [qualimero](https://qualimero.com/en/blog/shopify-transaction-fees), [innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026) |
| Shopify Grow ("Shopify") | USD 105 = SAR 393.75 | USD 79/mo = SAR 296.25/mo | [truescho](https://truescho.com/en/blog/best-ecommerce-platforms-saudi-arabia), [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/) |
| Shopify Advanced | USD 399 = SAR 1,496.25 | USD 299/mo = SAR 1,121.25/mo | same |
| Shopify Plus | not found in this session's sources (commonly cited "from USD 2,300/month" = SAR 8,625; **unverified**) | — | — |

- Salla's own comparison: Shopify starts at about AED 146/month on monthly billing, domain separate — [salla.com](https://salla.com/en-ae/salla-vs-shopify) (vendor marketing).
- No official Shopify Saudi regional/SAR price found; one Saudi guide quotes Basic ≈ SAR 112/month — [lkwjd](https://lkwjd.com/how-to-build-shopify-store) [3rd-party].
- Discounts: third-party coupon sites claim up to 55% off annual Salla plans (unverified); a government (MCIT) listing mentions 15% off annual Plus/Pro — [MCIT](https://code.mcit.gov.sa/en/taxonomy/term/718).
- Zid→Shopify migration cost article exists — [bybloshorizon](https://bybloshorizon.com/blog/zid-to-shopify-migration-cost) (not opened).

**Typical extra app costs on Shopify (KSA)**
- ZATCA e-invoice apps: USD 20–80/month (SAR 75–300) — [innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026); or SAR 100–300/month by invoice volume — [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/). Named apps: Marmin ZATCA Invoice with QR, Qoyod Connector, QuiXcel ZATCA Connector.
- Gateway integration: free native apps, or one-time ~USD 249 for a custom Tap build — [ECOSIRE](https://ecosire.com/apps/shopify/payment-tap).
- Reviews, loyalty, Arabic translation, WhatsApp apps: no reliable 2026 price found in this session (gap).

### Inferences
- Illustrative monthly fixed cost, smallest serious tier, annual billing: Salla Plus ≈ SAR 83/mo (990/12); Zid Rise ≈ SAR 99 (monthly figure); Shopify Basic SAR 109 + ZATCA app SAR 75–300 ≈ SAR 184–409/mo, before any reviews/loyalty/WhatsApp/translation apps and before the 2% surcharge on sales.
- At SAR 50,000/month of card sales, Shopify Basic's 2% surcharge alone is SAR 1,000/month, which makes Advanced (0.6% = SAR 300) or Grow (1% = SAR 500) cheaper overall despite the higher subscription. This is arithmetic on cited rates, not a quote.

### Gaps
- Official Salla monthly prices and current Zid prices could not be fetched.
- Shopify Plus 2026 price not sourced.
- Review/loyalty/translation/WhatsApp app prices not found.

## 4. VAT and ZATCA e-invoicing; Saudi Business Center certificate

### Takeaway
Phase 2 (integration) is now rolling down to small businesses: Wave 24 (taxable revenue > SAR 375,000) was due 30 June 2026 and Wave 25 (> SAR 187,500) is reported for 1 February 2027. Salla is reported to include Phase 2 e-invoicing natively at no extra cost. Shopify needs a paid third-party app. Store verification has moved from Maroof to the Saudi Business Center's Business Platform.

### Cited findings
- Wave 23: VAT-taxable revenue > SAR 750,000, deadline 31 Mar 2026; Wave 24: SAR 375,000–750,000 (2022–2024 revenue), deadline 30 Jun 2026, announced 26 Sep 2025 — [beancount.io (Oct 2026)](https://beancount.io/blog/2026/10/06/saudi-arabia-zatca-wave-24-e-invoicing-sme-guide), [flick.network](https://www.flick.network/en-sa/zatca-wave-24-phase-2-einvoicing-2026-guide) [3rd-party].
- Wave 25: announced 24 Jul 2026, threshold SAR 187,500 (2022–2025 revenue), deadline 1 Feb 2027 — [deixtra](https://deixtra.com/blog/zatca-e-invoicing-phase-2-wave-25-integration-guide) [3rd-party]. One source said no further wave announced as of Sep 2026 — [nexus.alskyline](https://nexus.alskyline.com/guides/zatca-e-invoicing-integration-waves-2026). **Not verified on zatca.gov.sa.**
- Salla: built-in Phase 2 e-invoicing (XML, QR, Fatoora submission, cryptographic signing), enabled in settings, no extra cost — [innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026), [zatcahub](https://www.zatcahub.com/); another source describes it as a free ZATCA integration app [3rd-party].
- Shopify: requires third-party ZATCA apps (Marmin, Qoyod Connector, QuiXcel), USD 20–80 or SAR 100–300/month — [innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026), [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/).
- Zid: no source this session confirmed native Phase 2 status (gap; a'mie can check its own Zid dashboard).
- Arabic: Salla's admin is Arabic-first; on Shopify Arabic/RTL is a configuration and often needs custom theme work — [innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026).
- Store verification: Ministry of Commerce now requires verification on the Saudi Business Center's Business Platform instead of Maroof, the only approved platform; Nafath login, domain TXT record, valid CR or freelance certificate, live store — [Salla help](https://help.salla.sa/en/article/verify-store-on-business-platform-instead-of-maroof/gno9ilestioyspm61yu5buzp) [official]. Salla and Zid provide footer fields to display verification details — [arabybot](https://arabybot.com/guides/saudi-online-store-authentication?lang=en) [3rd-party]. Some 2026 guides still cite Maroof (outdated).

### Inferences
- If a'mie's taxable revenue is above SAR 187,500, Phase 2 integration applies by 1 Feb 2027 at the latest (if Wave 25 is confirmed). A move to Shopify then adds a recurring ZATCA app cost and an integration risk; staying on Zid/Salla keeps it native (Zid status to confirm).
- On Shopify, the verification certificate can still be shown in the footer via theme editing; there is no built-in field (inference, unverified).

### Gaps
- Zid's native Phase 2 support, Shopify app Phase 2 certification status, and ZATCA's own wave notices were not verified on primary sources.

## 5. GCC multi-country selling

### Takeaway
Shopify Markets is the most mature multi-country tool (per-country currency, pricing, duties/taxes at checkout; Markets Pro can act as merchant of record). Search found nothing specific on Salla/Zid multi-currency features beyond Salla's SMSA GCC shipping (SAR 44.6 first 2 kg). VAT differs across the GCC, and goods from Saudi to the GCC are not automatically duty-free.

### Cited findings
- GCC VAT 2026: KSA 15%, Bahrain 10%, UAE 5%, Oman 5%; Kuwait and Qatar have no VAT — [gccinvoice](https://gccinvoice.com/blog/gcc-vat-rates-country-guide); another source lists Kuwait/Qatar at 5% (conflict, likely wrong) — [salmangul](https://salmangul.com/cross-border-ecommerce-gcc/).
- Duty-free GCC movement needs GCC-origin goods with a certificate of origin; non-origin goods typically face 5% customs duty — [salmangul](https://salmangul.com/cross-border-ecommerce-gcc/) [3rd-party].
- Shopify Markets: per-country currency (e.g. QAR), shipping rates, duties and taxes at checkout — [zaadcore](https://zaadcore.com/services/shopify-commerce/locations/doha/); per-country tax setup — [easyappsecom UAE](https://easyappsecom.com/guides/selling-on-shopify-uae); Markets Pro makes Shopify the legal seller handling tax, customs and filings — [ecosire](https://ecosire.com/blog/shopify-markets-international-pricing-tax-currency) (availability for KSA-based merchants unverified).
- Tap integrations support SAR, AED, KWD, BHD, QAR, OMR and local methods (KNET, Benefit) — [ECOSIRE](https://ecosire.com/apps/shopify/payment-tap).
- SMSA GCC from Salla: UAE, Bahrain, Kuwait SAR 44.6 first 2 kg — [Salla help](https://help.salla.sa/en/article/integrating-smsa-international-shipping-gcc/g0y774eifh9rwajiul70376j) [official].

### Inferences
- If GCC expansion is a near-term goal, Shopify Markets is a real advantage. For a KSA-first brand, Salla/Zid plus a GCC-capable carrier (SMSA/Aramex) is probably enough. Per-country pricing and duties display on Salla/Zid still need confirmation.

### Gaps
- Salla and Zid multi-currency / multi-market feature details were not found.
- Whether Markets Pro is available to a Saudi-registered Shopify merchant was not verified.
