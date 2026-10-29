# Migration paths, risks and support: Zid → Salla, Zid → Shopify, or staying on Zid (KSA, as of Oct 2026)

Research date: 2026-10-29. Method note: WebFetch could not reach any source in this session (partners.salla.com, help.zid.sa, codilar.sa and magnetoitsolutions.com all failed DNS resolution in the sandbox), so every finding below comes from search-engine result summaries, not full page reads. Treat figures as "reported by source X". Unless a date is given, items are undated or the date is the publication year shown in the source title. Many sources are agencies selling migration services, and they are flagged as such.

## 1. Migration tools and services: what data moves

### Takeaway
No source showed a turnkey "Zid → Salla" or "Zid → Shopify" connector from LitExtension or Cart2Cart. Salla runs its own "move to Salla from other platforms" programme with terms and benefits for eligible merchants. Zid → Shopify is done by agencies or by CSV/API export plus Matrixify. Under every path, customer passwords and SEO URLs do not carry over, and theme, payments, shipping and discount logic have to be rebuilt.

### Cited Findings
- Salla publishes terms for a "store transfer from other platforms to Salla" service (شروط وأحكام خدمة انتقال المتاجر من منصات أخرى إلى منصة سلة). The search summary says benefits go to *eligible* merchants and include a free theme, and that Salla may offer a custom deal or delivery method after its technical team assesses the store. I could not read the full eligibility or scope (page not fetchable). — [Salla Partners legal](https://partners.salla.com/legal/%D8%B4%D8%B1%D9%88%D8%B7-%D9%88%D8%A3%D8%AD%D9%83%D8%A7%D9%85-%D8%AE%D8%AF%D9%85%D8%A9-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84-%D8%A7%D9%84%D9%85%D8%AA%D8%A7%D8%AC%D8%B1-%D9%85%D9%86-%D9%85%D9%86%D8%B5%D8%A7%D8%AA-%D8%A3%D8%AE%D8%B1%D9%89-%D8%A5%D9%84%D9%89-%D9%85%D9%86%D8%B5%D8%A9-%D8%B3%D9%84%D8%A9)
- Salla's merchant services marketplace has a "move your store" (نقل متجرك) category of paid services, mostly from independent providers. — [Salla services](https://salla.com/services/list/1414105111)
- Third-party sellers offer "free upload of 500 products with store transfer" deals that exclude platform, domain and theme fees. — [salatips](https://salatips.com/ar/%D9%85%D8%AA%D8%AC%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%B3%D9%84%D8%A9/p2134151325); [Khamsat listing](https://khamsat.com/programming/woocommerce-development/3276578-%D9%86%D9%82%D9%84-%D9%88%D8%A7%D8%B6%D8%A7%D9%81%D8%A9-%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA-%D9%85%D9%86-%D9%85%D9%86%D8%B5%D8%A9-%D8%B3%D9%84%D9%87-%D9%88-%D8%B2%D8%AF-%D8%A7%D9%84%D9%89-%D9%85%D8%AA%D8%AC%D8%B1%D9%83-%D8%B9%D9%84%D9%89-%D9%88%D9%88%D8%B1%D8%AF%D8%A8%D8%B1%D9%8A%D8%B3)
- Zid has a help article on moving *from Salla to Zid* (the reverse direction), and its site has "Switch to Zid: ZID x Salla / ZID x Shopify" pages. Both platforms compete to win merchants over. — [Zid help: transfer from Salla to Zid](https://help.zid.sa/transfer-from-salla-to-zid/); [Zid Safeer / solutions](https://zid.sa/en/safeer)
- Zapier and Anchanto offer ongoing Zid↔Salla sync (orders, inventory), not one-off migration. That is useful for a hybrid setup. — [Zapier Salla–Zid](https://zapier.com/apps/salla/integrations/zid); [Anchanto Apr 2023](https://anchanto.com/anchanto-integrations-update-april-2023/)
- LitExtension (Shopify app "LE – Store Migration & Import") claims 140+ source platforms plus CSV/Excel/DB, and migrates products, customers, orders, categories, reviews, multi-language content and gift cards, with a free demo of up to 200 entities. Zid was **not** confirmed as a named source in the excerpts. — [Shopify App Store: LE](https://apps.shopify.com/litextension-shopify-migration-app); [LitExtension](https://litextension.com/de/shopify-migration.html)
- Cart2Cart's general entity list covers products, images, variants, categories, customers, orders, coupons, reviews, blog posts, CMS pages and multi-language. Cart2Cart **does not migrate SEO data (product/category URLs)**, and some entities have to be moved manually. Zid/Salla support was not confirmed. — [Cart2Cart: data entities](https://www.shopping-cart-migration.com/migration-guides/5998-store-data-not-available-for-migration); [Cart2Cart FAQ](https://www.shopping-cart-migration.com/faq/specific-shopping-cart-questions)
- Passwords: Matrixify says no platform lets you export real customer passwords. Imported Shopify customers start inactive and have to be invited (set "Send Account Activation Email" = TRUE on import, or send bulk invites later). — [Matrixify tutorial](https://matrixify.app/tutorials/migrate-customers-new-shopify-store-activate-new-accounts/); [Shopify Community](https://community.shopify.com/t/new-shopify-store-adding-existing-customers/302316)
- Merchants worry that bulk account invites could be flagged as spam and hurt the sending domain. The thread ended without a workaround. — [Shopify Community](https://community.shopify.com/t/new-shopify-store-adding-existing-customers/302316/2)
- Zid → Shopify guides list storefront design, Arabic RTL layout, payment gateways, shipping rules and custom discount logic as things to **rebuild**. They also list mada, STC Pay, Tabby, Tamara and ZATCA as KSA-specific setup items. Customers have to reset passwords on first login. — [Codilar: Zid to Shopify](https://www.codilar.com/blog/zid-to-shopify-migration/); [Magneto IT (agency)](https://magnetoitsolutions.com/sa/blog/migrate-salla-zid-shopify)
- Zid data access paths: third-party Zid↔Odoo connectors sync products, orders and customers, which shows API access to these entities exists. — [Odoo app: ZID connector](https://apps.odoo.com/apps/modules/17.0/sh_zid_connector); [bi_zid_odoo_connector](https://apps.odoo.com/apps/modules/17.0/bi_zid_odoo_connector)
- Zid's developer platform added a Blogs API in July 2026 (41 endpoints: settings, categories, posts, tags), which makes blog content exportable through the API. — [Zid developer blog](https://zid.sa/en/partners/developers/blog/); [Zid dev updates](https://zid.sa/en/partners/developers/blog/category/updates/)

### Inferences
- For a'mie (50–100 SKUs), products, variants, images and categories are a small, low-risk move by CSV and API. The real work is the URL redirect map, theme and RTL rebuild, payments, and re-inviting customers.
- The Zid MCP connected to this workspace can list products, categories, customers, orders, reviews, coupons and blog/pages. That makes a full JSON backup before any move feasible without third-party tools (inference from tool scope, not from a web source).
- Reviews, loyalty points, gift cards and store credit are the entities most likely to be lost. Plan to export them separately and re-import them with an app, or retire them with customer notice.

### Gaps
- Zid's native CSV export scope (products/customers/orders) on help.zid.sa could not be read. Search did not return the article.
- Whether LitExtension or Cart2Cart officially list Zid or Salla as source or target is unconfirmed.
- Eligibility, timeline and lock-in conditions in Salla's migration-service terms (for example a required plan or commitment period) could not be read.
- Loyalty points, gift cards and wallet balance portability: no source found.

## 2. SEO migration: slugs, 301s, domain, GSC, traffic dip

### Takeaway
Google treats a platform change on the same domain as a site move with URL changes. Every old URL needs a one-to-one 301, redirects should stay for at least 180 days (ideally a year), and some fluctuation is expected. No published Saudi recovery data was found. Shopify forces `/products/` and `/collections/` prefixes and stores non-Latin handles as percent-encoded strings. Salla's redirect tooling could not be confirmed from an official source.

### Cited Findings
- Google: a move is processed only after Googlebot has visited every old and new URL. There is no fixed timeline, and it can take several months, with important URLs processed sooner. Combining a move with URL or content redesign "will probably" cause some traffic loss while Google reassesses pages. — [Google Search Central: site move with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes); [Google: what is a site move](https://developers.google.com/search/docs/advanced/crawling/what-is-site-move)
- Keep redirects for **at least 180 days**, longer if Google still sends traffic to them. — [Google Change of Address tool help](https://support.google.com/webmasters/answer/9370220?hl=en). Search Engine Land recommends one year. — [Search Engine Land](https://searchengineland.com/url-changes-is-not-so-simple-for-google-search-378648)
- Note: the Change of Address tool is for *domain* changes. If amie-sa.com stays the domain, only the URL-level 301s apply (inference from Google's tool scope above).
- Older reporting: Google said it takes "a couple of weeks for things to smooth out", but competitive terms may lag (old, low weight). — [Search Engine Watch](https://searchenginewatch.com/?p=10479)
- Shopify supports bulk redirect import by CSV (Online Store > Navigation > URL redirects > Import). — [Shopify Help: URL redirects](https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect)
- Redirects for multilingual Shopify stores must include the locale path (for example `/fr/collections/...`) (third-party app blog). — [ShopCircle](https://shopcircle.co/blogs/news/bulk-redirects-for-multilingual-shopify-sites)
- Non-Latin (Cyrillic) Shopify handles become long percent-encoded strings. A vendor sells transliteration plus 301 tooling. The same likely applies to Arabic, but this is **unverified for Arabic**. — [htmlBurger (vendor)](https://htmlburger.com/blog/cyro-shopify-app/)
- Saudi agency guides call full Salla/Zid → Shopify 301 mapping "non-negotiable" and warn that skipping it loses "three to six months" of search equity (agency claim). — [Codilar SA (agency)](https://www.codilar.sa/blog/salla-to-shopify-migration-the-saudi-merchants-guide-in-2026)
- Arabic migration best practice: export all old URLs, map page to page, import redirects **before** launch, submit the new sitemap, and monitor GSC for 90 days. Don't redirect everything to the homepage, and return 404/410 for retired products. Old collections, articles, brand pages and indexed images are easy to forget. — [Snaabble](https://snaabble.com/blog/migrate-store-to-custom-system); [esafqa](https://esafqa.com/blog/alhifaz-ala-tartib-google-ind-naql-almatjar/)
- Zid and Shopify URL formats differ, so every product, collection and blog URL needs a 301 before go-live, or Google treats the old URLs as deleted. — [Codilar: Zid to Shopify](https://www.codilar.com/blog/zid-to-shopify-migration/)

### Inferences
- a'mie's Zid locale-prefixed duplicates (for example `/ar-eg/...`, plus trailing-slash variants) multiply the redirect map. Each indexed variant needs its own 301 to the single canonical new URL. Pull the full indexed URL list from GSC (Pages report) and a crawl, not just the product list.
- Moving to Shopify means Arabic slugs survive only as percent-encoded handles under fixed `/products/` and `/collections/` prefixes. Every URL changes, which is the riskiest SEO scenario. Moving to Salla also changes URLs, since Salla uses its own product URL scheme with IDs (unverified, no official source found).
- Keeping the domain (amie-sa.com) and only re-pointing DNS avoids a domain move. GSC property and history stay, and no Change of Address is needed.

### Gaps
- No Salla official doc on custom 301 redirects or slug control was found.
- No Zid doc was found on fixing locale duplicates (`/ar-eg/`) or trailing slashes.
- No measured traffic-dip and recovery case data for Saudi Zid/Salla/Shopify migrations was found (only agency assertions).

## 3. Pixels, catalogs and ad-account disruption

### Takeaway
Merchant Center is the main risk. Platform or domain changes have triggered "misrepresentation" suspensions in documented merchant threads, and changing product IDs sends items back through review (up to about 5 business days). No source quantified Meta, Snap or TikTok learning-phase effects after a migration.

### Cited Findings
- A merchant moving BigCommerce → Shopify was suspended for misrepresentation shortly after and cleared by re-verifying. A later primary-domain change triggered a second suspension that two review requests did not lift (forum, anecdotal). — [Shopify Community](https://community.shopify.com/t/changed-domain-name-and-google-suspension-for-misrepresentation/338503)
- Changing product IDs makes Google treat products as new and re-review them (up to 5 business days). Large data changes also trigger review. Keep IDs and feed data stable, and edit the scheduled-fetch URL rather than recreating the feed. — [FeedArmy](https://feedarmy.com/kb/migrating-feeds-in-google-merchant-center/)
- Advice: re-verify the website in GMC before switching, and keep both domains active for a while (community). — [Shopify Community: rebranding & GMC](https://community.shopify.com/t/rebranding-impact-on-google-merchant-centre/369540)
- The Content API for Shopping was reported to shut down on 18 Aug 2026, so programmatic feeds must use the Merchant API (secondary source, July 2026). — [Digital Applied](https://www.digitalapplied.com/blog/google-merchant-center-drops-next-rename-2026)

### Inferences
- Preserve SKU and product IDs as the GMC/Meta `id` across platforms where possible. A Shopify-native feed app may emit `shopify_SA_<productid>_<variantid>` IDs, which would reset product history (unverified, check the chosen feed app).
- Expect conversion-event gaps during cutover. Run old and new pixels in parallel on a staging domain, and switch campaigns to the new events before DNS cutover.

### Gaps
- Meta, Snap and TikTok learning-phase and attribution impact after a store-platform switch: no source found.
- Salla and Shopify native catalog-sync behaviour for Snap and TikTok in KSA: not researched to primary sources.

## 4. Timelines, costs (SAR) and who can help in KSA

### Takeaway
Agency sources quote 4–8 weeks for Salla/Zid → Shopify, and that range is aimed at larger catalogs. A 50–100 SKU store is plausibly 2–4 weeks (inference). Costs range widely, from SAR 3,000–8,000 for a theme-based Shopify build to SAR 25,000+ for a quoted "Zid → Shopify migration". Salla is far cheaper to run: about SAR 990–2,990 a year, versus Shopify's plan plus gateway surcharge plus apps. KSA Shopify Plus partners found are Dubai-based. Salla has its own migration programme and services marketplace.

### Cited Findings
- Timeline: 4–8 weeks for Salla → Shopify, including payments, ZATCA, RTL and redirects. Another estimate puts a 1,000–2,000 SKU store at 4–8 weeks plus 30 days of stabilisation (agency). — [Codilar SA](https://www.codilar.sa/blog/salla-to-shopify-migration-the-saudi-merchants-guide-in-2026)
- Zid → Shopify migration quoted at **SAR 25,000–250,000** depending on catalog and custom work (agency, likely enterprise-skewed). — [Codilar AE: Zid to Shopify](https://www.codilar.ae/blog/zid-to-shopify-migration)
- Shopify build in KSA: SAR 3,000–8,000 for a standard theme store, SAR 15,000–40,000 for a custom bilingual store with ZATCA. Retainers SAR 1,500–5,000 per month (agency). — [RedRock SA](https://www.redrock.com.sa/blog/shopify-development-saudi-arabia-complete-guide/)
- Shopify Payments is **not available in Saudi Arabia** (Oct 2026 guides). Merchants use Moyasar, PayTabs, HyperPay or Tap. Shopify adds a third-party gateway surcharge of about 2% (Basic), 1% (Shopify) or 0.5% (Advanced). — [Oneonic 2026](https://oneonic.com/shopify-for-saudi-arabia/); [Byblos Horizon](https://bybloshorizon.com/blog/zid-to-shopify-migration-cost); [Beeps Digital](https://beepsdigital.com/blog/shopify-ecommerce-saudi-arabia/)
- Gateway apps cost about SAR 150–300 per month (agency). — [Codilar SA](https://www.codilar.sa/blog/salla-to-shopify-migration-the-saudi-merchants-guide-in-2026)
- Shopify reportedly announced improved RTL/Arabic support across admin, checkout, customer accounts and Horizon themes on 2 Oct 2026 (secondhand, **unverified**, check the Shopify changelog). — [Amwhiz 2026](https://www.amwhiz.com/blog/shopify-store-uae-saudi-arabia)
- Shopify plan prices conflict: Basic about SAR 112 per month (RedRock) vs $39 (about SAR 146) (Innovatrix); Plus from about SAR 2,250–2,300 per month. — [RedRock](https://www.redrock.com.sa/blog/shopify-development-saudi-arabia-complete-guide/); [Innovatrix](https://www.innovatrixinfotech.com/blog/salla-vs-shopify-saudi-arabia-2026)
- Salla plans (official page per search summary): Basic free, Plus about SAR 990 per year (SAR 99 per month), Pro about SAR 2,990 per year (SAR 299 per month), Special negotiated. The iOS app reportedly charges more. Some blogs quote other figures, which look unreliable. — [Salla plans](https://salla.com/en-sa/plans); [Snaabble](https://snaabble.com/en/blog/custom-store-vs-platforms)
- Shopify Plus partners serving KSA: **Creative971** (Dubai, Plus partner, 5.0 from 42 reviews, built a localized Arabic Plus store for Springfield KSA) and **The i.o agency** (Dubai, Plus partner, in the directory since Jul 2025). No Riyadh-based Plus partner surfaced. — [Shopify Plus partners: Creative971](https://www.shopify.com/plus/partners/creative971); [Shopify partner directory: the i.o agency](https://www.shopify.com/partners/directory/partner/the-i-o-agency-plus)
- Other KSA-facing Shopify agencies (self-described, partner status unverified): Codilar SA, RedRock, Oneonic, Globify, Magneto IT. — [Globify KSA](https://www.globify.ae/shopify-ksa); [Oneonic KSA](https://oneonic.com/locations/saudi-arabia/)
- Support: blogs say Salla offers 24/7 Arabic support (chat, phone, email). One comparison claims 2–4 hour response for Salla vs 2–6 hours for Zid. Sources generally rate Salla's Arabic support above Zid's. **No official statement found.** — [Isnaad](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison); [Nafas Digital](https://www.nafasdigital.com/the-difference-between-zid-and-salla/); [Truescho](https://truescho.com/en/blog/best-ecommerce-platforms-saudi-arabia)
- Salla 4.0 reportedly powers about 68,000 stores with Tap Payments (Tap blog, partner source). — [Tap blog](https://blog.tap.company/salla-4-0-saudi-ecommerce/)

### Inferences
- Rough budget for a'mie (inference, not sourced as a package):
  - Zid → Salla: SAR 0–5,000 if Salla's migration programme applies, plus the Salla plan.
  - Zid → Shopify: about SAR 8,000–25,000 for agency build, migration and redirects, plus about SAR 150–300 per month for the gateway app and a 1–2% surcharge.
- Shopify's Arabic support is mostly through partners. Shopify's own support isn't documented as Arabic-first in any source found.

### Gaps
- No itemized SAR quote for a 50–100 SKU Zid → Salla move was found.
- Salla partner agency directory and Salla migration SLA timelines were not found.
- Shopify support language and hours for KSA were not found.

## 5. Contract and lock-in

### Takeaway
Zid's terms (an older version, verify the live page) allow cancellation at any time, with access until the paid period ends. Renewal must be turned off at least 3 days before period end, and fees are non-refundable with no partial-period credit. No explicit data-export-on-exit clause was found for any of the three platforms.

### Cited Findings
- Zid terms: cancel anytime and keep service until period end; you are responsible for cancelling auto-renewal **at least 3 days before** period end; close the account via support or help@zid.sa; payments non-refundable with no partial-period credits; a separate refund path within 14 days under the return policy. Page version may be about 3+ years old. — [Zid Terms & Conditions](https://zid.sa/en/terms-conditions/)
- Salla's migration programme has its own terms. Conditions such as plan commitment could not be read. — [Salla Partners legal](https://partners.salla.com/legal/%D8%B4%D8%B1%D9%88%D8%B7-%D9%88%D8%A3%D8%AD%D9%83%D8%A7%D9%85-%D8%AE%D8%AF%D9%85%D8%A9-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84-%D8%A7%D9%84%D9%85%D8%AA%D8%A7%D8%AC%D8%B1-%D9%85%D9%86-%D9%85%D9%86%D8%B5%D8%A7%D8%AA-%D8%A3%D8%AE%D8%B1%D9%89-%D8%A5%D9%84%D9%89-%D9%85%D9%86%D8%B5%D8%A9-%D8%B3%D9%84%D8%A9)

### Inferences
- Time any move to a'mie's Zid renewal date. Run Zid and the new platform in parallel until the redirects are live, since redirects from old Zid URLs only work while DNS points at the new platform. Zid cannot serve them after cutover.

### Gaps
- Zid data-export rights after cancellation, the current (2026) Zid terms, Salla general merchant terms and Shopify KSA terms: not read.

## 6. Stay on Zid and de-risk, or run a hybrid

### Takeaway
Zid is still actively developing its platform in 2026: a new Account/Store Branding API (migration due 30 Sep 2026), a Blogs API (Jul 2026), Vitrin themes with brand templates, and an open-source AI agent skill (8 Sep 2026). No 2026 Zid Pay or Zid Ship announcements were found. Hybrid sync tools (Zapier, Anchanto, Odoo connectors) exist for running Zid alongside Salla.

### Cited Findings
- Zid is retiring `GET v1/managers/profile` (migration due 30 Sep 2026) in favour of Store Branding and Account Profile endpoints. — [Zid dev blog: Account API migration](https://zid.sa/en/partners/developers/blog/account-api-migration/)
- Blogs API released July 2026; Product Brands support in Vitrin themes (`brands.jinja`, `brand.jinja`); open-source Zid AI Agent Skill released 8 Sep 2026. — [Zid developer blog](https://zid.sa/en/partners/developers/blog/); [Zid theme docs](https://docs.zid.sa/theme-development); [Zid GitHub](https://github.com/zidsa)
- Older Twig themes are described as deprecated in favour of Vitrin (third-party agency claim). — [Filweb](https://filweb.org/zid-store-design/)
- Zid Pay is said to have no setup or monthly fee, with rates varying by network and plan (secondary, unofficial). — [Etihadfal Tech](https://etihadfaltech.com/blogs/e-commerce-solutions/zid-e-commerce-development-for-saudi-businesses-how-to-build-launch-and-scale-in-2026/)
- Commentators frame Zid as suited to stores past about 100 orders a month and Salla as the easier starting point (opinion). — [Isnaad](https://www.isnaad.ai/en/salla-vs-zid-vs-shopify-comparison)
- Salla reportedly lacks native multi-currency, multi-language and market pricing, which is a common reason to add Shopify for GCC or international sales (agency claim). — [Codilar SA](https://www.codilar.sa/blog/salla-to-shopify-migration-the-saudi-merchants-guide-in-2026)

### Inferences
- De-risk on Zid without moving:
  - Take a full API backup using the connected Zid tools.
  - Lock canonical URLs, disable or noindex unused locales (`/ar-eg/` etc.) where Zid settings allow, and fix trailing slashes through canonical tags and sitemap.
  - Keep product IDs stable for GMC.
  - Build the theme on Vitrin so the theme is not on deprecated tech.
- A hybrid works best as a *separate* channel or domain (for example a Shopify GCC store on a subdomain or ccTLD, or a Salla-hosted second storefront). It needs distinct content or hreflang to avoid duplicate-content issues with the main store. Inventory can sync via Zapier, Anchanto or Odoo.

### Gaps
- How to remove locale-prefixed duplicates and trailing-slash variants inside Zid: no official doc found. This needs testing in the Zid dashboard and theme.
- Zid Pay and Zid Ship 2026 pricing and changes: not found.
- Whether Zid lets you edit robots.txt, add custom redirects or remove locales: not confirmed.

## 7. Real case studies (Saudi/GCC brands that switched platforms)

### Takeaway
No named, verifiable Saudi or GCC brand case study of Zid ↔ Salla or Zid/Salla → Shopify migration outcomes (traffic, revenue) was found. The only concrete example is Springfield's localized Arabic Shopify Plus store for KSA, which was a new build by a retail partner, not documented as a migration from Zid or Salla.

### Cited Findings
- Springfield KSA localized Arabic Shopify Plus store built by Creative971 with a local retail partner. — [Shopify Plus partners: Creative971](https://www.shopify.com/plus/partners/creative971)
- A Shopify-vs-Salla blog cites an anonymous "Saudi beauty brand" success story (KSA + UAE), unnamed and unverifiable. — [Byblos Horizon](https://bybloshorizon.com/blog/shopify-vs-salla-vs-zid)
- Zid and Salla both market "switch to us" pages, which shows platform switching is common, but they publish no outcome data. — [Zid Safeer](https://zid.sa/en/safeer); [Zid help: Salla to Zid](https://help.zid.sa/transfer-from-salla-to-zid/)

### Inferences
- Without published Saudi outcome data, use Google's guidance (expect fluctuation for weeks to months) and treat agency "3–6 months lost if no redirects" claims as the downside case.

### Gaps
- No named case studies with before/after metrics. Merchant communities (X/Twitter Arabic threads, Salla and Zid community groups) were not reachable through search in this session.
