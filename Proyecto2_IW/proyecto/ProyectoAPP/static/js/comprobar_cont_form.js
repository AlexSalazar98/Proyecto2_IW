function comprobarClave() {

    var cont1 = document.getElementById('Contraseña').value;
	    cont2 = document.getElementById('Repetir_Contraseña').value;

    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
    }else{
        document.Form_regist.submit();
    }
}
