function comprobarClave() {

    var cont1 = document.getElementById('Contraseña').value,
	    cont2 = document.getElementById('Repetir_Contraseña').value,
	    apellido1 = document.getElementById('Apellido_1').required;


    if (cont1 != cont2)  {
        alert('Las contraseñas no coinciden');
        return false;
    }else{
        return true;
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

function mostrarContrasena2(){
    var tipo = document.getElementById("Contraseña");
    var icono = document.getElementById("ojo2");
    if(tipo.type == "password"){
        tipo.type = "text";
        icono.textContent = "visibility";
    }else{
        tipo.type = "password";
        icono.textContent = "visibility_off";
    }
}

function mostrarContrasena3(){
    var tipo = document.getElementById("Repetir_Contraseña");
    var icono = document.getElementById("ojo3");
    if(tipo.type == "password"){
        tipo.type = "text";
        icono.textContent = "visibility";
    }else{
        tipo.type = "password";
        icono.textContent = "visibility_off";
    }
}


