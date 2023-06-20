
from tabnanny import verbose
from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    idMasc= models.IntegerField(primary_key=True, verbose_name="Id TipoMasc")
    nombreTipo= models.CharField(max_length=50, blank=True, verbose_name="Tipo de Mascota")
    
    def __str__(self) -> str:
        return self.nombreTipo
    
class Marca(models.Model):
    idMarca= models.IntegerField(primary_key=True, verbose_name="Id Marca")
    nombreMarca= models.CharField(max_length=50, blank=True, verbose_name="Marca")

    def __str__(self) -> str:
        return self.nombreMarca 
    
class Alimento(models.Model):
    cod= models.IntegerField(primary_key=True, verbose_name="Codigo")
    nombre= models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    tipo= models.ForeignKey(TipoMascota, on_delete=models.CASCADE, verbose_name="Tipo de Mascota")
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    imagen= models.ImageField(upload_to="imagenes",null=True , blank=True, verbose_name="Imagen")
    precio= models.IntegerField(default=0 , blank=True, verbose_name="Precio")

    def __str__(self) -> str:
        return self.nombre
