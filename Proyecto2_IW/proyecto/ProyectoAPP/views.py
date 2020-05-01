from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from ProyectoAPP.models import Usuarios, Departamento, Categoria, Clientes, Proyectos, Empleados, Tareas, \
    Nivel_Prioridad, Estado_Proyecto, Estado
from django.views.generic import DetailView


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
                    'responsable': b.responsable,
                    'id_tarea': b.id
                }
                lista_pasar.append(conj)
    lista_empleados = []
    for a in pro_select.empleados.all():
        lista_empleados.append(a)

    # Recogemos los objetos necesaios para cargar la info necesaria
    clientes = Clientes.objects.order_by('empresa')

    responsable = Empleados.objects.order_by('nombre')

    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

    estado_proyecto = Estado_Proyecto.objects.order_by('estado')

    tareas = Tareas.objects.order_by('nombre')

    departamento = Departamento.objects.order_by('nombre')

    estado_tarea = Estado.objects.order_by('estado')

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

        'clientes': clientes,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamentos': departamento,
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

    # Recogemos sus datos del HTML
    nuevo_proyecto.nombre = request.POST["Nombre_Proyecto"]
    nuevo_proyecto.fecha_inicio = request.POST["Fecha_Inicio"]
    nuevo_proyecto.fecha_fin = request.POST["Fecha_Fin"]
    nuevo_proyecto.descripcion = request.POST["Descripcion_Proyecto"]
    nuevo_proyecto.presupuesto = float(request.POST["Presupuesto"])
    nuevo_proyecto.departamento = Departamento.objects.get(nombre=request.POST["Departamento"])
    nuevo_proyecto.estado = Estado_Proyecto.objects.get(estado=request.POST["Estado"])
    nuevo_proyecto.cliente = Clientes.objects.get(id=request.POST["Cliente"])
    tareas_recogidas = request.POST.getlist("Tareas")
    empleados_recogidos = request.POST.getlist("Empleados")

    # Guardamos el nuevo proyecto en BBDD
    nuevo_proyecto.save()

    todas_las_tareas = Tareas.objects.all()
    todos_los_empleados = Empleados.objects.all()

    for tr in tareas_recogidas:
        for tlt in todas_las_tareas:
            if int(tr) == int(tlt.id):
                nuevo_proyecto.tareas_a_realizar.add(tlt)

    for er in empleados_recogidos:
        for tle in todos_los_empleados:
            if int(er) == int(tle.id):
                nuevo_proyecto.empleados.add(tle)

    return redirect('PaginaPrincipal')


# Funcion para mostrar los proyectos en la P.principal en función de los botones de clientes
def ProyectosPorCliente(request):
    # Recogemos la infor del boton seleccionado
    n_cliente = request.POST["botones_cliente"]

    # Miramos que boton nos han seleccionado. Si es el de todos, devolveremos todos los proyectos
    if n_cliente == 'Todos':
        # proyectos = Proyectos.objects.order_by('nombre')
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


def DiccionarioTablas(datos, titulo, col1, col2, col3):
    # Recogemos los objetos necesaios para cargar la info necesaria
    clientes = Clientes.objects.order_by('empresa')
    responsable = Empleados.objects.order_by('nombre')
    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')
    estado_proyecto = Estado_Proyecto.objects.order_by('estado')
    tareas = Tareas.objects.order_by('nombre')
    departamento = Departamento.objects.order_by('nombre')
    estado_tarea = Estado.objects.order_by('estado')

    context = {
        'datos': datos,
        'titulo': titulo,
        'col1': col1,
        'col2': col2,
        'col3': col3,

        'clientes': clientes,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamentos': departamento,
    }

    return context


# Funcion para modificar los clientes
def ModificarClientes(request):
    clientes = Clientes.objects.order_by('empresa')

    context = DiccionarioTablas(clientes, "Clientes", "Empresa", "Persona de contacto", "Telefono")

    return render(request, 'TablaModificarClientes.html', context)


# Funcion para modificar los empleados
def ModificarEmpleados(request):
    empleados = Empleados.objects.order_by('nombre')

    context = DiccionarioTablas(empleados, "Empleados", "Nombre", "Apellido", "Telefono")

    return render(request, 'TablaModificarEmpleados.html', context)


