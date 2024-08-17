from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=52)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    


