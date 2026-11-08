# Glow Friday · Storyboard الفيديو الرئيسي (Reel / TikTok 9:16)

> **On-screen copy:** the reviewed, binding version is `onscreen-copy-reviewed.md`. Default end card has no % («أسعار خاصة على منتجات مختارة») until the MoC licence and Saleh's numbers are confirmed.

_Owner: design-visual-storyteller (campaign director) · 2026-11-08 · Status: DRAFT → amie-reviewer → human approval_
_Pipeline: storyboard → (new stills only: design-image-prompt-engineer) → Higgsfield draft 480p → amie-visual-qa → human OK → finalize 1080p → edit_

---

## 0. الملخص في سطرين
- **الفكرة:** يوم تسوّق هادي وفخم. الكاميرا بتمشي على شنط a'mie وعلب الهدايا والمنتجات، كل حاجة أبيض وأسود/محايد، واللون الوحيد هو **الشريطة الساتان العنابي «GLOW FRIDAY»**. الخصم بيظهر بس في الـ end card.
- **القاعدة الذهبية:** كل لقطة AI بتبدأ من صورة حقيقية أو معتمدة (image-to-video). الكاميرا والنور والقماش والورق هم اللي بيتحركوا، والمنتجات والإيدين ثابتين. وأي كلام أو لوجو أو خصم بيتضاف في المونتاج.

## 1. Deliverables
| # | Asset | Format | Length | Sound | Notes |
|---|---|---|---|---|---|
| D1 | Main Reel / TikTok | 9:16, 1080×1920 | 18 s (15 s MVS version) | music + SFX | 3 end-card variants: teaser / launch / last chance |
| D2 | Bumper | 9:16 (+ 1:1 crop for feed if needed) | 6 s | music sting | cut from D1 shots, no new generation |
| D3 | Web-hero loop | 9:16 mobile + 16:9 desktop | 6 s seamless | **silent** | no text baked in (site HTML adds text). Free version already exists, see §6 |

---

## 2. Inventory of the start frames (اللي موجود فعلاً وحالته)

| File | What it is | Use? |
|---|---|---|
| `content/campaigns/2026-11-glow-friday/hero/src/hero-clean-plate.png` | **Real photo**, 9:16 (720×1280): black wire basket, white a'mie boxes (Lemongrass butter, Body Glow, Hand Cream, Sleek Secret, Lip Plump), **real burgundy "GLOW FRIDAY" ribbon**, no offer text, small a'mie logo at bottom | ✅ **S2 + web-hero.** The truest asset we have |
| `hero/src/hero-plate-nologo.png` | Same plate without the logo. **Opened 2026-11-08 (prompt engineer): same photo and size, no baked logo** | ✅ **S2 start frame (replaces the clean plate, so the logo is added in the edit and cannot warp)** + end-card background |
| `hero/src/hero-original.webp` | Same photo with "20% TO 40% OFF" baked in | ❌ as a start frame (baked %). Colour reference for the ribbon only |
| `hero/glow-friday-hero-mobile-9x16-notext.mp4`, `…-desktop-16x9-notext.mp4` (+ posters) | Existing **local** 6 s motion loops from `tools/images/render_glow_hero.js` | ✅ free fallback for S2 and **already a usable D3** |
| `key-visuals/kv-convertible-real-bags.jpg` | Approved AI still, 4:5 (1792×2240): classic convertible, burgundy leather seats, real white bags with rope handles and silver logo, "GLOW FRIDAY" bag, Lemongrass jars + dry brush, Hair Wax + Sleek Secret + Sleek Brush, Body Glow | ✅ **S1 hook.** The seats are burgundy, so they match the accent |
| `key-visuals/kv-convertible-bags.jpg`, `…-products-a/b.jpg`, `…-logo-colour-a/b.jpg` | Earlier convertible variants | ⚠️ not opened in this pass. MISSING QA status, so use only `kv-convertible-real-bags.jpg` |
| `key-visuals/kv-bags-stack-20.jpg` / `kv-bags-stack-raw.png` | Stacked bags held by a model | ❌ **Wrong bag:** kraft/beige paper, pink ribbon handles, brown logo, and "20%" baked in. It breaks the bag rule |
| `key-visuals/kv-hotel-cart-bags.jpg` | Bell cart with bags | ❌ **Wrong bag:** cream bags with a brown printed logo, no silver foil |
| `banners/src/bg-hair-set.png` | Clean B&W plate, 4:5: Sleek Brush + Hair Wax (open) + Sleek Secret, dusty-rose "GLOW FRIDAY" ribbon | ✅ **S3**, after a local fix: ribbon hue to burgundy |
| `banners/src/bg-scrub-butter.png` | Clean B&W plate, 4:5: **Lavender** SALT SCRUB 300 ML on top of WHIPPED BODY BUTTER 250 ML, dusty-rose ribbon. Labels correct | ✅ **S4**, after the same ribbon fix |
| `banners/src/bg-lemongrass-set.png` | Lemongrass set plate | ❌ **Label errors:** butter reads "300 mL" (real: 250 ML) and scrub reads "SEA SALT SCRUB" (real: "SALT SCRUB") |
| `banners/glow-friday-*-20.png`, `moodboard-20.png` | Finished banners with "20%" baked in | ❌ as start frames |
| `images/amie-chocolate-bodyglow-closeup-a.jpg` (and `-b`, `-shoulder-*`, `-lips-*`, `-two-hands-*`, `-face-hold-*`, `-brush-*`) | Model holding Body Glow + Chocolate stick, lilac wall, hands already in pose, **bare shoulders** | ⚠️ **S5 option A.** Hands exist already, so they may stay but must not move. Modesty: needs a team OK (see Risks) |
| `content/brand/product-refs/body-glow-front.jpg`, `body-glow-reference-sheet.jpg` | Official Body Glow packshots | ✅ **S5 option B** (no person, safest) |
| `content/brand/product-refs/shopping-bag-real.jpg` | **Real photo** of 3 white a'mie bags on a tray, 750×1000 (low-res) | ✅ end-card background (local only, soft/blurred is fine) |
| `product-refs/hair-set-products.jpg`, `lavender-*.jpg`, `lemongrass-set.jpg`, `hair-set-with-pouch.jpg` | Official packshots | Reference images to attach (image refs), not start frames |
| `content/campaigns/hair-wax-concept/*.jpg` | Hair Wax concept series, rose/terracotta palette | ❌ off-palette for B&W Glow Friday. Not used |
| `videos/amie-glow-friday-hair-set-motion.mp4` + `drive-video-library.csv` | Existing **real** footage edits (local `tools/ads/glow_friday_video.py`) | ✅ free B-roll fallback (real hands, real labels) |

