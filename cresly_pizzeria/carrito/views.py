from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
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

from django.shortcuts import get_object_or_404, redirect
from .models import Producto
from .carrito import Carrito
from django.urls import reverse

def eliminar_producto(request, producto_id, sabor_1=None, sabor_2=None):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Si sabor_1 o sabor_2 están vacíos, se manejan como None
    sabor_1 = None if sabor_1 == '' else sabor_1
    sabor_2 = None if sabor_2 == '' else sabor_2
    
    carrito.eliminar(producto, sabor_1=sabor_1, sabor_2=sabor_2)
    return redirect('ver_carrito')




def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('ver_carrito')

def actualizar_cantidad(request, producto_id):
    carrito = Carrito(request)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito.agregar(producto_id, cantidad=cantidad, actualizar_cantidad=True)
    return redirect(reverse('carrito'))