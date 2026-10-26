# Live ad links: findings and fixes (26 Oct 2026)

Source: Claude Desktop check (`2026-10-26-ad-links-check-desktop.md`, run from a US server) + Supermetrics spend for 19–25 Oct. Nothing has been changed in any account. Every fix below needs approval and is done inside the ad platform or Zid.

## Fix today
| # | What | Where | Why |
|---|---|---|---|
| 1 | Pause Singleimage-21–NDV-PDP, SingleImage-ND-03-PDP, SingleImage-ND-04-PDP | Meta | Creative says "Code: ND96 20%" + national day. ND96 expired 10 Oct in Zid. ~868 SAR/week, 2 purchases. NDV-PDP also says "بدون حروق أو تصبغات" (forbidden claim). |
| 2 | Change link of SingleVideo-UGC-12-PDP from `/ar-eg/products/into-the-glow-collection` to `/products/into-the-glow-collection` | Snapchat | `/ar-eg/` shows the price in Egyptian pounds (4,348.73 ج.م). |

## This week
| # | What | Where | Why |
|---|---|---|---|
| 3 | Stop Google sending clicks to `/ar-us/`, `/ar-fr/`, `/ar-ae/`, `/ar-gb/`, `/ar-de/`, `/ar-jo/` (URL exclusions in PMax, check Merchant Center feed links, review Zid markets/currencies) | Google Ads / GMC / Zid | Those prefixes force USD, EUR, AED. ~65+ clicks/week on `/ar-us/` alone. |
| 4 | Move PMax away from the tanning category; stop ads to Summer Set (SingleVideo-08 on Meta, SingleVideo-UGC-02/06 + SingleImage-12 on Snap) | Google / Meta / Snap | Season is over; Red Cherry (part of Summer Set) shows "نفذت الكمية". Tanning category is PMax's biggest spend (410 SAR/week). |
| 5 | Plan to stop the RGD20 TikTok ad on 31 Oct | TikTok | Caption says national-day offers; code RGD20 ends 31 Oct. |
| 6 | Add UTM to Meta Carousel Ad (`/products`) and Snap Scrub IMG/Vid, Lavender collection IMG, Chocolate highlighter | Meta / Snap | No UTM, so GA4 can't attribute them. |

## Site fixes (Zid, need approval)
- Badge typo "نفذت الكمية" → "نفدت الكمية".
- Chocolate Highlighter Set description: "تجمع هذه المجموعة بين وفرشاة المكياج" is missing a word.
- Store title shows "A.mi" in the browser tab.
- Homepage still has "الصيف يبدا من ايمي".

## Lower risk, note for creative team
- Instagram video (hair products) shows Jordan/Nike logos; tan video shows a Vilebrequin bag. Avoid other brands' logos in paid creative.
