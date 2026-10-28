# a'mie: new paid-social ad drafts (8 concepts)

_Drafted 2026-10-28 by paid-media-creative-strategist. Status: **DRAFT, not reviewed.** Next step is `amie-reviewer`, then human approval. Nothing here is published or uploaded to any ad account or to Zid._

---

## 0. Read this first

### What the last 14 days tell us (to 27 Oct 2026, figures from the brief)

| Platform | Winner | Spend | Purchases | ROAS | CPA (spend / purchases) |
|---|---|---|---|---|---|
| TikTok (SAR) | Hair care - UGC - 1 | 672 | 17 | 6.3 | 39.5 SAR |
| TikTok (SAR) | اللمعة - UGC - 2 (glow) | 473 | 19 | 10.7 | 24.9 SAR |
| Snapchat (USD) | Collection-Frame (catalog) | 59 | 23 | 24 | 2.57 USD |
| Snapchat (USD) | Scrub IMG | 95 | 12 | 12 | 7.9 USD |
| Snapchat (USD) | Lavender collection IMG | 56 | 10 | MISSING | 5.6 USD |
| Snapchat (USD) | Chocolate highlighter | 38 | 8 | MISSING | 4.75 USD |
| Meta (USD) | SingleVideo-07 (cold, broad F) | 291 | 11 | 3.4 | 26.5 USD |
| Meta (USD) | Carousel Ad (catalog) | 302 | 9 | 2.9 | 33.6 USD |

Patterns behind these concepts:
1. Creator UGC wins on TikTok (hair and glow). Glow converts at lower CPA than hair.
2. Catalog and collection formats win on Snap and hold up on Meta. Static single-image PDP ads lose on Meta (Summer Set, Hair Set: ROAS 0.8 to 2.0). This draft has **no static single-image PDP ads**.
3. Snap scrub and Lavender ads work in a season with dry skin (Oct to Feb, per product-marketing.md). Body care gets two concepts.
4. Paid-social traffic converts poorly on PDPs. Most concepts land on a **category** page. The two that land on a PDP are sets (Into The Glow, Chocolate Highlighter Set), and each has a landing test written into its hypothesis.

### Constraints applied
- Summer Set: not advertised (retired). No tan products at all, since the season is over.
- Highlighter singles (Marshmallow / Chocolate): not advertised. Only the **highlighter sets** and **Into The Glow** are.
- Out of stock per the CRO data export (`research/cro-2026-10/data/zid_product_pages.csv`), so not used: Lip Plump, Hand Cream, Red Cherry, Signature Gift Box, Hand & Foot Set.
- No discount code. product-marketing.md lists no active code. ND96 and SUMMER26 are expired, and creator code G10 belongs to one creator, so it is not used here.
- No COD, no competitor names, no "افضل/الأول/الأكثر", no therapeutic or safety-absolute wording, no internal numbers (orders, ranks) in copy.
- Allowed proof points used: "مسجّلة في هيئة الغذاء والدواء" and "صنع في السعودية" (verified 2026-10-22). Registration numbers: MISSING, so none are quoted.
- Prices appear in only two concepts. Each one is marked **verify on Zid before launch** (rule in product-facts.md section 8).

### Landing URLs
URLs come from repo data (`research/cro-2026-10/data/zid_product_pages.csv`, `content/categories/categories-seo-geo.json`). They are **not** in product-marketing.md, so every one is marked "repo, verify live". They have no trailing slash and no `/ar-eg/` or other locale prefix. Arabic slugs must be percent-encoded when pasted into ad managers. Check that each one returns 200 in incognito mobile before launch (see `content/zid-prompts/05-check-live-ad-links.txt`).

| Key | URL | Status |
|---|---|---|
| CAT-HAIR | https://amie-sa.com/categories/1411716/العناية-بالشعر | repo, verify live |
| CAT-BODY | https://amie-sa.com/categories/977204/العناية-بالجسم | repo, verify live |
| CAT-FRAG | https://amie-sa.com/categories/977207/العطور | repo, verify live |
| CAT-GLOW | https://amie-sa.com/categories/1759672/لمعة-الجسم | repo, verify live. Shows highlighter singles until they are hidden |
| PDP-ITG | https://amie-sa.com/products/into-the-glow-collection | repo, verify live |
| PDP-CHOC-SET | https://amie-sa.com/products/amie-chocolate-body-highlighter-set | repo, verify live |

