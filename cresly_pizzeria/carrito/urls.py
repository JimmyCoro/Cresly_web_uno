from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('limpiar_carrito/', views.limpiar_carrito, name='limpiar_carrito'),
    path('eliminar_producto/<int:producto_id>/<str:sabor_1>/(<str:sabor_2>/)?', views.eliminar_producto, name='eliminar_producto'),
]