**Missing for the Lalenzi "stacked bags" beat:** we have no correct still of stacked real bags. See optional S7.

---

## 3. Local prep before any credit is spent (مجاني, لازم يخلص الأول)
Save everything to `content/campaigns/2026-11-glow-friday/video/start-frames/`:

| Out file | From | Op |
|---|---|---|
| `sf-01-car-9x16.jpg` | `kv-convertible-real-bags.jpg` | Centre-left crop 1260×2240 (x≈140–1400) so the "GLOW FRIDAY" bag and the hair-set bag stay in frame. Cool the white balance slightly so the bags read white, not cream |
| `sf-01-car-9x16-end.jpg` | same | 108% crop of `sf-01` (end keyframe, locks packaging) |
| `sf-02-basket.png` | `hero-plate-nologo.png` (changed from `hero-clean-plate.png`: no baked logo) | Upscale to 1080×1920 (local Lanczos; AI upscale only if it looks soft: cost MISSING) |
| `sf-02-basket-end.png` | same | 108% crop centred on the bow (changed from 112%: the 720 px source goes soft when enlarged). Exact numbers in S2 PROMPT (final) |
| `sf-03-hairset-9x16.png` | `bg-hair-set.png` | (a) Recolour the ribbon from dusty rose to the real burgundy: masked hue/sat shift, colour sampled with an eyedropper from `hero-original.webp` (hex MISSING until sampled). (b) Extend the plain grey background top and bottom to 9:16 (1792×3186) and scale to 1080×1920 |
| `sf-03-hairset-end.png` | same | 110% crop centred on the Hair Wax |
| `sf-04-scrubbutter-9x16.png` (+ `-end`) | `bg-scrub-butter.png` | Same ribbon recolour and pad to 9:16 |
| `sf-05a-glow-9x16.jpg` | `amie-chocolate-bodyglow-closeup-a.jpg` | 9:16 crop 1152×2048 on both products and hands; background graded lilac → neutral grey |
| `sf-05b-glow-9x16.png` (+ `-end`) | `body-glow-front.jpg` | Extend the plain **beige** background to 9:16 (the packshot is beige, not grey; a cut-out onto grey risks halos). Neutralise in the grade. Exact numbers in S5 PROMPT (final) |
| `sf-05a-glow-9x16-end.jpg` | `sf-05a` | 103% centre crop (end keyframe, locks hands and products) |

> Exact crop, pad and recolour numbers for each file are in the matching shot's **PROMPT (final)** block in §4 (prompt-engineer pass, 2026-11-08). **Status (2026-11-08): all `sf-*` start/end frames and `ec-bg.jpg` are made** by `tools/images/prep_video_start_frames.py` (free, local). Ribbon recoloured to the real burgundy (sampled from the hero plate, OpenCV HSV ≈ 174/212/95 ≈ #5F1020 mid-tone). S1 white balance is at half strength to keep the seats burgundy. S5-A wall is **not** graded yet (only needed if S5-A is approved). Run `amie-visual-qa` on the frames before the first generation.
| `ec-bg.jpg` | `shopping-bag-real.jpg` or `hero-plate-nologo.png` | 9:16 crop, soft blur and darken for text legibility |

---

## 4. Shot list: main Reel (18 s)

> Model defaults: **Seedance 2.5**, image-to-video, start frame (+ end frame where given), **480p draft**, 9:16, 5 s (min 4 s; trim in the edit), 1 shot per request. Finalize the approved draft at **1080p within 7 days**. **Kling 4.0** with start/end keyframes is the 2nd try if Seedance drifts on packaging. **Grok Video 1.5** (2–15 s) is the 3rd option for short beats. Draft tier for Kling/Grok: MISSING.
> Credits per shot: **MISSING** for every video model (get a quote first). Prices are not invented here.

**Prompt-engineer pass (2026-11-08):** every AI shot below now has a **PROMPT (final)** block that is ready to paste. The old constraint tail is already built into each final prompt, so do not add it a second time.

