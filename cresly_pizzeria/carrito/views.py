from django.shortcuts import render, redirect
from .carrito import Carrito
from menu.models import Producto


def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('carrito:ver_carrito')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito:ver_carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito:ver_carrito')
