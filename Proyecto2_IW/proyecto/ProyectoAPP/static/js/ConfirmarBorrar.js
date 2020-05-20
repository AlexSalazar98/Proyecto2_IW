// Funcion de confirmar el borrado de objetos
function ConfirmarBorrar(){

    if (confirm("¿Desea eliminar el registro?")){
        return true;
    }else{
        return false;
    }

}

// Funcion para enviar los datos modificados desde tareas mediante AJAX
function enviar(){
    /* FormData:
        Recoge del form de HTML el "name" y "value" de cada "INPUT" para montar los datos y enviarlos al servidor.
        Esta objeto ya cuenta con la seguridad de "csrf_token"
     */
    const data = new FormData(document.getElementById('formulario'));
    fetch("http://127.0.0.1:8000/ProyectoAPP/ActualizarClienteAJAX/", {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .then((data) => {
        alert("Cliente modificado correctamente!")
    })

}

// Evento para guardar cambios
var btn = document.getElementById('Guardar_Cambios_Cliente');
btn.addEventListener('click', enviar);
