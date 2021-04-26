let swiper = new Swiper(".swiper-container",{
   effect: "coverflow",
   grabCursor: true,
   centeredSlides: true,
   slidesPerView: "auto",
   coverflowEffect: {
      rotate: 20,
      stretch: 0,
      depth: 200,
      modifier: 1,
      slideShadows: true,
   },
   loop: true,
   autoplay: {
      delay: 20000,
      disableOnInteraction: false,
   },
   breakpoints: {
      640: {
         slidesPerView: 2,
         spaceBetween: 10,
         grabCursor: false,
      },
      768: {
         slidesPerView: 2,
         spaceBetween: 10,
         grabCursor: false,
      },
      1024: {
         slidesPerView: 3,
         spaceBetween: 10,
         grabCursor: false,
      },
      1366: {
         slidesPerView: 4,
         spaceBetween: 10,
         grabCursor: false,
      },
   },
});

let burger = document.querySelector(".navbar__burger");
let show = document.querySelector(".content__navbar--list");

function myFunc() {
   burger.addEventListener("click", function () {
      burger.classList.toggle("active");
      show.classList.toggle("showMenu");
      document.body.classList.toggle("disable__scroll");
   });
}
myFunc();

// check all
// let checkbox = document.querySelector('input[type="checkbox"]');
// let checks = document.querySelectorAll(".all");

// checkbox.addEventListener("click", () => {
//    if (checkbox.checked == true) {
//       checks.forEach((item) => {
//          item.innerHTML = `<input type="checkbox" checked>
// 					 <div class="state p-success-o">
// 					 	<label></label>`;
//       });
//    } else {
//       checks.forEach((item) => {
//          item.innerHTML = `<input type="checkbox"> 
// 					<div class="state p-success-o">
// 						<label></label>`;
//       });
//    }
// });

// colculate

function colculate() {
   let productSum = document.querySelectorAll(".shopproduct__info b");
	let result = document.querySelector(".shopingcard__item--summ span");
	
	productSum.forEach((sum, index) => {
		
		console.log(+sum.textContent)
		console.log(index)
	})
	console.log(productSum)
}
colculate()

//karta raqam input
function space(el, after) {
   after = after || 4;
   let v = el.value.replace(/[^\dA-Z]/g, ''),
       reg = new RegExp(".{" + after + "}","g")
   el.value = v.replace(reg, function (a, b, c) {
       return a + ' ';
   });
}

let el = document.getElementById('card');
el.addEventListener('keyup', function () {
   space(this, 4);
});


//muddat input
document.getElementById('data').addEventListener('keydown', function (e) {
   let value = this.value.replace(/\s+/g, '/');
   let isBackspace = e.key === 'Backspace';

   if ((e.key.length === 1 && /^[^\d\s]+$/.test(e.key)) || (!isBackspace && value.length === 4)) {
       e.preventDefault();
       return false;
   }

   this.value = value.split('').reverse().join('').replace(/\B(?=(\d{2})+(?!\d))/g, "/").split('').reverse().join('').trim();
});
