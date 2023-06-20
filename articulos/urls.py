from django.urls import path
from .views import inicio,contactanos,mision,pago,tienda,crear,eliminar,modificar,registrar,mostrarAdmin,mostrarUsuario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contactanos/', contactanos, name="contactanos"),
    path('mision/', mision, name="mision"),
    path('pago/', pago, name="pago"),
    path('tienda/', tienda, name="tienda"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/',registrar,name="registrar"),
    path('mostrarAdmin/',mostrarAdmin, name="mostrarAdmin"),
    path('mostrarUsuario/',mostrarUsuario, name="mostrarUsuario"),
]