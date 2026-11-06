# a'mie — Product visual library

What every product and its packaging looks like. It is for image prompts and image review. Read it before writing any image prompt or checking any image. Facts about ingredients, sizes and claims live in `product-facts.md`; this file covers only how things look.

**Reference photos** (official, from the Zid store) are in `content/brand/product-refs/`. Always attach the matching photo to an image generation, and never describe a product from memory.

**Status of each entry:**
- ✅ Read from the official photo.
- ⚠️ VERIFY: not confirmed yet, so ask the team or check the real product before relying on it.

## Brand look
| Item | Value |
|---|---|
| Logo | «a'mie» wordmark (lowercase, with the apostrophe accent) and the «a'» monogram on lids. Spell it a'mie, never amie, AMIE or ايمي, in brand text. |
| Logo file | `content/link-card/logo-dark.png` (dark brown #3A2522) and `logo-white.png`. |
| Logo on shopping bags | Silver metallic foil. ✅ (`shopping-bag-real.jpg`) |
| Campaign accent (Glow Friday) | Dusty-rose satin ribbon, #8E5A55. "GLOW FRIDAY" printed in silver on the ribbon. |
| Packaging palette | Blush pink (body care jars), black (hair care), cream/ivory (Body Glow, Sleek Secret), dark-brown gradient (Chocolate stick). |

## Shopping bag ✅
- White paper bag, clean matte finish.
- White twisted rope handles.
- «a'mie» logo in **silver foil**, centred.
- Not cream, not brown, no ribbon handles. One small dusty-rose bow is allowed as a campaign accent only.
- Reference: `shopping-bag-real.jpg`.

## Body care

### Sea Salt Body Scrub, 300 ml (Lavender / Lemongrass) ✅
- Clear glass jar, round and low; blush-pink flat screw lid with the «a'» monogram.
- Scrub visible through the glass: pale pink salt with darker specks.
- Front print (dark grey), top to bottom: «a'mie» / scent name in serif («Lavender» or «Lemongrass») / «SALT SCRUB» (small caps) / «300 ML».
- **The label really says «SALT SCRUB», not «SEA SALT SCRUB».**
- Reference: `lavender-body-scrub.jpg`, `lavender-set.jpg`, `lemongrass-set.jpg`.

### Whipped Body Butter, 250 ml (Lavender / Lemongrass) ✅
- Opaque blush-pink jar, the same shape as the scrub jar; blush-pink lid with the «a'» monogram.
- White whipped butter inside.
- Front print (dark grey): «a'mie» / scent in serif / «WHIPPED BODY BUTTER» / «250 ML».
- Reference: `lavender-body-butter.jpg`.

### Dry body brush (in the Lavender and Lemongrass sets) ✅
- Round wooden head with natural tan bristles.
- Wooden handle wrapped in jute rope, with a rope loop at the end.
- Reference: `lavender-set.jpg`.

### Set photos ✅
- Lavender Set and Lemongrass Set: scrub jar + butter jar + dry brush, shown on a beige background.
- Reference: `lavender-set.jpg`, `lemongrass-set.jpg`.

## Body glow / highlighters

### Body Glow, 120 ml ✅
- Matte cream/ivory cylinder with a **short** cream pump head. No long nozzle, no lotion spout.
- **Scale:** about twice the height of the Chocolate stick and about the same width.
- Terracotta/rose-brown serif print, top to bottom: «BODY GLOW» / «LIGHTWEIGHT BODY SHIMMER» / «WATER-LIKE GLOW, SILKY, LUMINOUS, SMOOTH SKIN WITH PERFUME» / «a'mie» logo / «120ML».
- Reference: `body-glow-reference-sheet.jpg`, `body-glow-front.jpg`.

### Chocolate Body Highlighter stick, 30 ml ✅
- Clear cap over the product. The body is a bronze-brown gradient fading to black at the base.
- «Chocolate» in serif, a small «BODY HIGHLIGHTER» line under it, and the «a'mie» logo in white lower down.
- Reference: campaign photos in `content/campaigns/2026-11-glow-friday/images/`. ⚠️ VERIFY: add an official packshot.

### Marshmallow Body Highlighter stick, 30 ml
- Same stick as Chocolate in a pearly pink-nude colour, printed «Marshmallow» (never «Marshmello»).
- ⚠️ VERIFY: no official packshot in the library yet.

## Hair care

### Hair Wax stick, 30 ml ✅
- Matte black cylinder stick, with the white wax visible at the top when open.
- Black cap with the «a'» monogram.
- Front print (white): «Hair Wax» in serif; next to it the «a'» monogram and a small line, «THE ULTIMATE STYLING SOLUTION FOR AN EFFORTLESS, GLOSSY AND CLEAN LOOK»; then the «a'mie» logo and «30 mL».
- ⚠️ VERIFY with the team: the small line was read off the store photo by the reviewer. In AI images, keep it tiny or blurred rather than invent words.
- Reference: `hair-set-products.jpg`.

### Sleek Secret Hair Mascara, 15 ml ✅
- Ivory squeeze tube with a white cap at the bottom.
- Printed vertically: «Sleek Secret» in serif, «a'» monogram, «HAIR MASCARA», the small line «SMOOTHS BABY HAIRS, TAMES FLY AWAYS, ENHANCES SHINE» (⚠️ VERIFY: read off the photo), «a'mie» logo, «15 mL».
- Reference: `hair-set-products.jpg`.

### Sleek Brush ✅
- Slim matte black brush with dense black bristles and a curved handle that narrows at the waist.
- «a'mie» printed vertically on the handle in white.
- Reference: `hair-set-products.jpg`.

### Hair Set pouch ✅
- Cream/off-white zip pouch with the «a'mie» logo in dark grey.
- Reference: `hair-set-with-pouch.jpg`.

## Not yet in the library (⚠️ add official photos)
Red Cherry, Deep Tan, Glittery Gold, Lip Plump, Foot Cream, Hand Cream, a'musk, Natura, Flora, gift box, mirror, a'mie bags (brown and cream pouches).

## Prompt rules (from what went wrong before)
1. **Attach the real photo:** always attach the product's reference photo, and write "exactly the same shape, colours and logo as image N".
2. **Write the label text yourself:** spell it out in quotes from this file. When the text is too small to know, say "small text, keep it minimal" instead of inventing words.
3. **State the scale:** say how big each product is against the others (Body Glow ≈ 2× the Chocolate stick).
4. **Hands:** when a hand holds a product, keep the hand where it already is in the base photo. Change only the grip, and a hidden label is fine. Inventing a new arm or hand pose rarely looks real.
5. **Bags:** use the real white bag with the silver foil logo, never a cream or brown one.
6. **Credits:** make the draft at quality medium, 1K (0.5 credits), and the final at high, 2K (2.75 credits), one image per request unless the user asks for more.
