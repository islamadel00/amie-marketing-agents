# Bilingual (Arabic + English) Product Naming for Saudi Beauty E-commerce, and the SEO Impact of Product Titles

Research notes, 2026-10-22. Market: Saudi Arabia / Gulf, Arabic-first, women 24–45. Brand: a'mie (ايمي), Zid store amie-sa.com, possible Shopify move.

**Method note (important for the report writer):** direct page fetching was blocked in this session (the proxy refused support.google.com, developers.google.com, nahdionline.com). Findings come from web-search result snippets/summaries of those pages plus one live Semrush query (Saudi database). Retailer title examples are quoted from search-result titles/URLs, which normally mirror the page's product title. Where I could not verify official wording on the live page, I say so.

---

## 1. E-commerce product-title best practices for SEO (structure, length, front-loading, stuffing; Google Merchant Center guidance)

### Takeaway
Google's own guidance is: one descriptive, unique title per product, built as **Brand + Product type + key attributes (+ variant/size)**, with the most important words in the **first ~70 characters** (150 is the hard limit in Merchant Center), no promotional text, no keyword stuffing. Amazon has tightened even further, reportedly to 75 characters from July 2026.

### Cited Findings
- Merchant Center `title` is capped at **150 characters**; the title is used to match the product to a shopper's search — [Google Merchant Center: Product data specification](https://support.google.com/merchants/answer/7052112?hl=en); [Google Merchant Center: Title [title] and structured title](https://support.google.com/merchants/answer/6324415?hl=en)
- Google: shoppers typically see only the **first ~70 characters** depending on screen size. Google "strongly encourages" 70 or fewer and recommends putting key details first, especially ones not visible in the image, because titles are truncated in most ad formats — [Google Merchant Center: Tips to optimize your product data](https://support.google.com/merchants/answer/7380908?hl=en); [Title [title]](https://support.google.com/merchants/answer/6324415?hl=en)
- Google's recommended pattern (apparel guide) is **Brand + Product Type + Other Important Attributes**, with the most important details in the first 70 characters — [Google Merchant Center: Best practices for clothing and accessories](https://support.google.com/merchants/answer/7348545?hl=en)
- For a product with variants, Google's **item group title** should be shorter and more generic than the variant titles and leave out variant details such as size and colour. That means variant titles carry the shade/size and the parent title does not — [Google Merchant Center: Item group title [item_group_title]](https://support.google.com/merchants/answer/17085146)
- Google offers a separate `structured_title` attribute that must be used when a title was generated with generative AI — [Title [title] and structured title](https://support.google.com/merchants/answer/6324415?hl=en)
- Merchant Center also has a `short_title` attribute for formats with limited space — [Google Merchant Center: Short title [short_title]](https://support.google.com/merchants/answer/11551083?hl=en-GB)
- Practitioner pattern for health & beauty titles: **Brand + product type + key ingredient/formula + size/count**. This is a third-party recommendation, not a Google rule — [GMC Suspension guide 2026](https://www.gmcsuspension.com/google-merchant-center-product-title-best-practices.html); [FeedArmy title optimization](https://feedarmy.com/kb/google-shopping-title-attribute-optimization-google-merchant-center/)
- Titles with promotional text (e.g. "free shipping", "best price") or a repeated store name risk disapproval or automatic rewrites (third-party summary of Google policy) — [Store Growers: GMC feed attributes 2026](https://www.storegrowers.com/google-merchant-center-feed-attributes/)
- Google Search (page `<title>`/title links): give every page a unique, descriptive, concise title, **avoid keyword stuffing**, and avoid boilerplate repeated across the site. Brand can be appended, and Google says it is "not necessary for every page" — [Google Search Central: Influencing title links](https://developers.google.com/search/docs/appearance/title-link); [Search Engine Journal coverage](https://www.searchenginejournal.com/google-title-links/422926/)
- Google's SEO Starter Guide repeats that there is no benefit to repeating the same words or phrases multiple times — [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- Title-tag length rules of thumb are about 50–60 characters / ~600 px on desktop. This is third-party advice, not an official Google limit — [Scalenut 2026](https://www.scalenut.com/blogs/meta-title-length-best-practices-2026)
- **Amazon:** from 21 Jan 2025, titles were limited to **200 characters** for most categories, banned characters were `! $ ? _ { } ^ ¬ ¦` unless part of the brand, and the same word could not be repeated more than twice (prepositions/articles excepted) — [Search Engine Land](https://searchengineland.com/amazon-title-policy-update-2025-450485); [Amazon Seller Forums announcement](https://sellercentral.amazon.com/seller-forums/discussions/t/b2b15728-0d43-453e-974f-59eb63f73059)
- **Amazon (single-source):** since 27 Jul 2026, titles in all categories except Media are reportedly limited to **75 characters**, with extra detail moved to "item highlights" (≤125 chars) and over-limit titles gradually replaced by AI-generated ones. I found only one detailed source for this, so it needs verification on Seller Central — [Amalytix](https://www.amalytix.com/en/knowledge/seo/amazon-product-title/)

### Inferences
- A single "master title" of ≤70 characters per language would satisfy Google Shopping, the store `<title>`, and the new Amazon limit together. Extra keywords (benefits, synonyms) belong in the description, the SEO meta title/description, and the alt text.
- For a'mie, the brand token "ايمي" / "a'mie" is short. Put it first in feeds (Brand field + title), but it does not need repeating inside every on-page H1 if the theme already shows the brand.
- For variant products (e.g. Body Highlighter Marshmallow / Chocolate), use a generic parent title (`ايمي هايلايتر الجسم ستيك`) with the shade on the variant (`… مارشميلو` / `… شوكولاتة`), matching Google's item-group logic.

### Gaps
- I could not open Google's Health & Beauty-specific title guidance, if a separate page exists. The search surfaced only the apparel guide and generic tips.
- The Amazon 75-character rule is single-sourced.

---

## 2. Arabic specifics: transliteration vs translation, brand spelling, spelling variants, size, feminine language

### Takeaway
Saudi/Gulf retailers do **both**: they transliterate signature English names into Arabic script (e.g. "إنتو ذا نايت", "بوم بوم", "ماسك ثيرابي") and put a translated generic product type next to them (معطر جسم، كريم، لوشن). Search demand sits overwhelmingly on the generic Arabic type word (سكراب، معطر جسم، تان، هايلايتر، مسك الطهارة), not on English or on literal synonyms. Semrush's Saudi data merges hamza/taa-marbuta/ال-لل variants into one volume, so pick one clean spelling and use it consistently.

### Cited Findings — real Saudi/Gulf retailer patterns for signature names
- Golden Scent (Saudi): **"باث آند بودي وركس إنتو ذا نايت فاين معطر جسم - 236 مل"**. The brand and the signature name "Into The Night" are both transliterated into Arabic script, followed by a translated type ("معطر جسم") and the size. This is the closest analogue to "Into The Glow" → **"إنتو ذا جلو"** — [Golden Scent](https://www.goldenscent.com/p/bath-body-works-into-the-night-fine-body-mist-for-women)
- Amazon.sa, by contrast, *translated* another Bath & Body Works scent name: "A Thousand Wishes" → **"ألف أمنية"**. Both approaches exist in-market — [Amazon.sa search results](https://www.amazon.sa/bath-and-body-works/s?k=bath+and+body+works&page=2)
- Faces (Saudi): **"انيشيو كريم الجسم ماسك ثيرابي"**. The brand (Initio) and signature name (Musk Therapy) are transliterated, and the type is translated ("كريم الجسم") — [Faces.sa](https://www.faces.sa/ar/p/initio-musk-therapy-128317328848.html)
- Nahdi (Saudi): **"سول دي جانيرو كريم بوم بوم البرازيلي 75مل"** (brand + type + transliterated signature name + size) — [Nahdi Sol de Janeiro brand page](https://www.nahdionline.com/ar-sa/plp/sol-de-janeiro)
- Nahdi: **"ناتيورا سايبريكا سكراب الجسم المنعش 370 مل"** (brand transliterated + "سكراب الجسم" + attribute + size), with English URL slug `natura-siberica-reviving-body-scrub-370-ml` — [Nahdi product page](https://www.nahdionline.com/ar-sa/natura-siberica-reviving-body-scrub-370-ml/pdp/101259628)
- Niceone (Saudi): **"كريم بوم بوم البرازيلي من سول دي جانيرو - 240مل"**. The type and name come first and the brand follows after "من" — [Niceone](https://niceonesa.com/en/care-body-care-body-moisturizer-sol-de-janeiro-brazilian-bum-bum-cream-240ml-n26749)
- Sephora Middle East (Arabic): **"كريم بوم ديا لتفتيح البشرة"** (type + transliterated name + benefit, with no brand and no size in the title) — [Sephora.me](https://www.sephora.me/qa-ar/p/%D9%83%D8%B1%D9%8A%D9%85-%D8%A8%D9%88%D9%85-%D8%AF%D9%8A%D8%A7-%D9%84%D8%AA%D9%81%D8%AA%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D8%A9/P10016788)
- Ananinja (Saudi): "سول دي جانيرو كريم بوم بوم البرازيلي 75 مل" — [Ananinja](https://ananinja.com/sa/ar/product/sol-de-janeiro-brazilian-bum-bum-cream-75-ml-1-19359929)
- Clarins (Gulf, Arabic) fully translates the type instead of transliterating: "لوشن حليبي للتسمير الذاتي" — [Clarins AE](https://ae.clarins.com/ar/%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA-%D9%84%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D8%A8%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D8%A9/%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA-%D8%A7%D9%84%D8%B9%D9%86%D8%A7%D9%8A%D8%A9-%D9%85%D9%86-%D8%A7%D9%84%D8%B4%D9%85%D8%B3/%D9%85%D8%B3%D8%AA%D8%AD%D8%B6%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%AA%D8%B3%D9%85%D9%8A%D8%B1-%D8%A7%D9%84%D8%B0%D8%A7%D8%AA%D9%8A-430/%D9%84%D9%88%D8%B4%D9%86-%D8%A7%D9%84%D8%AA%D8%B3%D9%85%D9%8A%D8%B1-%D8%A7%D9%84%D8%B0%D8%A7%D8%AA%D9%8A-%D8%A8%D8%A7%D9%84%D8%AD%D9%84%D9%8A%D8%A8-CS01706069.html)
- Care-outlet: "سوبري تان - لوشن تسمير الجسم تشيري بومب 235 مل" (brand – type – transliterated scent name – size) — [Care Outlet](https://care-outlet.com/products/supre-tan-cherry-bomb-body-tanning-lotion-235ml)
- Negative example, Amazon.ae Arabic machine-style keyword stuffing: "دوف لوشن تسمير البشرة بالتدريج من سمر ريفايفيد متوسط الى داكن للحصول على لوشن تسمير الجسم ذاتي التوهج للشمس لجميع انواع البشرة، 200 مل (عبوة من قطعة واحدة)". It repeats "لوشن تسمير" and runs to roughly 150+ characters — [Amazon.ae](https://www.amazon.ae/-/ar/%D8%AF%D9%88%D9%81-%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D8%A9-%D8%A8%D8%A7%D9%84%D8%AA%D8%AF%D8%B1%D9%8A%D8%AC-%D8%B1%D9%8A%D9%81%D8%A7%D9%8A%D9%81%D9%8A%D8%AF-%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D8%A9%D8%8C/dp/B0152X4GQS)
- Abdul Samad Al Qurashi (Saudi fragrance house) uses a plain Arabic descriptive name: "مسك الجسم الأبيض" — [ASQ](https://sa.abdulsamadalqurashi.com/en/%D9%85%D8%B3%D9%83-%D8%A7%D9%84%D8%AC%D8%B3%D9%85-%D8%A7%D9%84%D8%A3%D8%A8%D9%8A%D8%B6/p1493022486)
- Spelling drift in the wild for one product type (Memwa body mist, Egypt-heavy results): "بادي ميست", "بادى مست", "بادي سبلاش", "معطر الجسم", "مسك الطهاره" vs "مسك الطهارة" all appear across retailers. Without a house style, the same product fragments into many spellings — [Veela Beauty](https://veelabeauty.com/en/memwa-musk-altahara-body-mist-250ml); [Lotus Cosmetics](https://lotuscosmeticseg.com/product/%D8%A8%D8%A7%D8%AF%D9%89-%D9%85%D8%B3%D8%AA-%D8%A8%D8%B1%D8%A7%D8%A6%D8%AD%D8%A9-%D9%85%D8%B3%D9%83-%D8%A7%D9%84%D8%B7%D9%87%D8%A7%D8%B1%D8%A9-250%D9%85%D9%84-%D9%84%D9%84%D9%86%D8%B3%D8%A7%D8%A1/); [Memwa Shop](https://memwashop.com/en/product/body-mist-musk-altahara/)
- Saudi Salla/Zid stores also bracket the two terms in category names, e.g. Jumanah: "معطر جسم (بودي ميست)" — [Jumanah](https://jumanah.co/categories/1412846/%D9%85%D8%B9%D8%B7%D8%B1-%D8%AC%D8%B3%D9%85-%D8%A8%D9%88%D8%AF%D9%8A-%D9%85%D9%8A%D8%B3%D8%AA)

### Cited Findings — Saudi search volume (Semrush, database `sa`, pulled 2026-10-22, monthly volume / KD)
Source for all rows: [Semrush Keyword Overview, SA database](https://www.semrush.com/analytics/keywordoverview/?db=sa) (live API query run for these notes).

| Term group | Variant → volume |
|---|---|
| Scrub | **سكراب 74,000** · سكراب الجسم 1,600 · سكراب للجسم 1,600 · مقشر الجسم 4,400 · مقشر للجسم 4,400 · body scrub (Latin) 1,600 |
| Musk | مسك 49,500 (KD 40) · **مسك الطهارة 5,400** · مسك الطهاره 5,400 · مسك الجسم 390 |
| Body mist | **معطر جسم 5,400** · معطر الجسم 5,400 · معطر للجسم 5,400 · بودي سبلاش 390 · بودي ميست 210 · body mist (Latin) 880 · بادي ميست / بودي مست → no data |
| Highlighter | **هايلايتر 4,400** · هايلايتر الجسم 260 · هايلايتر للجسم 30 · body highlighter / شيمر للجسم → no data |
| Tan | **تان 12,100** · تان للجسم 390 · كريم تسمير 90 · تسمير 70 · self tan (Latin) 720 · تسمير ذاتي / لوشن تسمير / زيت تسمير → no data |
| Moisturiser | كريم جسم 4,400 · مرطب جسم 4,400 · زبدة الجسم 1,600 · لوشن الجسم 880 · زيت جسم 2,400 |
| Wash | غسول الجسم 9,900 · صابون جسم 3,600 · شاور جل 2,400 |
| Deodorant | مزيل عرق 60,500 · مزيل رائحة → no data |
| Brand | ايمي 2,400 · إيمي 2,400 (KD 23, mixed navigational/informational intent) · amie 480 · amie sa → no data |

- The identical volumes for ة/ه (الطهارة/الطهاره), ا/إ (ايمي/إيمي) and ال/لل (الجسم/للجسم) show that **Semrush groups these orthographic variants** into one cluster, much as Google Keyword Planner groups close variants. The tool therefore cannot tell you which spelling Saudis actually type more. — [Semrush SA data above]; consistent with practitioner advice that Google normalizes many, "but not all" Arabic variants and that Search Console should be the check — [Hady Web: Arabic SEO Saudi 2026](https://hadyweb.com/blog/arabic-seo-saudi-arabia); [Arfadia: Arabic keyword research Qatar](https://www.arfadia.com/blog/arabic-keyword-research-qatar/)
- Practitioner guides name the three main variant families: hamza on alef (أ/إ/آ vs ا), taa marbuta vs haa (ة vs ه), final ي vs ى. They advise not creating separate pages per variant when intent and SERPs overlap, and using Search Console impressions as the ground truth for Saudi typing habits — [Arfadia](https://www.arfadia.com/blog/arabic-keyword-research-qatar/); [Hady Web](https://hadyweb.com/blog/arabic-seo-saudi-arabia)
- On-site search engines often do **not** normalize Arabic variants by default (hamza, ي/ى, ك forms). This is documented as a missing feature in Discourse, for example. A store's internal search may therefore miss "مسك الطهاره" if the product says "مسك الطهارة" — [Discourse Meta](https://meta.discourse.org/t/arabic-search-normalization-missing-support-for-hamza-variants-ya-kaf-forms-and-orthographic-equivalence/384253?tl=en)
- a'mie's own context file already standardizes the brand as **"ايمي"** (no hamza) — /home/user/amie-marketing-agents/.claude/product-marketing.md (line 1, 6)

### Inferences
- **Signature names (Into The Glow, Marshmallow, Deep Tan, Red Cherry, etc.):** the dominant Saudi retailer pattern is to *transliterate* the signature name into Arabic script and attach a translated *generic type* that carries the search demand: `ايمي إنتو ذا جلو – طقم هايلايتر الجسم`. Keep the Latin original in the English title, and optionally in the Arabic description or alt text, so people who search in Latin script still match.
- **Head terms to use as the "type" word in Arabic titles** (by Saudi volume): سكراب (not مقشر, though mention مقشر in the description), معطر جسم (with بودي ميست in the description or brackets, not the reverse), تان (not تسمير; تان has about 170× the volume of تسمير), هايلايتر, مسك الطهارة (the specific variant is a 5.4k niche with low KD 10; bare مسك is 49.5k but competitive, KD 40), كريم جسم / مرطب جسم, غسول الجسم.
- **Spelling choice:** since Google and Semrush cluster ة/ه and ا/إ, choose the *correct standard* spelling (الطهارة with ة) for professionalism and apply it consistently. Add the informal variants (الطهاره, بادي ميست) only as hidden search tags or synonyms in store search, not in visible titles.
- **Brand spelling:** keep "ايمي" (matches the existing brand file). Because the query "ايمي" is ambiguous (a common female name/word), pair it with a category word in titles (`ايمي سكراب…`) and use "a'mie" in English. The bare brand query has low commercial specificity.
- **Size:** most Saudi pharmacy/marketplace titles include size at the end ("370 مل", "75مل", "- 236 مل"), while Sephora ME omits it. Include size at the end when the product comes in more than one size or for feed/marketplace titles, and use a consistent format (`200 مل`, with a space, Arabic "مل").
- **Feminine language:** none of the retailer titles above use gendered words in the *title* (e.g. "للنساء" appears only on some Egyptian sellers). Feminine address (ضعيه، استخدمي) appears in *descriptions* (e.g. Nahdi's "ضعيه على البشرة الرطبة"). So keep titles gender-neutral nouns and use feminine voice in body copy.

### Gaps
- No source gave verified click or conversion impact of transliterated vs translated signature names in Arabic.
- Semrush returned no data for several low-volume variants (بادي ميست, بودي مست, تسمير ذاتي, لوشن تسمير, شيمر للجسم, body highlighter, amie sa), so their volume is likely below Semrush's threshold. This is not confirmed as zero.
- Real Saudi typing preference between ة/ه and ا/إ can only be seen in a'mie's own Google Search Console queries, which were not accessed here.
- I could not open Boots KSA or Noon Saudi product pages for title examples.

---

## 3. How Saudi/Gulf retailers format Arabic and English product titles (examples)

### Takeaway
Three formats dominate: (a) **pharmacy/marketplace format, brand-first**: `Brand + type + name/attribute + size` (Nahdi, Ananinja, Golden Scent); (b) **type-first with "من Brand"** (Niceone, beauty-10); (c) **prestige/brand-site format**: `type + name + benefit`, no size, brand shown separately (Sephora ME, Clarins). English slugs are common even on Arabic pages (Nahdi, Faces, Golden Scent).

### Cited Findings
- Nahdi AR title + EN slug: "ناتيورا سايبريكا سكراب الجسم المنعش 370 مل" → `/ar-sa/natura-siberica-reviving-body-scrub-370-ml/pdp/101259628` — [Nahdi](https://www.nahdionline.com/ar-sa/natura-siberica-reviving-body-scrub-370-ml/pdp/101259628)
- Nahdi: "سول دي جانيرو كريم بوم بوم البرازيلي 75مل" — [Nahdi](https://www.nahdionline.com/ar-sa/plp/sol-de-janeiro)
- Niceone: "كريم بوم بوم البرازيلي من سول دي جانيرو - 240مل", with an English slug containing the category path `care-body-care-body-moisturizer-sol-de-janeiro-brazilian-bum-bum-cream-240ml-n26749` — [Niceone](https://niceonesa.com/en/care-body-care-body-moisturizer-sol-de-janeiro-brazilian-bum-bum-cream-240ml-n26749)
- Beauty-10: "كريم بوم بوم البرازيلي من سول دي جانيرو - 75مل" (Arabic slug) — [beauty-10](https://beauty-10.com/%D9%83%D8%B1%D9%8A%D9%85-%D8%A8%D9%88%D9%85-%D8%A8%D9%88%D9%85-%D8%A7%D9%84%D8%A8%D8%B1%D8%A7%D8%B2%D9%8A%D9%84%D9%8A-%D9%85%D9%86-%D8%B3%D9%88%D9%84-%D8%AF%D9%8A-%D8%AC%D8%A7%D9%86%D9%8A%D8%B1%D9%88)
- Golden Scent: "باث آند بودي وركس إنتو ذا نايت فاين معطر جسم - 236 مل", English slug `bath-body-works-into-the-night-fine-body-mist-for-women` — [Golden Scent](https://www.goldenscent.com/p/bath-body-works-into-the-night-fine-body-mist-for-women)
- Faces: "انيشيو كريم الجسم ماسك ثيرابي", English slug `initio-musk-therapy` — [Faces](https://www.faces.sa/ar/p/initio-musk-therapy-128317328848.html). Faces' Arabic category pages use the head term "سكراب للجسم ومقشرات" (combining both words) — [Faces category](https://www.faces.sa/ar/body-scrub-exfoliant)
- Sephora ME: "كريم بوم ديا لتفتيح البشرة" (Arabic slug, no brand or size) — [Sephora.me](https://www.sephora.me/qa-ar/p/%D9%83%D8%B1%D9%8A%D9%85-%D8%A8%D9%88%D9%85-%D8%AF%D9%8A%D8%A7-%D9%84%D8%AA%D9%81%D8%AA%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%B4%D8%B1%D8%A9/P10016788)
- Amazon.sa English listing example: "Bath & Body Works Japanese Cherry Blossom Fine Fragrance Mist, 236ml" (Brand + name + type, size) — [Amazon.sa](https://www.amazon.sa/bath-and-body-works/s?k=bath+and+body+works&page=2)
- The Body Shop KSA Arabic category for body mists is "افضل عطور الجسم" at `/fragrance/body-mists` — [The Body Shop SA](https://www.thebodyshop.com.sa/east/ar/fragrance/body-mists)
- Local Saudi/Gulf small stores often use type + scent in Arabic only, e.g. "بودي ميست مسك" — [Alwaleef](https://alwaleef.com/en/products/%D8%A8%D9%88%D8%AF%D9%8A-%D9%85%D9%8A%D8%B3%D8%AA-%D9%85%D8%B3%D9%83)

### Inferences
- For a brand selling only its own products (a'mie), the "brand-first" pharmacy format is the right template for **marketplace/feed** titles (Noon, Amazon.sa, Google Shopping), where the brand must be visible. On the **own store**, a cleaner "type + signature name" format (Sephora style) is acceptable because the brand is already in the logo and `<title>`, but the brand should still be in the SEO title.
- A practical a'mie template:
  - AR: `ايمي | [نوع المنتج بالعربي] [الاسم المميز بحروف عربية] [الصفة/الرائحة] [الحجم]` → e.g. `ايمي سكراب الجسم ريد تشيري 250 مل`
  - EN: `a'mie [Signature Name] [Product Type] – [Shade/Scent], [Size]` → e.g. `a'mie Red Cherry Body Scrub, 250 ml`
- The English slug should mirror the English title (Nahdi/Golden Scent pattern), even for the Arabic page.

### Gaps
- No Boots KSA, Noon.sa or local Saudi body-care DTC brand (Zid/Salla) product-title examples were verified beyond those listed.
- I found no data on whether brand-first or type-first ordering ranks better in Arabic Google results.

---

## 4. URL slugs: renaming on Zid/Shopify, English slug best practice, 301 redirects

### Takeaway
Google prefers short, readable, hyphen-separated slugs, and non-ASCII (Arabic) characters must be percent-encoded. That is why most big Gulf retailers use **English slugs even on Arabic pages**. On Shopify, changing a handle creates a 301 **only if** "Create a URL redirect" is ticked. On Zid, the repo's own rules state that renaming changes the URL, so do not rename live products; set the slug and SEO fields instead.

### Cited Findings
- Google supports URLs per IETF STD 66. Reserved and non-ASCII characters must be percent-encoded (older wording: UTF-8 encoded). Separating words (hyphens preferred over underscores) is recommended — [Google Search Central: URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure); [SERoundtable on the 2025 update](https://www.seroundtable.com/google-url-structure-guidelines-supported-characters-35747.html)
- Shopify: editing a product/collection/page handle shows a **"Create a URL redirect"** checkbox, and the old URL is 301-redirected only if it is ticked. Shopify's built-in redirect tool makes only 301s. Missing redirects can be added under Online Store/Content → URL Redirects — [Tiny-img Shopify redirects guide](https://tiny-img.com/blog/shopify-redirects/); [ShopCircle 2026 guide](https://shopcircle.co/blogs/news/shopify-url-handle-changes-redirects-guide)
- Shopify (staff, community): adding a translated URL handle creates a 301, but **changing an already-translated handle does not auto-create a redirect**, which matters for an Arabic + English Shopify store — [Shopify Community](https://community.shopify.com/t/301-redirects-in-shopify-url-translations/283759)
- Shopify community case: after URL changes, old URLs redirected to the homepage instead of the matching product. The fix is per-URL 301s (old → exact new page) — [Shopify Community](https://community.shopify.com/t/404-pages-after-an-seo-app-after-changing-url/334975)
- Zid: product/page SEO fields (page title, meta description, URL) are editable per product. Guides recommend descriptive keyword slugs instead of numeric defaults. This comes from third-party guides; the official help center confirms SEO fields for brand pages — [Zid Help: brands](https://help.zid.sa/catalog-brands/); [Webskeet Zid SEO guide](https://webskeet.com/ar/blog/zid-seo-guide); [Dane Al Salloum Zid SEO 2026](https://danealsalloum.com/zid-store-seo-guide-2026/)
- Internal repo rules (a'mie): "Renaming a category or product in Zid changes its URL — don't rename." "Updating a category description through the Zid API resets its SEO title… set SEO titles last." Take a backup before bulk edits — /home/user/amie-marketing-agents/CLAUDE.md

### Inferences
- **On Zid now:** change the *display name* only if the URL impact is accepted. Otherwise improve the SEO title, meta description and description, and leave names and URLs alone. If a rename is approved, record old URL → new URL and check whether Zid offers a redirect. I found no source confirming Zid auto-redirects on rename (see Gaps).
- **On a Shopify migration:** this is the one moment to fix names and slugs cleanly. Map every old Zid URL to its new Shopify handle and bulk-import 301s (Shopify redirect CSV). Set English handles like `red-cherry-body-scrub`, and decide once on translated Arabic handles. Avoid editing translated handles later, because those changes don't auto-redirect.
- Use English, lowercase, hyphenated slugs without brand or size unless needed to separate variants, e.g. `into-the-glow-body-highlighter-set`. Arabic slugs become long percent-encoded strings when shared.

### Gaps
- I could not confirm whether Zid creates automatic 301s when a product name or slug changes. The official help-center article on product URLs was not reachable, and the CLAUDE.md rule implies it does not.
- No source on Zid URL format for Arabic vs English storefronts.

---

## 5. Do product names affect AI search / GEO (entity consistency)?

### Takeaway
GEO guidance consistently recommends identical product and brand naming across site, schema, marketplaces and social, because inconsistent names cause "entity confusion". The evidence is mostly from vendor blogs, and direct proof that consistency drives citations is thin, though the advice is low-cost and aligns with Google's structured-data and Merchant Center practices.

### Cited Findings
- "Entity confusion" happens when search engines/LLMs find mixed versions of a brand's or product's name and can't tell which facts belong together. Keep name, product data and descriptions consistent across website, schema, review platforms and directories — [LSEO: brand consistency in AI answers](https://lseo.com/generative-engine-optimization/brand-consistency-across-the-web-reducing-entity-confusion-in-ai-answers/)
- When multiple sources use the same product names, retrieval systems can cluster information more effectively. Use the same product terminology on every channel — [Fuel Online: brand entity optimization](https://fuelonline.com/ai-seo-geo/how-llms-choose-which-brands-to-recommend-the-complete-brand-entity-optimization-guide/); [Yotpo: LLM optimization](https://www.yotpo.com/blog/llm-optimization/)
- Inconsistent social bios are a warning sign for unclear entity signals. Match name and description across website, Google Business Profile, social profiles and directories — [LSEO](https://lseo.com/generative-engine-optimization/brand-consistency-across-the-web-reducing-entity-confusion-in-ai-answers/); [Jeff Pastorius](https://jeffpastorius.com/blog/how-large-language-models-decide-which-brands-to-mention/)
- Academic: AI search engines favour earned (third-party) media over brand-owned content (UK iGaming study). Single-point-in-time GEO measurements are unreliable due to system variability — [arXiv 2603.12282](https://arxiv.org/pdf/2603.12282); [arXiv 2606.21595](https://arxiv.org/pdf/2606.21595)
- Caveat: the "independent sources weighted ~2:1 over brand claims" statistic circulating in GEO blogs is unsourced — [search summary of Fuel Online / Jeff Pastorius](https://fuelonline.com/ai-seo-geo/how-llms-choose-which-brands-to-recommend-the-complete-brand-entity-optimization-guide/)

### Inferences
- For a'mie: lock one canonical bilingual name per product (e.g. `a'mie Into The Glow Body Highlighter Set` / `ايمي إنتو ذا جلو طقم هايلايتر الجسم`) and reuse it verbatim in Zid/Shopify titles, Product schema `name` + `brand`, Google Merchant feed, Noon/Amazon listings, TikTok/Instagram shop catalogues, influencer briefs and ad naming. Today, names like "Glow Set", "Body Glow" and "Into The Glow" (from the top-seller list in product-marketing.md) are close enough to be confused. A naming tree should make each one clearly distinct.
- Always pairing the signature name with the generic type ("Deep Tan" + "تان للجسم") helps both LLMs and Google map the entity to the category query ("أفضل تان للجسم").

### Gaps
- I found no study measuring product-name consistency against AI citation rates. The evidence is practitioner consensus only.
- I found no Arabic-specific GEO research, e.g. whether LLMs link "إنتو ذا جلو" and "Into The Glow" as one entity.
