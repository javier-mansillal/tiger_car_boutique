from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiculoSerializer
from core.models import Vehiculo
# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.filter(es_nuevo=True).values()
    serializer_class = VehiculoSerializer