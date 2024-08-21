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
        ('TRC', 'Tres Carnes'),
        ('CHA', 'Champiñones'),
        ('HAW', 'Hawaiana'),
        ('PEP', 'Pepperoni'),
        ('TQ', 'Tres Quesos'),
        ('CHO', 'Chorizo'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor_1 = models.CharField(max_length=3, choices=SABOR_CHOICES)
    sabor_2 = models.CharField(max_length=3, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1} / {self.sabor_2 if self.sabor_2 else ''}"

class Alitas(models.Model):
    SABOR_CHOICES = [
        ('BBQ', 'BBQ'),
        ('MYM', 'Miel y Mostaza'),
        ('MAR', 'Macaruyá'),
        ('BRS', 'Broster'),
        ('PIN', 'Piña'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor_1 = models.CharField(max_length=3, choices=SABOR_CHOICES)
    sabor_2 = models.CharField(max_length=3, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1} / {self.sabor_2 if self.sabor_2 else ''}"
    
    
    
class Bebida(models.Model):
    SABOR_CHOICES = [
        ('CCC', 'Coca COla'),
        ('FNT', 'Fanta'),
        ('FIO', 'Fiora'),
        ('SPR', 'Sprite'),
        ('INK', 'Inka'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sabor = models.CharField(max_length=3, choices=SABOR_CHOICES)

    def __str__(self):
        return f"{self.sabor_1}"
    
    