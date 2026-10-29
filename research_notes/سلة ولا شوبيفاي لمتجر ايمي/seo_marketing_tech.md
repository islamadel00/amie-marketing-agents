# SEO/URL control, storefront tech and marketing/tracking stack: Salla vs Shopify (Zid as baseline), as of Oct 2026

Research date: 2026-10-29. Method: web search only. **Direct page fetches failed** because help.salla.sa and help.shopify.com are outside this session's allowed network domains, so the findings below come from search-result summaries of those pages. Treat platform-doc claims as "seen in search snippet, not read in full". Sources are labelled [OFFICIAL] (vendor help/dev docs), [VENDOR-MKT] (agency, theme seller or app vendor blog with a commercial interest) or [COMMUNITY] (merchant forum). Dates are the research date unless a source date is known.

Zid baseline (from the brief, not re-researched): locale-prefix duplicate URLs (/ar/, /ar-eg/, /ar-sa/, /en-sa/; 402 of the top 500 GSC pages are locale copies), trailing-slash duplicates that convert far worse, a category API that resets SEO titles, limited analytics access, Arabic slugs.

## 1. SEO: URLs/slugs, canonicals, hreflang, redirects, robots/sitemap, structured data, speed, RTL, translation

### Takeaway
Shopify gives the most documented, predictable international-SEO setup: auto-generated hreflang from Markets, subfolder locales, robots.txt.liquid, and an established redirect tool. Its trade-offs are a fixed `/products/` and `/collections/` path and weak support for Arabic (Unicode) handles, so Latin handles are the norm. Salla has editable robots.txt, a sitemap, custom product slugs and an SEO settings API. I found **no Salla documentation on a 301 redirect manager, hreflang or canonical control**, which is exactly the area where Zid is failing today. Salla's fit on the duplicate-URL problem is therefore unproven and needs a hands-on test.

