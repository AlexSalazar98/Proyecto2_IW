from django.db import models

# Clase para la creacion de Clientes
from django.urls import reverse


class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    localizacion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numero_cuenta = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.empresa}"


# Clase para categoria usuario (Jefe dep. / Gerente / Ingeniero)
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.nombre}"


# Clase para departamentos
class Departamento(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.nombre}"


# Clase para la creacion de Usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length=10)
    apellido1 = models.CharField(max_length=10)
    apellido2 = models.CharField(max_length=10)
    sexo = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.CharField(max_length=21, unique=True)
    contraseña = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}"


# Clase para la creacion de Empleados
class Empleados(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"


# Clase estado para recopilar el estado de las tareas
class Estado(models.Model):
    estado = models.CharField(max_length=20, default="Abierta")

    def __str__(self):
        return f"{self.estado}"


class Nivel_Prioridad(models.Model):
    nivel_prioridad = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nivel_prioridad}"


# Clase para la creacion de Tareas
class Tareas(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    nivel_prioridad = models.ForeignKey(Nivel_Prioridad, on_delete=models.CASCADE)
    estado_tarea = models.ForeignKey(Estado, on_delete=models.CASCADE)
    notas_adicionales_escritas_empleado = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Estado_Proyecto(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.estado}"


# Clase para la creacion de Proyectos
class Proyectos(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tareas_a_realizar = models.ManyToManyField(Tareas)
    empleados = models.ManyToManyField(Empleados)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado_Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} -- {self.fecha_inicio}"
