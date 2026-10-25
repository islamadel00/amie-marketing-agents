# 04 — Social (Instagram) and influencers

Period: 2026-05-01 to 2026-10-24. Sources: Instagram Insights (IGI, @amie__sa, via Supermetrics; read-only) and the influencer tracking workbook (sheets "حجوزات و أداء المؤثرين" + "Copy of …"). No transfer/shipping sheets were opened, and no personal or bank data was copied. Data: `data/ig_*.csv`, `data/influencers_clean.csv`.

## Part A — Instagram

### Account, monthly

| Month | Reach | Views (account-wide) | Accounts engaged | Follows | Unfollows | Net | Posts (R/C/I) |
|---|---|---|---|---|---|---|---|
| May | 52,848 | 409,461 | 1,501 | 637 | 248 | +389 | 14 (5/4/5) |
| Jun | **175,353** | **819,399** | 1,512 | 666 | 218 | +448 | 15 (1/10/4) |
| Jul | 49,097 | 433,197 | 1,043 | 601 | 228 | +373 | 17 (3/10/4) |
| Aug | 37,383 | 331,372 | 1,818 | **954** | 205 | **+749** | 5 (1/4/0) |
| Sep | 52,151 | 297,613 | 904 | 413 | 191 | +222 | 9 (6/1/2) |
| Oct 1–24 | 9,642 | 217,965 | 983 | 310 | 169 | +141 | 9 (3/5/1) |

R/C/I = reels/carousels/images.

- Followers on 24 Oct: **35,293** (443 posts). Net growth over the period was about **+2,322**, so the account started at roughly 32,970 (+7%).
- Clicks to the website are close to zero in the data. Bio-link clicks attributed to posts were 44 / 11 / 116 / – / 8 / 0 by month. Profile contact taps were Call 229 and Email 35. The API returned no website-tap breakdown.
- Stories: the API only returns stories that are live now (6 on 24–25 Oct, about 400 views and 312–354 reach each). There is **no story history** for the period.

### Content: 69 feed posts and reels (≈2.7 per week)

| Format | n | Median reach | Median views | Median ER (by reach) | Saves/post | Shares/post |
|---|---|---|---|---|---|---|
| Carousel | 33 | 2,437 | 4,922 | 2.25% | 19.3 | 15.1 |
| Image | 16 | 2,424 | 4,124 | 1.97% | 18.3 | 35.0 |
| Reel | 19 | 2,310 | 2,624 | 1.86% | 15.5 | 11.4 |

The giveaway post is excluded from this table. ER = (likes + comments + saves + shares) / reach.

Reels do not beat static posts here. The median reel gets fewer views than the median carousel (2.6k vs 4.9k), so the reels are not being pushed by the algorithm.

By product theme (median reach / ER): **Tan range** (Red Cherry, Deep Tan, Glittery Gold; 19 posts) 3,168 / 2.45%, with the most saves (25.5/post). Body highlighter/glow (16) 2,152 / 2.21%. Body care scrub/butter (7) 2,437 / 2.09%. Hair (7) 2,421 / **1.61%, the weakest**. Lip (3) and fragrance (2) are too few posts to judge.

**Best posts**

| Date | Format | Reach | ER | What it shows |
|---|---|---|---|---|
| 21 May | Image | **22,995** | 4.4% | "coffee can wait… but this glow?" bronzed summer-tan lifestyle. 213 profile visits, 14 follows. Likely boosted |
| 16 Aug | Carousel | 4,880 | 126% | Dream Bundle giveaway (follow + comment + tag). 3,325 comments, 2,247 shares. Drove the August follower spike |
| 22 Jun | Carousel | 6,114 | **4.6%** | Red Cherry tan, "Catch the Sun. Wear the Glow". 89 saves, 132 shares |
| 2 Sep | Reel | 6,957 | 1.7% | Back to Routine collection |
| 4 Oct | Reel | 5,337 | 1.8% | Into The Glow bundle (glow gel + highlighter) |

**Worst posts.** The four lowest-reach posts all came in October: 547–783 reach (Into The Glow, body glow, lavender butter). The lowest ER went to the hair wax stick image (0.58%), the Red Cherry/Deep Tan "summer dump" (0.64%) and the highlighter shade-guide reel (0.75%). Posts with a tagline only and no product benefit get few saves.

**Trend.** Median ER holds flat at about 2% every month (May 2.33%, Oct 2.09%). Median reach per post halved from 2,831 in July to 1,386 in October. Posting fell from 15–17 a month in May–July to 5–9 a month from August. Engagement per follower is very low: the median post reaches only about 7% of followers, and ER by followers is 0.14%.

### Audience vs target (Saudi women 18–35)

| Dimension | Value |
|---|---|
| Country | Saudi Arabia 83.2%, other GCC 9.2% (Kuwait 4.9%, UAE, Qatar) |
| City | Riyadh 37.5%, Jeddah 20.1%, Dammam/Khobar/Dhahran 7.7%, Mecca 2.6%, Medina 2.2% |
| Gender | Female 47.5%, male 3.7%, **unspecified 48.8%**. Of known gender, 92.6% are female |
| Age | 18–24 10.3%, **25–34 48.4%**, 35–44 31.3%, 45+ 9.8% |

Country and gender fit the target well. On age, only about **59% of followers are 18–34**. The core is 25–34, with a large 35–44 group, and 18–24 is under-represented at 10%.

## Part B — Influencers

