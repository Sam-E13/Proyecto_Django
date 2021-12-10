from abc import abstractclassmethod
from django.db import models

# Create your models here.

class claseModelo(models.Model):
    activo = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)

class Meta:
    abstract = True
