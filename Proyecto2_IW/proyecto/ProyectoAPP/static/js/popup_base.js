// Recogemos variables del HTML
var Cliente = document.getElementById('Cliente'),
	overlay_Cliente = document.getElementById('overlay_Cliente'),
	popup_Cliente = document.getElementById('pop-up_Cliente'),
	enlCerrarPopup_Cliente = document.getElementById('btn-cerrar-popup_Cliente'),

	Empleado = document.getElementById('Empleado'),
	overlay_Empleado = document.getElementById('overlay_Empleado'),
	popup_Empleado = document.getElementById('pop-up_Empleado'),
	enlCerrarPopup_Empleado = document.getElementById('btn-cerrar-popup_Empleado'),

	Tarea = document.getElementById('Tarea'),
	overlay_Tarea = document.getElementById('overlay_Tarea'),
	popup_Tarea = document.getElementById('pop-up_Tarea'),
	enlCerrarPopup_Tarea = document.getElementById('btn-cerrar-popup_Tarea');

    Proyecto = document.getElementById('Proyecto'),
	overlay_Proyecto = document.getElementById('overlay_Proyecto'),
	popup_Proyecto = document.getElementById('pop-up_Proyecto'),
	enlCerrarPopup_Proyecto = document.getElementById('btn-cerrar-popup_Proyecto');



// EventListener para abrir los Pop-up
Cliente.addEventListener('click', function(){
	overlay_Cliente.classList.add('active');
	popup_Cliente.classList.add('active');
});

Empleado.addEventListener('click', function(){
	overlay_Empleado.classList.add('active');
	popup_Empleado.classList.add('active');
});


Tarea.addEventListener('click', function(){
	overlay_Tarea.classList.add('active');
	popup_Tarea.classList.add('active');
});

Proyecto.addEventListener('click', function(){
	overlay_Proyecto.classList.add('active');
	popup_Proyecto.classList.add('active');
});




// EventListener para cerrar los Pop-up
enlCerrarPopup_Cliente.addEventListener('click', function(){
	overlay_Cliente.classList.remove('active');
	popup_Cliente.classList.remove('active');
});

enlCerrarPopup_Empleado.addEventListener('click', function(){
	overlay_Empleado.classList.remove('active');
	popup_Empleado.classList.remove('active');
});


enlCerrarPopup_Tarea.addEventListener('click', function(){
	overlay_Tarea.classList.remove('active');
	popup_Tarea.classList.remove('active');
});

enlCerrarPopup_Proyecto.addEventListener('click', function(){
	overlay_Proyecto.classList.remove('active');
	popup_Proyecto.classList.remove('active');
});

// Funcion para comprobar si esta repetido el nombre del proyecto
function NomProyectoRep(){

    var nuevo_nombre = document.querySelector('#Nombre_Proyecto').value;

    fetch("http://127.0.0.1:8000/ProyectoAPP/NombProyecto/")
        .then((response) => response.json())
        .then((json) => {

            for (i = 0; i < json.length; i++){
                /* indexOf:
                    Esta funcion compara dos valores y devuelve un numero en funcion del resultado de la comparacion.
                */
                if(json[i].nombre.toLowerCase().indexOf(nuevo_nombre) !== -1){
                    alert("El nombre escogido para el proyecto ya existe!");
                    break;
                }
            };

        });

}
