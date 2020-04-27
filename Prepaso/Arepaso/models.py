from django.db import models

    
class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)

    def __str__(self):
        return f"ID={self.id}, NOMBRE={self.nombre}, CIF={self.cif}"


class Trabajador(models.Model):
    nombre_trabajador = models.CharField(max_length=40)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return f"ID={self.id}, NOMBRE={self.nombre_trabajador}, EMPRESA={self.empresa}, FECHA DE NACIMIENTO={self.fecha_nacimiento}, ANTIGÜEDAD={self.antiguedad}"
