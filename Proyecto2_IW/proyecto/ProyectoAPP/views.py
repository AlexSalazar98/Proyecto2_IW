from django.shortcuts import render, redirect
from ProyectoAPP.models import Usuarios, Departamento, Categoria, Clientes, Proyectos, Empleados, Tareas, \
    Nivel_Prioridad, Estado_Proyecto, Estado


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

        for us in listausrec:
            if us['usuario'] == usuario and us['contraseña'] == contraseña:
                return redirect('PaginaPrincipal')
                break


# Funcion para mostrar la pagina principal de la aplicacion
def PaginaPricipal(request):
    # Recogemos los objetos necesaios para cargar la info necesaria en la pagina principal
    clientes = Clientes.objects.order_by('empresa')

    proyectos = Proyectos.objects.order_by('nombre')

    responsable = Empleados.objects.order_by('nombre')

    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

    estado_proyecto = Estado_Proyecto.objects.order_by('estado')

    tareas = Tareas.objects.order_by('nombre')

    departamento = Departamento.objects.order_by('nombre')

    estado_tarea = Estado.objects.order_by('estado')

    # Pasamo la info necesaria a la pagina principal
    context = {
        'clientes': clientes,
        'proyectos': proyectos,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamento': departamento,
    }

    return render(request, 'TablaPrincipal.html', context)


# Funcion para llamar al formulacio de registo
def LlamarFormulario(request):
    # Recogemos de BBDD los datos necesarios para mostrar en el formulario
    departamentos = Departamento.objects.order_by('nombre')
    categoria = Categoria.objects.order_by('nombre')

    # Pasamos los datos al formulario
    context = {
        'departamentos': departamentos,
        'categoria': categoria
    }
    return render(request, 'Formulario.html', context)


# Funcion para recoger los datos de formulario de registro y guardarlos en BBDD
def RecogerFormulario(request):
    # Creamos nuevo ususario
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

    # Guardamos el nuevo usuario en BBDD
    UsuarioGuardado.save()

    return redirect('PaginaPrincipal')


# Funcion para mostrar los datos completos de los proyectos
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

    return render(request, 'detalles_proyecto.html', context)


# Formulario para registrar un nuevo cliente en BBDD
def Nuevo_Cliente(request):
    # Creamos un nuevo cliente
    nuevo_cliente = Clientes()

    # Recogemos los datos del HTML
    nuevo_cliente.nombre = request.POST["nombre"]
    nuevo_cliente.empresa = request.POST["Empresa"]
    nuevo_cliente.email = request.POST["Email"]
    nuevo_cliente.localizacion = request.POST["Localizacion"]
    nuevo_cliente.telefono = request.POST["Telefono"]
    nuevo_cliente.numero_cuenta = request.POST["Numero_Cuenta"]

    # Guardamos los datos en BBDD
    nuevo_cliente.save()

    return redirect('PaginaPrincipal')


# Formulario para registrar nuevo empleado en BBDD
def Nuevo_Empleado(request):
    # Creamo un nuevo empleado
    nuevo_empleado = Empleados()

    # Recogemos los datos de HTML
    nuevo_empleado.dni = request.POST["DNI"]
    nuevo_empleado.nombre = request.POST["nombre"]
    nuevo_empleado.apellido = request.POST["Apellido"]
    nuevo_empleado.email = request.POST["Email"]
    nuevo_empleado.telefono = request.POST["Telefono"]

    # Guardamos el nuevo empleado en BBDD
    nuevo_empleado.save()

    return redirect('PaginaPrincipal')


# Funcion para crear nueva tarea en BBDD
def Nueva_Tarea(request):
    # Creamos una nueva tarea
    nueva_tarea = Tareas()

    # Recogemos sus datos del HTML
    nueva_tarea.nombre = request.POST["Nombre_Tarea"]
    nueva_tarea.descripcion = request.POST["Descripcion_Tarea"]
    nueva_tarea.estado_tarea = Estado.objects.get(estado=request.POST["Estado"])
    nueva_tarea.fecha_fin = request.POST["Fecha_Fin"]
    nueva_tarea.fecha_inicio = request.POST["Fecha_Inicio"]
    nueva_tarea.nivel_prioridad = Nivel_Prioridad.objects.get(nivel_prioridad=request.POST["Prioridad"])
    nueva_tarea.notas_adicionales_escritas_empleado = request.POST["Notas_Empleado"]
    nueva_tarea.responsable = Empleados.objects.get(id=request.POST["Responsable"])

    # Guardamos la nueva tarea en BBDD
    nueva_tarea.save()

    return redirect('PaginaPrincipal')


