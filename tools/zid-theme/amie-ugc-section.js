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
