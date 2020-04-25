function ConfirmarBorrar(){

    var mensaje = confirm("¿Desea eliminar el registro?");

    //print(mensaje);

    if (mensaje != false){
        document.getElementById('Borrar-Registro').submit();
    }

}
