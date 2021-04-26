var galleryThumbs = new Swiper('.gallery-thumbs', {
    spaceBetween: 0,
    slidesPerView: 4,
    loop: true,
    freeMode: true,
    loopedSlides: 5,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
});
var galleryTop = new Swiper('.gallery-top', {
    spaceBetween: 10,
    loop: true,
    loopedSlides: 5,
    navigation: {
        nextEl: '.wrappers__button__next',
        prevEl: '.wrappers__button__prev',
    },
    thumbs: {
        swiper: galleryThumbs,
    },
});

 
let burger = document.querySelector(".navbar__burger");
let show = document.querySelector('.content__navbar--list')

function myFunc() {
	burger.addEventListener("click", function () {
		console.log(1)
		burger.classList.toggle('active')
		show.classList.toggle('showMenu')
		document.body.classList.toggle('disable__scroll')
	});
}
myFunc();