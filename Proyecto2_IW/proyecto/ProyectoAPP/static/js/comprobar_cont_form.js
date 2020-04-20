function comprobarClave() {

    var cont1 = document.getElementById('Contraseña').value,
	    cont2 = document.getElementById('Repetir_Contraseña').value;

    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
    }else{
        document.getElementById('Alta_Registro').submit();
    }
}

function Usuario(){

    var nombre = document.getElementById('Nombre').value,
        apellido = document.getElementById('Apellido_1').value,
        user = document.querySelectorAll(".User"),
        union;


        union = nombre.toLowerCase() + "." + apellido.toLowerCase();

    for(var i = 0; i < user.length;i++){
        user[i].value = union;
     }

}