# Funcion para modificar los proyectos
def ModificarProyectos(request):
    proyectos = Proyectos.objects.order_by('nombre')

    context = DiccionarioTablas(proyectos, "Proyectos", "Nombre", "Cliente", "Estado")

    return render(request, 'TablaModificarProyectos.html', context)


# Funcion para modificar los tareas
def ModificarTareas(request):
    tareas = Tareas.objects.order_by('nombre')

    context = DiccionarioTablas(tareas, "Tareas", "Nombre", "Prioridad", "Estado")

    return render(request, 'TablaModificarTareas.html', context)


# Funcion para eliminar clientes
def BorrarCliente(request):
    # Recuperamos el id del cliente a borrar desde el HTML
    id = request.POST["btn-delete-cliente"]

    # Obtenemos el objeto a borrar de BBDD filtrado por el id obtenido
    cliente_a_borrar = Clientes.objects.filter(id=id)

    # Borramos el objeto
    cliente_a_borrar.delete()

    # Recargamos la tabla de Clientes
    return redirect('ModificarClientes')


# Funcion para eliminar empleados
def BorrarEmpleados(request):
    # Recuperamos el id del empleados a borrar desde el HTML
    id = request.POST["btn-delete-empleados"]

    # Obtenemos el objeto a borrar de BBDD filtrado por el id obtenido
    empleado_a_borrar = Empleados.objects.filter(id=id)

    # Borramos el objeto
    empleado_a_borrar.delete()

    # Recargamos la tabla de Empleaods
    return redirect('ModificarEmpleados')


# Funcion para eliminar proyectos
def BorrarProyectos(request):
    # Recuperamos el id del proyectos a borrar desde el HTML
    id = request.POST["btn-delete-proyectos"]

    # Obtenemos el objeto a borrar de BBDD filtrado por el id obtenido
    proyecto_a_borrar = Proyectos.objects.filter(id=id)

    # Borramos el objeto
    proyecto_a_borrar.delete()

    # Recargamos la tabla de Proyectos
    return redirect('ModificarProyectos')


# Funcion para eliminar tareas
def BorrarTareas(request):
    # Recuperamos el id del tareas a borrar desde el HTML
    id = request.POST["btn-delete-tarea"]

    # Obtenemos el objeto a borrar de BBDD filtrado por el id obtenido
    tareas_a_borrar = Tareas.objects.filter(id=id)

    # Borramos el objeto
    tareas_a_borrar.delete()

    # Recargamos la tabla de Tareas
    return redirect('ModificarTareas')


# Funcion para cargar el cliente seleccionado
def FormModificarClientes(request):
    id = request.POST['btn-edit-cliente']

    clientes = Clientes.objects.all()

    cliente_slec = ""

    # Recogemos los objetos necesaios para cargar la info necesaria
    clientes = Clientes.objects.order_by('empresa')

    responsable = Empleados.objects.order_by('nombre')

    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

    estado_proyecto = Estado_Proyecto.objects.order_by('estado')

    tareas = Tareas.objects.order_by('nombre')

    departamento = Departamento.objects.order_by('nombre')

    estado_tarea = Estado.objects.order_by('estado')

    for c in clientes:
        if int(id) == c.id:
            cliente_slec = c
            break

    context = {
        'cliente': cliente_slec,

        'clientes': clientes,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamentos': departamento,
    }

    return render(request, 'FormModificarCliente.html', context)


# Clase para mostrar los datos completos de las tareas
class DetallesTareas(DetailView):
    model = Tareas
    template_name = 'detalles_tareas.html'

    def get_context_data(self, **kwargs):
        context = super(DetallesTareas, self).get_context_data(**kwargs)

        # Recogemos los objetos necesaios para cargar la info necesaria
        clientes = Clientes.objects.order_by('empresa')

        responsable = Empleados.objects.order_by('nombre')

        prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')

        estado_proyecto = Estado_Proyecto.objects.order_by('estado')

        tareas = Tareas.objects.order_by('nombre')

        departamento = Departamento.objects.order_by('nombre')

        estado_tarea = Estado.objects.order_by('estado')

        context['clientes'] = clientes
        context['responsable'] = responsable
        context['prioridad'] = prioridad
        context['estado_proyecto'] = estado_proyecto
        context['tareas_p'] = tareas
        context['departamento'] = departamento
        context['estado_tarea'] = estado_tarea

        return context


