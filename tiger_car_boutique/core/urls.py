from django.urls import path

from . import views
app_name = 'core'
urlpatterns = [
    path("", views.lista_vehiculo, name="lista_vehiculo"),
    path("create/", views.crear_vehiculo, name="crear_vehiculo"),
]