UTMs: `utm_source={meta|tiktok|snapchat}&utm_medium=cpc&utm_campaign={theme}-2026-11&utm_content={ad name}`. Use each platform's dynamic macros for utm_content where available. Ad names follow `{CREATIVE-ID}_{PRODUCT}_{FORMAT}_{RATIO}_{ANGLE}_{HOOK}_{CREATOR}_V{N}`.

### Measurement rules (apply to every hypothesis)
- Decision window: 14 days, or 30 purchases per arm, whichever comes first. Below 15 purchases per arm the result is "inconclusive", whatever the ROAS says. These are proposed decision rules, not data.
- Primary metric: platform-reported purchase ROAS. Cross-check against Zid orders with matching UTMs.
- Tracking caveat: the GA4 export shows **0 add-to-carts for Into The Glow** against 319 units sold (May to Oct). GA4 cannot judge PDP-ITG. Use platform purchases plus Zid orders. Flag to `paid-media-tracking-specialist`.
- Benchmarks are the same-platform winners in the table above, over the same 14-day window length.

---

## META (Reels / Feed)

### M1: Hair Wax, "baby hairs, no heat" UGC Reel
- **Platform / format:** Meta, single video (Reels + Feed + Stories), 9:16 master, 4:5 crop for Feed. Creator UGC, run as a partnership ad if the creator allows.
- **Product:** Hair Wax 30 ml + Sleek Brush (Hair Set shown as the bundle option on the category page).
- **Landing:** CAT-HAIR (repo, verify live)
- **Ad name:** `M1_HAIRWAX_VID_9x16_NOHEAT_AFTERGYM_{CREATOR}_V1`
- **Hook (0 to 2 s):** Close-up of front hairline with baby hairs standing up after taking off a gym cap or abaya shayla. Creator on camera: "شعري بعد النادي… شوفي."
- **On-screen text:**
  1. (0 to 2 s) شعر يطير بعد النادي؟
  2. (3 to 8 s) واكس ستيك + فرشاة سليك
  3. (9 to 15 s) بدون حرارة
  4. (end card) شمع العسل + زيت اللوز الحلو
- **Script / visual brief (20 to 25 s):**
  - 0 to 2 s: hook above, raw phone footage, natural light.
  - 3 to 8 s: twist the wax stick up, swipe once along the hairline, then the Sleek Brush (curved side) smooths it back. Close-up of the bristles.
  - 9 to 15 s: side-by-side of the hairline before and after, same light, same angle, no filter.
  - 16 to 20 s: creator says "سريع بعد الشاور أو النادي، ومافيه سشوار." Then she drops the wax in her bag.
  - 21 to 25 s: end card with product, logo, "صنع في السعودية".
- **Primary text (AR):**
  > شعرك الصغير يطير بعد الشاور أو النادي؟
  > مرّة وحدة بواكس a'mie الستيك، وبعدها فرشاة سليك، وتطلعين بشعر مرتب وأملس بدون حرارة.
  > فيه شمع العسل وزيت اللوز الحلو، وحجمه يدخل الشنطة.
  > صنع في السعودية ومسجّل في هيئة الغذاء والدواء.
- **Headline (≤40):** شعر مرتب بدون حرارة (19 chars). EN: Neat hair, no heat
- **Description (optional):** واكس + فرشاة سليك
- **CTA:** Shop Now / تسوّقي الآن
- **Test hypothesis:** A creator UGC Reel built on the hair angle that won on TikTok will beat Meta's best current ad. **Metric:** purchase ROAS. **Comparison:** M1 vs SingleVideo-07, same broad-female cold ad set, 50/50 budget. **Expected direction:** M1 ROAS ≥ 3.4 and CPA ≤ 26.5 USD. **Falsified if:** M1 ROAS < 3.4 at ≥ 15 purchases. That would mean the hair UGC win does not carry over to Meta.
- **Creator brief:** use B1 below.

