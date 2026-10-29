/* ============================================================
   a'mie — Custom JS (نسخة نضيفة)
   زد ← المتجر الإلكتروني ← الثيمات ← ⋮ ← تعديل JS
   امسحي كل اللي في الخانة وحطي الملف ده مكانه.
   ============================================================ */


/* ------------------------------------------------------------
   1) تحديد عرض الوصف في السلايدر الرئيسي
   ------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".slide-content .description").forEach(function (el) {
    el.classList.add("limit-width");
  });
});


/* ------------------------------------------------------------
   2) زرار الواتساب العائم (الشكل في الـCSS — جزء 7)
   ------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {

  const waBtn = document.createElement('a');
  waBtn.target = "_blank";
  waBtn.className = "wa-btn";

  // سحب اسم المنتج
  const productName = document.querySelector("h1")?.innerText || "هذا المنتج";

  // سحب لينك الصفحة
  const productUrl = window.location.href;

  // الرسالة
  const message = `مرحبا 👋
اريد الاستفسار عن المنتج:
${productName}

${productUrl}`;

  const encodedMessage = encodeURIComponent(message);

  // لينك واتساب
  waBtn.href = `https://wa.me/966506922203?text=${encodedMessage}`;

  // أيقونة واتساب
  waBtn.innerHTML = `
  <svg viewBox="0 0 32 32" width="22" height="22" fill="white">
    <path d="M16 .4C7.4.4.4 7.3.4 15.9c0 2.8.7 5.5 2.1 7.9L.4 31.6l8-2.1c2.3 1.3 4.9 2 7.6 2 8.6 0 15.6-7 15.6-15.6S24.6.4 16 .4zm0 28.5c-2.4 0-4.7-.6-6.7-1.8l-.5-.3-4.7 1.2 1.3-4.6-.3-.5c-1.3-2-2-4.4-2-6.8C3.1 8.5 9 2.6 16 2.6s12.9 5.9 12.9 13.1S23 28.9 16 28.9z"/>
  </svg>
  `;

  document.body.appendChild(waBtn);

  // يظهر بعد 1.5 ثانية
  setTimeout(function () {
    waBtn.style.opacity = "1";
  }, 1500);

});


/* ------------------------------------------------------------
   3) كروت المدونة (صورة + مقتطف + رابط) — الشكل في الـCSS جزء 6
   ------------------------------------------------------------ */
