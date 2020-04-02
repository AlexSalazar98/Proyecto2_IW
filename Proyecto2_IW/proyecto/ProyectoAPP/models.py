from django.db import models


# Clase para la creacion de Clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=50)
    email = models.EmailField()
    localizacion = models.CharField()
    telefono = models.IntegerField(max_length=9)
    numero_cuenta = models.CharField()


# Clase para categoria usuario
class Categoria(models.Model):
    nombre = models.CharField()


# Clase para departamentos
class Departamento(models.Model):
    nombre = models.CharField()


# Clase para la creacion de Usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


# Clase para la creacion de Empleados
class Empleados(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    telefono = models.IntegerField(max_length=9)


# Clase para la creacion de Tareas
class Tareas(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleados, on_delete=models.SET_NULL)
    nivel_prioridad = models.CharField()
    estado_tarea = models.CharField()
    notas_adicionales_escritas_empleado = models.TextField()


# Clase para la creacion de Proyectos
class Proyectos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tareas_a_realizar = models.ManyToManyField(Tareas)
    empleados = models.ManyToManyField(Empleados, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