**Shared settings (every AI shot unless the block says otherwise)**
- **Seedance 2.5:** image-to-video · start + end frame · 1 output per request · aspect **9:16** · **generate_audio: false** (music is added in the edit) · draft **480p** · final **1080p** through Seedance finalize **within 7 days** of the draft. Record the seed of each approved draft.
- **Kling 4.0 (backup):** image-to-video · start + end frame · same prompt · paste the negative list into Kling's negative-prompt field · 5 s · 9:16 · audio off. Draft/final tier names and credit costs: MISSING (get the quote).
- **Negative list:** if the Seedance UI has no negative field, paste it as the last line, starting "Avoid:". Base list: `warped text, garbled letters, extra hands, extra fingers, morphing packaging, melting labels, new logos, added text or watermark, colour shift of ribbon or bag, product resizing, camera shake, fast motion, flicker`.
- **Reference images:** do not attach product-ref packshots as extra generation inputs. The start/end frames are the lock, and the colour packshots would fight the B&W plates. `amie-visual-qa` uses the refs to compare against. (Flag for `amie-reviewer`: this deliberately differs from the still-image rule.)
- Pixel coordinates below refer to the **original** file size unless marked "in the 1080×1920 frame".

### S1 · HOOK · 0.0–3.0 s · "the car full of bags" (MVS ✅)
#### PROMPT (final) · S1
- **Start-frame check** (`key-visuals/kv-convertible-real-bags.jpg`, opened): exists, 1792×2240 (4:5), and matches the storyboard. It shows white bags with rope handles and a silver-foil «a'mie», a "GLOW FRIDAY" bag in silver serif, burgundy seats, Lemongrass jars with the dry brush, Sleek Brush + Hair Wax + Sleek Secret, and a Body Glow with a short pump that matches `body-glow-front.jpg`. Flags:
  - The bags render warm ivory, not white, so the white-balance step below is required.
  - The top-right bag carries a small **dusty-rose bow**. The library allows one as a bag accent, and the crop puts most of it out of frame. The bow-tail motion was removed for that reason.
  - The small sub-lines under "Lemongrass" and the Hair Wax claim line are AI squiggles, not real words. Keep them tiny; QA zooms on them.
  - The angle is high three-quarter from the driver's side, not "overhead". The prompt is corrected.
- **Local prep (free):**
  1. Crop x 140–1400, y 0–2240 (1260×2240), then Lanczos to 1080×1920, giving `start-frames/sf-01-car-9x16.jpg`.
  2. White balance: neutral-pick on the face of the "GLOW FRIDAY" bag so the bags read white. Mask the seats so they stay burgundy. Any visible bit of the dusty-rose bow can stay (allowed) or take the same burgundy as the S3 ribbon fix.
  3. End frame: from the 1080×1920 start, crop 1000×1778 at x 40, y 120 (≈108%, shifted down for the tilt), then scale to 1080×1920, giving `sf-01-car-9x16-end.jpg`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-01-car-9x16.jpg` · end `…/start-frames/sf-01-car-9x16-end.jpg` · 5 s (trim to 3 s in the edit) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames.
- **Prompt:**
```
High-angle view looking down into a classic convertible with burgundy leather seats, filled with white paper shopping bags with rope handles and silver foil logos, a'mie products standing in the open bags. Camera: one very slow push-in with a slight downward tilt, ending exactly on the end frame. Secondary motion only: soft dappled leaf shadows drift slowly across the seats and bags; the tissue paper edges inside the open bags flutter very slightly. Light keeps the same direction, warmth and intensity as the start frame throughout. Calm, slow, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; bags stay white, seats stay burgundy; no new objects, no hands, no people, no text generation.
```
- **Negative:** base list + `cream or brown bags, bag print changing, "GLOW FRIDAY" misspelled, car moving, extra bags`
- **Edit text:** see `onscreen-copy-reviewed.md` (reviewed). Teaser «Glow Friday قرّبت» / "Glow Friday is coming" · launch «Glow Friday بدأت» / "Glow Friday is here" · 1 Dec «آخر يوم لـ Glow Friday» / "Last day of Glow Friday"
- **Sound:** track starts on frame 1, soft downbeat; SFX light paper rustle.
- **Risks:** the «a'mie» foil logo and "GLOW FRIDAY" bag text can warp with perspective, and the small product labels can melt. The KV is AI and the bags are a touch warm compared with the real white bag.
- **Free fallback:** ffmpeg zoompan 1.00→1.08 over 3 s on `sf-01`, plus a semi-transparent animated leaf-shadow overlay (multiply blend) drifting left to right.

### S2 · PRODUCT / ACCENT · 3.0–6.0 s · "the ribbon basket" (MVS ✅)
#### PROMPT (final) · S2
- **Start-frame check** (`hero/src/hero-clean-plate.png` and `hero-plate-nologo.png`, both opened): both exist at 720×1280 (9:16) and match the storyboard. They show the real burgundy ribbon with white sans-serif "GLOW FRIDAY", plus boxes for Lemongrass (WHIPPED BODY BUTTER / 250 ML), BODY GLOW (120ML), Hand Cream, Sleek Secret and Lip Plump, and an «a'» monogram box. Labels are correct. Flags:
  - The clean plate has a baked «a'mie» logo at the bottom, so the shot now uses the **no-logo plate** and the logo goes in the edit.
  - The source is low-res and the small box sub-lines are already soft, so the end crop is reduced to 108%.
- **Local prep (free):**
  1. Lanczos 1.5× upscale of `hero-plate-nologo.png` to 1080×1920, giving `start-frames/sf-02-basket.png`.
  2. End frame: crop 1000×1778 at x 40, y 116 (centred on the bow knot at about x 540, y 1005 in the 1080×1920 frame), then scale to 1080×1920, giving `sf-02-basket-end.png`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-02-basket.png` · end `…/start-frames/sf-02-basket-end.png` · 5 s (trim to 3 s) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames.
