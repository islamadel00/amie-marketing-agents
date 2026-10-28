# Site and category architecture from search demand (amie-seo draft, pending amie-reviewer)

Non-branded: 242 clicks / 67,267 impressions (0.36%) in 29 Jul–27 Oct. Query export capped at 1,000 rows; سكراب, مسك, كريم القدمين MISSING.

Demand map: تان cluster 13,693 impr / 24 clicks / pos 7–8.5 → tan category 1436861; واكس cluster 9,411 / 16 / 11–21 → wax product; لمعة جسم 3,946 / 22 / 4.2–6.1 → category لمعة الجسم 1756504; هايلايتر الجسم 932 / 3 → same category; العناية بالجسم 1,879 / 7 / 12.4 → 977204; مرطب شفاه 441 / pos 26.9 (out of stock); البيبي هير / فرشاة سليك 415; توزيعات / بوكس هدايا 302 → 1411717.

Category tree: keep the 8 visible categories and names (no renames: same category ID already indexed under two slugs, e.g. Gifts /هدايا vs /مجموعة-الهدايا-والعروض, Tan /tanning-product vs /منتجات-التان, Perfumes /perfumes vs /العطور, Body care /body-products vs /العناية-بالجسم). Menu order by demand: التان, لمعة الجسم, العناية بالشعر, العناية بالجسم, العطور, الهدايا, المجموعات, الأكثر مبيعاً. Merge اللمعة والإشراقة 1756501 into 1756504 and hide; Tanning products (2nd) into 1436861; hide accessories 977206, Featured, Recent, Latest, Packages, منتجات مختاره, Eid gifts from menu (keep URLs). 977205 skin-care: confirm what it is. 301 redirects in Zid MISSING → hide, don't delete.

Cannibalisation: لمعة جسم (Glow Set 2,004 impr pos 4.7 vs Body Glow, /ar-om/ copy, two glow categories); العناية بالجسم (static page /pages/العناية-بالجسم 1,568 impr vs category); واكس (product vs locale copies vs blog); هايلايتر split across Chocolate + locale Marshmello copies; layering article under /blogs/ and /pages/.

Duplicate URLs: 402 of top 500 GSC pages are locale copies (~41.6k impr); shipping-and-payment for QA/LB/BH/FR 15k impr. Trailing slash (GA4): hair category 4,955 sessions/15% engaged/96 adds vs clean 3,337/91%/803; Summer Set 8,649/86 vs 11,983/1,253; tan category 1,935/15 vs 6,663/592. Fix: turn off all markets except SA (AR+EN); canonical to unprefixed, hreflang ar/en, x-default /; clean ad links.

Brand drop: branded clicks 5,662 → 2,553; homepage 3,976 → 1,577 (CTR 11.9% → 6.0%); "ايمي" CTR 9.1% → 4.95% at ~same position; "amie" 1,211 → 591, pos 7.1 → 10.5, Google shows /en/. Fixes: homepage title/meta, Arabic default, English title on /en/, disable unused markets, one spelling "a'mie ايمي", Organization schema.

Title/meta drafts (≤60 / ≤155): homepage, tan category, hair wax, Glow Set (contents to confirm), Deep Tan, body care 977204, curly-hair blog, foot cream (removes "يعالج"). Full text in the agent report; all need amie-reviewer + human approval. Zid rule: descriptions first, SEO titles last in the dashboard.
