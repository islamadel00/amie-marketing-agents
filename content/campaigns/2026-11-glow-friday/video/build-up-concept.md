# Glow Friday · "Build-up" reel: the basket assembles itself (reverse trick)

_Owner: design-image-prompt-engineer · 2026-11-08 · Status: DRAFT → amie-reviewer → human approval_
_Nothing has been generated. No Higgsfield tool was called. Credit cost per clip: **MISSING**, same as storyboard §9. Get the Higgsfield quote and tell the user the total before any generation._

---

## 0. Idea and technique

- **What the viewer sees:** an empty black wire basket on pale stone. The white a'mie boxes go in one by one, the burgundy "GLOW FRIDAY" ribbon is laid over them and tied, and the video lands on the team's **real** photo, then hands off to the hero loop and the end card.
- **What we generate:** the opposite, the **disassembly**, with `start-frames/sf-02-basket.png` as the **start frame**. Then we reverse it locally (`ffmpeg -vf reverse`). The reversed clip ends on the real, accurate photo. Any label wobble happens mid-motion and goes by fast.
- **Two versions to test, keep the better one:**
  - **A:** hands, two generations.
  - **B:** no hands, magic stop-motion, one generation.

### Start frame: what is in it (opened, 1080×1920, top-down)
Positions are in the 1080×1920 frame. QA uses them, and the prompts describe boxes by position because models follow positions better than names.

| # | Box | Where | Visible label text |
|---|---|---|---|
| 1 | Large square box, monogram on top | top-left (≈ x 215–500, y 555–905) | «a'» monogram only |
| 2 | Tall slim box, standing upright | top centre-right (≈ x 590–760, y 455–800) | «a'» / «a'mie» / "Hand Cream" + small lines |
| 3 | Tall slim box | far right, upper (≈ x 760–890, y 525–1050) | «a'mie» / "Sleek Secret" + small line |
| 4 | Slim box | far right, lower (≈ x 770–890, y 1050–1430) | «a'mie» / "Lip Plump" + small lines |
| 5 | Tall box | centre (≈ x 580–780, y 810–1440) | «a'mie» / "BODY GLOW" / small lines / "120ML" |
| 6 | Partly hidden box | left middle, under the bow (≈ x 240–570, y 905–1140) | label not readable. ⚠️ VERIFY with the team what it is |
| 7 | Large flat box | bottom-left (≈ x 180–580, y 1140–1460) | «a'mie» / "Lemongrass" / "WHIPPED BODY BUTTER" / "250 ML" |

- **Ribbon:** a deep burgundy satin ribbon, white sans-serif "GLOW FRIDAY".
  - A vertical band (x ≈ 480–570) and a horizontal band (y ≈ 960–1040) cross at the bow knot (≈ x 540, y 1005).
  - Two loops point up-left and up-right. Two long tails sweep down-left and down-right and curl along the bottom of the basket.