# Funcion para guardar datos modificados de clientes
def ActualizarClientes(request):
    id = request.POST['btn-modificar-cliente']

    clientes = Clientes.objects.all()

    cliente_a_actualizar = ""

    for c in clientes:
        if c.id == int(id):
            cliente_a_actualizar = c

    cliente_a_actualizar.nombre = request.POST['nombre']
    cliente_a_actualizar.empresa = request.POST['Empresa']
    cliente_a_actualizar.email = request.POST['Email']
    cliente_a_actualizar.localizacion = request.POST['Localizacion']
    cliente_a_actualizar.telefono = request.POST['Telefono']
    cliente_a_actualizar.numero_cuenta = request.POST['Numero_Cuenta']

    cliente_a_actualizar.save()

    return redirect('ModificarClientes')


# Funcion para cargar el empleado seleccionado
def FormModificarEmpleado(request):
    id = request.POST['btn-edit-empleados']

    empleados = Empleados.objects.all()

    tarea = Tareas.objects.all()
    nivel_prioridad = Nivel_Prioridad.objects.all()
    estado = Estado_Proyecto.objects.all()
    departamentos = Departamento.objects.all()
    cliente = Clientes.objects.all()
    estado_tareas = Estado.objects.all()

    empleado_slec = ""

    for c in empleados:
        if int(id) == c.id:
            empleado_slec = c
            break

    context = {
        'empleado': empleado_slec,

        'tareas': tarea,
        'estado_proyecto': estado,
        'prioridades': nivel_prioridad,
        'responsable': empleados,
        'departamentos': departamentos,
        'clientes': cliente,
        'estado_tarea': estado_tareas,

    }

    return render(request, 'FormModificarEmpleado.html', context)


# Funcion para guardar datos modificados de empleados
def ActualizarEmpleado(request):
    id = request.POST['btn-modificar-empleado']

    empleados = Empleados.objects.all()

    empleado_a_actualizar = ""

    for e in empleados:
        if e.id == int(id):
            empleado_a_actualizar = e

    empleado_a_actualizar.dni = request.POST['dni']
    empleado_a_actualizar.email = request.POST['email']
    empleado_a_actualizar.nombre = request.POST['nombre']
    empleado_a_actualizar.apellido = request.POST['apellido']
    empleado_a_actualizar.telefono = request.POST['telefono']

    empleado_a_actualizar.save()

    return redirect('ModificarEmpleados')


# Funcion para cargar la tarea seleccionada
def FormModificarTarea(request):
    id = request.POST['btn-edit-tareas']

    tarea = Tareas.objects.all()
    empleados = Empleados.objects.order_by('nombre')
    nivel_prioridad = Nivel_Prioridad.objects.all()
    estado_tarea = Estado.objects.all()
    clientes = Clientes.objects.order_by('empresa')
    departamentos = Departamento.objects.all()
    resp = Empleados.objects.order_by('nombre')
    estado = Estado_Proyecto.objects.order_by('estado')

    tarea_slec = ""
    resp_nombre = ""
    resp_actual = ""
    prio = ""
    prio_actual = ""
    est = ""
    est_actual = ""

    resto_resp = []
    resto_prio = []
    resto_est = []

    for t in tarea:
        if int(id) == t.id:
            tarea_slec = t
            resp_nombre = t.responsable
            prio = t.nivel_prioridad
            est = t.estado_tarea
            break

    for e in empleados:
        if str(resp_nombre) == str(e.nombre):
            resp_actual = e
        else:
            resto_resp.append(e)

    for n in nivel_prioridad:
        if str(prio) == str(n.nivel_prioridad):
            prio_actual = n
        else:
            resto_prio.append(n)

    for es in estado_tarea:
        if str(est) == es.estado:
            est_actual = es
        else:
            resto_est.append(es)

    context = {
        'tarea': tarea_slec,
        'resp_id': resp_actual.id,
        'resp_nom': resp_actual.nombre,
        'resp_ape': resp_actual.apellido,
        'responsable': resto_resp,
        'prio_actual': prio_actual,
        'prioridad': resto_prio,
        'est_actual': est_actual,
        'estado_tarea': resto_est,

        'tareas': tarea,
        'estado_proyecto': estado,
        'prioridades': nivel_prioridad,
        'responsables': resp,
        'departamentos': departamentos,
        'clientes': clientes,
        'estado_tareas': estado_tarea,

    }

    return render(request, 'FormModificarTarea.html', context)


