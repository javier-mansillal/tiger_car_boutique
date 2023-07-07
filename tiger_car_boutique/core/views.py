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
        es_nuevo= request.POST.get('es_nuevo', False) == 'on'
        es_nuevo = True if request.POST.get('es_nuevo') == 'on' else False
        vehiculo= Vehiculo(marca=marca, modelo=modelo, año=año, kilometraje= kilometraje, precio=precio, es_nuevo=es_nuevo)
        vehiculo.save()

        return redirect('/vehiculos/')
    return render(request, 'core/crear_vehiculo.html')