`influencers_clean.csv` has 141 rows. After removing 7 duplicates, 133 remain. One "influencer" row is a photo shoot (Anas, 2,127 SAR, booked) and is excluded from the counts below.

| Status | Count | Notes |
|---|---|---|
| Executed ("تم الإعلان") | **21** | 11 paid, 10 UGC/gifted |
| Booked ("تم حجز موعد") | 6 | Shuroq and Shaimaa on monthly lifestyle contracts (5,000 and 4,000), Ghadi 9,500 (27/28 Oct), Sara Bugnah 9,200, Hessa Alsudais 9,375, Maylan (UGC) |
| Quotes (no status) | 59 | 53 proposed, 6 rejected; 57 have a price |
| Seeded, no post logged | 46 | UGC product gifts with no status recorded |
| Approved, no status | 1 | Nancy, 1,500 |

**Cash spent on executed creators: 147,401 SAR**, or **130,151 SAR** if Yasmeen's second 17,250 entry turns out to be a duplicate. Two coded creators (aya, FHD) have cost "؟", so the real total is higher.

**Codes.** 9 executed creators had codes. Sales are logged for 6 of them, totalling **59,272 SAR**.

| Creator (platform) | Code | Cost SAR | Sales SAR | ROAS |
|---|---|---|---|---|
| Lulu Albudaiwi (Snap) | lulu | 34,500 | – (sheet: 0) | 0 |
| Style Najla (Snap) | NAJLA | 34,500 | not logged | – |
| Yasmeen Aldakheel (Snap) | Y10 | 17,250 | 16,320 | 0.95 |
| Fatina Hunaidi (Snap) | FTD | 13,800 | 14,013 | 1.02 |
| Raghad (TikTok, KW) | RGD10/RGD20 | 11,101 (900 KWD) | not logged | – |
| Shaimaa (Snap) | sh10 | 3,000 | 6,066 | **2.02** (only promoted post besides Raghad) |
| Shuroq (TikTok) | SH | 3,000 | 5,355 | **1.79** |
| Aya Jamal (Snap) | aya | ? | 16,459 | – |
| Fahda (Snap) | FHD | ? | 1,059 | – |

The coded creators cost 117,151 SAR in known cash and returned 59,272 SAR in logged code sales, a blended ROAS of **0.51**. The two creators who cost 3,000 SAR each returned about 2×. The 34,500 SAR creators returned nothing that was logged.

**Quote prices** (57 priced, VAT added where "+ ضريبة"): range **400–45,000 SAR**, median 9,000, mean 10,921. By band: under 5k: 18, 5–15k: 24, 15–25k: 11, 25k and over: 4 (Shaden 45k, Dalal 28.75k, Yara Alnamlah and Dana Tamim ≈23k).

**Instagram measurability.** None of the 21 executed creators has an Instagram profile link. The links show 9 TikTok, 7 Snapchat, 1 X and 4 with no link. As a result, no IGPD2 profile pull was possible. Instagram links appear only on 10 quote rows.

## Data quality issues

- **Date swaps (10 fixed, all flagged).** Day/month inversions: 02-08→08-02, 05-08→08-05, 11-08→08-11, 12-08→08-12, 02-09→09-02, 03-09→09-03 (×2), 06-09→09-06, and Najla 05-10→10-05 (the glow package launched 24 Sep). The text date "17-7-2026" was normalised. aya/FHD "2026-05-01" may be 5 Jan and were kept with an "uncertain" flag.
- **Platform column unreliable.** On 46 rows the "Platform" column disagrees with the profile link (for example, "TikTok" rows that link to Snapchat). Platform was therefore taken from the link.
- **Duplicates removed (7):** Shuroq row 18, Nouf ×2, Latifa, Reema/ريما, Alanoud Alfallaj quote, Shahad Almuhanna/Alhanna. Yasmeen's 17,250 SAR entries on 27 Jun and 2 Aug are flagged as a possible duplicate and kept.
- **Conflicts and gaps.** Raghad's code is RGD10 in the main sheet and RGD20 in the Copy sheet. Her cost is 900 KWD, which is 10,980 SAR at ×12.2, but the sheet records 11,101 SAR. Two costs are "؟". The ROAS formulas show #DIV/0!. 46 gifted UGC rows have no post status.
- **Instagram data.** October reach (9.6k) is out of line with views (218k), which suggests "views" includes paid or boosted delivery. The June reach spike (175k) cannot be explained from organic posts alone, and paid data is outside this file. Story history is unavailable. Follows/unfollows come from the API's `follow_type` split (FOLLOWER = follows, NON_FOLLOWER = unfollows); this reading is confirmed by the daily new-follower sum for October (310).

## What stands out

- **Influencer money is concentrated in two 34,500 SAR Snapchat posts with no logged sales.** Meanwhile 3,000 SAR mid-tier creators (Shaimaa, Shuroq) returned about 2×. Logged code ROAS across coded creators is 0.51.
- **Instagram reach is shrinking while engagement quality holds.** ER stays at about 2%, but median reach per post halved from July to October as posting dropped from about 16 to 5–9 posts a month.
- **The tan range is the content winner.** It has the highest reach, ER and saves, and its 21 May image (23k reach) is the account's best post. Hair content is the weakest.
- **The giveaway worked for growth.** It produced August's +749 net follows (about 2× a normal month), but gross new follows have since dropped to about 13 a day in October.
- **The audience is Saudi and female but older than the target.** 25–44 makes up 80% of followers and 18–24 only 10%. Instagram also sends almost no traffic to the store (bio-link clicks in the double digits per month).