# Funcion para crear un nuevo proyecto en BBDD
def Nuevo_Proyecto(request):
    # Creamos un nuevo proyecto
    nuevo_proyecto = Proyectos()

    # Recogemos sus datos de la BBDD
    nuevo_proyecto.nombre = request.POST["Nombre_Proyecto"]
    nuevo_proyecto.fecha_inicio = request.POST["Fecha_Inicio"]
    nuevo_proyecto.fecha_fin = request.POST["Fecha_Fin"]
    nuevo_proyecto.descripcion = request.POST["Descripcion_Proyecto"]
    nuevo_proyecto.presupuesto = float(request.POST["Presupuesto"])
    nuevo_proyecto.departamento = Departamento.objects.get(nombre=request.POST["Departamento"])
    nuevo_proyecto.estado = Estado_Proyecto.objects.get(estado=request.POST["Estado"])
    nuevo_proyecto.cliente = Clientes.objects.get(id=request.POST["Cliente"])
    mirar_tarea = request.POST["Tareas[]"]
    # print(mirar_tarea)

    # Guardamos el nuevo proyecto en BBDD
    nuevo_proyecto.save()

    # Aqui deberiamos asignarle los empleados y las tareas recogidas previamente del HTML al nuevo proyecto guardado
    # nuevo_proyecto.empleados = nuevo_proyecto.empleados.add(id=request.POST["Empleados"])
    # nuevo_proyecto.tareas_a_realizar = nuevo_proyecto.tareas_a_realizar.add(id=request.POST["Tareas"])

    return redirect('PaginaPrincipal')


# Funcion para mostrar los proyectos en la P.principal en función de los botones de clientes
def ProyectosPorCliente(request):
    # Recogemos la infor del boton seleccionado
    n_cliente = request.POST["botones_cliente"]

    # Miramos que boton nos han seleccionado. Si es el de todos, devolveremos todos los proyectos
    if n_cliente == 'Todos':
        #proyectos = Proyectos.objects.order_by('nombre')
        return redirect('PaginaPrincipal')

    # Si es otro, sacaremos los proyectos filtrados por ese dato que nos pasen (id de la empresa)
    else:
        proyectos = Proyectos.objects.filter(cliente=n_cliente)

    # A partir de aqui cargamos el resto de datos que necesita la P.principal para funcionar (excepto proyectos)
    clientes = Clientes.objects.order_by('empresa')

    responsable = Empleados.objects.order_by('nombre')

    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

    estado_proyecto = Estado_Proyecto.objects.order_by('estado')

    tareas = Tareas.objects.order_by('nombre')

    departamento = Departamento.objects.order_by('nombre')

    estado_tarea = Estado.objects.order_by('estado')

    # Lo juntamos toodo para mandarlo en la respuesta
    context = {
        'clientes': clientes,
        'proyectos': proyectos,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamento': departamento,
    }

    return render(request, 'TablaPrincipal.html', context)


# Funcion para modificar los clientes
def ModificarClientes (request):

    clientes = Clientes.objects.order_by('empresa')

    context = {
        'datos': clientes,
        'titulo': "Clientes",
        'col1':  "Empresa",
        'col2': "Persona Contacto",
        'col3': "Telefono"

    }

    return render(request, 'ModificarClientes.html', context)


# Funcion para modificar los empleados
def ModificarEmpleados (request):

    empleados = Empleados.objects.order_by('nombre')

    context = {
        'datos': empleados,
        'titulo': "Empleados",
        'col1':  "Nombre",
        'col2': "Apellido",
        'col3': "Telefono"

    }

    return render(request, 'ModificarEmpleados.html', context)


# Funcion para modificar los proyectos
def ModificarProyectos (request):

    proyectos = Proyectos.objects.order_by('nombre')

    context = {
        'datos': proyectos,
        'titulo': "Proyectos",
        'col1':  "Nombre",
        'col2': "Cliente",
        'col3': "Estado"

    }

    return render(request, 'ModificarProyectos.html', context)


# Funcion para modificar los tareas
def ModificarTareas(request):

    tareas = Tareas.objects.order_by('nombre')

    context = {
        'datos': tareas,
        'titulo': "Tareas",
        'col1':  "Nombre",
        'col2': "Prioridad",
        'col3': "Estado"

    }

    return render(request, 'ModificarTareas.html', context)
