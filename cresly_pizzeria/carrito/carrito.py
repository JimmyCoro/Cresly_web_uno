from django.conf import settings
from menu.models import Producto

class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        if not carrito:
            carrito = self.session[settings.CART_SESSION_ID] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1, sabor=None, sabor_1=None, sabor_2=None, sabor_alita_1=None, sabor_alita_2=None, sabor_bebida=None, actualizar_cantidad=False):
        # Crear una clave única basada en el ID del producto y los sabores
        producto_id = str(producto.id)

        # Agregar la lógica para asegurar que el sabor de la bebida se incluya en la clave si es necesario
        if producto.categoria.nombre_categoria == 'Bebidas':
            clave_producto = f'{producto_id}_{sabor_bebida or "N/A"}'
        else:
            clave_producto = f'{producto_id}_{sabor_1 or "N/A"}_{sabor_2 or "N/A"}'

        if clave_producto not in self.carrito:
            # Añadir el producto con una clave única que incluye los sabores
            self.carrito[clave_producto] = {
                'cantidad': 0,
                'precio': str(producto.precio),
                'sabor_1': sabor_1,
                'sabor_2': sabor_2,
                'sabor_alita_1': sabor_alita_1,
                'sabor_alita_2': sabor_alita_2,
                'sabor_bebida': sabor_bebida,
                'sabor': sabor,
            }

        if actualizar_cantidad:
            self.carrito[clave_producto]['cantidad'] = cantidad
        else:
            self.carrito[clave_producto]['cantidad'] += cantidad

        # Actualizar los sabores en caso de que se proporcionen
        if sabor_1 is not None:
            self.carrito[clave_producto]['sabor_1'] = sabor_1
        if sabor_2 is not None:
            self.carrito[clave_producto]['sabor_2'] = sabor_2
        if sabor_alita_1 is not None:
            self.carrito[clave_producto]['sabor_alita_1'] = sabor_alita_1
        if sabor_alita_2 is not None:
            self.carrito[clave_producto]['sabor_alita_2'] = sabor_alita_2
        if sabor_bebida is not None:
            self.carrito[clave_producto]['sabor_bebida'] = sabor_bebida


        self.guardar()

    def guardar(self):
        self.session[settings.CART_SESSION_ID] = self.carrito
        self.session.modified = True

    def eliminar(self, producto, sabor_1=None, sabor_2=None):
        producto_id = str(producto.id)
        clave_producto = f'{producto_id}_{sabor_1 or "N/A"}_{sabor_2 or "N/A"}'
        
        if clave_producto in self.carrito:
            del self.carrito[clave_producto]
            self.guardar()


    def limpiar(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def __iter__(self):
        producto_ids = {clave.split('_')[0] for clave in self.carrito.keys()}
        productos = Producto.objects.filter(id__in=producto_ids)
        
        for producto in productos:
            for clave, item in self.carrito.items():
                if clave.startswith(str(producto.id)):
                    item['producto'] = producto
                    item['precio'] = float(item['precio'])
                    item['total_precio'] = item['precio'] * item['cantidad']
                    yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())

    def get_total_precio(self):
        return sum(float(item['precio']) * item['cantidad'] for item in self.carrito.values())