# Funcion para cargar el proyecto seleccionado
def FormModificarProyecto(request):
    id = request.POST['btn-edit-proyectos']

    proyectos = Proyectos.objects.all()
    tarea = Tareas.objects.all()
    empleados = Empleados.objects.order_by('nombre')
    nivel_prioridad = Nivel_Prioridad.objects.all()
    estado = Estado_Proyecto.objects.all()
    departamentos = Departamento.objects.all()
    cliente = Clientes.objects.all()
    estado_tareas = Estado.objects.all()

    pro_sel = ""
    cli_actual = ""
    dep_actual = ""
    est_actual = ""
    tar_actuales = []
    emp_actuales = []

    resto_cli = []
    resto_dep = []
    resto_est = []
    resto_tar = []
    resto_empl = []

    for p in proyectos:
        if int(p.id) == int(id):
            pro_sel = p
            cli_actual = p.cliente
            dep_actual = p.departamento
            est_actual = p.estado
            tar_actuales = p.tareas_a_realizar.all()
            emp_actuales = p.empleados.all()

    for c in cliente:
        if str(cli_actual) == c.empresa:
            cli_actual = c
        else:
            resto_cli.append(c)

    for d in departamentos:
        if str(dep_actual) == d.nombre:
            dep_actual = d
        else:
            resto_dep.append(d)

    for e in estado:
        if str(est_actual) == e.estado:
            est_actual = e
        else:
            resto_est.append(e)

    for t in tarea:
        resto_tar.append(t)

    for t_a in tar_actuales:
        resto_tar.remove(t_a)

    for em in empleados:
        resto_empl.append(em)

    for emple in emp_actuales:
        resto_empl.remove(emple)

    context = {

        'pro': pro_sel,
        'cli_actual': cli_actual.empresa,
        'cli_actual_id': cli_actual.id,
        'resto_cli': resto_cli,
        'dep_actual': dep_actual.nombre,
        'dep_actual_id': dep_actual.id,
        'resto_dep': resto_dep,
        'est_actual': est_actual.estado,
        'est_actual_id': est_actual.id,
        'resto_est': resto_est,
        'tar_actuales': tar_actuales,
        'resto_tar': resto_tar,
        'emp_actuales': emp_actuales,
        'resto_empl': resto_empl,

        'tareas': tarea,
        'estado_proyecto': estado,
        'prioridades': nivel_prioridad,
        'responsable': empleados,
        'departamentos': departamentos,
        'clientes': cliente,
        'estado_tarea': estado_tareas,

    }

    return render(request, 'FormModificarProyecto.html', context)


# Funcion para guardar datos modificados de tareas
def ActualizarTarea(request):
    id = request.POST['btn-modificar-tarea']

    tareas = Tareas.objects.all()

    tarea_a_actualizar = ""

    for t in tareas:
        if t.id == int(id):
            tarea_a_actualizar = t

    tarea_a_actualizar.nombre = request.POST['Nombre_Tarea']
    tarea_a_actualizar.descripcion = request.POST['Descripcion_Tarea']
    tarea_a_actualizar.fecha_inicio = request.POST['Fecha_Inicio']
    tarea_a_actualizar.fecha_fin = request.POST['Fecha_Fin']
    tarea_a_actualizar.responsable = Empleados.objects.get(id=request.POST["Responsable"])
    tarea_a_actualizar.nivel_prioridad = Nivel_Prioridad.objects.get(id=request.POST["Prioridad"])
    tarea_a_actualizar.estado_tarea = Estado.objects.get(id=request.POST["Estado_Tarea"])
    tarea_a_actualizar.notas_adicionales_escritas_empleado = request.POST['Notas_Empleado']

    tarea_a_actualizar.save()

    return redirect('ModificarTareas')


