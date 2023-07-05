from django.urls import path, include
from rest_framework import routers
from . import views
from .views import VehiculoViewSet

router = routers.DefaultRouter()
router.register('vehiculo', VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
