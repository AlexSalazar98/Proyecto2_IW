var enlAbrirPopup = document.getElementById('enlAbrirPopup'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('pop-up'),
	enlCerrarPopup = document.getElementById('btn-cerrar-popup');


enlAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

enlCerrarPopup.addEventListener('click', function(){
	overlay.classList.remove('active');
	popup.classList.remove('active');
});