### Cited Findings
**Salla**
- [OFFICIAL] Salla's SEO page sits under Marketing tools. robots.txt is editable from general settings, where the sitemap and home-page SEO also live (Salla help, seen 2026-10) — [Salla help: improve store SEO](https://help.salla.sa/en/article/improve-store-seo/gmzx0xblr3ajerkciyoxke1e)
- [OFFICIAL] Bilingual sitemap entries appear only when multi-language is on, English is added and product names exist in both languages. The English link does not appear in the sitemap for an Arabic-only store — [Salla help: improve store SEO](https://help.salla.sa/en/article/improve-store-seo/gmzx0xblr3ajerkciyoxke1e)
- [OFFICIAL] Products have a custom product link (slug) field in their SEO section. If it is left empty, Salla uses the default link — [Salla help via search snippet](https://help.salla.sa/en/article/improve-store-seo/gmzx0xblr3ajerkciyoxke1e); also [mt-themes (VENDOR-MKT)](https://mt-themes.com/en/blog/product-seo-boost-visibility-on-salla-zid)
- [OFFICIAL] The Merchant API has an "Update SEO Settings" endpoint with a `friendly_urls_status` flag. Its exact effect is undocumented in the snippet — [docs.salla.dev Update SEO Settings](https://docs.salla.dev/5394263e0)
- **Not found:** any Salla doc on a 301 redirect manager, auto-redirect on slug change, canonical controls or hreflang output. Several searches in English and Arabic (2026-10) returned none — see searches cited in [Salla help](https://help.salla.sa/en/article/improve-store-seo/gmzx0xblr3ajerkciyoxke1e) and [dohour.net Salla SEO guide 2026 (VENDOR-MKT)](https://dohour.net/salla-seo-ultimate-guide-2026/)
- [VENDOR-MKT] Arabic SEO blogs warn that Salla stores which launch Arabic and English versions without correct hreflang get treated as duplicates. They also say the platform generates multiple URLs for the same product via categories, brands, filters and internal search — [dohour.net (2026)](https://dohour.net/salla-seo-ultimate-guide-2026/); [rankxseo: technical SEO for Salla](https://rankxseo.com/blog/%D8%A7%D9%84%D8%B3%D9%8A%D9%88-%D8%A7%D9%84%D8%AA%D9%82%D9%86%D9%8A-%D9%84%D9%85%D8%AA%D8%AC%D8%B1-%D8%B3%D9%84%D8%A9/); [rankxseo: 13 Salla SEO errors](https://rankxseo.com/blog/%D8%A7%D8%AE%D8%B7%D8%A7%D8%A1-%D8%A7%D9%84%D8%B3%D9%8A%D9%88-%D9%81%D9%8A-%D8%B3%D9%84%D8%A9/). These sources describe the risk but do not show whether Salla emits hreflang itself.
- [VENDOR-MKT] On Arabic slugs, one Salla SEO blog says Google understands them, but they become unshareable after percent-encoding. Some practitioners prefer Latin slugs — [rankxseo](https://rankxseo.com/blog/%D8%A7%D8%AE%D8%B7%D8%A7%D8%A1-%D8%A7%D9%84%D8%B3%D9%8A%D9%88-%D9%81%D9%8A-%D8%B3%D9%84%D8%A9/)
- [VENDOR-MKT] Several 2026 comparisons say Salla's SEO is "solid out of the box but lacks some granular controls" next to Shopify. They also say Salla and Zid auto-generate clean Arabic URLs and meta, while Shopify needs careful configuration — [h-haboubi 2026](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/); [lucidly.ae 2026](https://lucidly.ae/blog/shopify/shopify-vs-salla); [ijjad 2026](https://www.ijjad.com/salla-vs-zid-vs-shopify-saudi-retailers)
- [OFFICIAL] Salla's Twilight theme review requires an average Lighthouse **accessibility** score of at least 90 on product, collection and home pages, and a theme size under 1 MB. This is not a speed or CWV requirement — [Twilight Technical Theme Review](https://docs.salla.dev/421888m0)
- No independent Core Web Vitals benchmark for Salla Twilight themes was found (2026-10) — [search context: mt-themes speed guide (VENDOR-MKT)](https://mt-themes.com/en/blog/post-1785852296447)

**Shopify**
- [OFFICIAL] Shopify recommends subfolders for most stores. Hreflang tags are generated automatically from market and language configuration and added to every page when a domain, subfolder or subdomain is assigned to a market and language. Translated pages are served at market-specific URLs — [Shopify Help: International SEO for markets](https://help.shopify.com/en/manual/markets/seo)
- [OFFICIAL] Hreflang codes take the form language plus optional region (e.g. en-us, fr-fr) — [Shopify Help: Markets SEO](https://help.shopify.com/en/manual/markets/seo). Whether an `ar-sa` folder is generated, or only `ar`, was not confirmed. [VENDOR-MKT] One agency notes merchants lack full control over folder naming (/fr vs /fr-fr) — [1digitalagency hreflang guide](https://www.1digitalagency.com/blog/how-to-correctly-implement-hreflang-with-shopify-markets-with-code-examples/)
- [VENDOR-MKT] A market with zero published translations does not get hreflang injected. Shopify generates the tags but does not validate them or prevent conflicting signals — [Shero Commerce hreflang audit](https://sherocommerce.com/blogs/insights/shopify-hreflang); [analyzify](https://analyzify.com/hub/shopify-markets-seo)
- [OFFICIAL] Translate & Adapt supports per-market adaptation of descriptions, promotions and legal text — [Shopify Help: Markets SEO](https://help.shopify.com/en/manual/markets/seo)
- [VENDOR-MKT] The core URL structure (`/products/`, `/collections/`) cannot be changed. A product is also reachable at `/collections/x/products/y`, and canonical points to `/products/y`. Filter and sort parameters create crawlable duplicates — [visionary-marketing 2026](https://visionary-marketing.co.uk/blog/shopify-seo-guide-2026); [1digitalagency: Shopify's biggest SEO limitations](https://www.1digitalagency.com/blog/shopify-s-biggest-seo-limitations-and-how-to-work-around-each-one-34494/); [Hallam](https://hallam.agency/blog/shopify-seo-issues-tips/)
- [VENDOR-MKT] robots.txt can be customised through a `robots.txt.liquid` theme template, though one source still claims Shopify controls robots.txt (conflicting) — [Hallam](https://hallam.agency/blog/shopify-seo-issues-tips/); [darkroom 2026](https://www.darkroomagency.com/observatory/shopify-seo-technical-optimization-2026)
- [COMMUNITY] Unicode (non-Latin) handles: one merchant reports the admin creates Unicode handles from titles, but the API would not accept updating a handle to Unicode — [Shopify Community: cannot update product handle with unicode](https://community.shopify.com/t/cannot-update-product-handle-with-unicode-characters/239594). Redirect validation measures percent-encoded length, so redirects for non-Latin (Cyrillic) URLs are rejected as too long — [Shopify Community: Cyrillic redirects](https://community.shopify.com/t/issue-with-url-encoding-of-cyrillic-characters-in-shopify-url-redirects/240533). Both threads are older than 2025, so they need re-testing.
- [VENDOR-MKT] Arabic Shopify guides from GCC agencies recommend Latin transliterated handles plus Arabic titles and meta, with separate /ar/ and /en/ URLs per locale — [klever.ae](https://www.klever.ae/blog/arabic-shopify-store); [cartworks](https://cartworks.io/blogs/shopify/shopify-multilingual-store-arabic-english); [dev.to bilingual KSA checklist](https://dev.to/ecommerce_southfield_5e85/shopify-seo-checklist-for-bilingual-english-arabic-stores-in-saudi-arabia-4501)
- [VENDOR-MKT] One source says Shopify has the strongest SEO foundation of the four Saudi platforms (meta control, structured data, blog tooling) — [h-haboubi 2026](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/)

**General (Google)**
- [OFFICIAL] Google ranks canonicalisation signals by strength: redirects first, then rel=canonical, then sitemap inclusion. Do not use robots.txt for canonicalisation — [Google Search Central: consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

### Inferences
- Zid's core pain (402 of the top 500 GSC pages are locale copies, plus trailing-slash duplicates) is a platform URL-routing and canonical problem. Shopify Markets is designed so that each locale is a deliberate subfolder with auto hreflang and self-canonicals, which is the right model, but only if a'mie configures one market (KSA) with ar and en, not many ar-xx variants. For Salla I could not establish how locales are pathed or whether hreflang and canonicals are emitted. **Recommended test before deciding:** crawl 2–3 live bilingual Salla beauty stores (Screaming Frog), checking hreflang, canonical, /en/ paths and trailing slashes.
- Migration risk on either platform: a'mie's Arabic Zid slugs will change, so a 301 map is mandatory. Shopify's URL Redirects tool (admin > Navigation > URL redirects, CSV import) is standard; this is from prior knowledge and was **not re-verified this session**. Watch the non-Latin redirect-length bug and use percent-encoded source paths. For Salla, the existence of a bulk 301 importer is unverified and is a **gating question for Salla support**.
- Arabic slugs: both platforms' practitioners push Latin slugs. Moving to Latin handles is an SEO change in its own right, and it is easier to make during a migration than at any other time.
- Shopify's fixed `/products/` and `/collections/` paths are a cosmetic limitation; they do not create duplicates the way Zid's locale copies do, because canonicals handle the collection-nested path.

### Gaps
- Salla: 301 redirect manager, auto-redirect on slug change, canonical tags, hreflang output, locale URL pattern, trailing-slash handling, structured data (Product, Review, Breadcrumb) output. No source found; the help center could not be fetched.
- Whether Shopify Markets produces `/ar-sa/` or `/ar/` for a single-country store, and whether Arabic handles currently work through the admin and API in 2026.
- Field CWV data (CrUX) for Salla Twilight vs Shopify Dawn and Horizon themes: no independent benchmark found.
- Quality of RTL Shopify themes (Dawn and Horizon RTL support) vs Salla Twilight themes: no cited evaluation found.
- Weglot vs Translate & Adapt for Arabic: not researched (out of call budget).

## 2. Tracking & marketing stack

### Takeaway
Both platforms cover the Saudi paid-social basics (Meta, Snap, TikTok pixels plus CAPI, and product catalogs). Salla does it largely natively or through first-party apps, with a unified "Salla Catalog" feed and a Snap Business Extension that syncs pixel, catalog and CAPI. Shopify has deeper server-side and event control and a much larger app ecosystem (Klaviyo native, Zoko, Wati and so on). **Klaviyo on Salla is limited:** the official integration collects subscribers but **does not sync abandoned carts**, which is a big gap for a DTC beauty brand.

### Cited Findings
**Salla**
- [OFFICIAL] Meta CAPI: install the "Facebook Conversion API" app from the Salla App Store after linking a Facebook Business account — [Salla help: Facebook Conversion API](https://help.salla.sa/article/741081803)
- [OFFICIAL] TikTok Events API: paste the pixel code and an access token. The app complements the pixel and does not replace it — [Salla help: TikTok Conversion API](https://help.salla.sa/article/%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-tiktok-conversion-api/zd0j9rru0h3cgbi593roxpmn); [Salla changelog](https://changelog.salla.sa/1294204451)
- [OFFICIAL] Snap: the Snap Business Extension under Marketing > Tracking tools syncs ad account, Snap Pixel, catalog and Conversions API automatically — [Salla help: Snap Business Extension](https://help.salla.sa/en/article/connect-snapchat-snap-business-extension/bc4caiy58eek7dmswse6vii4)
- [OFFICIAL] "Salla Catalog" generates one product-feed link (choose language and currency) that connects to Snapchat, TikTok, Google, Meta and X — [Salla help: Salla Catalog](https://help.salla.sa/en/article/salla-catalog/xcng7dyne2ig5re94wh63s0m). A Merchant Center feed article exists but its content was not visible.
- [OFFICIAL] Klaviyo: the official Salla integration shows subscription forms and syncs customer data. It **does not currently support abandoned-cart syncing** — [Salla help: connecting Klaviyo](https://help.salla.sa/en/article/connecting-klaviyo-for-email-and-sms/uyfoc8mncs9wylzuyikvi4qe). The alternatives are the third-party paid app Scalera ([Salla help: Scalera](https://help.salla.sa/en/article/scalera-connect-klaviyo-via/xnyo0fo89i8z8hxn73br5g5z)) and Zapier ([Zapier](https://zapier.com/apps/klaviyo/integrations/salla)).
- [OFFICIAL] WhatsApp: Salla's WhatsApp Chat App comes from a partnership with WhatsApp and provides Business API capabilities with a multi-agent shared inbox (source about 1 year old). Third-party Rasi adds campaigns, abandoned-cart and shipping messages, and an AI assistant — [Salla help: Rasi](https://help.salla.sa/en/article/rasi-whatsapp-marketing-app/eydlnfxh09lytr6tmm2d34s5)
- [OFFICIAL] Loyalty: Salla's paid first-party Loyalty Rewards app (points for purchases, reviews, profile completion, sharing). Third-party Wala X has 42 reviews — [Salla App Store: Wala X](https://apps.salla.sa/en/app/861510477)
- [OFFICIAL/dev blog] Affiliate marketing is built into Salla packages — [Salla Developers blog](https://salla.dev/blog/affiliate-marketing-for-salla-packages-explained/)
- [VENDOR-MKT] A paid-ads agency says basic pixel tracking is fine on both. Event deduplication, custom conversion values and profit-adjusted values are "doable but less room to manoeuvre" on Salla. It rates server-side depth as "deepest, via apps" on Shopify and "improving" on Salla — [AdGrow: Salla, Zid or Shopify for paid ads](https://adgrow.ae/blog/salla-zid-shopify-paid-ads-saudi-arabia/)
- [VENDOR-MKT] Snap Pixel is present on roughly half of Gulf Shopify stores against more than 80% of Salla and Zid stores (adoption, not capability) — [gccfy](https://gccfy.com/en/blog/snapchat-ads-saudi-arabia)
- [VENDOR-MKT] Conversion-tracking guide for Salla (MENA) — [trackingconsulting.com](https://trackingconsulting.com/blog/salla-conversion-tracking-guide). Not read in full.

**Zid (baseline)**
- [OFFICIAL] Zid has native TikTok Pixel and TikTok Conversion API linking — [Zid help (intercom)](https://intercom.help/zid/ar/articles/9545470-%D8%A7%D9%84%D8%B1%D8%A8%D8%B7-%D9%85%D8%B9-tiktok-pixel-%D9%88-tiktok-conversion-api)

**Shopify**
- [COMMUNITY/VENDOR-MKT] The Google & YouTube app installs GA4 gtag via Customer Events and is the easiest path, but offers no customisation and is hard to debug. GTM custom pixels are the alternative. Consent-mode integrations can silently block purchase events — [Analytics Mania](https://www.analyticsmania.com/post/how-to-install-google-analytics-4-on-shopify/); [Shopify Community thread](https://community.shopify.com/t/google-youtube-app-not-sending-purchase-events-to-ga4-after-reinstallation/660780/13)
- [VENDOR-MKT] WhatsApp apps on Shopify (2026): Zoko rated 4.9 (452 reviews) from $49.99/mo, with AI bot, cart recovery and catalog checkout. Wati rated 3.8 (122 reviews) from $69/mo — [Kanal comparison 2026](https://getkanal.com/best-shopify-apps/best-whatsapp-apps-for-shopify). Zoko bills in USD (claimed by a competitor) — [Chatarmin](https://chatarmin.com/en/blog/zoko-alternative)
- [VENDOR-MKT] Salla and Zid include mada, STC Pay, ZATCA Phase 2, Tabby and Tamara by default. Shopify typically needs apps for these — [lucidly.ae](https://lucidly.ae/blog/shopify/shopify-vs-salla)

### Inferences
- For a'mie's Snap-heavy Saudi paid mix, Salla's Snap Business Extension (pixel, catalog and CAPI in one) is as good as or simpler than Shopify's equivalent. Meta and TikTok CAPI exist on both.
- Retention is where Shopify wins clearly. Klaviyo on Shopify (first-party integration, from prior knowledge, not re-verified this session) gives full event sync, flows and abandoned cart. On Salla, a'mie would rely on Salla-native abandoned-cart tools, Rasi or other WhatsApp apps, or the paid Scalera bridge.
- Analytics access (a Zid pain): Shopify's Customer Events and web pixels plus a GTM custom pixel give the brand control of its own GA4 ecommerce stream. Salla's GA4 depth was not established.

### Gaps
- Salla GA4 ecommerce (native vs app, server-side or not) and GTM support: not found.
- Shopify native Snapchat and TikTok app CAPI details for KSA, and the Meta channel catalog: no official doc retrieved.
- Product reviews with photos on Salla: no native photo-review feature found. Shopify relies on apps (Judge.me, Loox and others; not researched).
- Influencer coupon attribution on each platform; LetsBot integrations (the LetsBot MCP connector failed to connect in this session).
- Klaviyo availability and data residency for KSA customers: not researched.

## 3. Developer / AI: APIs, webhooks, app stores, headless, MCP

### Takeaway
Shopify is far ahead on developer surface: Storefront API, Hydrogen headless, Dev MCP, a Storefront MCP endpoint on every store, and the Sidekick admin AI. These come with 2026 churn around the Universal Commerce Protocol (UCP). Salla has a documented Merchant API v2 with webhooks and Twilight themes. Webhooks are plan-gated. I found no official public Salla MCP announcement on the web, but a "Salla store assistant" MCP connector is live in this Claude environment, as are Zid and Shopify connectors.

### Cited Findings
- [OFFICIAL] Salla Merchant API v2 webhooks: subscribe, update, list, list events and unsubscribe. New webhooks default to v2 — [docs.salla.dev Register Webhook](https://docs.salla.dev/5394134e0); [Webhooks overview](https://docs.salla.dev/841782f0). App lifecycle events come via the Partners portal — [App Events](https://docs.salla.dev/421413m0)
- [OFFICIAL] Salla store-level webhooks are available on Pro and Special plans only, with a limit of 10 (disabled ones count) — [Salla help: webhooks](https://help.salla.sa/en/article/sending-notifications-to-external-services-via-webhooks/fzsikgjw2m8dfm8j5ep2ez4e)
- [OFFICIAL] Salla docs cite a 60,000+ store reach for App Store developers. A third-party catalog says 80,000+ (conflict) — [docs.salla.dev](https://docs.salla.dev/); [apis.io](https://apis.io/providers/salla/). No Salla App Store app count was found.
- [COMMUNITY] The only Salla MCP found on the web is a community template (placeholder "your-username" repo, MIT) with product, order and customer tools — [LobeHub listing](https://lobehub.com/en/mcp/your-username-salla-mcp-server)
- [VENDOR-MKT] Zid MCP via Zapier and viaSocket (third party) — [Zapier Zid MCP](https://zapier.com/mcp/zid); [viaSocket](https://viasocket.com/mcp/zid)
- [VENDOR-MKT; conflicting details] Shopify Storefront MCP endpoint at `https://{shop}.myshopify.com/api/mcp`, reportedly GA in early 2026. Catalog and cart tooling is moving to the Universal Commerce Protocol, with one source citing a June 15, 2026 cutover for the old catalog endpoint. Dev MCP is a local docs and GraphQL validation server. The AI Toolkit was reportedly open-sourced (MIT) on 2026-04-09. Sidekick is the admin AI — [chatarmin 2026](https://chatarmin.com/en/blog/mcp-servers-e-commerce); [stellagent 2026](https://stellagent.ai/insights/shopify-ai-agentic-commerce-strategy); [claudefa.st](https://claudefa.st/blog/tools/mcp-extensions/shopify-ai-toolkit); [revize](https://revize.app/blog/shopify-mcp-developer-guide-2026). **Unverified against shopify.dev**, which could not be fetched.

### Inferences
- **First-hand observation (this session, 2026-10-29, no URL):** the Claude environment has connected MCP servers for (a) Zid (`zid_*` tools: orders, products, reports, store, plus manage tools with plan_id confirmation), (b) a "Salla store assistant" server whose tools cover orders, products and variants, customers, reports (sales, affiliates, conversion funnel, rating sentiment), and Store Design (theme versions, homepage components, landing pages, menus), and (c) Shopify (GraphQL query and mutation, analytics query, products). So all three platforms are reachable by AI agents today. Whether the Salla and Zid connectors are vendor-official could not be confirmed from public sources. The Salla connector notably exposes theme and landing-page editing, which the Zid connector here does not by default.
- For a'mie's agent workflow (this repo), Shopify's GraphQL Admin API and MCP give the richest programmatic SEO control (handles, SEO fields, redirects and metafields via API). Separately, the Zid "category API resets SEO title" issue should be tested on any platform before bulk edits.
- Headless (Hydrogen and the Storefront API) is a real Shopify option but is overkill for a'mie at its current stage. No Salla headless storefront offering was found.

### Gaps
- Salla App Store size and Shopify App Store size (2026): no numbers retrieved.
- Official status of Salla and Zid MCP connectors; Salla AI features (any "Salla AI" or assistant announcements).
- Shopify API rate limits and plan gating relevant to a'mie: not researched.

## 4. Known merchant complaints / limitations (2025–2026)

### Takeaway
Few independent 2025–2026 complaint sources surfaced. On Shopify, the documented gripes are fixed URL paths, parameter duplicates, apps needed for local payments and e-invoicing, USD billing, and AI/MCP spec churn. On Salla, they are less granular SEO control, Klaviyo without abandoned-cart sync, plan-gated webhooks, a smaller app ecosystem and weaker server-side event control. Most comparisons are vendor or agency content.

### Cited Findings
- [VENDOR-MKT] Salla: smaller app ecosystem; SEO lacks granular controls — [h-haboubi 2026](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/); [isnaad 2026](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison)
- [VENDOR-MKT] Salla: less room for deduplication and custom or profit-based conversion values — [AdGrow](https://adgrow.ae/blog/salla-zid-shopify-paid-ads-saudi-arabia/)
- [OFFICIAL] Salla: Klaviyo has no abandoned-cart sync — [Salla help](https://help.salla.sa/en/article/connecting-klaviyo-for-email-and-sms/uyfoc8mncs9wylzuyikvi4qe). Webhooks are limited to Pro and Special plans, 10 max — [Salla help](https://help.salla.sa/en/article/sending-notifications-to-external-services-via-webhooks/fzsikgjw2m8dfm8j5ep2ez4e)
- [VENDOR-MKT] Shopify: fixed URL structure and parameter duplicates — [1digitalagency](https://www.1digitalagency.com/blog/shopify-s-biggest-seo-limitations-and-how-to-work-around-each-one-34494/). [COMMUNITY] Shopify: GA4 purchase events failing after app reinstall or consent issues — [Shopify Community](https://community.shopify.com/t/google-youtube-app-not-sending-purchase-events-to-ga4-after-reinstallation/660780/13). Non-Latin redirect bug — [Shopify Community](https://community.shopify.com/t/issue-with-url-encoding-of-cyrillic-characters-in-shopify-url-redirects/240533)
- [VENDOR-MKT] Market share conflict in KSA: one source has Salla leading (citing ECDB); another has Shopify at 38%, WooCommerce 24% and Salla 18% — summarised from [h-haboubi](https://h-haboubi.com/blog/others/best-ecommerce-platform-saudi-arabia/) and [ibrahimsyouri](https://ibrahimsyouri.com/insights/ecommerce-platforms-saudi-arabia-2026/) (attribution between the two was not confirmed in the snippet)
- [VENDOR-MKT] About 4,480 live Shopify stores in Saudi Arabia — [StoreLeads](https://storeleads.app/reports/shopify/SA/top-stores)

### Inferences
- Net for a growth-focused bilingual DTC beauty brand: Shopify fixes Zid's analytics-access and international-SEO-architecture problems with documented tools, at the cost of apps for local payments and e-invoicing and USD app spend. Salla is a lower-friction Saudi-native move with strong Snap/TikTok/Meta wiring. Its fit on the specific Zid SEO pains (locale duplicates, trailing slashes, redirects) **remains unverified**, so it should be validated with a crawl of live Salla stores and written answers from Salla support before committing.

### Gaps
- Independent merchant reviews (Trustpilot, Reddit, X) of Salla and Shopify from 2025–2026: not retrieved.
- Salla outage and support-quality complaints: not researched.
- Whether Salla has the Zid-style "category update resets SEO title" behaviour: unknown.
