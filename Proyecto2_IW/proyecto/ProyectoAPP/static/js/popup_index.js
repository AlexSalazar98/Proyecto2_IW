var enlAbrirPopup = document.getElementById('enlAbrirPopup'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('pop-up'),
	enlCerrarPopup = document.getElementById('btn-cerrar-popup'),

	enlAbrirPopupemail = document.getElementById('enlAbrirPopup-email'),
	overlayemail = document.getElementById('overlay-email'),
	popupemail = document.getElementById('pop-up-email'),
	enlCerrarPopupemail = document.getElementById('btn-cerrar-popup-email');




enlAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

enlCerrarPopup.addEventListener('click', function(){
	overlay.classList.remove('active');
	popup.classList.remove('active');
});

enlAbrirPopupemail.addEventListener('click', function(){

    overlay.classList.remove('active');
	popup.classList.remove('active');

	overlayemail.classList.add('active');
	popupemail.classList.add('active');
});

enlCerrarPopupemail.addEventListener('click', function(){
	overlayemail.classList.remove('active');
	popupemail.classList.remove('active');
});


function mostrarContrasena(){
    var tipo = document.getElementById("password");
    var icono = document.getElementById("ojo");
    if(tipo.type == "password"){
        tipo.type = "text";
        icono.textContent = "visibility";
    }else{
        tipo.type = "password";
        icono.textContent = "visibility_off";
    }
}


