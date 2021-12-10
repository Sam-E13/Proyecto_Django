from django.db import models

from generales.models import claseModelo

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    #Se sugiere nombrar la clase en singular 
    #No se deben indicar los campos clave 
    #Django genera en automatico las Primary key 

    def __str__(self):
        return '%s' % (self.nombre)


class Producto (models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.descripcion)
class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.nombre)

class Pedido (models.Model):
    no_pedido = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.no_pedido)