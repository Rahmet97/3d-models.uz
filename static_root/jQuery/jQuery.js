$(function () {
   var prev = '<img src="./img/icons/arrow-left.svg" alt="arrow" class="prev--btn">';   
   var next = '<img src="./img/icons/arrow-right.svg" alt="arrow" class="next--btn">';

   $(".owl-carousel").owlCarousel({
      loop: true,
      margin: 30,
      mouseDrag: true,
      dots: false,
      nav: true,
      slideBy: 1,
      autoplayHoverPause: true,
      autoplayTimeout: 3000,
      autoplay: false,
      autoplaySpeed: 3000,
      stagePadding: 30,
      navText: [prev, next],
      responsive: {
         0: {
            items: 1,
            dots: true,
         },
         375: {
				items: 1,
            dots: true,
				
         },
         768: {
            items: 2,
         },
         1024: {
            items: 3,
            nav: true,
         },
         1600: {
            items: 4,
				nav: true,
				margin: 120,
				
         },
      },
   });
});