(function () {
  var LIST_SEL = '.blog-list', ITEM_SEL = '.blog-item';

  // رابط المقال ← صورة الداش بورد (الأضمن). أضيفي سطر لكل مقال جديد.
  var THUMBS = {
    '/blogs/summer-tanning-routine':
      'https://media.zid.store/thumbs/blogs/019e83bd-80bd-70b0-ad30-c138aa746ff7-thumbnail-800x800-70.jpg'
  };

  function ready(fn) { document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  function cGet(k) { try { return JSON.parse(sessionStorage.getItem('amieBlog:' + k)); } catch (e) { return null; } }
  function cSet(k, v) { try { sessionStorage.setItem('amieBlog:' + k, JSON.stringify(v)); } catch (e) {} }

  function parseDoc(html) {
    var d = new DOMParser().parseFromString(html, 'text/html');
    var pick = function (s, a) { var e = d.querySelector(s); return e ? e.getAttribute(a) : null; };
    // الأولوية: صورة الثمبنيل اللي اترفعت في الداش بورد
    var m = html.match(/https?:\/\/media\.zid\.store\/thumbs\/blogs\/[^"'\s)]+\.(?:jpe?g|png|webp)/i);
    var img = m ? m[0] : null;
    if (!img) img = pick('meta[property="og:image"]', 'content') || pick('meta[name="twitter:image"]', 'content');
    var desc = pick('meta[property="og:description"]', 'content') || pick('meta[name="description"]', 'content');
    return { img: img, desc: desc };
  }

  function fill(item, data) {
    var img = item.querySelector('.blog-thumb img');
    if (img && data.img) img.src = data.img;
    if (data.desc && !item.querySelector('.blog-excerpt')) {
      var h = item.querySelector('h2');
      if (h) { var p = document.createElement('p'); p.className = 'blog-excerpt'; p.textContent = data.desc; h.parentNode.insertBefore(p, h.nextSibling); }
    }
    if (!item.querySelector('.blog-more')) { var mo = document.createElement('div'); mo.className = 'blog-more'; mo.textContent = 'اقرئي المقال ←'; item.appendChild(mo); }
  }

  function enhance(item) {
    var link = item.querySelector('a[href]'); if (!link || item.querySelector('.blog-thumb')) return;
    var href = link.getAttribute('href');

    var thumb = document.createElement('a'); thumb.className = 'blog-thumb'; thumb.href = href;
    var img = document.createElement('img'); img.alt = (link.textContent || '').trim(); img.loading = 'lazy';
    thumb.appendChild(img); item.insertBefore(thumb, item.firstChild);

    if (THUMBS[href]) img.src = THUMBS[href];

    var cached = cGet(href);
    if (cached) { fill(item, THUMBS[href] ? { desc: cached.desc } : cached); return; }
    fetch(href, { credentials: 'same-origin' }).then(function (r) { return r.text(); })
      .then(function (html) {
        var data = parseDoc(html); cSet(href, data);
        fill(item, THUMBS[href] ? { desc: data.desc } : data);
      })
      .catch(function () {});
  }

  function run() {
    var items = document.querySelectorAll(LIST_SEL + ' ' + ITEM_SEL);
    if (!items.length) return false; items.forEach(enhance); return true;
  }
  ready(function () { if (run()) return; var n = 0, t = setInterval(function () { if (run() || ++n > 20) clearInterval(t); }, 300); });
})();


/* ------------------------------------------------------------
   4) صفحة الدفع — ملاحظة العنوان الوطني
   ------------------------------------------------------------ */
(function () {
  var ID = "amie-na-note";
  function place() {
    if (document.getElementById(ID)) return true;
    var h = Array.prototype.find.call(
      document.querySelectorAll("h6"),
      function (el) { return (el.textContent || "").trim() === "التوصيل"; }
    );
    if (!h) return false;
    var header = h.closest(".css-ijk136") || h.parentNode;
    if (!header || !header.parentNode) return false;

    var n = document.createElement("div");
    n.id = ID;
    n.innerHTML = '<p dir="rtl" style="margin:10px 0;color:#5b4f43;font-size:13px;line-height:1.6">يرجى التأكد من إدخال العنوان الوطني لسرعة توصيل طلبك</p>';
    header.parentNode.insertBefore(n, header.nextSibling);
    return true;
  }
  var t = 0, timer = setInterval(function () {
    if (place() || ++t >= 20) clearInterval(timer);
  }, 400);
})();


/* ------------------------------------------------------------
   5) صفحة المنتج — سطر الشحن المبرّد + لينك لصفحة المدن
   بيظهر في المنتجات اللي في ONLY_PRODUCTS بس.
   ------------------------------------------------------------ */
(function () {
  "use strict";

  var PAGE_PATH = "/pages/Cold%20Delivery";

  // المنتجات اللي السطر يظهر فيها (slug من لينك المنتج)
  var ONLY_PRODUCTS = [
    "ريد",                                  // الرد تشيري
    "amie-chocolate-body-highlighter-set",  // هايلايتر الشوكولاتة
    "amie-marshmallow-body-highlighter",    // هايلايتر المارشميلو
    "into-the-glow-collection",             // مجموعة Into the Glow
    "واكس-آيمي-للشعر"                       // الواكس
  ];

  var ID = "amie-cold-line";

  var TEXT = {
    ar: { line: "الشحن المبرّد متوفر لمدن مختارة.", link: "الإطلاع علي المدن" },
    en: { line: "Chilled delivery is available in selected cities.", link: "See cities" }
  };

  var CSS =
    "#amie-cold-line{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:14px 0 0;font-size:13px;line-height:1.6;color:#6E625B}" +
    "#amie-cold-line svg{flex:0 0 auto;color:#653126}" +
    "#amie-cold-line a{color:#653126;font-weight:600;text-decoration:underline;text-underline-offset:3px}";

  var ICON =
    '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">' +
    '<path d="M12 2v20M3.5 7l17 10M20.5 7l-17 10M9.5 3.5 12 5.5l2.5-2M9.5 20.5 12 18.5l2.5 2"/></svg>';

  function localePrefix() {
    var m = location.pathname.match(/^\/((?:en|ar)-[a-z]{2})(?=\/)/i);
    return m ? "/" + m[1] : "";
  }

  function isEnglish() {
    return /^\/en-/i.test(location.pathname) || (document.documentElement.lang || "").toLowerCase().indexOf("en") === 0;
  }

  function currentSlug() {
    var m = location.pathname.match(/\/products\/([^\/?#]+)/);
    return m ? decodeURIComponent(m[1]) : "";
  }

  function place() {
    if (document.getElementById(ID)) return true;

    // مش من المنتجات المختارة؟ يقف خالص
    if (ONLY_PRODUCTS.indexOf(currentSlug()) === -1) return true;

    var details = document.getElementById("productPageDetails");
    if (!details) return false;

    var anchor = details.querySelector("#product-form") || details.querySelector(".product-payments--widget");
    if (!anchor) return false;

    if (!document.getElementById(ID + "-style")) {
      var s = document.createElement("style");
      s.id = ID + "-style";
      s.textContent = CSS;
      document.head.appendChild(s);
    }

    var t = isEnglish() ? TEXT.en : TEXT.ar;
    var p = document.createElement("p");
    p.id = ID;
    p.innerHTML = ICON + '<span>' + t.line + '</span> <a href="' + localePrefix() + PAGE_PATH + '">' + t.link + '</a>';

    anchor.parentNode.insertBefore(p, anchor);
    return true;
  }

  function boot() {
    if (place()) return;
    var tries = 0;
    var timer = setInterval(function () {
      if (place() || ++tries > 50) clearInterval(timer);
    }, 200);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();


/* ------------------------------------------------------------
   6) تصغير ارتفاع التوب بار على الموبايل
   ------------------------------------------------------------ */
(function () {
  if (!window.matchMedia("(max-width: 640px)").matches) return;

  var ID = "amie-topbar-fix";
  var SEL = ".animated-banner__slider-container";
  var CSS = SEL + "{padding:0 !important;}";

  function inject(root) {
    if (root.querySelector("#" + ID)) return;
    var s = document.createElement("style");
    s.id = ID;
    s.textContent = CSS;
    (root.head || root).appendChild(s);
  }

  function find() {
    if (document.querySelector(SEL)) { inject(document); return true; }
    var hosts = document.querySelectorAll("*");
    for (var i = 0; i < hosts.length; i++) {
      var r = hosts[i].shadowRoot;
      if (r && r.querySelector(SEL)) { inject(r); return true; }
    }
    return false;
  }

  if (find()) return;
  var tries = 0;
  var timer = setInterval(function () {
    if (find() || ++tries >= 15) clearInterval(timer);
  }, 300);
})();


/* ------------------------------------------------------------
   7) صفحة المنتج — ملاحظة الهدية (مجموعة اللافندر والليمون قراس)
   ------------------------------------------------------------ */
(function () {
  var GIFT_PRODUCTS = {
    '4ddb1426-e764-4cab-aece-058ce2766003': 'عند شرائكِ مجموعة اللافندر، احصلي على فرشاة الجسم الجافة هدية',
    'd4e7a9a2-752c-44a6-91c3-2acab35ba9b8': 'عند شرائكِ مجموعة الليمون قراس، احصلي على فرشاة الجسم الجافة هدية'
  };

  function addGiftNote() {
    var idInput = document.getElementById('product-id');
    if (!idInput) return;
    var text = GIFT_PRODUCTS[idInput.value];
    if (!text) return;
    if (document.querySelector('.amie-gift-note')) return;

    if (!document.getElementById('amie-gift-style')) {
      var style = document.createElement('style');
      style.id = 'amie-gift-style';
      style.textContent =
        '.amie-gift-note{display:block!important;margin:16px 0 6px!important;padding:14px 18px!important;' +
        'background:#28272a!important;color:#fff!important;border-radius:14px!important;font-size:15px!important;' +
        'font-weight:700!important;line-height:1.6!important;text-align:center!important;}' +
        '@media (max-width:768px){.amie-gift-note{font-size:13.5px!important;padding:12px 14px!important;}}';
      document.head.appendChild(style);
    }

    var desc = document.querySelector('.product-short-description');
    if (!desc) return;

    var note = document.createElement('div');
    note.className = 'amie-gift-note';
    note.textContent = text;
    desc.insertAdjacentElement('afterend', note);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addGiftNote);
  } else {
    addGiftNote();
  }
  setTimeout(addGiftNote, 1500);
})();


/* ------------------------------------------------------------
   8) السلايدرات — تشغيل الحركة التلقائية
   الثيم بيكتب إعداد autoplay غلط (autoplayautoplay-delay)
   فالسلايدرات بتقف. الجزء ده بيشغّل الحركة لأي سلايدر
   مفعّل فيه autoplay من زد (البانر + الآراء + أي سلايدر تاني).
   سكشن "الأكثر مبيعًا" متساب في حاله (بيمشي بإعدادات زد بس).
   + سكشن الآراء: سرعة أهدى + تلوين النجوم + نقط تحت السلايدر.
   شكل سكشن الآراء في الـCSS — جزء 9.
   ------------------------------------------------------------ */
(function () {
  "use strict";

  var REVIEWS = 'section[section-id="432de894-a7ea-402a-98cf-2e2d73d6d2bf"]';
  var SKIP = 'section[section-id="f371d893-770e-4813-b8d7-d7d8564d1ecb"]'; // الأكثر مبيعًا
  var DEFAULT_DELAY = 3500;
  var REVIEWS_DELAY = 6000; // سرعة سكشن الآراء (6 ثواني) — كل 1000 = ثانية
  var REVIEWS_SPEED = 700;  // مدة الانتقال بين الآراء

  /* ---------- قراءة إعداد autoplay من السلايدر ---------- */
  function autoplayDelay(slider) {
    var attrs = slider.attributes;
    for (var i = 0; i < attrs.length; i++) {
      var name = attrs[i].name.toLowerCase();
      if (name.indexOf("autoplay") === -1) continue;
      if (attrs[i].value === "false") return 0;
      var v = parseInt(attrs[i].value, 10);
      return v > 500 ? v : DEFAULT_DELAY;
    }
    return 0; // autoplay مش مفعّل في زد
  }

  function lastIndex(sw) {
    var per = Math.max(1, Math.round(sw.params.slidesPerView) || 1);
    return Math.max(0, sw.slides.length - per);
  }

  /* ---------- حركة تلقائية ---------- */
  function runAutoplay(el, sw, delay) {
    sw.params.rewind = true;
    if (sw.autoplay && typeof sw.autoplay.start === "function") {
      sw.params.autoplay = { delay: delay, disableOnInteraction: false, pauseOnMouseEnter: true };
      sw.autoplay.start();
      return;
    }
    var paused = false;
    el.addEventListener("mouseenter", function () { paused = true; });
    el.addEventListener("mouseleave", function () { paused = false; });
    setInterval(function () {
      if (paused || document.hidden) return;
      if (sw.activeIndex >= lastIndex(sw)) sw.slideTo(0);
      else sw.slideNext();
    }, delay);
  }

  /* ---------- نقط سكشن الآراء ---------- */
  function buildDots(el, sw) {
    if (el.parentNode.querySelector(".amie-rev-dots")) return;
    var wrap = document.createElement("div");
    wrap.className = "amie-rev-dots";
    wrap.setAttribute("aria-label", "آراء العملاء");

    function render() {
      var n = lastIndex(sw) + 1;
      if (wrap.children.length !== n) {
        wrap.innerHTML = "";
        for (var i = 0; i < n; i++) {
          var b = document.createElement("button");
          b.type = "button";
          b.setAttribute("aria-label", "رأي " + (i + 1));
          (function (idx) { b.addEventListener("click", function () { sw.slideTo(idx); }); })(i);
          wrap.appendChild(b);
        }
      }
      var active = Math.min(sw.activeIndex, n - 1);
      Array.prototype.forEach.call(wrap.children, function (b, i) {
        b.classList.toggle("is-active", i === active);
      });
    }

    el.parentNode.insertBefore(wrap, el.nextSibling);
    render();
    sw.on("slideChange", render);
    sw.on("resize", render);
  }

  /* ---------- نجوم سكشن الآراء ---------- */
  var STAR_CSS =
    ".star path:first-of-type{fill:rgba(101,49,38,.18)!important}" +
    ".star path:first-of-type ~ path{fill:#8b2635!important}";

  function paintStars() {
    var stars = document.querySelectorAll(REVIEWS + " aui-star-rating");
    var done = 0;
    stars.forEach(function (el) {
      var root = el.shadowRoot;
      if (!root) return;
      if (!root.getElementById("amie-star-style")) {
        var s = document.createElement("style");
        s.id = "amie-star-style";
        s.textContent = STAR_CSS;
        root.appendChild(s);
      }
      done++;
    });
    return stars.length > 0 && done === stars.length;
  }

  /* ---------- كل السلايدرات ---------- */
  function startSliders() {
    var sliders = document.querySelectorAll("aui-slider");
    var pending = 0;
    sliders.forEach(function (slider) {
      if (slider.closest(SKIP)) return; // الأكثر مبيعًا: ماتلمسوش
      var el = slider.querySelector("swiper-container");
      var sw = el && el.swiper;
      if (!sw || !sw.slides || !sw.slides.length) { pending++; return; }
      if (sw.__amieAuto) return;
      sw.__amieAuto = true;

      var isReviews = !!slider.closest(REVIEWS);
      var delay = isReviews ? REVIEWS_DELAY : autoplayDelay(slider);
      if (isReviews) sw.params.speed = REVIEWS_SPEED;
      if (delay) runAutoplay(el, sw, delay);
      if (isReviews) buildDots(el, sw);
    });
    return sliders.length > 0 && pending === 0;
  }

  /* ---------- تشغيل ---------- */
  function boot() {
    var starsOk = paintStars();
    var slidersOk = startSliders();
    if (starsOk && slidersOk) return;

    var tries = 0;
    var timer = setInterval(function () {
      if (!starsOk) starsOk = paintStars();
      if (!slidersOk) slidersOk = startSliders();
      if ((starsOk && slidersOk) || ++tries > 75) clearInterval(timer);
    }, 200);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
