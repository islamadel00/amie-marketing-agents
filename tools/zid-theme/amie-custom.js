/* ============================================================
   a'mie — Custom JS
   ============================================================ */


/* ------------------------------------------------------------
   1) تحديد عرض الوصف في السلايدر
   ------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".slide-content .description").forEach(function (el) {
    el.classList.add("limit-width");
  });
});


/* ------------------------------------------------------------
   2) زرار الواتساب العائم
   ------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", function () {

  const waBtn = document.createElement('a');
  waBtn.target = "_blank";
  waBtn.className = "wa-btn";

  // 🧠 سحب اسم المنتج
  const productName = document.querySelector("h1")?.innerText || "هذا المنتج";

  // 🔗 سحب لينك الصفحة
  const productUrl = window.location.href;

  // 💬 الرسالة
  const message = `مرحبا 👋
اريد الاستفسار عن المنتج:
${productName}

${productUrl}`;

  const encodedMessage = encodeURIComponent(message);

  // 📲 لينك واتساب
  waBtn.href = `https://wa.me/966506922203?text=${encodedMessage}`;

  // 🎨 أيقونة واتساب
  waBtn.innerHTML = `
  <svg viewBox="0 0 32 32" width="22" height="22" fill="white">
    <path d="M16 .4C7.4.4.4 7.3.4 15.9c0 2.8.7 5.5 2.1 7.9L.4 31.6l8-2.1c2.3 1.3 4.9 2 7.6 2 8.6 0 15.6-7 15.6-15.6S24.6.4 16 .4zm0 28.5c-2.4 0-4.7-.6-6.7-1.8l-.5-.3-4.7 1.2 1.3-4.6-.3-.5c-1.3-2-2-4.4-2-6.8C3.1 8.5 9 2.6 16 2.6s12.9 5.9 12.9 13.1S23 28.9 16 28.9z"/>
  </svg>
  `;

  document.body.appendChild(waBtn);

  // ⏱️ يظهر بعد 1.5 ثانية
  setTimeout(function () {
    waBtn.style.opacity = "1";
  }, 1500);

});




/* ------------------------------------------------------------
   4) ملاحظة العنوان الوطني في صفحة الدفع
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
   9) صفحة المنتج — سطر الشحن المبرّد + لينك لصفحة المدن
   بيظهر في المنتجات اللي في ONLY_PRODUCTS بس.
   ------------------------------------------------------------ */
