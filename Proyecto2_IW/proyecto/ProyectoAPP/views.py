from django.shortcuts import render
from django.http import HttpResponse
from ProyectoAPP.models import Usuarios, Departamento, Categoria, Clientes, Proyectos, Empleados


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

        clientes = Clientes.objects.order_by('empresa')
<<<<<<< HEAD
        proyectos = Proyectos.objects.order_by('nombre')
=======
        proyectos = Proyectos.objects.all()
        responsable = Empleados.objects.order_by('nombre')
>>>>>>> 01923a6ccbcb3fdce061a2531da5b0bad4397d80

        for us in listausrec:
            if us['usuario'] == usuario and us['contraseña'] == contraseña:
                context = {
                    'clientes': clientes,
                    'proyectos': proyectos,
                    'responsable': responsable,
                }
                return render(request, 'TablaPrincipal.html', context)
                break


def PaginaPricipal(request):
    return render(request, 'TablaPrincipal.html')


def LlamarFormulario(request):
    departamentos = Departamento.objects.order_by('nombre')
    categoria = Categoria.objects.order_by('nombre')
    context = {
        'departamentos': departamentos,
        'categoria': categoria
    }
    return render(request, 'Formulario.html', context)


def RecogerFormulario(request):
    UsuarioGuardado = Usuarios()

    # Recogemos datos del HTML
    UsuarioGuardado.nombre = request.POST["nombre"]
    UsuarioGuardado.apellido1 = request.POST["Apellido_1"]
    UsuarioGuardado.apellido2 = request.POST["Apellido_2"]
    UsuarioGuardado.sexo = request.POST.get('Sexo')
    UsuarioGuardado.fecha_nacimiento = request.POST["Fecha_Nacimiento"]
    UsuarioGuardado.departamento = Departamento.objects.get(nombre=request.POST["Departamento"])
    UsuarioGuardado.categoria = Categoria.objects.get(nombre=request.POST["Categoria"])
    UsuarioGuardado.contraseña = request.POST["Contraseña"]
    repContraseña = request.POST["Repetir_Contraseña"]
    UsuarioGuardado.email = request.POST["Correo_Electronico"]

    UsuarioGuardado.save()

    return render(request, 'TablaPrincipal.html')


def DetallesProyecto(request):
    id_proyect = request.POST["eleccion"]
    proyecto = Proyectos.objects.order_by('id')

    pro_select = ""

    for pro in proyecto:
        if int(id_proyect) == int(pro.id):
            pro_select = pro

    #return render(request, 'detalles_proyecto.html')
    return HttpResponse(f"Nombre del proyecto: {pro_select.nombre}; presupuesto: {pro_select.cliente}")
