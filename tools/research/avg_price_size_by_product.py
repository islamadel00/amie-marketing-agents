"""Double-check: average competitor selling price and pack size per a'mie product.

Rows come from the three price files in research/market-2026-11 (all dated 2026-11-03):
  V = 07-competitor-prices-verified.csv  (product page opened)
  M = 07-marketplaces-top5.csv           (top search results on noon, amazon.sa, nahdi, al-dawaa, watsons, sephora)
  S = 06-saudi-competitors-social.csv    (Saudi brands' own stores)
  W = page opened again on 2026-11-14 (web re-check); prices shown in USD were converted at 3.75
Each row: (source, brand, product, size, unit, price_now, price_regular, flag)
price_now = what the shopper pays today (promo price if one is shown).
One row per competitor product; the same product at two retailers is averaged.
Left out: results marked not matching, sets, face products, multi-packs, and luxury outliers.
"""
import csv, statistics as st, sys

OUT = sys.argv[1]
N = None
P = {  # a'mie product: (size, unit, price, [rows])
"Deep Tan (زيت تان)": (150, "ml", 159, [
 ("W","Carrot Sun","Oil Gold",200,"ml",104.65,161,"price changed since 3 Nov (was 80.5)"),
 ("W","Carrot Sun","Sun Tan Oil Papaya",200,"ml",104.65,161,"price changed since 3 Nov (was 80.5)"),
 ("V+M","Carrot Sun","Carrot Spray (Desertcart 64, Amazon 40)",200,"ml",52,82,"import"),
 ("V","Beesline","Suntan Oil Gold",200,"ml",92,184,""),
 ("V+M","Beesline","Deep Tan Carrot (Chefaa 83.95, Amazon 21.42, Nahdi 31.05)",200,"ml",45.5,70.6,""),
 ("V","Beesline","Brown Tan Dry Feel Oil",N,"ml",109,109,""),
 ("V","Mia","Brown Tan Dry Feel Oil",150,"ml",65,65,""),
 ("M","Cocosolis","Aloha tanning oil",110,"ml",50.91,227.65,""),
 ("M","Zona","Tanning oil",150,"ml",96,129,""),
 ("M","Eight Fifty","Tanning oil",N,"ml",160,160,""),
 ("M","Tango","Tan oil",N,"ml",38,38,""),
 ("M","Hawaiian Tropic","Coconut tanning oil",200,"ml",57.12,63,""),
 ("M","Calypso","Deep tanning oil SPF30 spray",200,"ml",31.4,52.26,""),
 ("M","Eveline","Amazing Oil tan SPF10",150,"ml",37.95,63.25,""),
 ("M","Babaria","Luminous tanning oil",100,"ml",31.05,51.75,""),
 ("M","Lancaster","Golden Tan Maximizer oil",N,"ml",220,220,""),
 ("W","Surge","Deep tanning oil",250,"ml",195,195,"saudi"),
 ("W","Waves Beauty","Tanning Oil",250,"ml",156.52,156.52,"saudi; out of stock"),
 ("W","Besito Body","Bosat Shams",N,"ml",96,150,"saudi; price changed since 3 Nov (was 150)"),
 ("W","Ladeena","Kissed by the Sun tanning spray",250,"ml",140,140,"saudi; new"),
 ("W","Waves Beauty","All Over Tanning Spray",100,"ml",156.52,156.52,"saudi; new"),
 ("S","Sunkissed.sa","Lions tan gold oil",N,"ml",199.99,220,"saudi"),
]),
"Red Cherry (كريم تان)": (200, "ml", 199, [
 ("V","Carrot Sun","Tropical Fruit Tanning Cream",350,"ml",115,115,""),
 ("V","Carrot Sun","Tanning Accelerator",350,"ml",164,164,"import"),
 ("M","Carrot Sun","Watermelon cream (Noon 103.35, Amazon 39.5, Nahdi 80.5)",350,"ml",74.5,110.9,""),
 ("M","Carrot Sun","Cocoa butter cream",N,"ml",77.9,115.92,""),
 ("M","Carrot Sun","Carrot cream oil (Amazon)",350,"ml",53,68,""),
 ("M","Carrot Sun","Cherry Bomb cream",350,"ml",115,115,""),
]),
"Glittery Gold (جل تان)": (120, "ml", 149, [
 ("V","Carroten","Tan Express Intensive Gel",150,"ml",143,143,"import"),
 ("M","Babaria","Bronze jelly coco",75,"ml",31.05,51.75,""),
 ("M","Babaria","Exotic bronze jelly",300,"ml",48.3,80.5,""),
 ("M","Babaria","Tropical jelly",300,"ml",55.2,92,""),
 ("M","(no brand)","Coconut tanning accelerator gel",N,"ml",60,80.5,""),
 ("W","Surge","Glitter Tan",250,"ml",207,207,"saudi; size found"),
]),
"Body Glow (لمعة الجسم)": (120, "ml", 176, [
 ("V","Anastasia Beverly Hills","Shimmer Body Oil",N,"ml",96.1,174.75,""),
 ("V","Tan-Luxe","The Glow Body Oil",80,"ml",129.95,129.95,""),
 ("V","Freshly Cosmetics","Glow Body Oil (travel)",50,"ml",66.54,71.23,""),
 ("V","Babor","Shimmer Oil",100,"ml",276,276,""),
 ("V","Soda","Shiny Gel Face & Body",N,"ml",49.25,49.25,""),
 ("M","Objet by Kundal","Satin Glow Shimmer Oil",45,"ml",139.8,215.05,""),
 ("M","Objet by Kundal","Satin Glow Body Oil",100,"ml",134.7,245,""),
 ("M","Yushas","Shimmer body oil spray (2 listings)",N,"ml",28.8,53,""),
 ("M","Glazed & Glisten","Golden body gel oil",N,"ml",58,78.59,""),
 ("M","(no brand)","Vanilla glow shimmer body oil",N,"ml",55.77,55.77,""),
 ("M","Tiwido","Shimmer body oil",N,"ml",34.4,34.4,""),
 ("M","(no brand)","Rose gold body shimmer spray",N,"ml",44.99,44.99,""),
 ("M","Vaseline","Bronze shimmer gel oil (Nahdi 62.1, Al-Dawaa 42.75)",200,"ml",52.4,59.5,""),
 ("M","Vaseline","Vanilla Glow gel oil (Nahdi 55.89, Al-Dawaa 42.75)",200,"ml",49.3,59.5,""),
 ("M","Bali Body","Body highlighter lotion",100,"ml",40,137.67,""),
 ("M+S","Hearts","Body Glow (Nahdi 88.32, own store 96)",120,"ml",92.2,103.2,"saudi?"),
 ("W","Besito Body","Besito Shimmer",N,"ml",96,160,"saudi; price changed since 3 Nov (was 160)"),
 ("W","Waves Beauty","Glowies body shimmer",120,"ml",156.52,156.52,"saudi; new"),
]),
"Body Highlighter stick (هايلايتر)": (30, "ml", 79, [
 ("V","KASH Beauty","Highlight Sculpt Stick",N,"g",75.95,75.95,"face"),
 ("V","Rimmel","Glow Stick Highlighter",5,"g",55,55,"face"),
 ("V","Inglot","Cream Stick Highlighter",6.2,"g",83,103,"face"),
 ("S","Hearts","Highlighter stick",N,"g",35.7,42,"saudi?"),
 ("M","Essence","Baby Got Glow highlighter stick",N,"g",19,19,"face"),
 ("M","Revolution","Blush & Highlight Stick",N,"g",55,55,"face"),
]),
"Hair Wax (واكس)": (30, "ml", 129, [
 ("V","Slick Hair Company","Wax Stick",50,"g",110,110,""),
 ("V","She Is Bomb","Hair Wax Stick",79.8,"ml",143,143,"import"),
 ("W","Clara","Hair styling wax",N,"g",94,109,"saudi; size not published"),
 ("M","IKT","Wax stick (2 listings)",N,"g",21.1,31,""),
 ("M","Calithea","Wax stick",N,"g",24.9,64,""),
 ("M","(no brand)","Wax stick (Amazon)",N,"g",16.9,25.9,""),
 ("M","(no brand)","2-in-1 wax stick with comb",N,"g",38.24,38.24,""),
 ("M","Castweave","Hair wax",15,"ml",39.9,39.9,""),
 ("M","You Are The Princess","Hair wax",N,"g",20,49.6,""),
 ("M","Nexxus","Sleek Stick strong hold",66.1,"g",39.85,72.45,""),
]),
"Sleek Secret (ماسكارا الشعر)": (15, "ml", 75, [
 ("V","Slick Hair Company","Slick Stick",10,"ml",87,87,""),
 ("V","The Smooth Company","The Smooth Stick",10,"ml",73,73,""),
 ("W","Clara","Flyaway hair mascara",N,"ml",83,97,"saudi; size not published"),
 ("M","Luxe Fume","Hair finishing stick",N,"ml",26,69,""),
 ("M","Okeil","Hair finishing stick",N,"ml",45.08,98,""),
 ("M","Hogoa","Anti-frizz hair cream stick",18,"ml",31,31,""),
 ("M","Sevich","2-in-1 styling stick",N,"ml",37.99,37.99,""),
 ("M","Kitsch","Flyaway stick",N,"ml",99.05,99.05,""),
]),
"Sleek Brush (فرشاة)": (N, "", 29, [
 ("W","Clara","Smoothing brush",N,"",47,59,"saudi"),
 ("V","Bounce Curl","Define EdgeLift Brush",N,"",212,212,"import"),
 ("V","Bounce Curl","Slick-Flex EdgeLift Brush",N,"",159,159,"import"),
]),
"Sea Salt Scrub (سكراب)": (300, "ml", 119, [
 ("V+M","Tree Hut","Shea Sugar Scrub (Desertcart 173, Amazon 99.5 and 82.2)",510,"g",118.2,118.2,""),
 ("V","Alba Botanica","Sea Salt Body Scrub",411,"g",112.7,112.7,""),
 ("V","Sunday Rain","Grapefruit & Sea Salt Scrub",265,"g",18.7,26.75,""),
 ("V","Soak Sunday","Rose Utopia Scrub",200,"g",71.5,71.5,""),
 ("M","Jardin d'Oleane","Sugar scrub (3 variants)",600,"g",26.7,41.7,""),
 ("M","Cream Cap","Body & face scrub (Noon 43, Nahdi 44.95)",500,"g",44,68.4,""),
 ("M","Cosmo","Sugar scrub shea",450,"g",15.81,15.81,""),
 ("M","Vinci Botanicals","Bergamot body scrub",N,"g",31.99,31.99,""),
 ("M","Dove","Vanilla sugar scrub",N,"g",44.5,51,""),
 ("M","(no brand)","Body scrub (Amazon)",N,"g",24.6,24.6,""),
 ("M","Global Star","Sugar scrub (3 variants)",600,"ml",14.98,32.2,""),
 ("M","Dr Teal's","Rose oil sugar scrub",538,"g",39.99,88,""),
 ("M","Superdrug","Vitamin E body scrub",300,"ml",79,79,""),
 ("W","Waves Beauty","Floral Musk Body Scrub",400,"ml",128.7,128.7,"saudi"),
 ("W","Ladeena","Marilyn body scrub",600,"g",150,150,"saudi; size found"),
 ("W","Jayla","La Poudrerie body scrub",500,"g",85,85,"saudi; new"),
 ("S","MZN","Sugar body scrub",N,"g",90,90,"saudi"),
 ("W","Cotton Skin","Cotton scrub",500,"ml",199,199,"saudi"),
]),
"Whipped Body Butter (زبدة الجسم)": (250, "ml", 119, [
 ("W","The Body Shop","Shea Body Butter",200,"ml",99,99,"price changed since 3 Nov (was 74 on promo)"),
 ("V","The Body Shop","Boost Whipped Body Cream",200,"ml",229,229,"import"),
 ("V","Tree Hut","Whipped Body Butter",N,"g",69.25,69.25,""),
 ("V","Kiehl's","Creme de Corps whipped",230,"g",281,281,"import"),
 ("M","Ashri Natural","Coconut body butter",100,"g",52,60,""),
 ("M","Taha","African shea butter",150,"g",29,29,""),
 ("M","African Shea Butter","Shea butter",250,"ml",24.99,24.99,""),
 ("M","Palmer's","Cocoa butter formula (Noon 23.5, Amazon 24.73)",100,"g",24.1,26.9,""),
 ("M","Skin Me","Taif rose body butter",200,"g",18.99,23.95,""),
 ("M","Dew","Body butter (2 variants)",250,"ml",15,15,""),
 ("M","Celia","Body butter (Nahdi 24.5, Al-Dawaa 20)",300,"g",22.25,40.4,""),
 ("M","Sorbet","Body butter (2 variants)",400,"ml",17.31,26.63,""),
 ("M","Fay","Body yogurt (2 variants)",280,"ml",32.78,43.7,""),
 ("W","Jayla","La Poudrerie body butter",350,"g",92,92,"saudi"),
 ("M","Tatcha","Indigo body butter",N,"g",247,247,""),
 ("M","Sol de Janeiro","Delicia Drench body butter (smaller size)",N,"g",120,120,""),
 ("M","Glossier","Creme de You body butter",N,"g",195,195,""),
 ("M","L'Occitane","Pure shea butter",N,"g",230,230,""),
 ("M","Youth To The People","Superberry body butter (smaller size)",N,"g",108,108,""),
 ("M","Weleda","Skin Food Body Butter",150,"ml",132,132,""),
 ("W","Waves Beauty","Floral Musk Body Butter",250,"ml",128.7,128.7,"saudi"),
 ("W","Ladeena","Turmeric butter",350,"g",100,100,"saudi; size found"),
 ("S","MZN","Pink musk body butter",N,"g",85,85,"saudi"),
 ("S","Clavar","Charming Body Butter",N,"g",112,112,"saudi"),
]),
"Foot Cream (كريم القدمين)": (75, "ml", 75, [
 ("V+M","Eucerin","Foot Cream 10% Urea (Nahdi)",100,"ml",47.94,96.6,""),
 ("V+M","Puravie","Urea Foot Cream 10% (Watsons 164, Al-Dawaa 131.43)",150,"ml",147.7,164.1,""),
 ("V","urea care","10% Urea cream",170,"g",77,77,"import"),
 ("M","Sunshine Natural","Vitamin E foot cream",100,"ml",21.85,100,""),
 ("M","Al Attar","Heel cream",200,"ml",29,49,""),
 ("M","O'Keeffe's","Healthy Feet (Noon 32.13 and 34.3, Amazon 49.72)",N,"g",38.7,40.1,""),
 ("M","Healthy Feet","Cracked heel cream",N,"g",49.64,49.64,""),
 ("M","(no brand)","Urea 40% foot cream",N,"g",26.9,26.9,""),
 ("M","Bare Feet","Foot moisturiser",100,"ml",27.15,54.21,""),
 ("M","Dermactive","Urea foot cream",60,"ml",33.65,44.85,""),
 ("M","Isis Pharma","Cicapro hand & foot",40,"ml",34.5,69,""),
 ("M","Avalon Care","Foot cream",90,"ml",39,54,""),
 ("M","Hansaplast","Foot cream",100,"ml",52.9,52.9,""),
 ("M","Bivies","Urea foot cream",150,"ml",35.08,35.08,""),
 ("M","CeraVe","SA Renewing Foot Cream (Al-Dawaa 72.99, Watsons 73)",88,"ml",73,73,""),
 ("M","Vaseline","Foot cream (Al-Dawaa 12.25, Watsons 26)",55,"g",19.1,25.25,""),
 ("M","L'Occitane","Shea foot cream",N,"ml",50,50,""),
]),
"Hand Cream (كريم اليدين)": (30, "ml", 49, [
 ("V","Neutrogena","Norwegian Formula Hand Cream",50,"ml",34,34,"import"),
 ("W","Jayla","Hand cream (Floral Maze)",30,"ml",24,24,"saudi; new"),
 ("W","Ladeena","Marilyn hand cream",N,"ml",45,45,"saudi; new; size not published"),
]),
"Lip Plump (مرطب الشفاه)": (10, "ml", 65, [
 ("W","Laneige","Lip Sleeping Mask",20,"g",135,135,""),
 ("W","Waves Beauty","Vanilla lip balm",10,"ml",67.83,67.83,"saudi; new"),
 ("W","Jayla","Vanilla lip balm",N,"ml",55,55,"saudi; new; out of stock"),
]),
"Flora / Natura (معطر الجسم)": (150, "ml", 129, [
 ("V","Victoria's Secret","Bare Vanilla Mist",250,"ml",50,50,"import"),
 ("V","Victoria's Secret","Coconut Passion Mist",250,"ml",50,50,"import"),
 ("V","Victoria's Secret","Temptation Mist",250,"ml",52,52,"import"),
 ("V","Victoria's Secret","Rush Mist",250,"ml",73,73,"import"),
 ("V","Victoria's Secret","Emerald Crush Mist",250,"ml",63,63,""),
 ("V","Bath & Body Works","Sweet Pea Mist",236,"ml",81,81,""),
 ("V","Sol de Janeiro","Cheirosa 68 Perfume Mist",90,"ml",125,125,""),
 ("V","Riddiance","Body & Hair Mist",150,"ml",49.45,49.45,""),
 ("V","Colour Me","Body Mist",150,"ml",23,23,""),
 ("M","Kiss My Body","Adore You body mist",88,"ml",17.36,17.36,""),
 ("M","Blatch","Powder musk body mist",250,"ml",62.44,80,""),
 ("M","Almajed for Oud","Candy hair & body mist",100,"ml",59,59,"saudi"),
 ("M","Lux","Body mist (2 variants)",N,"ml",53.3,62.9,""),
 ("M","Body Cology","Vanilla body mist",N,"ml",20.4,20.4,""),
 ("M","Body Spa","Sweet Candy body spray",250,"ml",24.75,33.01,""),
 ("M","Body Spa","Patchouli body spray",100,"ml",15,20,""),
 ("S","MZN","Powder body mist",N,"ml",55,55,"saudi"),
 ("W","Jayla","La Poudrerie body mist",200,"ml",70,70,"saudi; size found"),
 ("W","Jayla","Soulful body mist",150,"ml",84,84,"saudi; new"),
 ("W","Ladeena","All over spray (Clean)",100,"ml",150,150,"saudi; size found"),
 ("W","Waves Beauty","All Over Spray Musk Touch",100,"ml",249.57,249.57,"saudi"),
 ("W","Cotton Skin","Hair & body mist",50,"ml",89,99,"saudi; new"),
]),
"a'musk (مسك)": (15, "ml", 99, [
 ("W","Almajed for Oud","Pure Musk All Over Spray",100,"ml",59.01,118,"saudi; spray"),
 ("V","Hamil Al Musk","Altahara musk oil",6,"ml",52,52,"import"),
 ("V","Tesori d'Oriente","White Musk",100,"ml",58,58,"import; spray"),
 ("W","Ladeena","Marilyn musk",15,"ml",75,75,"saudi; size found"),
 ("W","Jayla","Jayla Joy musk",15,"ml",80,80,"saudi; size found"),
]),
}

