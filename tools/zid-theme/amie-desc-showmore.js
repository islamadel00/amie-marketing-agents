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