- **Prompt:**
```
Top-down photo of a black wire basket on a pale stone surface, holding white a'mie product boxes tied with a deep burgundy satin ribbon printed "GLOW FRIDAY" in white. Camera: one slow, straight push-in toward the bow, no rotation, ending exactly on the end frame. Secondary motion only: a soft diagonal band of window light glides from upper left to lower right across the boxes, and a gentle sheen travels along the satin; the ribbon itself does not move. Soft daylight with the same colour temperature as the start frame throughout. Quiet, slow, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; ribbon stays deep burgundy; no new objects, no hands, no text generation.
```
- **Negative:** base list + `ribbon untying, bow changing shape, ribbon lettering redrawn, basket wires bending, logo appearing at the bottom`
- **Edit text:** AR «لمعتك كاملة بأسعار Glow Friday» · EN "Your full glow, at Glow Friday prices" (reviewer fix: «بسعر أخف» promises a price cut while the MoC licence is on hold; still needs human approval)
- **Sound:** satin "swish" SFX on the light sweep.
- **Risks:** ribbon lettering re-drawn wrong, small box text garbled.
- **Free fallback:** use `hero/glow-friday-hero-mobile-9x16-notext.mp4` (already rendered), or ffmpeg zoompan plus an HTML light-sweep gradient pass in `tools/images/glow_hero.html`.

### S3 · PRODUCT · 6.0–8.5 s · Hair Set (MVS ✅, top seller)
#### PROMPT (final) · S3
- **Start-frame check** (`banners/src/bg-hair-set.png`, opened): exists, 1792×2240 (4:5). The labels match the library: Sleek Brush with «a'mie» vertical; Hair Wax open with the white dome, "Hair Wax", the small claim line, «a'mie» and "30 mL"; Sleek Secret with "Sleek Secret", «a'», "HAIR MASCARA", the small line, «a'mie» and "15 mL". Flags:
  - ⚠️ **Old ribbon colour:** the ribbon is dusty rose and must be recoloured before use.
  - ⚠️ **Ribbon lettering style:** this ribbon prints "GLOW FRIDAY" in silver **serif**, while the real ribbon (`hero-clean-plate.png`) uses white **sans-serif**. The recolour fixes the hue only, so a human must accept the serif lettering or choose the free fallback.
  - **Scale in the plate:** the brush is tallest, then the Sleek Secret tube, and the Hair Wax is the shortest. The storyboard's "Hair Wax ≈ tube height" was wrong. The plate is the reference.
  - **Ribbon motion removed:** every ribbon segment, including both floor tails, carries lettering, and any lift would warp it (§11.3).
- **Local prep (free):**
  1. **Ribbon recolour:** select the ribbon by colour range on the rose hue, refine the mask by hand, and exclude the light lettering pixels. Shift hue/saturation/lightness with Curves to match the burgundy sampled with an eyedropper from the mid-tone of the vertical ribbon band in `hero-clean-plate.png` (around x 350, y 470). Hex value: MISSING until sampled. Check that nothing else in the plate picks up colour.
  2. **Pad to 9:16:** canvas 1792×3186, adding 600 px on top and 346 px at the bottom. Fill the top by extending the grey gradient and the bottom by extending the floor (heal or clone, no AI outpaint). The product bases then land at about y 1470 in the 1080×1920 frame, clear of the bottom 420 px UI zone.
  3. Scale to 1080×1920, giving `start-frames/sf-03-hairset-9x16.png`.
  4. End frame: crop 982×1745 at x 66, y 175 (≈110%, on the Hair Wax), then scale to 1080×1920, giving `sf-03-hairset-end.png`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-03-hairset-9x16.png` · end `…/start-frames/sf-03-hairset-end.png` · 4 s (trim to 2.5 s) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames, 5 s.
- **Prompt:**
```
Black-and-white studio still life on a seamless grey background: a slim black hair brush, an open black Hair Wax stick with a white wax dome, and an ivory Sleek Secret tube, wrapped by a deep burgundy satin ribbon printed "GLOW FRIDAY". Camera: one slow, straight dolly-in at eye level toward the Hair Wax, no orbit, no rotation, ending exactly on the end frame. Secondary motion only: a soft studio light sweep passes left to right across the products and a faint sheen moves along the satin; the ribbon itself stays still. Same soft key light as the start frame, neutral grey tones; the burgundy ribbon is the only colour. Slow, minimal, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; no new objects, no hands, no text generation.
```
- **Negative:** base list + `products rotating, label text rewritten, wax dome changing, ribbon turning pink or rose, colour appearing on the products`
- **Edit text:** AR «مجموعة الشعر» · EN "Hair Set" (never name the brush, per the reviewer)
- **Sound:** beat hit on the cut.
- **Risks:** the tiny Hair Wax claim line (⚠️ VERIFY in the library) will scramble. That is acceptable only if it stays blurred-small, so QA zooms on it.
- **Free fallback:** ffmpeg push-in 1.00→1.06 plus an HTML light sweep. Or 2.5 s of real footage from `videos/amie-glow-friday-hair-set-motion.mp4`.

### S4 · PRODUCT · 8.5–11.0 s · Scrub + Butter (winter dry skin)
#### PROMPT (final) · S4
- **Start-frame check** (`banners/src/bg-scrub-butter.png`, opened): exists, 1792×2240 (4:5). The labels are correct: «a'mie» / "Lavender" / "SALT SCRUB" / "300 ML" on the clear glass jar, «a'mie» / "Lavender" / "WHIPPED BODY BUTTER" / "250 ML" on the lower jar, and the «a'» monogram on the lid. Flags:
  - ⚠️ **Old ribbon colour:** the ribbon is dusty rose and must be recoloured. Its lettering is sans-serif, which is close to the real ribbon.
  - **Packaging colour:** the plate is B&W, so the lids and butter jar read light grey instead of blush pink, and the scrub reads grey instead of pale pink. That fits the campaign grade, but the human approver should know the product colours are not true here.
  - **Ribbon motion removed:** the left floor tail carries "GLOW FRIDAY", and swaying it would warp the letters.
- **Local prep (free):**
  1. Ribbon recolour exactly as in S3 step 1.
  2. Pad to 9:16: canvas 1792×3186, adding 400 px on top and 546 px at the bottom, with the same fill method as S3. The jar base lands at about y 1477 in the 1080×1920 frame.
  3. Scale to 1080×1920, giving `start-frames/sf-04-scrubbutter-9x16.png`.
  4. End frame: crop 982×1745 at x 49, y 0 (≈110%, top-anchored on the scrub jar, which creates the upward crane), then scale to 1080×1920, giving `sf-04-scrubbutter-end.png`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-04-scrubbutter-9x16.png` · end `…/start-frames/sf-04-scrubbutter-end.png` · 4 s (trim to 2.5 s) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames, 5 s. Grok Video 1.5 (start image only, 3 s) is the last resort; its tier and settings are MISSING.
