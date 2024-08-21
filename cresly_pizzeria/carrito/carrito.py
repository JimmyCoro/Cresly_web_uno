from django.conf import settings
from menu.models import Producto

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            # Guardar un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0, 'precio': str(producto.precio)}

        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad

        self.guardar()

    def guardar(self):
        self.session[settings.CART_SESSION_ID] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    def limpiar(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def __iter__(self):
        producto_ids = self.carrito.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        for producto in productos:
            self.carrito[str(producto.id)]['producto'] = producto

        for item in self.carrito.values():
            item['precio'] = float(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())

    def get_total_precio(self):
        return sum(float(item['precio']) * item['cantidad'] for item in self.carrito.values())
