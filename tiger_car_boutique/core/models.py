from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año  = models.PositiveIntegerField()
    Kilometraje = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

