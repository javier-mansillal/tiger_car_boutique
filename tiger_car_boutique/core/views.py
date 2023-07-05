from django.shortcuts import render, redirect
from.models import Vehiculo

# Create your views here.
def lista_vehiculo(request):
    vehiculos =Vehiculo.objects.all()
    return render(request, "core/lista_vehiculo.html",{'vehiculos': vehiculos})


def crear_vehiculo(request):
    if request.method =='POST':
        marca= request.POST['marca']
        modelo= request.POST['modelo']
        año= request.POST['año']
        kilometraje= request.POST['kilometraje']
        precio= request.POST['precio']
        vehiculo= request.POST['vehiculo']
        vehiculo= vehiculo(marca=marca, modelo=modelo, año=año, kilometraje= kilometraje, precio=precio)
        vehiculo.save()

        return redirect('lista_vehiculo')
    return render(request, 'core/crear_vehiculo.html')


