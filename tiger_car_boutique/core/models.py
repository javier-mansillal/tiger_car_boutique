from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año  = models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    es_nuevo = models.BooleanField()

    def __str__(self):
        return (str(self.marca) + ' ' + str(self.modelo))
