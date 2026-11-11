# Glow Friday «السلة» reel, v1 (2026-11-11)

9:16, 1080×1920, 20.7 s, no audio. Draft for approval. Idea: every real moment of use puts its product in the basket; the ribbon ties at the end and the basket becomes the site hero.

| # | Time | Shot | Source | Text |
|---|---|---|---|---|
| 1 | 0.0–1.9 | Model on the giant Lemongrass jar | Real shoot, library #2 | GLOW FRIDAY · سلّتك جاهزة؟ |
| 2 | 1.9–3.2 | Empty basket | Made: AI plate of the real photo | نعبّيها لك |
| 3 | 3.2–4.7 | Model holding the Lemongrass jar | Real shoot, #24 | للجسم |
| 4 | 4.7–5.8 | Monogram + Lemongrass boxes drop in | Made: local stop-motion, real boxes | — |
| 5 | 5.8–7.3 | Sleek Secret on hair | Real UGC, #12 | للشعر |
| 6 | 7.3–8.4 | Sleek Secret box drops in | Made | — |
| 7 | 8.4–9.9 | Body Glow + Chocolate close-up | Made: approved still with a slow push | للّمعة |
| 8 | 9.9–10.7 | Body Glow box drops in | Made | — |
| 9 | 10.7–12.1 | Lip Plump | Real UGC, #25 | للشفايف |
| 10 | 12.1–13.2 | Lip Plump + Hand Cream boxes | Made | — |
| 11 | 13.2–15.8 | Ribbon ties, light sweep | Made; last frame is the real photo | GLOW FRIDAY |
| 12 | 15.8–17.5 | Real a'mie shopping bag | Real, #14 | — |
| 13 | 17.5–20.7 | End card = site hero loop | Made locally | 20% to 40% off on selected items |

## How it is built
- `tools/video/basket_build.py`: the basket build-up. Boxes and labels are pixels of the real photo. Higgsfield made only two plates (empty basket; boxes without ribbon), 1.5 credits each, and the no-ribbon plate is used only under the ribbon footprint.
- `tools/video/glow_friday_basket_reel.py`: cuts the real clips (Drive proxies, see `drive-video-library.csv`), adds the overlays and joins everything.
- `overlays/`: text PNGs, rendered from `ov.html` with `node ov.js`.

## Open before publishing
- New on-screen lines («سلّتك جاهزة؟», «نعبّيها لك», «للجسم / للشعر / للّمعة / للشفايف») need `amie-reviewer` and a human OK.
- The end card says 20–40%. The reviewer's rule still stands: confirm the MoC discount licence and Saleh's numbers, or switch to «أسعار خاصة على منتجات مختارة».
- Real clips are 720p proxies. For the final, re-cut from the Drive originals at 1080p.
- Shots 5 and 9 are creator UGC: confirm usage rights for ads. Shot 7 shows bare shoulders (modesty decision).
- Music is not included. Add a licensed or in-app track (about 120 BPM; cuts land every ~1.3 s).
- The middle-left hidden box under the bow was drawn by the AI and its print was removed. Confirm which product it is.