- **Light:** soft, even daylight from above with soft shadows. The basket rim runs from y ≈ 410 to y ≈ 1560. There is no text overlay and no logo.
- **Scale (the same in every frame):** the two square boxes (#1, #7) are the largest. Body Glow (#5) is the tallest box, about 2× the height of the Hand Cream box (#2). Sleek Secret (#3) and Lip Plump (#4) are the narrowest.
- **Reference rule:**
  - Hand Cream and Lip Plump have **no official packshot** in the library, so `sf-02-basket.png` itself is the reference.
  - Following storyboard §0 "Shared settings", no packshots are attached as extra video inputs. The start frame is the lock, and `amie-visual-qa` compares against the refs.
  - (Flag for `amie-reviewer`: this deliberately differs from the still-image rule, same as the storyboard.)

### Removal order (generation) → build order (what the viewer sees)
- **Generation (disassembly):** ribbon off → Hand Cream (#2) → Sleek Secret (#3) → Lip Plump (#4) → Body Glow (#5) → monogram box (#1) → hidden box (#6) → Lemongrass (#7) → empty basket.
- **After reversal (assembly):** empty basket → Lemongrass → hidden box → monogram box → Body Glow → Lip Plump → Sleek Secret → Hand Cream → ribbon tied → real photo.
- The big flat boxes go in first and the slim ones last, which reads like a real packer.

### Rules for "it has to look right in reverse"
- **No gravity cues in the generation:** nothing falls, drops, bounces or shakes dust. Reversed, those would look like objects flying upward.
- **Hands:** they *lift* things away. In reverse, they carry things in and set them down.
- **Even pace:** constant, slow movement with short still pauses between boxes. Even moves reverse cleanly and give clean cut points for the speed ramp.
- **End state of every clip:** a still frame with no hands (empty basket, or the basket without the ribbon). After reversal it becomes a clean opening frame.

---

## 1. Beat sheet (بعد العكس · ده اللي المشاهدة هتشوفه)

> الموسيقى 120 BPM (البيت = 0.5 ث) زي الـ storyboard. كل علبة بتنزل على بيت. الكلام على الشاشة من `onscreen-copy-reviewed.md` بس، والـ end card الافتراضي من غير أي %.

### نسخة A · بالإيدين (≈ 16.5 ث)
| الوقت | اللي بيحصل | صوت |
|---|---|---|
| 0.0–0.5 | السلة السودا فاضية على الرخام الفاتح، الكاميرا ثابتة من فوق | الإيقاع يبدأ |
| 0.5–1.0 | إيد داخلة من طرف الكادر الشمال بعلبة Lemongrass الكبيرة وبتحطها تحت على الشمال | "تك" خفيف |
| 1.0–1.5 | العلبة اللي في النص على الشمال (اللي تحت الفيونكة) | تك |
| 1.5–2.5 | علبة المونوجرام «a'» الكبيرة فوق على الشمال | تك |
| 2.5–3.5 | علبة BODY GLOW الطويلة في النص | تك |
| 3.5–4.5 | Lip Plump، يمين تحت | تك |
| 4.5–5.5 | Sleek Secret، يمين فوق | تك |
| 5.5–6.5 | Hand Cream آخر واحدة فوق في النص، والإيد تطلع فاضية من الطرف | تك |
| 6.5–9.5 | الإيدين يدخلوا من تحت بالشريطة العنابي «GLOW FRIDAY»، يفردوها على العلب ويشدّوا الفيونكة. دي اللحظة الأبطأ (سرعة 1×) | swish ساتان |
| 9.5–10.5 | الإيدين يطلعوا، والكادر يستقر على **الصورة الحقيقية** بالظبط. ثانية ثابتة | نفَس هادي |
| 10.5–12.5 | لوب الهيرو المحلي (لمعة نور ماشية على العلب واللوجو بيظهر) + سوبر اختياري | |
| 12.5–16.5 | الـ end card (S6) | chime على اللوجو |

### نسخة B · من غير إيدين، stop-motion سحري (≈ 15 ث)
| الوقت | اللي بيحصل | صوت |
|---|---|---|
| 0.0–0.5 | السلة فاضية، كاميرا ثابتة | الإيقاع يبدأ |
| 0.5–5.0 | العلب داخلة لوحدها من أطراف الكادر، واحدة ورا واحدة بحركة stop-motion "متقطّعة" نضيفة، كل علبة تقف في مكانها على نص بيت. نفس الترتيب: Lemongrass ← العلبة اللي في النص ← المونوجرام ← BODY GLOW ← Lip Plump ← Sleek Secret ← Hand Cream | تك على كل علبة |
| 5.0–7.5 | الشريطة بتزحف لوحدها من الأطراف، تلف على العلب وتربط نفسها فيونكة | swish |
| 7.5–8.5 | الاستقرار على **الصورة الحقيقية**، ثانية ثابتة | |
| 8.5–10.5 | لوب الهيرو + سوبر اختياري | |
| 10.5–15.0 | الـ end card (S6) | chime |

### الكلام على الشاشة (من الملف المراجَع بس)
- **أثناء التجميع:** مفيش كلام. خلّي الحركة هي اللي تحكي.
- **على الصورة الحقيقية / لوب الهيرو:** حسب المرحلة:
  - تيزر «Glow Friday قرّبت»
  - إطلاق «Glow Friday بدأت»
  - 1 ديسمبر «آخر يوم لـ Glow Friday»
  - أو سطر S2 «لمعتك كاملة بأسعار Glow Friday»، وده لسه مستني موافقة بشرية.
- **مكان الكلام:** فوق السلة (y ≈ 260–400)، بره الـ 250 بكسل اللي فوق والـ 420 اللي تحت.
- **الـ end card الافتراضي:**
  - «Glow Friday»
  - «أسعار خاصة على منتجات مختارة»
  - «من 25 نوفمبر لين 1 ديسمبر»
  - «تسوّقي الآن · amie-sa.com» + اللوجو
- **التيزر (18–23 نوفمبر):** «Glow Friday قرّبت · من 25 نوفمبر».
- **مفيش % ولا «خصم» قبل ما:**
  1. رخصة وزارة التجارة تتأكد،
  2. وصالح يأكد الأرقام.

---

## 2. Version A: hands

### 2.1 Split into two generations (recommended)
A ribbon release plus seven box removals with hands is too much for one generation, and every extra action raises the chance of an extra finger or a hand passing through a box. So we split:

| Clip | Generation (disassembly) | Start frame | End frame | Raw length | Used after reversal |
|---|---|---|---|---|---|
| **A1** ribbon off | hands loosen the bow and lift the ribbon away, then leave | `sf-02-basket.png` | none | 5 s | the tie, 6.5–9.5 s, at 1× |
| **A2** boxes out | hands lift the 7 boxes out, one at a time, until the basket is empty | **last frame of A1** (basket without the ribbon, no hands) | none (optional: empty-basket plate, see 2.2) | 10 s (or 2 × 5 s, see below) | the boxes, 0.5–6.5 s, ramped about 1.5× |

**How they join:**
- A2 starts on A1's last frame, so after reversal A2_rev *ends* on that frame and A1_rev *starts* on it. The join is continuous by construction.
- The join frame has no hands and nothing moving, so a 4-frame dissolve hides any tiny re-encode difference.

**Order of work:**
1. Draft A1 at 480p, then QA.
2. If A1 passes, finalize A1 at 1080p.
3. Extract the **1080p** last frame of A1: `ffmpeg -sseof -0.1 -i A1_1080.mp4 -update 1 -frames:v 1 start-frames/sf-02a-noribbon.png`.
4. QA that frame (labels, box count, no hands, no ribbon scraps).
5. Draft A2 from it, QA it, then finalize A2.

- **Why A1 is finalized before A2 is drafted:** the start image of A2 then has full resolution, so A2's 1080p final is not built on a soft 480p frame.
- **Cheaper alternative:** draft A2 from A1's 480p draft frame and accept a slightly softer box sequence. It is fast and ramped, so it may pass.

**If Seedance cannot do 10 s (VERIFY in the UI):** split A2 into two 5 s clips.
- **A2a:** remove #2, #3, #4, #5.
- **A2b:** remove #1, #6, #7.
- A2b starts on A2a's last frame, with the same join method.

### 2.2 Model and settings
- **Seedance 2.5 (first):**
  - image-to-video · **start frame only** · 1 output per request · 9:16 · **generate_audio: false** · draft **480p** → final **1080p** via Seedance finalize **within 7 days** of the draft.
  - A1: 5 s. A2: 10 s, or 2 × 5 s.
  - Record the seed of each approved draft.
  - Paste the negative list as the last line, starting "Avoid:", if the UI has no negative field.
- **Why there is no end frame by default:**
  - The natural end frame is an empty basket. We don't have one, and making it needs an AI image edit of `sf-02` (remove all boxes and ribbon). That is 0.5 credits at medium 1K, plus 2.75 at high 2K for the final, and it must go through `amie-visual-qa`.
  - It has no labels, so the edit itself is low risk. But a start frame and an end frame that are this different often make the model **cross-fade or melt** the boxes away instead of carrying them out.
  - Use an empty-basket end frame **only** if the start-only draft stops half-way, invents new boxes or drifts the camera. It goes on A2 (and A2b), never on A1.
- **Kling 4.0 (backup, after 2 failed Seedance drafts on a clip):**
  - Same start frame and same prompt, with the negative list in Kling's negative field.
  - 5 s / 10 s (supported durations: VERIFY), 9:16, audio off.
  - Tier names and credits: MISSING.
- Max 2 drafts per clip, as the storyboard says. After that, use the free fallback (§5).

### 2.3 Hands brief (applies to A1 and A2)
- **Look:**
  - A woman's pair of hands with neat, short-to-medium natural nails in a nude or sheer finish.
  - No jewellery (at most one minimal thin ring).
  - Plain **long sleeves** in soft ivory knit visible at the wrists. This keeps the look modest, and the sleeve visibly entering from the frame edge anchors each hand to the edge.
- **Entry and exit:**
  - Hands enter and leave **only across the frame edges**: left, right and bottom.
  - The sleeve must stay connected to the edge the whole time. A hand never appears or disappears in the middle of the frame.
- **Count:**
  - **Never more than two hands** in frame.
  - A1 uses both hands.
  - In A2, the right hand removes the right-column boxes through the right edge and the left hand removes the left boxes through the left edge, with one hand per box. The other hand stays out of frame.
- **Grip:**
  - Fingers hold a box by its side edges, with the thumb on one side and the fingers on the opposite side.
  - Each finger stays on the box surface and never sinks into it.
  - A hand covering part of a label is fine (library rule 4: a hidden label is fine).
- **Pace:** slow, calm, deliberate, with a short still pause after each box leaves.

### 2.4 Prompt A1: ribbon off (paste as is)
```
Locked-off top-down photo, camera perfectly still for the whole shot: a black wire basket on a pale stone surface, filled with white a'mie product boxes, tied with a deep burgundy satin ribbon printed "GLOW FRIDAY" in white sans-serif letters, the bow knot at the centre. Soft, even daylight from above, soft shadows, exactly as in the start frame.
Action, slow and calm: a woman's pair of hands with neat short natural nails, nude polish, no jewellery, ivory knit sleeves at the wrists, enters from the bottom edge of the frame, the left hand from the lower left and the right hand from the lower right, sleeves always connected to the frame edge. The right hand gently pulls one ribbon tail so the bow loosens and opens; both hands then lift the loose ribbon smoothly up and away and carry it out through the bottom edge of the frame. The hands leave the frame completely. The last second is a still frame: the basket full of boxes, no ribbon, no hands.
Exactly two hands, five fingers each, always separate; fingers touch only the ribbon and never pass through any box. The boxes do not move: every box keeps its exact position, size, orientation and printed label ("Lemongrass", "WHIPPED BODY BUTTER", "250 ML", "BODY GLOW", "120ML", "Hand Cream", "Sleek Secret", "Lip Plump", the a' monogram). Nothing falls or drops. No new objects, no text generation, no logo. Calm, slow, premium mood.
```

### 2.5 Prompt A2: boxes out (paste as is; start frame = A1's last frame)
```
Locked-off top-down photo, camera perfectly still for the whole shot: a black wire basket on a pale stone surface, filled with plain white a'mie product boxes, no ribbon. Soft, even daylight from above, soft shadows, exactly as in the start frame.
Action, slow, calm and evenly paced, one box at a time with a short still pause after each: a woman's hand with neat short natural nails, nude polish, no jewellery, ivory knit sleeve at the wrist, enters from the nearest side edge of the frame, grips one box by its side edges, lifts it just clear of the basket and carries it flat out through the same edge, keeping the box the same size and the same way up. Order: the right hand takes out the tall slim box at top centre-right, then the tall slim box at the far right top, then the slim box at the far right bottom, then the tall box in the centre, each through the right edge; then the left hand takes out the large square box at top left, then the box in the left middle, then the large flat box at bottom left, each through the left edge. The last second is a still frame: the empty black wire basket on pale stone, no boxes, no hands.
Never more than two hands in frame, five fingers each, sleeves always connected to the frame edge; hands never appear in the middle of the frame. Fingers stay on the box surface and never pass through a box; boxes never pass through each other or through the basket wires. Each box keeps its own printed label while it moves ("Lemongrass", "WHIPPED BODY BUTTER", "250 ML", "BODY GLOW", "120ML", "Hand Cream", "Sleek Secret", "Lip Plump", the a' monogram) and is never duplicated or replaced. The basket never moves or bends. Nothing falls or drops. No new objects, no text generation, no logo. Calm, slow, premium mood.
```
_A2a / A2b split:_ use the same prompt and keep only the boxes for that clip in the "Order:" sentence.
- A2a's last-second line reads "the basket with only the large square box at top left, the box in the left middle and the large flat box at bottom left".
- A2b's last-second line keeps "the empty black wire basket".

### 2.6 Negative list A
```
warped text, garbled letters, extra hands, extra fingers, morphing packaging, melting labels, new logos, added text or watermark, colour shift of ribbon or bag, product resizing, camera shake, fast motion, flicker, third hand, sixth finger, fused or merged fingers, merged hands, hands appearing in the middle of the frame, floating hand without arm, hand passing through box, fingers sinking into box, box passing through basket wires, box changing label, box duplicating, box vanishing or dissolving, new boxes appearing, ribbon lettering redrawn, "GLOW FRIDAY" misspelled, ribbon turning pink or rose, rings, bracelets, watch, long acrylic nails, bright nail colour, bare forearms, objects falling, dust, camera zoom, camera rotation, basket moving, logo appearing at the bottom
```

### 2.7 What QA must check (`amie-visual-qa`, on the reversed and the raw clip)
1. **Hands:**
   - Step through every 0.25 s, and every frame while a hand touches a box or the ribbon.
   - Exactly ≤2 hands, 5 fingers each, no merged hands.
   - Each sleeve stays connected to the frame edge, and no hand enters or leaves mid-frame.
   - No fingers inside a box and no box passing through a hand.
   - **Any extra finger or limb, even for 1 frame at 1×, is a reject.**
2. **Labels:**
   - Zoom 100% on every box in its last still pose (after reversal: when it is set down) and compare with `sf-02-basket.png`.
   - "Lemongrass / WHIPPED BODY BUTTER / 250 ML", "BODY GLOW / 120ML", "Hand Cream", "Sleek Secret", "Lip Plump", the «a'» monogram and «a'mie».
   - A box must never turn into another product (for example "Lavender") or show a different size.
   - Soft text mid-motion is acceptable. **Wrong readable words are not.**
3. **Box count and identity:** 7 boxes, no duplicates, no new boxes. The empty-basket frame is really empty (no ghost box, no leftover ribbon scrap).
4. **Ribbon (A1):**
   - "GLOW FRIDAY" stays spelled right whenever it is readable, and is fully correct in the last 1.5 s before the landing.
   - It stays deep burgundy, never pink or rose.
5. **Scale:** every box keeps its size relative to the others. Body Glow stays ≈2× the Hand Cream box height.
6. **Basket and camera:** no wire bending, no basket drift, no zoom or rotation, light stays constant.
7. **Join (A2_rev → A1_rev):** no jump in box positions and no flash at the dissolve.
8. **Reverse read:**
   - Watch the reversed cut at full speed.
   - Hands must read as *placing*, not as being pulled backwards.
   - Nothing must look like it is flying up against gravity.
9. **Landing:** the dissolve into the real `sf-02` frame shows no visible pop in box positions.

---

## 3. Version B: no hands, magical stop-motion

### 3.1 One generation
- **Clip B:** ribbon off, then the 7 boxes out, from `sf-02-basket.png`. 10 s raw.
- If 10 s is not offered (VERIFY), split it like A:
  - **B1:** ribbon off, 5 s.
  - **B2:** boxes out, 5 s, starting on B1's last frame.
  - Join them as in A, by reversing both and putting B2_rev before B1_rev.
- **Stop-motion feel:** the prompt asks for crisp start-and-stop timing per box. The **stepped cadence** is added locally, after reversal, by dropping to 10–12 fps and holding frames (`fps=12,fps=30`).
  - Asking a video model for "stop-motion" directly tends to make the whole frame jitter and the labels "boil", which is the opposite of what QA needs.
  - Smooth generation plus local stepping is free and fully controllable.

### 3.2 Model and settings
- **Seedance 2.5 (first):**
  - image-to-video · **start frame only** · 1 output · 9:16 · 10 s (or 2 × 5 s) · generate_audio false · draft 480p → final 1080p within 7 days.
  - Record the seed.
- **End frame:** same logic as A §2.2. Start-only first. The empty-basket plate (0.5 / 2.75 credits, through `amie-visual-qa`) is only for a retry if the boxes melt away instead of gliding out.
- **Kling 4.0 (backup):** same start frame and prompt, with the negative list in its negative field. 10 s or 2 × 5 s (VERIFY), 9:16, audio off. Credits: MISSING.

### 3.3 Prompt B (paste as is)
```
Locked-off top-down photo, camera perfectly still for the whole shot: a black wire basket on a pale stone surface, filled with white a'mie product boxes, tied with a deep burgundy satin ribbon printed "GLOW FRIDAY" in white sans-serif letters, the bow knot at the centre. Soft, even daylight from above, soft shadows, exactly as in the start frame. No hands, no people anywhere.
Magical object animation, as if moved by an invisible force, with crisp, evenly timed moves: each object starts and stops cleanly, with a short still pause between objects. First the bow unties itself: the loops shrink and the knot opens, and the ribbon slides away smoothly in straight lines out through the frame edges, the horizontal band to the left and right edges, the vertical band and the tails to the top and bottom edges. Then, one box at a time, each box rises just slightly, keeping its size and keeping the same side up, and glides flat out through the nearest side edge: the tall slim box at top centre-right, the tall slim box at the far right top, the slim box at the far right bottom and the tall box in the centre go out through the right edge; the large square box at top left, the box in the left middle and the large flat box at bottom left go out through the left edge. The last second is a still frame: the empty black wire basket on pale stone.
Each box keeps its own printed label while it moves ("Lemongrass", "WHIPPED BODY BUTTER", "250 ML", "BODY GLOW", "120ML", "Hand Cream", "Sleek Secret", "Lip Plump", the a' monogram) and is never duplicated, replaced or dissolved; boxes never pass through each other or through the basket wires. The ribbon stays deep burgundy. The basket never moves or bends. Nothing falls, bounces or spins. No new objects, no text generation, no logo. Calm, precise, premium mood.
```

### 3.4 Negative list B
```
warped text, garbled letters, extra hands, extra fingers, morphing packaging, melting labels, new logos, added text or watermark, colour shift of ribbon or bag, product resizing, camera shake, fast motion, flicker, hands, fingers, arms, people, shadow of a hand, box changing label, box duplicating, box vanishing or dissolving, box fading out, new boxes appearing, boxes spinning or flipping, box passing through basket wires, boxes colliding, ribbon lettering redrawn, "GLOW FRIDAY" misspelled, ribbon turning pink or rose, ribbon tangling, sparkles, glitter, magic particles, glow effects, objects falling, camera zoom, camera rotation, basket moving, frame jitter, logo appearing at the bottom
```

### 3.5 What QA must check
1. **No people:** no hand, finger, arm or hand shadow in any frame.
2. **Boxes leave physically:**
   - Each box exits *through an edge*, with no fade-out, melt or pop.
   - After reversal, each one slides in and settles, it does not "materialise".
   - Box count: 7, with no duplicates.
3. **Labels:** same check as A item 2 (100% zoom on each box's settled pose against `sf-02`).
   - In B, check also the frame where each box *starts* moving (after reversal: where it stops). That is where a stop-motion step holds longest and any label error stays on screen for 3 frames.
4. **Ribbon:**
   - "GLOW FRIDAY" correct whenever readable, and fully correct in the last 1.5 s.
   - Burgundy, not rose.
   - The self-tying bow, after reversal, ends exactly in the real bow shape (the landing dissolve covers only small differences).
5. **No magic effects:** no sparkles or particles. The magic comes only from the motion.
6. **Stepping:** after the local `fps=12` pass, the labels must not strobe and the steps must look even. If they strobe, try `fps=10` or skip the stepping on the settle frames.
7. **Basket, camera and light:** as in A item 6. Then do the landing check.

---

## 4. Local post (free; same for A and B, differences noted)
Use the file names below, or adjust them. Get each length with `ffprobe -v error -show_entries format=duration -of csv=p=0 FILE`. `reverse` buffers the whole clip in RAM: a 10 s 1080p clip needs about 1 GB, so split it first if memory is short.

```bash
cd /home/user/amie-marketing-agents/content/campaigns/2026-11-glow-friday/video

# 1 · Reverse (and normalise to the edit spec: 1080x1920, 30 fps, no audio)
ffmpeg -i A1.mp4 -vf "reverse,fps=30,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p" -an A1_rev.mp4
ffmpeg -i A2.mp4 -vf "reverse,fps=30,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p" -an A2_rev.mp4
#   Version B: same command on B.mp4 -> B_rev.mp4 (one clip, so skip step 2)

# 2 · Version A only: join boxes-in (A2_rev) then ribbon-tie (A1_rev), 4-frame dissolve
ffmpeg -i A2_rev.mp4 -i A1_rev.mp4 -filter_complex \
 "[0:v][1:v]xfade=transition=fade:duration=0.13:offset=<A2_rev_len-0.13>[v]" -map "[v]" -an A_build.mp4

# 3 · Speed ramp: the boxes part is faster (about 1.5x A, about 1.3x B); the ribbon tie stays at 1x
#     T = time where the ribbon starts entering (read it off the reversed clip)
ffmpeg -i A_build.mp4 -filter_complex \
 "[0:v]trim=0:T,setpts=(PTS-STARTPTS)/1.5[a];[0:v]trim=T,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[v]" \
 -map "[v]" A_ramp.mp4
#     For a smooth ease into the tie, do the ramp as a speed curve in CapCut instead (same target timings as the beat sheet).
#     Then retime each box so it settles on a beat (0.5 s grid, 120 BPM).

# 3b · Version B only: stop-motion stepping on the moving part (before the landing)
ffmpeg -i B_ramp.mp4 -vf "fps=12,fps=30" -an B_step.mp4

# 4 · Land on the REAL photo + 1 s hold: 0.2 s dissolve from the generated last frame into sf-02, then 1.0 s still
ffmpeg -i A_ramp.mp4 -loop 1 -t 1.2 -i start-frames/sf-02-basket.png -filter_complex \
 "[1:v]fps=30,format=yuv420p,setsar=1[s];[0:v]setsar=1[v0];[v0][s]xfade=transition=fade:duration=0.2:offset=<A_ramp_len-0.2>[v]" \
 -map "[v]" -an A_landed.mp4
#   (B: input B_step.mp4 -> B_landed.mp4)
```

**Why step 4 matters:** the generated first frame (our last frame after reversal) is a re-render of the photo and is softer at 480p. Dissolving into the actual `sf-02-basket.png` makes the hold pixel-true.

### 5 · Hand-off into the hero loop and the end card
1. **Hero loop:**
   - Append the first 2 s of `content/campaigns/2026-11-glow-friday/hero/glow-friday-hero-mobile-9x16-notext.mp4` with a 0.2 s dissolve.
   - Its framing matches `sf-02` (poster checked: same basket position). VERIFY by overlaying its first frame on `sf-02` at 50% opacity.
   - This loop has the «a'mie» logo baked at the bottom, so the dissolve doubles as the logo fade-in.
   - Put the optional phase super from the beat sheet here.
2. **End card (S6, local, 0 credits):**
   - Freeze the loop's last frame, then blur and darken it (or use `start-frames/ec-bg.jpg`).
   - Fade the text up line by line on the beat (0.5 s steps), with the logo last.
   - Readex Pro (AR) and Montserrat (EN).
   - **Copy only from `onscreen-copy-reviewed.md`:** default L2 «أسعار خاصة على منتجات مختارة» / "Special prices on selected items", with no %. During 18–23 Nov use the teaser card instead.
   - `{{MIN}}/{{MAX}}` stays off until the MoC licence and Saleh's numbers are confirmed.
3. **Grade:** as in storyboard §8 (low saturation, burgundy protected).
4. **Export:** 1080×1920 H.264, 30 fps, bt709, with the music added in the edit.
5. **Review:** export → `amie-visual-qa` (frames at 0.5 s steps, plus the hand and label checks above) → `amie-reviewer` (supers) → human.

---

## 5. Free fallback (if both versions fail QA twice)
- **Best for A, honestly:** a **real phone shoot of the same reverse trick**.
  - Lock a phone overhead on the same stone, with the real basket, boxes and ribbon.
  - Film a team member slowly untying and unpacking, then reverse locally.
  - It costs 0 credits and gives real hands and real labels.
  - Storyboard §11.9 already says hand actions such as "untying the ribbon" should be shot rather than generated.
- **Minimal option:** the existing hero loop alone (storyboard S2 fallback).

---

## 6. Risk: A vs B, and which to draft first

Version A carries clearly more risk:
- Hands are the #1 failure in this repo (storyboard §11.1, library rule 4), and a hand untying a satin bow is about the hardest motion a video model is asked to do.
- A also needs two generations and a join. That roughly doubles the credits, doubles the chances of failure, and adds the cost of finalizing A1 before A2 can be drafted on a sharp frame.
- Every box removal is a new chance for a sixth finger or for fingers sinking through cardboard.
- It also goes against the storyboard's own advice to shoot hand actions for real rather than generate them.

Version B removes the hand risk entirely and runs as one clip. Its real risks are:
- boxes dissolving or popping out instead of gliding through an edge;
- a box's label changing mid-glide;
- the ribbon lettering re-drawing as it slides.

The reverse trick protects both versions at the end, because the last second is the real photo either way.

**If credits allow only one draft, generate B first.** It is cheaper, it has fewer failure modes, and its stop-motion cadence hides small label wobble. If A's hand look is still wanted afterwards, the phone shoot in §5 gets it at zero credits with real labels.
