from django.contrib import admin

from menu.models import * 

modelos = [Categoria, Producto]
  
admin.site.register(modelos)
