function abrir(){

    var overlay_Responsable = document.getElementById('overlay_Responsable'),
	    popup_Responsable = document.getElementById('pop-up_Responsable'),
	    enlCerrarPopup_Responsable = document.getElementById('btn-cerrar-popup_Responsable');

	overlay_Responsable.classList.add('active');
	popup_Responsable.classList.add('active');


	enlCerrarPopup_Responsable.addEventListener('click', function(){
	overlay_Responsable.classList.remove('active');
	popup_Responsable.classList.remove('active');
    });

}


function domResponsable(pk){
    var url = "http://127.0.0.1:8000/ProyectoAPP/DetalleResponsable/" + pk + "/";

    var div_dni = document.getElementById("DNI_Empleado-c"),
        div_nombre = document.getElementById("Empresa-empleado-c"),
        div_apellido = document.getElementById("Apellido-empleado-c"),
        div_email = document.getElementById("Email-empleado-c"),
        div_telefono = document.getElementById("Tel-empleado-c");

    var input_dni = document.createElement("INPUT");


    fetch(url)
        .then((response) => response.json())
        .then((json) => {

            console.log(json.nombre);
            div_dni.innerHTML = "";
            input_dni.type = 'text';
            input_dni.value = json.dni;
            input_dni.setAttribute("id", "DNI");
            input_dni.setAttribute("readonly", true);
            div_dni.appendChild(input_dni);

            div_nombre.innerHTML = "<input type='text' readonly='true' value="+ json.nombre +">";

            div_apellido.innerHTML = `<input type='text' readonly='true' value='${ json.apellido }'>`;

            div_email.innerHTML = "<input type='text' readonly='true' value="+ json.email +">";

            div_telefono.innerHTML = `<input type='number' readonly='true' value='${ json.telefono }'>`;

            abrir();

        });
}
