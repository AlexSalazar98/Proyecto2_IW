function comprobarClave() {

    var cont1 = document.getElementById('Contraseña'),
	    cont2 = document.getElementById('Repetir_Contraseña');

    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
    }else{
        document.Form_regist.submit();
    }
}
