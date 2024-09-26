from django.db import models
from django.contrib.auth.models import User
from menu.models import Producto

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    direccion = models.CharField(max_length=255, default="Sin dirección")
    telefono = models.CharField(max_length=20)    # Teléfono del cliente
    datos_entrega = models.TextField(blank=True, null=True)  # Otros detalles de entrega

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    sabor_1 = models.CharField(max_length=100, blank=True, null=True)
    sabor_2 = models.CharField(max_length=100, blank=True, null=True)
    sabor_alita_1 = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo para sabor de alita
    sabor_alita_2 = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo para sabor de alita
    sabor_bebida = models.CharField(max_length=100, blank=True, null=True)    # Nuevo campo para sabor de bebida
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre_producto} - Pedido {self.pedido.id}"
