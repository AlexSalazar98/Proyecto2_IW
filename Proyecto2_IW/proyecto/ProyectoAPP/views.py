from django.shortcuts import render
from django.http import HttpResponse
from ProyectoAPP.models import Usuarios, Departamento, Categoria, Clientes, Proyectos, Empleados, Tareas, Nivel_Prioridad, Estado_Proyecto, Estado


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

        clientes = Clientes.objects.order_by('empresa')

        proyectos = Proyectos.objects.order_by('nombre')

        responsable = Empleados.objects.order_by('nombre')

        prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

        estado = Estado_Proyecto.objects.order_by('estado')

        tareas = Tareas.objects.order_by('nombre')

        departamento = Departamento.objects.order_by('nombre')

        for us in listausrec:
            if us['usuario'] == usuario and us['contraseña'] == contraseña:
                context = {
                    'clientes': clientes,
                    'proyectos': proyectos,
                    'responsable': responsable,
                    'prioridad': prioridad,
                    'estado': estado,
                    'tareas': tareas,
                    'departamento': departamento,
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
    UsuarioGuardado.user = request.POST["User"]
    UsuarioGuardado.email = request.POST["Correo_Electronico"]

    UsuarioGuardado.save()

    clientes = Clientes.objects.order_by('empresa')

    proyectos = Proyectos.objects.order_by('nombre')

    responsable = Empleados.objects.order_by('nombre')
    context = {
        'clientes': clientes,
        'proyectos': proyectos,
        'responsable': responsable,
    }
    return render(request, 'TablaPrincipal.html', context)


def DetallesProyecto(request):
    # Recogemos del .HTML
    id_proyect = request.POST["eleccion"]
    # Recogemos proyectos de BBDD
    proyecto = Proyectos.objects.all()

    pro_select = ""

    # Buscamos y obtenemos el proyecto que queremos
    for pro in proyecto:
        if int(id_proyect) == int(pro.id):
            pro_select = pro

    # Obtenemos tareas de BBDD
    tareas = Tareas.objects.all()

    # Creamos lista para agrupar tareas con sus responsables
    lista_pasar = []

    # Buscamos tareas obtenemos responsables y agrupamos
    for a in pro_select.tareas_a_realizar.all():
        for b in tareas:
            if str(a) == str(b.nombre):
                conj = {
                    'tarea': a,
                    'responsable': b.responsable
                }
                lista_pasar.append(conj)
    lista_empleados = []
    for a in pro_select.empleados.all():
        lista_empleados.append(a)

    print(lista_empleados)
    # Creamos el context con lo que vamos a pasar al HTML de mostrar
    context = {
        'nombre': pro_select.nombre,
        'descripcion': pro_select.descripcion,
        'fecha_inicio': pro_select.fecha_inicio,
        'fecha_fin': pro_select.fecha_fin,
        'presupuesto': pro_select.presupuesto,
        'cliente': pro_select.cliente,
        'tareas_a_realizar': lista_pasar,
        'empleados': lista_empleados,
        'departamento': pro_select.departamento,
        'estado': str(pro_select.estado),
    }
    print(pro_select.empleados.all())
    return render(request, 'detalles_proyecto.html', context)

def Nuevo_Cliente (request):

    nuevo_cliente = Clientes()

    nuevo_cliente.nombre = request.POST["nombre"]
    nuevo_cliente.empresa = request.POST["Empresa"]
    nuevo_cliente.email = request.POST["Email"]
    nuevo_cliente.localizacion = request.POST["Localizacion"]
    nuevo_cliente.telefono = request.POST["Telefono"]
    nuevo_cliente.numero_cuenta = request.POST["Numero_Cuenta"]

    nuevo_cliente.save()

    clientes = Clientes.objects.order_by('empresa')

    proyectos = Proyectos.objects.order_by('nombre')

    responsable = Empleados.objects.order_by('nombre')
    context = {
        'clientes': clientes,
        'proyectos': proyectos,
        'responsable': responsable,
    }

    return render(request, 'TablaPrincipal.html', context)


def Nuevo_Empleado (request):

    nuevo_empleado = Empleados()

    nuevo_empleado.dni = request.POST["DNI"]
    nuevo_empleado.nombre = request.POST["nombre"]
    nuevo_empleado.apellido = request.POST["Apellido"]
    nuevo_empleado.email = request.POST["Email"]
    nuevo_empleado.telefono = request.POST["Telefono"]

    nuevo_empleado.save()

    return render(request, 'TablaPrincipal.html')


def Envio_Datos_Nuevo (request):

    cliente = Clientes.objects.order_by('nombre')
    tareas = Tareas.objects.order_by('nombre')
    empleados = Empleados.objects.order_by('nombre')
    departamento = Departamento.objects.order_by('nombre')
    estado = Estado.objects.order_by('estado')

    context = {
        'cliente': cliente,
        'tareas': tareas,
        'empleados': empleados,
        'departamento': departamento,
        'estado': estado,
    }

    return render(request, 'TablaPrincipal.html', context)


