from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .carrito import Carrito
from menu.models import Producto
from .models import Pedido, DetallePedido
from django.conf import settings  


def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id) 
    carrito.agregar(producto)
    return redirect('carrito:ver_carrito')

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

@login_required
def finalizar_compra(request):
    carrito = Carrito(request)

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        datos_entrega = request.POST.get('datos_entrega')

        # Crear el pedido con los datos adicionales
        pedido = Pedido.objects.create(
            cliente=request.user,
            total=carrito.get_total_precio(),
            direccion=direccion,
            telefono=telefono,
            datos_entrega=datos_entrega
        )

        # Crear detalles de pedido (productos en el carrito)
        for item in carrito:
            DetallePedido.objects.create(
                pedido=pedido,
                producto=item['producto'],
                cantidad=item['cantidad'],
                sabor_1=item['sabor_1'],
                sabor_2=item['sabor_2'],
                precio_unitario=item['precio'],
                subtotal=item['total_precio']
            )

        # Limpia el carrito después de crear el pedido
        print("Antes de limpiar el carrito:", request.session.get(settings.CART_SESSION_ID))
        carrito.limpiar()
        print("Después de limpiar el carrito:", request.session.get(settings.CART_SESSION_ID))

        # Redirigir a una página de éxito
        return redirect('exito_pedido')

    return redirect('ver_carrito')


def exito_pedido(request):
    # Obtén el último pedido del usuario
    pedido = Pedido.objects.filter(cliente=request.user).order_by('-id').first()
    detalles = DetallePedido.objects.filter(pedido=pedido) if pedido else []

    return render(request, 'carrito/exito_pedido.html', {
        'pedido': pedido,
        'detalles': detalles,
    })