### M2: Body mists "which scent is yours", catalog carousel
- **Platform / format:** Meta Advantage+ catalog ad, carousel. Card 1 is a 4:5 video intro, cards 2 to 4 are the catalog product set "Fragrance" (Natura, Flora, a'musk).
- **Product:** Natura Body Mist 150 ml, Flora Body Mist 150 ml, a'musk 15 ml.
- **Landing:** CAT-FRAG (repo, verify live). Catalog cards deep-link to their own product, which is the catalog default.
- **Ad name:** `M2_MISTS_CAROUSEL_4x5_SCENTFINDER_3WAYS_BRAND_V1`
- **Hook (0 to 2 s, intro card video):** Three bottles side by side, a hand hovers, then picks one. Text: "وش ريحتك؟"
- **On-screen text (per card):**
  - Card 1 (intro): وش ريحتك؟ دافية، زهرية، ولا مسك ناعم
  - Card 2 Natura: دافية: فانيليا وجوز هند وتونكا
  - Card 3 Flora: زهرية: حمضيات وأزهار بيضاء ومسك
  - Card 4 a'musk: مسك ناعم بلمسة يلانغ يلانغ، حجم الشنطة
- **Visual brief:** Smoky-white background, black and silver props, one mood ingredient per card (vanilla pod / white flowers / soft fabric). Real bottle shots, no renders of products that do not exist.
- **Primary text (AR):**
  > ثلاث روائح، اختاري اللي تشبهك:
  > ناتورا، دافية بالفانيليا وجوز الهند.
  > فلورا، زهرية منعشة بلمسة حمضيات ومسك.
  > مسك a'mie، ناعم وأنثوي ويدخل شنطتك.
  > وبتغليف فخم جاهز للإهداء.
- **Headline (≤40):** اختاري ريحتك: ناتورا، فلورا أو مسك (34 chars). EN: Pick your scent
- **Prices (optional, verify on Zid before launch):** a'musk 99 ر.س · Natura / Flora 129 ر.س each. The catalog pulls the live price, so leave prices out of the text.
- **CTA:** Shop Now / تسوّقي الآن
- **Test hypothesis:** A scent-led catalog carousel with a choice hook beats the generic catalog carousel. **Metric:** purchase ROAS (secondary: outbound CTR). **Comparison:** M2 vs the existing "Carousel Ad" catalog, same audience, 50/50. **Expected direction:** M2 ROAS > 2.9 and outbound CTR higher than Carousel Ad. **Falsified if:** M2 ROAS ≤ 2.9 at ≥ 15 purchases.
- **Note:** a'musk's product page slug and SEO say "oil" while the how-to says "spray" (CRO data). Copy here says only "مسك", without oil or spray, until that is fixed.

### M3: Winter body-care routine, Collection (Instant Experience)
- **Platform / format:** Meta Collection ad. 9:16 video cover above 4 catalog tiles (Lavender Set, Lemongrass Set, Lemongrass Sea Salt Scrub, Lavender Whipped Body Butter). Instant Experience template: "Storefront".
- **Product:** Sea Salt Body Scrub (Lavender / Lemongrass) and Whipped Body Butter, plus their sets.
- **Landing:** Instant Experience, then CAT-BODY (repo, verify live) as the "see all" destination.
- **Ad name:** `M3_BODYSETS_COLLECTION_9x16_WINTERDRY_TEXTURE_BRAND_V1`
- **Hook (0 to 2 s):** Macro shot of a finger scooping the salt scrub, then the whipped butter swirled into a peak. No voice, ASMR sound.
- **On-screen text:**
  1. (0 to 2 s) جفاف الشتاء بدأ
  2. (3 to 6 s) الخطوة 1: سكراب ملح البحر
  3. (7 to 10 s) الخطوة 2: زبدة مخفوقة خفيفة
  4. (end) لافندر أو ليمون قراس؟
  5. Small legal line on any Lavender scrub frame: يحتوي على قشور مكسرات
- **Visual brief (12 to 15 s):** Bathroom shelf in soft light, then scrub on a wet arm (no skin "results" claims, only the texture), rinse, then butter melting into skin on a forearm. End on both scents side by side.
- **Primary text (AR):**
  > روتين الشتاء في خطوتين:
  > سكراب بملح البحر وزبدة الشيا والمانجو للتقشير، وبعده زبدة جسم مخفوقة خفيفة تمتص بسرعة بدون إحساس دهني.
  > اختاري رائحتك: لافندر أو ليمون قراس، أو خذي المجموعة كاملة.
  > ملاحظة: سكراب اللافندر يحتوي على قشور مكسرات.
- **Headline (≤40):** روتين الشتاء لبشرة أنعم (23 chars). EN: Winter routine for softer skin
- **CTA:** Shop Now / تسوّقي الآن
- **Test hypothesis:** Body care in a collection format on Meta can repeat Snap's collection result in the dry-skin season. **Metric:** purchase ROAS. **Comparison:** M3 vs the static single-image PDP ads it replaces (Summer Set / Hair Set, ROAS 0.8 to 2.0 over the last 14 days). The bar is the top of that range. **Expected direction:** M3 ROAS > 2.0. **Stretch:** ≥ 2.9, which matches Carousel Ad. **Falsified if:** M3 ROAS ≤ 2.0 at ≥ 15 purchases.
- **Data note:** Lavender scrub size reads "300 مل" on the sheet and "300 جرام" on Zid (unresolved). No size appears in this ad.

---

## TIKTOK (UGC / Spark Ads)

### T1: Hair Wax "3 situations" UGC (iteration of Hair care - UGC - 1)
- **Platform / format:** TikTok in-feed, Spark Ad on the creator's organic post, 9:16, 15 to 20 s.
- **Product:** Hair Wax 30 ml + Sleek Brush.
- **Landing:** CAT-HAIR (repo, verify live)
- **Ad name:** `T1_HAIRWAX_UGC_9x16_3MOMENTS_DAWAM_{CREATOR}_V1`
- **Hook (0 to 2 s):** Creator in car mirror, hairline frizzy: "الساعة ٧ وعندي دوام، وشعري كذا؟"
- **On-screen text:**
  1. الدوام ٧ الصبح
  2. بعد النادي
  3. قبل طلعة العشا
  4. نفس الواكس، ثواني وخلاص
- **Script:**
  - 0 to 2 s: hook (car mirror).
  - 3 to 7 s: "الدوام": one swipe of wax, then Sleek Brush, done in the car.
  - 8 to 12 s: "بعد النادي": sweaty hairline, same two steps.
  - 13 to 17 s: "قبل العشا": slick back bun, brush tail used for the parting.
  - 18 to 20 s: holds stick to camera: "بدون حرارة، وحجمه يدخل الشنطة."
- **Primary text / caption (AR):** شعري الصغير مرتب في كل مشوار، بدون سشوار ولا حرارة. واكس a'mie + فرشاة سليك.
- **Display name:** a'mie ايمي
- **CTA:** Shop now
- **Test hypothesis:** A "multi-situation" structure beats the original single-demo hair UGC. **Metric:** purchase ROAS (secondary: 2-second view rate). **Comparison:** T1 vs Hair care - UGC - 1, same ad group, equal budget. **Expected direction:** T1 ROAS > 6.3 and CPA < 39.5 SAR. **Falsified if:** T1 ROAS ≤ 6.3 at ≥ 15 purchases. In that case keep the original structure and refresh only the hook.
- **Creator brief:** B1.

### T2: Into The Glow GRWM for an evening occasion (iteration of اللمعة - UGC - 2)
- **Platform / format:** TikTok Spark Ad, 9:16, 20 to 30 s, get-ready-with-me.
- **Product:** Into The Glow Collection. Assumed to be the "glow box" in the brief. **Mapping UNVERIFIED**, so confirm with the team. Box contents are **MISSING** from the fact files, so the ad shows the box as received and does not list contents in text.
- **Landing:** PDP-ITG (repo, verify live). It is a set, and it is the URL already used in the influencer link.
- **Stock flag:** Marshmallow shade variant had 41 units in the CRO export. Confirm stock before scaling, or have the creator feature the Chocolate shade.
- **Ad name:** `T2_INTOTHEGLOW_UGC_9x16_GRWM_EVENING_{CREATOR}_V1`
- **Hook (0 to 2 s):** Creator opens the box toward camera, then a quick cut to a shimmering collarbone under a ring light: "لمعة المناسبة، من البوكس هذا."
- **On-screen text:**
  1. تجهزي معي لمناسبة الليلة
  2. لمعة على الترقوة والكتف
  3. من أول تمريرة
  4. Into The Glow من a'mie
- **Script:**
  - 0 to 2 s: hook.
  - 3 to 10 s: unbox. Show the packaging (black / silver look). Show each item as it actually is, no voice-over listing ingredients.
  - 11 to 20 s: apply highlighter stick on collarbone, shoulders, and shin, then blend with the makeup brush. Turn under light to show the shine.
  - 21 to 27 s: outfit on, walk past window light: "تبين لمعة واضحة وناعمة."
  - 28 to 30 s: box on the dresser, logo.
- **Primary text / caption (AR):** لمعة للمناسبات من أول تمريرة، على الترقوة والكتوف والرجلين. بوكس Into The Glow من a'mie، جاهز لك أو هدية لصاحبتك.
- **CTA:** Shop now
- **Test hypothesis:** An occasion GRWM framing beats the current glow UGC. **Metric:** purchase ROAS. **Comparison:** T2 vs اللمعة - UGC - 2, same ad group, equal budget. **Expected direction:** T2 ROAS > 10.7. **Falsified if:** T2 ROAS ≤ 10.7 at ≥ 15 purchases.
  - **Landing sub-test (run after the creative test):** T2 to PDP-ITG vs T2 to CAT-GLOW. CAT-GLOW only qualifies once the highlighter singles are hidden. **Metric:** purchases per landing-page view (platform). **Expected direction:** CAT-GLOW higher, given that paid-social traffic converts poorly on PDPs. **Falsified if:** PDP-ITG is equal or higher at ≥ 15 purchases per arm.
- **Creator brief:** B2.

### T3: Body mists "my 3 scents" UGC
- **Platform / format:** TikTok Spark Ad, 9:16, 15 to 25 s.
- **Product:** Natura, Flora, a'musk. Lead with Natura (top revenue scent). Flora is the fastest-growing, so it gets the second slot.
- **Landing:** CAT-FRAG (repo, verify live)
- **Ad name:** `T3_MISTS_UGC_9x16_3SCENTS_MOODS_{CREATOR}_V1`
- **Hook (0 to 2 s):** Creator sprays into the air and walks through it: "كل واحد يسألني وش ريحتك… هذي هي."
- **On-screen text:**
  1. وش ريحتك؟
  2. ناتورا: للمساء، دافية
  3. فلورا: للصبح والدوام
  4. مسك a'mie: في الشنطة دايم
- **Script:**
  - 0 to 2 s: hook.
  - 3 to 9 s: Natura sprayed on hair and neck, evening outfit: "فانيليا وجوز هند، ريحتها دافية."
  - 10 to 16 s: Flora, morning, office bag: "زهرية منعشة فيها حمضيات."
  - 17 to 22 s: a'musk out of the handbag: "مسك ناعم، صغير ويدخل أي شنطة."
  - 23 to 25 s: three bottles lined up: "أي وحدة تبين؟"
- **Primary text / caption (AR):** ثلاث روائح لثلاث أوقات: ناتورا للمساء، فلورا للصبح، ومسك a'mie للشنطة. أي وحدة تشبهك؟
- **CTA:** Shop now
- **Test hypothesis:** Fragrance UGC can match the hair UGC benchmark on TikTok. **Metric:** purchase ROAS. **Comparison:** T3 vs Hair care - UGC - 1 over a 14-day window of the same length. **Expected direction:** T3 ROAS ≥ 6.3. **Falsified if:** T3 ROAS < 6.3 at ≥ 15 purchases. In that case fragrance stays in catalog formats (M2) and leaves UGC.
- **Creator brief:** B3.

---

## SNAPCHAT (9:16)

### S1: Winter scrub Collection (builds on Scrub IMG + Collection-Frame)
- **Platform / format:** Snapchat Collection Ad. 9:16 hero (image or 6 s video) plus 4 catalog product tiles: Lemongrass Sea Salt Scrub, Lavender scrub, Lavender Set, Lemongrass Set.
- **Product:** Sea Salt Body Scrub (both scents) and body-care sets.
- **Landing:** CAT-BODY (repo, verify live). Tiles deep-link to their products.
- **Ad name:** `S1_SCRUB_COLLECTION_9x16_WINTERDRY_SALTMACRO_BRAND_V1`
- **Hook (0 to 2 s):** Macro of salt grains in the jar, a finger scoops a mound toward camera.
- **On-screen text:**
  1. موسم الجفاف بدأ
  2. سكراب بملح البحر وزبدة الشيا والمانجو
  3. لافندر أو ليمون قراس
  4. Small line on Lavender tile and frame: يحتوي على قشور مكسرات
- **Visual brief:** Same visual DNA as Scrub IMG (product-forward, bold texture), now in a collection layout because Collection-Frame was the top Snap ad. Smoky-white set, lavender sprig / lemongrass stalk props. Brand name "a'mie" small top-left. Text inside safe zones (top 150 px and bottom 300 px clear on 1080×1920).
- **Brand name / headline (≤34):** سكراب ملح البحر لشتاء أنعم (26 chars). EN: Sea salt scrub for a softer winter
- **Primary text (where shown) (AR):** حبيبات ملح البحر للتقشير، وزبدة الشيا والمانجو لنعومة بعد الشاور. اختاري لافندر أو ليمون قراس.
- **CTA:** Shop Now / تسوّقي
- **Test hypothesis:** Putting the winning scrub creative inside the winning collection format beats the scrub single image. **Metric:** purchase ROAS (secondary: CPA). **Comparison:** S1 vs Scrub IMG, same ad squad, equal budget. **Expected direction:** S1 ROAS > 12 and CPA < 7.9 USD. **Falsified if:** S1 ROAS ≤ 12 at ≥ 15 purchases.

### S2: Chocolate Highlighter SET, bronze swipe (replaces the hidden single)
- **Platform / format:** Snapchat single video, 9:16, 6 to 8 s, no voice, trending audio.
- **Product:** Chocolate Body Highlighter Set (highlighter + makeup brush). The single is being hidden, so the ad promotes the set only.
- **Landing:** PDP-CHOC-SET, https://amie-sa.com/products/amie-chocolate-body-highlighter-set, no trailing slash (repo, verify live). The live Meta link in `05-check-live-ad-links.txt` (#04) has a trailing slash. Do not copy it.
- **Ad name:** `S2_CHOCSET_VID_9x16_SWIPE_COLLARBONE_BRAND_V1`
- **Hook (0 to 2 s):** One swipe of the bronze stick across the collarbone, then the hand turns the shoulder into the light so the shimmer catches.
- **On-screen text:**
  1. تمريرة وحدة
  2. لمعة برونزية على الترقوة
  3. الستيك + فرشاة الميك أب
  4. (optional, verify on Zid before launch) 99 ر.س
- **Visual brief:** 0 to 2 s swipe. 3 to 5 s brush blends the edge. 6 to 8 s the set (stick + brush) on a dark silver surface. Show warm-to-deep skin tones on at least one shot. Text inside Snap safe zones.
- **Brand name / headline (≤34):** لمعة برونزية من أول تمريرة (26 chars). EN: Bronze glow from the first swipe
- **Primary text (AR):** هايلايتر الجسم تشوكلت مع فرشاة الميك أب: لمعة برونزية من أول تمريرة، بزبدة الشيا والكاكاو. للترقوة والكتوف واليدين.
- **CTA:** Shop Now / تسوّقي
- **Test hypothesis:** Selling the set as a video keeps the efficiency of the single-product image. **Metric:** CPA (secondary: ROAS). **Comparison:** S2 vs "Chocolate highlighter" (38 USD / 8 purchases = 4.75 USD CPA). **Expected direction:** S2 CPA ≤ 4.75 USD. The set is priced higher than the single (99 vs 79 ر.س, verify on Zid), so ROAS per order should also rise. **Falsified if:** S2 CPA > 4.75 USD at ≥ 15 purchases.

---

## Creator briefs (UGC concepts)

### B1: Hair Wax + Sleek Brush (for M1 and T1)
- **Who:** Saudi woman 18 to 35 with visible baby hairs or flyaways, natural hair texture, everyday look (office, gym, student).
- **Show:** the real problem first (frizz after a gym cap, shayla, or shower). Then one swipe of wax and one pass of the Sleek Brush, in one continuous take where possible. Before/after in the same light and angle, with no filter or smoothing apps.
- **Say (your own words, Saudi dialect):** no heat, quick after the shower or gym, fits in the bag, beeswax and sweet almond oil.
- **Do not say:** "آمن", "خالي من…", "علاج", "يقوّي/ينبت الشعر", "الأفضل/الأشهر", any price comparison, any other brand's name, any discount code (unless the a'mie team gives you one in writing), anything about payment on delivery.
- **Deliver:** 2 versions (car-mirror hook and gym hook), 9:16, 15 to 25 s, raw plus edited, no burned-in captions on the raw cut. Native-language captions file separately.