def r(x, d=0):
    return "" if x is None else (round(x, d) if d else int(round(x)))

rows, summary = [], []
for name, (osz, ounit, oprice, comps) in P.items():
    now = [c[5] for c in comps]
    reg = [c[6] for c in comps]
    sized = [c for c in comps if c[3]]
    sizes = [c[3] for c in sized]
    same = [c for c in sized if osz and abs(c[3] - osz) / osz <= 0.10]
    per100 = [c[5] / c[3] * 100 for c in sized]
    avg_now = st.mean(now); med_now = st.median(now)
    avg_size = st.mean(sizes) if sizes else None
    avg100 = st.mean(per100) if per100 else None
    med100 = st.median(per100) if per100 else None
    our100 = oprice / osz * 100 if osz else None
    sa = [c for c in comps if 'saudi' in c[7]]
    sa_sz = [c[3] for c in sa if c[3]]
    summary.append(dict(product=name, our_size=osz, our_unit=ounit, our_price=oprice,
        our_per100=r(our100, 1), n=len(comps), avg_now=r(avg_now), median_now=r(med_now),
        avg_regular=r(st.mean(reg)), min_now=r(min(now)), max_now=r(max(now)),
        n_with_size=len(sizes), n_same_size=len(same), avg_size=r(avg_size),
        min_size=r(min(sizes)) if sizes else "", max_size=r(max(sizes)) if sizes else "",
        avg_per100=r(avg100, 1), median_per100=r(med100, 1),
        n_saudi=len(sa), saudi_avg_now=r(st.mean([c[5] for c in sa])) if sa else '',
        saudi_avg_size=r(st.mean(sa_sz)) if sa_sz else '', n_rechecked=len([c for c in comps if c[0]=='W'])))
    for c in comps:
        rows.append([name, *c[:3], c[3] or "MISSING", c[4], c[5], c[6],
                     round(c[5] / c[3] * 100, 1) if c[3] else "MISSING", c[7]])

with open(OUT + "08-avg-price-size-rows.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["amie_product", "source", "brand", "product", "size", "unit", "price_now_sar",
                "price_regular_sar", "price_per_100_now", "flag"])
    w.writerows(rows)
with open(OUT + "08-avg-price-size-summary.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0]))
    w.writeheader(); w.writerows(summary)
for s in summary:
    print(s)
