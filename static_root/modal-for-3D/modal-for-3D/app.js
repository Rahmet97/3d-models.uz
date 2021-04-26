let modal = document.querySelector('.modal')
let modalBg = document.querySelector('.modal--bg')

function hideResult() {
	modalBg.style.opacity = '0'
	modalBg.style.visibility = 'hidden'
	modal.style.opacity = '0'
	modal.style.visibility = 'hidden'
}
hideResult()

input.addEventListener('keypress', function (e) {
	if (e.keyCode == 13) {
		modalBg.style.opacity = '1'
		modalBg.style.visibility = 'visible'
		modal.style.opacity = '1'
		modal.style.visibility = 'visible'
	}
})

closeBtn.addEventListener('click', function () {
	hideResult()
})
modalBg.addEventListener('click', function () {
	hideResult()
})