- **Prompt:**
```
Black-and-white studio still life on a seamless grey background: a clear glass jar of speckled salt scrub with a light lid, stacked on an opaque light jar of whipped body butter, wrapped by a deep burgundy satin ribbon printed "GLOW FRIDAY". Camera: one slow push-in with a gentle upward crane from the lower jar's label to the scrub lid, ending exactly on the end frame. Secondary motion only: a soft light sweep crosses the jars and a faint sheen moves along the satin; the ribbon and the scrub texture stay still. Same soft key light as the start frame, neutral grey tones; the burgundy ribbon is the only colour. Slow, minimal, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; no new objects, no hands, no text generation.
```
- **Negative:** base list + `scrub texture boiling or moving, jars separating or sliding, lid opening, "SEA SALT SCRUB", ribbon turning pink or rose`
- **Edit text:** AR «سكراب وزبدة لبشرة ناعمة في الشتاء» · EN "Scrub + butter for soft winter skin" (reviewer fix: «لجفاف» reads as a treatment claim). If the **Lavender** set is in the offer, the caption/landing page needs the nut-shell allergy note (the scrub contains nut shells).
- **Risks:** jar label text, the scrub texture "boiling". Which set is on offer (Lemongrass vs Lavender) is MISSING, because the plate shows Lavender.
- **Free fallback:** ffmpeg push-in plus a light sweep.

### S5 · PRODUCT · 11.0–14.0 s · Body Glow + Chocolate (the "glow")
#### PROMPT (final) · S5-B (default, no person)
- **Start-frame check** (`content/brand/product-refs/body-glow-front.jpg`, opened): exists, the official packshot at 1200×1600 (3:4). The label matches the library: "BODY GLOW" / «a'» "LIGHTWEIGHT BODY SHIMMER / WATER-LIKE GLOW, SILKY, LUMINOUS, SMOOTH SKIN WITH PERFUME" / «a'mie» / "120ML", with a short pump. Flags:
  - The background is plain warm **beige**, not grey as the storyboard claimed.
  - The **cap lies on its side** next to the bottle. It is part of the frame and has to be locked too.
  - Removed: "parallax" (it makes a single object rotate) and "shimmer bokeh" (it adds new objects).
  - Added an end frame to lock the packaging.