# Funcion para actualizar el proyecto seleccionado
def ActualizarProyecto(request):
    # Recogemos el id del HTML
    id = request.POST['btn-modificar-proyecto']

    # Recogemos el objeto de la BBDD
    proyectos = Proyectos.objects.all()

    actualizar_proyecto = ""
    for p in proyectos:
        if int(p.id) == int(id):
            actualizar_proyecto = p

    # Recogemos sus datos del HTML
    actualizar_proyecto.nombre = request.POST["Nombre_Proyecto"]
    actualizar_proyecto.fecha_inicio = request.POST["Fecha_Inicio"]
    actualizar_proyecto.fecha_fin = request.POST["Fecha_Fin"]
    actualizar_proyecto.descripcion = request.POST["Descripcion_Proyecto"]
    actualizar_proyecto.presupuesto = float(request.POST["Presupuesto"])
    actualizar_proyecto.departamento = Departamento.objects.get(id=request.POST["Departamento"])
    actualizar_proyecto.estado = Estado_Proyecto.objects.get(id=request.POST["Estado"])
    actualizar_proyecto.cliente = Clientes.objects.get(id=request.POST["Cliente"])
    tareas_recogidas = request.POST.getlist("Tareas")
    empleados_recogidos = request.POST.getlist("Empleados")

    # Limpiamos las posibles asignaciones que pueda tener el objeto
    actualizar_proyecto.tareas_a_realizar.clear()
    actualizar_proyecto.empleados.clear()

    todas_las_tareas = Tareas.objects.all()
    todos_los_empleados = Empleados.objects.all()

    # Buscamos los objetos asignados nuevamente para añadirlos
    for tr in tareas_recogidas:
        for tlt in todas_las_tareas:
            if int(tr) == int(tlt.id):
                actualizar_proyecto.tareas_a_realizar.add(tlt)

    for er in empleados_recogidos:
        for tle in todos_los_empleados:
            if int(er) == int(tle.id):
                actualizar_proyecto.empleados.add(tle)

    # Guardamos el nuevo proyecto en BBDD
    actualizar_proyecto.save()
    return redirect('ModificarProyectos')


def diccionarioBuscador(obj):
    # Recogemos los objetos necesaios para cargar la info necesaria en la pagina principal
    clientes = Clientes.objects.order_by('empresa')
    responsable = Empleados.objects.order_by('nombre')
    prioridad = Nivel_Prioridad.objects.order_by('nivel_prioridad')
    estado_proyecto = Estado_Proyecto.objects.order_by('estado')
    tareas = Tareas.objects.order_by('nombre')
    departamento = Departamento.objects.order_by('nombre')
    estado_tarea = Estado.objects.order_by('estado')

    context = {
        'proyectos': obj,

        'clientes': clientes,
        'responsable': responsable,
        'prioridad': prioridad,
        'estado_tarea': estado_tarea,
        'estado_proyecto': estado_proyecto,
        'tareas': tareas,
        'departamento': departamento,
    }

    return context


