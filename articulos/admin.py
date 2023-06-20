from django.contrib import admin
from .models import Alimento,Marca,TipoMascota

# Register your models here.

admin.site.register(Alimento)
admin.site.register(Marca)
admin.site.register(TipoMascota)

