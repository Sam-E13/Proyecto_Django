from django.contrib import admin

from .models import Categoria, Cliente, Pedido, Producto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)