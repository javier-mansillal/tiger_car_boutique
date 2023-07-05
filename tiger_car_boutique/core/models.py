from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    año = models.IntegerField()
    kilometraje = models.IntegerField()
    precio = models.IntegerField()
    vehiculo = models.CharField(max_length=300)
    es_nuevo = models.BooleanField()
    
    def __str__(self):
        return self.vehiculo