### B2: Into The Glow (for T2)
- **Who:** woman 18 to 35 who gets ready for evening occasions (weddings, gatherings). Feature at least one warm or deep skin tone.
- **Show:** an honest unboxing (show only what is in the box, and do not describe contents we haven't confirmed). Then apply on collarbone, shoulders, and legs, blend with the brush, and turn under one light source so the shimmer reads on camera.
- **Say:** shine from the first swipe, soft not loud, works for an occasion, gift-ready box.
- **Do not say:** "يوحّد اللون", "تفتيح", "آمن", any sun or tan claim, "الأول/الأفضل", other brands, codes, COD.
- **Deliver:** 1 GRWM cut 20 to 30 s plus one 8 s collarbone close-up for reuse on Snap. 9:16, raw plus edited.

### B3: Body mists (for T3)
- **Who:** woman 24 to 40, day-to-evening lifestyle (office, outings).
- **Show:** each scent in its moment: Natura in the evening, Flora in the morning, a'musk from the handbag. Spray on body (hair only for Natura and a'musk, the two confirmed for hair; Flora hair use is UNVERIFIED). The bottle label must be readable for at least 1 second each.
- **Say:** the notes as written on the product (Natura: vanilla, coconut, tonka. Flora: citrus, white flowers, musk. a'musk: musk, ylang-ylang). Personal feeling ("أحبها للمساء") is fine. Do not invent longevity hours.
- **Do not say:** "يدوم ٢٤ ساعة" or any number, "علاج عطري", "يريّح الأعصاب", "مثل عطر [brand]", other brands, codes, COD.
- **Deliver:** 15 to 25 s, 9:16, raw plus edited, plus 3 separate 5 s clips (one per scent) for catalog intro cards (M2).

---

## Open items / MISSING (for reviewer and team)
1. "Glow box" = Into The Glow Collection? UNVERIFIED. Into The Glow box contents: MISSING.
2. All landing URLs come from repo data. Check each live (200, Arabic, in stock) before launch.
3. Highlighter singles must be hidden before CAT-GLOW is used as a landing page.
4. Prices (99 / 129 / 99 ر.س) need checking on Zid before they go in any creative.
5. ROAS for Snap "Lavender collection IMG" and "Chocolate highlighter": MISSING (only spend and purchases given).
6. SingleVideo-07 creative content (product, hook) is MISSING, so M1 is benchmarked on results only.
7. Into The Glow GA4 add-to-cart tracking reads 0. Refer to `paid-media-tracking-specialist`.
8. SFDA certificate or registration numbers: MISSING. Copy uses the plain statement only.
