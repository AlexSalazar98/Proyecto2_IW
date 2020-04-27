from django.db import models


class empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)


class trabajador(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)
