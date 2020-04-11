from django.shortcuts import render
from django.http import HttpResponse
from ProyectoAPP.models import Usuarios, Departamento, Categoria


# import js2py


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
        ape = u.apellido1.lower()
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
                # PaginaPricipal(request)
                # usuario_registrado = True
                # return HttpResponse(f"usuario {usuario} contraseña: {contraseña}; {usuario_registrado} ")
                return render(request, 'TablaPrincipal.html')
                break


def PaginaPricipal(request):
    return render(request, 'TablaPrincipal.html')


def LlamarFormulario(request):
    departamentos = Departamento.objects.order_by('nombre')
    categoria = Categoria.objects.order_by('nombre')
    context ={
        'departamentos': departamentos,
        'categoria': categoria
    }
    return render(request, 'Formulario.html', context)


def RecogerFormulario(request):
    # Recogemos datos del HTML
    nombre = request.POST["nombre"]
    apellido1 = request.POST["Apellido_1"]
    apellido2 = request.POST["Apellido_2"]
    Sexo = request.POST.get('Sexo')
    fecha_nacimiento = request.POST["Fecha_Nacimiento"]
    departamento = request.POST["Departamento"]
    categoria = request.POST["Categoria"]
    usuario = nombre.lower() + "." + apellido1.lower()
    contraseña = request.POST["Contraseña"]
    repContraseña = request.POST["Repetir_Contraseña"]
    email = request.POST["Correo_Electronico"]

    return HttpResponse(
        f"nombre {nombre} apellido 1 {apellido1} apellido 2 {apellido2} sexo {Sexo} fecha nacimiento {fecha_nacimiento}"
        f" departamentos {departamento} categoria {categoria} usuario {usuario} contraseña {contraseña}"
        f" repContraseña {repContraseña} email {email} ")
    # return render(request, 'Formulario.html')
