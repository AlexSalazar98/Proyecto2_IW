function comprobarClave() {

    var cont1 = document.getElementById('Contraseña').value,
	    cont2 = document.getElementById('Repetir_Contraseña').value;
	    //Formulario = document.getElementById('Formulario');

    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
        /*Formulario.Contraseña.value = "";
        Formulario.Repetir_Contraseña.value = "";
        Formulario.Contraseña.focus();*/
    }else{
        document.getElementById('Alta_Registro').submit();
    }
}

function Usuario(){

    var nombre = document.getElementById('Nombre').value,
        apellido = document.getElementById('Apellido_1').value,
        user = document.querySelectorAll(".User"),

        union = nombre.toLowerCase() + "." + apellido.toLowerCase();

    for(var i = 0; i < user.length;i++){
        user[i].value = union;
     }

}
