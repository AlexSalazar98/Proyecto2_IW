from django.db import models


# Clase para la creacion de Clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=50)
    email = models.EmailField()
    localizacion = models.TextField()
    telefono = models.IntegerField()
    numero_cuenta = models.CharField(max_length=24)


# Clase para categoria usuario (Jefe dep. / Gerente / Ingeniero)
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)


# Clase para departamentos
class Departamento(models.Model):
    nombre = models.CharField(max_length=30)


# Clase para la creacion de Usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contraseña = models.CharField(max_length=10)


# Clase para la creacion de Empleados
class Empleados(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    telefono = models.IntegerField()


# Clase estado para recopilar el estado de las tareas
class Estado(models.Model):
    estado = models.CharField(max_length=20, default="Abierta")

    def __str__(self):
        return f"Estado = {self.estado}"


# Clase para la creacion de Tareas
class Tareas(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    nivel_prioridad = models.CharField(max_length=20)
    estado_tarea = models.ForeignKey(Estado, on_delete=models.CASCADE)
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
    empleados = models.ManyToManyField(Empleados)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
