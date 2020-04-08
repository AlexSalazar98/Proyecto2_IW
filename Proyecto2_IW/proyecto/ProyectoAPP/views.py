from django.shortcuts import render
from django.http import HttpResponse
from ProyectoAPP.models import Usuarios


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    # Recogemos datos del HTML
    usuario = request.POST['Usuario'].lower()  # alex.salazar
    contraseña = request.POST["Contraseña"].lower()

    # Recogemos datos de DDBB
    user = Usuarios.objects.order_by("nombre")

    # Montamos lista con:
    listausrec = []
    for u in user:
        # Recogemos nombre ususario
        nomb = u.nombre.lower()
        # Recogemos primer apellido usuario
        ape = u.apellido.lower()
        # Montamos > nombre_de_usuario = nombre.apellido
        union = nomb + "." + ape
        # Recogermos contraseña
        cont = u.contraseña

        # Almacenamos nombre_de_usuario y contraseña juntos
        user_com = {
            'usuario': union,
            'contraseña': cont
        }

        # Los añadimos a la lista para comprobar despues
        listausrec.append(user_com)

        usuario_registrado = False

        for us in listausrec:
            if us['usuario'] == usuario and us['contraseña'] == contraseña:
                usuario_registrado = True
            break

    return HttpResponse(f"usuario {usuario} contraseña: {contraseña}; {usuario_registrado} ")


def PaginaPricipal(request):
    return render(request, 'TablaPrincipal.html')
