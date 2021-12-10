from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalogos.forms import ProductoForm, ClienteForm
from .models import Categoria, Producto, Cliente


# Create your views here.
def home (request):
    return render(request, 'home.html')

#Creacion de las funciones para el crud

#Basada en funciones 
def crearProducto (request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
            form = ProductoForm()
            return render (request, 'crear_producto.html', {'form':form})

def listarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos' : productos}
    return render (request, 'listar_producto.html', contexto)

def editarProducto(request,id):
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect ('home')
    return render (request, 'crear_producto.html', {'form' : form})

def eliminarProducto(request,id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect ('home')
    return render (request, 'eliminar_producto.html', {'producto' : producto })

def crearCliente (request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
    else:
            form = ClienteForm()
            return render (request, 'crear_cliente.html', {'form':form})

def listarCliente(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes' : clientes}
    return render (request, 'listar_cliente.html', contexto)

def editarCliente(request,id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
    else:
        form=ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect ('home')
    return render (request, 'crear_cliente.html', {'form' : form})

def eliminarCliente(request,id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect ('home')
    return render (request, 'eliminar_cliente.html', {'cliente' : cliente })

def categorias (request):
    #return render(request, 'categorias.html')
    #Uso de los Querysets de Django -- Consultas de la base de datos mendiante ORM
    categ= Categoria.objects.all() #Select * from Ccategoria
    contexto = {'categorias':categ}

    return render (request, 'categorias.html', contexto)

def productos (request):
    return render(request, 'productos.html')
