from django.shortcuts import render
from django.http import HttpResponse
from ProyectoAPP.models import Usuarios


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    # Recogemos datos del HTML
    usuario = request.POST['Usuario'].lower()
    contraseña = request.POST["Contraseña"].lower()

    # Recogemos datos de DDBB
    user = Usuarios.objects.order_by("nombre")
    listausrec = []
    for u in user:
        nomb = u.nombre.lower()
        ape = u.apellido.lower()
        union = nomb + "." + ape
        listausrec.append(union)

    return HttpResponse(f"usuario {usuario} contraseña: {contraseña}; {listausrec}")
