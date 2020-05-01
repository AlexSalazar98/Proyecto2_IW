from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('entrar/', views.login, name="entrar"),

    path('PaginaPrincipal/', views.PaginaPricipal, name="PaginaPrincipal"),

    path('Registro/', views.LlamarFormulario, name="LlamarFormulario"),
    path('Registrar/', views.RecogerFormulario, name="RecogerFormulario"),

    path('DetallesProyecto/', views.DetallesProyecto, name="DetallesProyecto"),

    path('DetallesProyecto/DetallesTareas/<int:pk>/', views.DetallesTareas.as_view(), name="DetallesTareas"),

    path('NuevoCliente/', views.Nuevo_Cliente, name="NuevoCliente"),
    path('NuevoEmpleado/', views.Nuevo_Empleado, name="NuevoEmpleado"),
    path('NuevaTarea/', views.Nueva_Tarea, name="NuevaTarea"),
    path('NuevoProyecto/', views.Nuevo_Proyecto, name="NuevoProyecto"),

    path('MostrarPorCliente/', views.ProyectosPorCliente, name="ProyectosPorClientes"),

    path('ModificarClientes/', views.ModificarClientes, name="ModificarClientes"),
    path('ModificarEmpleados/', views.ModificarEmpleados, name="ModificarEmpleados"),
    path('ModificarProyectos/', views.ModificarProyectos, name="ModificarProyectos"),
    path('ModificarTareas/', views.ModificarTareas, name="ModificarTareas"),

    path('BorrarCliente/', views.BorrarCliente, name="BorrarCliente"),
    path('BorrarEmpleado/', views.BorrarEmpleados, name="BorrarEmpleado"),
    path('BorrarProyecto/', views.BorrarProyectos, name="BorrarProyecto"),
    path('BorrarTarea/', views.BorrarTareas, name="BorrarTarea"),

    path('FormModificarClientes/', views.FormModificarClientes, name="FormModificarClientes"),
    path('FormModificarEmpleado/', views.FormModificarEmpleado, name="FormModificarEmpleado"),
    path('FormModificarTarea/', views.FormModificarTarea, name="FormModificarTarea"),
    path('FormModificarProyecto/', views.FormModificarProyecto, name="FormModificarProyecto"),

    path('ActualizarCliente/', views.ActualizarClientes, name="ActualizarCliente"),
    path('ActualizarEmpleado/', views.ActualizarEmpleado, name="ActualizarEmpleado"),
    path('ActualizarTarea/', views.ActualizarTarea, name="ActualizarTarea"),
    path('ActualizarProyecto/', views.ActualizarProyecto, name="ActualizarProyecto"),

    path('Buscador/', views.Buscador, name="Buscador"),

    path('RecuperarCredenciales/', views.recuperarcredenciales, name="RecuperarCredenciales"),

]


