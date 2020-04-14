function comprobarClave() {

<<<<<<< HEAD
    var cont1 = document.getElementById('Contraseña').value,
=======
    var cont1 = document.getElementById('Contraseña').value;
>>>>>>> 83724ec05e5473cf33d6a3c921f53c2ff4bdcfa0
	    cont2 = document.getElementById('Repetir_Contraseña').value;

    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
    }else{
        document.getElementById('Alta_Registro').submit();
        return " url 'RecogerFormulario' "
    }
}