(function () {
  "use strict";

  var PAGE_PATH = "/pages/Cold%20Delivery";

  // ✏️ المنتجات اللي السطر يظهر فيها (slug من لينك المنتج)
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
   10) تصغير ارتفاع التوب بار على الموبايل
   ------------------------------------------------------------ */
(function () {
  // على الديسكتوب مفيش داعي يشتغل أصلًا
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
    // 1) الأسرع: الصفحة العادية
    if (document.querySelector(SEL)) { inject(document); return true; }
    // 2) لو مش لاقيه، يدوّر جوه الـ shadow roots بس
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
   11) السلايدرات — تشغيل الحركة التلقائية
   الثيم بيكتب إعداد autoplay غلط (autoplayautoplay-delay)
   فالسلايدرات بتقف. الجزء ده بيشغّل الحركة لأي سلايدر
   مفعّل فيه autoplay من زد (البانر + الآراء + أي سلايدر تاني).
   + سكشن الآراء: سرعة أهدى + تلوين النجوم + نقط تحت السلايدر.
   شكل سكشن الآراء في ملف الـ CSS — جزء 8.
   ------------------------------------------------------------ */
(function () {
  "use strict";

  var REVIEWS = 'section[section-id="432de894-a7ea-402a-98cf-2e2d73d6d2bf"]';
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
/* 12) سكشن الفيديوهات — الفيديو اللي في النص كبير والجناب أصغر (موبايل) */
(function () {
  function setup() {
    if (window.matchMedia('(min-width: 1024px)').matches) return;
    document.querySelectorAll('section[id^="instgram-slider"] swiper-container').forEach(function (sc) {
      var sw = sc.swiper;
      if (!sw || sw.__amieCentered) return;
      sw.__amieCentered = true;
      sw.params.centeredSlides = true;
      sw.update();
      if (sw.slides.length > 2) sw.slideTo(1, 0);
    });
  }
  var n = 0, t = setInterval(function () { setup(); if (++n > 40) clearInterval(t); }, 250);
})();
/* 21) صفحة المنتج — إظهار الوصف كامل من غير "عرض المزيد" (الأقسام بتتفتح وتتقفل أصلًا) */
(function () {
  function fix() {
    document.querySelectorAll('.product-page aui-show-more').forEach(function (el) {
      var root = el.shadowRoot;
      if (!root || root.__amieFull) return;
      root.__amieFull = true;
      var s = document.createElement('style');
      s.textContent =
        '.show-more-content{max-height:none!important;overflow:visible!important;cursor:auto!important;color:inherit!important}' +
        '.show-more-content::after{display:none!important}' +
        '.show-more-btn{display:none!important}';
      root.appendChild(s);
    });
  }
  var n = 0, t = setInterval(function () { fix(); if (++n > 40) clearInterval(t); }, 250);
})();
/* ------------------------------------------------------------
   13) صفحة المدونة — إعادة تحميل صور المقالات اللي فضلت فاضية
   ------------------------------------------------------------ */
(function () {
  "use strict";

  function getBlog(slug, attempt) {
    attempt = attempt || 0;
    return fetch("/api/v1/blogs/" + encodeURIComponent(slug), { headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
      .then(function (res) {
        var blog = res && (res.blog || res.data || res);
        if (!blog || typeof blog !== "object") throw new Error("Bad response");
        return blog;
      })
      .catch(function (err) {
        if (attempt >= 3) throw err;
        return new Promise(function (ok) { setTimeout(ok, 500 * Math.pow(2, attempt)); })
          .then(function () { return getBlog(slug, attempt + 1); });
      });
  }

  function fix(card) {
    if (card.__amieFix) return;
    card.__amieFix = true;
    getBlog(card.getAttribute("data-blog-slug")).then(function (blog) {
      var c = blog.cover && blog.cover.image;
      var url = c && (c.medium || c.small || c.large || c.full_size);
      var img = card.querySelector(".blog-card__img");
      if (url && img) {
        img.addEventListener("load", function () {
          img.classList.remove("opacity-0");
          card.classList.add("has-cover");
          var ph = card.querySelector(".blog-card__placeholder");
          if (ph) ph.classList.add("hidden");
        });
        img.src = url;
      }
      var ex = card.querySelector(".blog-card__excerpt");
      if (ex && !ex.textContent.trim() && blog.snippet) ex.textContent = blog.snippet;
    }).catch(function () {});
  }

  function scan() {
    var cards = document.querySelectorAll(".blog-card[data-blog-slug]");
    var waiting = 0;
    cards.forEach(function (card) {
      if (card.classList.contains("is-loading")) { waiting++; return; }
      if (!card.classList.contains("has-cover")) fix(card);
    });
    return cards.length > 0 && waiting === 0;
  }

  var n = 0, t = setInterval(function () {
    if ((scan() && n > 5) || ++n > 60) clearInterval(t);
  }, 500);
})();
/* ------------------------------------------------------------
   22) القائمة الجانبية — ترتيب شبه Moonglaze
   الرئيسية / الأقسام (بتفتح وتقفل) / جميع المنتجات
   الأقسام بتتسحب من القائمة اللي في زد، فأي قسم يتضاف هناك
   هيظهر هنا لوحده. الشكل في ملف الـ CSS — جزء 14.
   ------------------------------------------------------------ */
(function () {
  "use strict";

  var ID = "amie-nav";

  function isEnglish() {
    return /^\/en-/i.test(location.pathname) || (document.documentElement.lang || "").toLowerCase().indexOf("en") === 0;
  }

  function localePrefix() {
    var m = location.pathname.match(/^\/((?:en|ar)-[a-z]{2})(?=\/|$)/i);
    return m ? "/" + m[1] : "";
  }

  function link(href, text, cls) {
    var a = document.createElement("a");
    a.href = href;
    a.className = cls;
    a.textContent = text;
    return a;
  }

  function build() {
    var content = document.querySelector(".side-menu .menu-content");
    if (!content) return false;
    if (content.querySelector("#" + ID)) return true;

    var buttons = content.querySelectorAll(".menu-item > button[data-url]");
    if (!buttons.length) return false;

    var en = isEnglish();
    var pre = localePrefix();
    var allUrl = "/products";
    var cats = [];

    Array.prototype.forEach.call(buttons, function (b) {
      var url = b.getAttribute("data-url") || "";
      var text = (b.textContent || "").trim();
      if (/^\/products\/?$/.test(url)) { allUrl = url; return; }
      cats.push({ url: url, text: text });
    });

    var nav = document.createElement("nav");
    nav.id = ID;

    nav.appendChild(link(pre + "/", en ? "Home" : "الرئيسية", "amie-nav__link"));

    var group = document.createElement("div");
    group.className = "amie-nav__group";
    var toggle = document.createElement("button");
    toggle.type = "button";
    toggle.className = "amie-nav__link amie-nav__toggle";
    toggle.setAttribute("aria-expanded", "false");
    toggle.innerHTML = "<span>" + (en ? "Categories" : "الأقسام") + '</span><span class="amie-nav__icon" aria-hidden="true"></span>';
    var sub = document.createElement("div");
    sub.className = "amie-nav__sub";
    cats.forEach(function (c) {
      sub.appendChild(link(c.url.indexOf("/") === 0 ? pre + c.url : c.url, c.text, "amie-nav__sublink"));
    });
    toggle.addEventListener("click", function () {
      var open = group.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    group.appendChild(toggle);
    group.appendChild(sub);
    nav.appendChild(group);

    nav.appendChild(link(pre + allUrl, en ? "Shop all" : "جميع المنتجات", "amie-nav__link"));

    content.insertBefore(nav, content.firstChild);
    content.classList.add("amie-nav-ready");
    return true;
  }

  function boot() {
    build();
    // الثيم ممكن يرسم القائمة من جديد، فنرجّع الترتيب بتاعنا لو اختفى
    new MutationObserver(function () { build(); })
      .observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
