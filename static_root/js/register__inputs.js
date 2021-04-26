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