# Funcion para Buscador
def Buscador(request):
    nombre_proyecto = request.POST["Nombre_proyecto"].lower()
    fecha_inicio = request.POST["Fecha_inicio"]
    fecha_fin = request.POST["Fecha_fin"]
    estado_proyecto = request.POST["Estado"]

    todos_proyectos = Proyectos.objects.all()

    context = {}
    proyectos = []
    proyectos1 = []
    proyectos2 = []
    proyectos3 = []

    if (nombre_proyecto == "") and (fecha_inicio == "") and (fecha_fin == "") and (estado_proyecto == ""):
        return redirect('PaginaPrincipal')
    elif (nombre_proyecto != "") and (fecha_inicio == "") and (fecha_fin == "") and (estado_proyecto == ""):
        for p in Proyectos.objects.filter(nombre__icontains=str(nombre_proyecto)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto == "") and (fecha_inicio != "") and (fecha_fin == "") and (estado_proyecto == ""):
        for p in Proyectos.objects.filter(fecha_inicio__icontains=str(fecha_inicio)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto == "") and (fecha_inicio == "") and (fecha_fin != "") and (estado_proyecto == ""):
        for p in Proyectos.objects.filter(fecha_fin__icontains=str(fecha_fin)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto == "") and (fecha_inicio == "") and (fecha_fin == "") and (estado_proyecto != ""):
        for p in Proyectos.objects.filter(estado=int(estado_proyecto)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto != "") and (fecha_inicio != "") and (fecha_fin == "") and (estado_proyecto == ""):
        for p in Proyectos.objects.filter(nombre__icontains=str(nombre_proyecto)).filter(fecha_inicio__icontains=str(fecha_inicio)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto != "") and (fecha_inicio == "") and (fecha_fin != "") and (estado_proyecto == ""):
        for p in Proyectos.objects.filter(nombre__icontains=str(nombre_proyecto)).filter(fecha_fin__icontains=str(fecha_fin)):
            proyectos.append(p)

        context = diccionarioBuscador(proyectos)

    elif (nombre_proyecto != "") and (fecha_inicio == "") and (fecha_fin == "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.nombre).lower() == nombre_proyecto:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.estado) == estado_proyecto:
                proyectos1.append(p1)

        context = diccionarioBuscador(proyectos1)

    elif (nombre_proyecto == "") and (fecha_inicio != "") and (fecha_fin != "") and (estado_proyecto == ""):
        for p in todos_proyectos:
            if str(p.fecha_inicio) == fecha_inicio:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_fin) == fecha_fin:
                proyectos1.append(p1)

        context = diccionarioBuscador(proyectos1)

    elif (nombre_proyecto == "") and (fecha_inicio != "") and (fecha_fin == "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.fecha_inicio) == fecha_inicio:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.estado) == estado_proyecto:
                proyectos1.append(p1)

        context = diccionarioBuscador(proyectos1)

    elif (nombre_proyecto == "") and (fecha_inicio == "") and (fecha_fin != "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.fecha_fin) == fecha_fin:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.estado) == estado_proyecto:
                proyectos1.append(p1)

        context = diccionarioBuscador(proyectos1)

    elif (nombre_proyecto != "") and (fecha_inicio != "") and (fecha_fin != "") and (estado_proyecto == ""):
        for p in todos_proyectos:
            if str(p.nombre).lower() == nombre_proyecto:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_inicio) == fecha_inicio:
                proyectos1.append(p1)

        for p2 in proyectos1:
            if str(p2.fecha_fin) == fecha_fin:
                proyectos2.append(p2)

        context = diccionarioBuscador(proyectos2)

    elif (nombre_proyecto != "") and (fecha_inicio != "") and (fecha_fin == "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.nombre).lower() == nombre_proyecto:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_inicio) == fecha_inicio:
                proyectos1.append(p1)

        for p2 in proyectos1:
            if str(p2.estado) == estado_proyecto:
                proyectos2.append(p2)

        context = diccionarioBuscador(proyectos2)

    elif (nombre_proyecto != "") and (fecha_inicio == "") and (fecha_fin != "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.nombre).lower() == nombre_proyecto:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_fin) == fecha_fin:
                proyectos1.append(p1)

        for p2 in proyectos1:
            if str(p2.estado) == estado_proyecto:
                proyectos2.append(p2)

        context = diccionarioBuscador(proyectos2)

    elif (nombre_proyecto == "") and (fecha_inicio != "") and (fecha_fin != "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.fecha_inicio) == fecha_inicio:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_fin) == fecha_fin:
                proyectos1.append(p1)

        for p2 in proyectos1:
            if str(p2.estado) == estado_proyecto:
                proyectos2.append(p2)

        context = diccionarioBuscador(proyectos2)

    elif (nombre_proyecto != "") and (fecha_inicio != "") and (fecha_fin != "") and (estado_proyecto != ""):
        for p in todos_proyectos:
            if str(p.nombre).lower() == nombre_proyecto:
                proyectos.append(p)

        for p1 in proyectos:
            if str(p1.fecha_inicio) == fecha_inicio:
                proyectos1.append(p1)

        for p2 in proyectos1:
            if str(p2.fecha_fin) == fecha_fin:
                proyectos2.append(p2)

        for p3 in proyectos2:
            if str(p3.estado) == estado_proyecto:
                proyectos3.append(p3)

        context = diccionarioBuscador(proyectos3)

    return render(request, 'TablaPrincipal.html', context)


def recuperarcredenciales(request):
    email = request.POST['email']

    usuario = Usuarios.objects.all()

    user = ""
    cont = ""

    for u in usuario:
        if email == u.email:
            user = u.user
            cont = u.contraseña

    asunto = "CREDENCIALES"
    mensaje = f"Tus credenciales son las siguientes. Usuario: {user} --- Contraseña: {cont}"
    email_from = settings.EMAIL_HOST_USER
    email_to = [email]
    send_mail(asunto, mensaje, email_from, email_to, fail_silently=False)


    return redirect('index')
