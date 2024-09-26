# models.py

from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(null=False, blank=False, max_length=70)
    descripcion = models.CharField(max_length=200)
    
        
    @property
    def get_producto(self):
        return Producto.objects.filter(categoria_id=self.id)
    
    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(default='', upload_to='producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_producto

class Pizza(models.Model):
    SABOR_CHOICES = [
        ('Tres Carnes', 'Tres Carnes'),
        ('Champiñones', 'Champiñones'),
        ('Hawaiana', 'Hawaiana'),
        ('Pepperoni', 'Pepperoni'),
        ('Tres Quesos', 'Tres Quesos'),
        ('Chorizo', 'Chorizo'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor_1 = models.CharField(max_length=15, choices=SABOR_CHOICES)
    sabor_2 = models.CharField(max_length=15, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1} / {self.sabor_2 if self.sabor_2 else ''}"

class Alitas(models.Model):
    SABOR_CHOICES = [
        ('BBQ', 'BBQ'),
        ('Miel y Mostaza', 'Miel y Mostaza'),
        ('Macaruyá', 'Macaruyá'),
        ('Broster', 'Broster'),
        ('Piña', 'Piña'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor_1 = models.CharField(max_length=15, choices=SABOR_CHOICES)
    sabor_2 = models.CharField(max_length=15, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1} / {self.sabor_2 if self.sabor_2 else ''}"
    
    
    
class Bebida(models.Model):
    SABOR_CHOICES = [
        ('Coca Cola', 'Coca Cola'),
        ('Fanta', 'Fanta'),
        ('Fiora', 'Fiora'),
        ('Sprite', 'Sprite'),
        ('Inka', 'Inka'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor = models.CharField(max_length=15, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1}"
    

# models.py

class ComboFamiliar(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pizza_sabor_1 = models.CharField(max_length=15, choices=Pizza.SABOR_CHOICES)
    pizza_sabor_2 = models.CharField(max_length=15, choices=Pizza.SABOR_CHOICES)
    alita_sabor_1 = models.CharField(max_length=15, choices=Alitas.SABOR_CHOICES)
    alita_sabor_2 = models.CharField(max_length=15, choices=Alitas.SABOR_CHOICES)
    bebida_sabor = models.CharField(max_length=15, choices=Bebida.SABOR_CHOICES)

    def __str__(self):
        return f"Combo: {self.producto.nombre_producto}, Pizzas: {self.pizza_sabor_1} / {self.pizza_sabor_2}, Alitas: {self.alita_sabor_1} / {self.alita_sabor_2}, Bebida: {self.bebida_sabor}"
