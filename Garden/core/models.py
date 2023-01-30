from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True, verbose_name = "Id de categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name = "Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Planta(models.Model):
    idPlanta = models.IntegerField( primary_key=True, verbose_name="Id de planta" )
    nombre = models.CharField(max_length=20, verbose_name="Nombre de planta" )
    precio = models.IntegerField(max_length=20, null=True , blank=True, verbose_name="precio" )
    stock = models.IntegerField( null=True , blank=True, verbose_name="stock" )
    idCategoria = models.ForeignKey('Categoria' , on_delete=models.CASCADE )
    imagen = models.CharField(max_length=60,null=True , blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.nombre