- **Local prep (free):**
  1. Extend the canvas to 1200×2133 by adding 267 px on top and at the bottom, filled with the sampled flat beige.
  2. Scale to 1080×1920, giving `start-frames/sf-05b-glow-9x16.png`. Neutralise the beige in the grade, not before generation.
  3. End frame: crop 1019×1811 at x 61, y 63 (≈106%, toward the "BODY GLOW" wordmark), then scale to 1080×1920, giving `sf-05b-glow-9x16-end.png`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-05b-glow-9x16.png` · end `…/start-frames/sf-05b-glow-9x16-end.png` · 4 s (trim to 3 s) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames, 5 s.
- **Prompt:**
```
Studio packshot on a plain warm beige background: a matte cream Body Glow pump bottle standing upright, its round cap lying on its side beside it. Camera: one slow, straight push-in toward the label, no rotation, no parallax, ending exactly on the end frame. Secondary motion only: a soft band of light slides slowly down the bottle and a gentle highlight glints across the pump head. Light keeps the same direction and colour as the start frame throughout. Calm, slow, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; no new objects, no hands, no text generation.
```
- **Negative:** base list + `bottle rotating, pump nozzle getting longer, cap moving, sparkles or bokeh particles, liquid appearing`

#### PROMPT (final) · S5-A (person; only after the team's modesty OK)
- **Start-frame check** (`images/amie-chocolate-bodyglow-closeup-a.jpg`, opened): exists, 2048×2048 (square). The labels match: "Chocolate / BODY HIGHLIGHTER / a'mie" and "BODY GLOW / «a'» LIGHTWEIGHT BODY SHIMMER … WITH PERFUME / a'mie / 120ML". Scale is right (the stick is about half the bottle's height). Both hands look natural, with every finger accounted for. Flags:
  - ⚠️ **Bare shoulders and upper chest:** the modesty decision is MISSING (§11.6).
  - **Lips:** they are slightly parted, not closed. They stay as they are.
  - **Wall:** lilac, which needs the grade step below.
- **Local prep (free):**
  1. Crop x 830–1982, y 0–2048 (1152×2048). This keeps both products, both hands and most of the face.
  2. Mask the wall only and grade it from lilac to neutral grey. Leave skin untouched.
  3. Scale to 1080×1920, giving `start-frames/sf-05a-glow-9x16.jpg`.
  4. End frame: crop 1048×1864 at x 16, y 28 (103% centre), then scale to 1080×1920, giving `sf-05a-glow-9x16-end.jpg`.
- **Settings:** Seedance 2.5 · start `content/campaigns/2026-11-glow-friday/video/start-frames/sf-05a-glow-9x16.jpg` · end `…/start-frames/sf-05a-glow-9x16-end.jpg` · 4 s (trim to 3 s) · draft 480p → final 1080p · 9:16 · generate_audio false. Backup: Kling 4.0 with the same frames, 5 s.
- **Prompt:**
```
Close-up beauty photo: a woman with closed eyes holds a bronze Chocolate highlighter stick and a cream Body Glow pump bottle beside her shoulder, plain wall behind. Camera: almost locked, one very slight push-in, ending exactly on the end frame. Secondary motion only: a few loose hair strands at the top of the frame lift gently in a soft breeze, and the sunlit highlight on her skin shifts slowly. Light keeps the same direction and warmth as the start frame throughout. Calm, serene, premium mood. The hands, fingers, face and both products already in the frame stay exactly where they are: no new hands, fingers or arms, no change of pose, eyes stay closed, mouth still. Keep every product, label, logo and packaging exactly as in the start frame; no new objects, no text generation.
```
- **Negative:** base list + `fingers merging, sixth finger, hand sliding, eyes opening, mouth moving, talking, head turning, products changing size, body exposure increasing`
- **Edit text:** option A «مجموعة سهرة تشوكلت» / "Chocolate Night Set" (name pending); option B (bottle only) «لمعة الجسم Body Glow» / "Body Glow". No «خصم» framing on new bundles.
- **Risks:** A: hands and fingers are the #1 failure, plus face drift and the modesty question. B: lower risk.
- **Free fallback:** Ken Burns on the still plus an animated specular "glint" PNG overlay (screen blend).

### S6 · OFFER + CTA · 14.0–18.0 s · End card (**local only, 0 credits**)
- **Background:** `ec-bg.jpg` (real bags) or the last frame of S2 frozen, blurred and darkened.
- **Built in:** CapCut or a variant of `tools/images/glow_hero.html` / `render_glow_hero.js`, Readex Pro (AR) + Montserrat (EN), black/white type, one burgundy rule line.
- **Motion:** text fades up line by line on the beat (0.5 s steps), logo last.
- **Text (editable layers, never AI):**
  - Line 1: «Glow Friday»
  - Line 2 (variable): «خصم من **{{MIN}}%** إلى **{{MAX}}%** على منتجات مختارة» / EN "{{MIN}}% to {{MAX}}% off selected items". Default placeholders 20/40, **final % pending Saleh.**
  - Line 3: «من 25 نوفمبر لين 1 ديسمبر»
  - CTA: «تسوّقي الآن · amie-sa.com» + a'mie logo (`content/link-card/logo-dark.png` / `logo-white.png`)
- **Variants:** Teaser «Glow Friday قرّبت · من 25 نوفمبر» (no %) · Launch (as above) · Last chance «آخر يوم لـ Glow Friday · العرض ينتهي الليلة 11:59 م».
- **Sound:** music resolves with a soft chime on the logo.

### S7 · OPTIONAL · Lalenzi "stacked bags" (only if credits remain)
- **No valid still exists** (`kv-bags-stack-*` use the wrong bag). Best: a **real phone shoot** of 3–4 real white a'mie bags stacked on a stone step or marble console, burgundy ribbon on the top bag, no person (≈15 min, 0 credits). Second best: a new still via `design-image-prompt-engineer` with `shopping-bag-real.jpg` attached (draft 0.5 + final 2.75 credits), then `amie-visual-qa`, then animate as S1 (light and shadow drift only).
- If it is made, it replaces S4 or S5 in the timeline.

---

## 5. Timeline table

| Time | Shot | Purpose | Source | Edit text (AR / EN) | Audio |
|---|---|---|---|---|---|
| 0.0–3.0 | S1 car | Hook | AI ← `kv-convertible-real-bags` | «Glow Friday بدأت» / Glow Friday is here | track in, paper rustle |
| 3.0–6.0 | S2 basket | Accent / brand | AI ← `hero-clean-plate` (fallback: existing mp4) | «لمعتك كاملة، بسعر أخف.» | satin swish |
| 6.0–8.5 | S3 hair set | Product | AI ← `bg-hair-set` (recoloured) | «مجموعة الشعر» / Hair Set | beat hit |
| 8.5–11.0 | S4 scrub+butter | Product | AI ← `bg-scrub-butter` (recoloured) | «سكراب وزبدة لجفاف الشتاء» | beat hit |
| 11.0–14.0 | S5 glow | Product | AI ← closeup-a (A) / body-glow-front (B) | «مجموعة سهرة تشوكلت» | shimmer SFX |
| 14.0–18.0 | S6 end card | Offer + CTA | **Local** | offer {{MIN}}–{{MAX}}% + dates + CTA | resolve + chime |

**MVS 15 s:** S1 (0–4) → S2 (4–8) → S3 (8–12) → S6 end card (12–15).
**Bumper 6 s (D2):** S1 (0–2) → S2 (2–3.5) → S6 short card (3.5–6: «Glow Friday» + offer + logo). No new generation.
**Web-hero loop 6 s (D3):** see §6.

## 6. Web-hero loop (silent, 6 s)
- **Free and already done:** `hero/glow-friday-hero-mobile-9x16-notext.mp4` + `…-desktop-16x9-notext.mp4`. Ship these unless the team wants more life.
- **AI upgrade (optional, last priority):** Seedance 2.5, start = end = `sf-02-basket.png` (same frame at both ends makes a seamless loop), 6 s, light sweep only, no camera move. Desktop 16:9 needs its own plate (outpaint the basket sides): cost MISSING. No text, no audio track.

#### PROMPT (final) · D3 web-hero loop (9:16 only)
- **Start-frame check:** uses `sf-02-basket.png`, built from the no-logo plate. See S2.
- **Settings:** Seedance 2.5 · start **and** end `content/campaigns/2026-11-glow-friday/video/start-frames/sf-02-basket.png` · 6 s if offered, otherwise 5 s (supported durations: VERIFY in the UI) · draft 480p → final 1080p · 9:16 · generate_audio false.
- **Prompt:**
```
Top-down photo of a black wire basket holding white a'mie product boxes tied with a deep burgundy satin ribbon printed "GLOW FRIDAY". Camera completely static. Secondary motion only: one soft diagonal band of window light glides slowly across the boxes from upper left to lower right and fades out, and a gentle sheen travels along the satin. The final frame matches the first frame exactly for a seamless loop. Same soft daylight throughout. Quiet, slow, premium mood. Keep every product, label, logo and packaging exactly as in the start frame; no new objects, no hands, no text generation.
```
- **Negative:** base list + `camera movement, zoom, ribbon moving`

## 7. Music & sound direction
- **Mood:** quiet luxury. Minimal deep house / downtempo, warm sub-bass, soft clap or finger-snap on 2 and 4, airy pad, no vocals (or wordless hum only). Avoid anything loud or "sale siren".
- **Tempo:** **120 BPM** (beat = 0.5 s, bar = 2 s), so cuts land on beats: 3.0 / 6.0 / 8.5 / 11.0 / 14.0.
- **SFX layer:** paper bag rustle (S1), satin swish (S2), soft "tick" on product cuts, gentle shimmer (S5), chime on the logo (S6).
- **Licensing:** royalty-free or the platform's commercial library only. Track source MISSING (pick in CapCut / TikTok Commercial Music Library). Web-hero is silent.

## 8. Edit plan
1. **Grade first:** neutral B&W / low saturation (about −70% sat) on all shots, protect the burgundy (ribbon + car seats) with an HSL qualifier. Skin in S5-A stays natural but desaturated about 30%, wall to neutral grey.
2. **Assemble** in CapCut (or `tools/ads/glow_friday_video.py`, whose spec format is in `video-specs/`). Cuts on the beat, hard cuts, no flashy transitions. One 6-frame light-leak dip into S6 at most.
3. **Supers:** Readex Pro (AR) above Montserrat Light (EN), white text with a soft shadow, inside the 9:16 safe zone (top 250 px and bottom 420 px clear for the UI). AR text is rendered as PNG (raqm), because ffmpeg drawtext breaks Arabic shaping (already handled in `glow_friday_video.py`). Its font/logo paths point to the session scratchpad, so restore them before use (MISSING after this session).
4. **End card** = separate layer project with 3 variants (teaser / launch / last chance) and % as an editable variable.
5. **Exports:** 1080×1920 H.264, 30 fps, bt709, AAC 48 kHz. Bumper 6 s. Web-hero: `-an`, faststart, also a poster JPG.
6. **Review:** export → `amie-visual-qa` (frames at 0.5 s steps, zoom on labels and hands) → `amie-reviewer` (supers and claims) → human.

## 9. Generation order (stop anywhere, every step leaves a usable cut)

| Priority | Shot | Model / mode | Why here | Running cut after this step |
|---|---|---|---|---|
| 0 | Local prep §3 + end card S6 + fallbacks | local | 0 credits | Full 15 s reel already possible with free Ken-Burns versions |
| 1 | **S1 car** | Seedance 2.5 · start+end · 5 s · 480p | Hook = biggest impact | |
| 2 | **S2 basket** | Seedance 2.5 · start+end · 5 s · 480p | Real ribbon, the campaign accent. Skip if the existing hero mp4 is judged enough | |
| 3 | **S3 hair set** | Seedance 2.5 · start+end · 5 s · 480p | Top seller | **MVS 15 s complete** |
| 4 | S5 glow (B first, A only if the team OKs the model shot) | Seedance 2.5 · start · 4 s · 480p | Second bundle | |
| 5 | S4 scrub+butter | Seedance 2.5 or Grok 1.5 | Winter angle | **Full 18 s** |
| 6 | Finalize approved drafts to 1080p | Seedance finalize | Within 7 days of each draft | |
| 7 | Kling 4.0 retries for any shot that failed QA twice | Kling start/end | Backup | |
| 8 | Web-hero AI loop / S7 stacked bags | Seedance / image pipeline | Nice-to-have | |

- **Minimum viable set = S1 + S2 + S3** (+ free local end card) → a usable 15 s reel.
- Max 2 draft attempts per shot. After the 2nd fail, use the free fallback and move on.
- **Marketing Studio:** not planned. Its UGC/unboxing presets generate hands handling products and moving labels, which is exactly what fails our QA. Test it once only if credits are plentiful, and never for the end card.
- **Credits:** per-shot prices MISSING. Get the quote for Seedance 480p 5 s, Seedance 1080p finalize, Kling 4.0 5 s and Grok 1.5 3 s, fill this column, and tell the user the total before generating.

| Shot | Draft cost | Finalize cost |
|---|---|---|
| S1–S5 | MISSING | MISSING |
| S7 still (if AI) | 0.5 | 2.75 |

## 10. Campaign timeline
| Phase | Dates | Reel version | End card |
|---|---|---|---|
| Teaser | 18–23 Nov | 15 s MVS + 6 s bumper | «Glow Friday قرّبت · من 25 نوفمبر» (no %) |
| Early access | 24 Nov | same | HOLD (mechanism undecided, see `copy-reviewed.md`) |
| Launch | 25 Nov – 30 Nov | full 18 s + bumper | offer {{MIN}}–{{MAX}}% «على منتجات مختارة» |
| Last chance | 1 Dec | 15 s + bumper | «آخر يوم · ينتهي الليلة 11:59 م» |
- **Production deadline:** drafts approved by 14 Nov, finals and edit locked by 17 Nov (teaser goes live 18 Nov). The Seedance 7-day finalize window means drafts made before 8–10 Nov may expire. Generate drafts no earlier than you can review them.

## 11. Risks & open points
1. **Hands (S5-A):** any new finger or arm = reject. Option B has no person, so it is the default.
2. **Label text:** QA every product frame at 100% zoom. Small lines (Hair Wax claim line, Body Glow sub-copy) may only be blurred, never re-worded.
3. **Ribbon lettering:** "GLOW FRIDAY" on the ribbon must stay legible and spelled right in every frame, otherwise use the free fallback.
4. **Scale:** Body Glow ≈ 2× the Chocolate stick. The AI must not resize products, which is why end keyframes are crops of the same still.
5. **Bag colour:** the convertible KV bags are slightly warm. Grade toward white. The real bag is white with a silver foil logo, never cream or brown.
6. **Modesty:** model shots show bare shoulders. The brand direction says modest styling, so a team decision is needed before S5-A runs in Saudi/Gulf paid media (MISSING).
7. **Offer wording conflict:** the brief asks for "20% to 40%", while `copy-reviewed.md` plans fixed bundle prices and "savings in SAR, not %". The Ministry of Commerce discount licence is also a reviewer HOLD. Final % pending Saleh. The end card is variable, so either version drops in.
8. **Which body-care set is on offer** (Lemongrass vs Lavender): MISSING. The only clean plate with correct labels is Lavender. The Lemongrass plate has wrong labels (300 mL butter, "SEA SALT SCRUB").
9. **When a real shoot is better:** stacked bags (S7) and any hand action (applying Body Glow, untying the ribbon) → shoot on a phone with the real products. Do not generate.
10. Forbidden in supers and captions: COD, «آمن», «علاج», «طبيعي 100%», «الأفضل/الأول», any comparison or competitor name.

## 12. Checklist: يوم ما الكريدت ينزل
- [ ] Get the Higgsfield quote (Seedance 480p/1080p, Kling 4.0, Grok 1.5), fill §9 and tell the user the total. Confirm the budget.
- [ ] §3 start frames exist in `video/start-frames/` (ribbon recoloured, 9:16, end crops made).
- [ ] End card S6 (3 variants) and the free-fallback cut of the 15 s reel are already rendered, so there is a safety net.
- [ ] Saleh's % confirmed, or the end card stays on {{MIN}}/{{MAX}} placeholders. MoC licence status checked.
- [ ] Team decision on S5-A (model shot) vs S5-B.
- [ ] Generate in order: S1 → S2 → S3 (stop and review MVS) → S5 → S4. One request per shot, 480p draft, 9:16, generate_audio false, start + end frames attached, paste the shot's PROMPT (final) and its negative list unchanged.
- [ ] Each draft → `amie-visual-qa` (labels, ribbon text, hands, scale, bag colour) → human OK.
- [ ] Finalize approved drafts at 1080p **within 7 days**. Note the draft date per shot.
- [ ] Edit (§8), export D1/D2/D3, run `amie-reviewer` on supers and captions, then human approval before posting.
- [ ] Save the finals to `content/campaigns/2026-11-glow-friday/video/` and record which model and prompt won per shot in this file.
