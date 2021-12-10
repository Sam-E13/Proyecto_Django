from django.urls import path

from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('categorias/',views.categorias, name='categorias'),
    path('productos/',views.productos, name='productos'),

    path('crear_producto/',views.crearProducto, name='crear_producto'),
    path('listar_producto/',views.listarProducto, name='listar_producto'),

    url(r'^editar_producto/(?P<id>\d+)$', views.editarProducto, name="editar_producto"),
    url(r'^eliminar_producto/(?P<id>\d+)$', views.eliminarProducto, name="eliminar_producto"),

    path('listar_cliente/',views.listarCliente, name='listar_cliente'),
    path('crear_cliente/',views.crearCliente, name='crear_cliente'),
    url(r'^editar_cliente/(?P<id>\d+)$', views.editarCliente, name="editar_cliente"),
    url(r'^eliminar_cliente/(?P<id>\d+)$', views.eliminarCliente, name="eliminar_cliente"),
        

]