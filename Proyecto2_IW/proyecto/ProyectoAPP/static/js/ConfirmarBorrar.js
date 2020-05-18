function ConfirmarBorrar(){

    //var mensaje = confirm("¿Desea eliminar el registro?");
    //alert("Registro eliminado correctamente")
    if (confirm("¿Desea eliminar el registro?")){
        return true;
    }else{
        return false;
    }

}

function enviar(){
    const data = new FormData(document.getElementById('formulario'));
    fetch("http://127.0.0.1:8000/ProyectoAPP/ActualizarClienteAJAX/", {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .then((data) => {
        //console.log(data);
        alert("Cliente modificado correctamente!")
    })

}


var btn = document.getElementById('Guardar_Cambios_Cliente');

btn.addEventListener('click', enviar);
