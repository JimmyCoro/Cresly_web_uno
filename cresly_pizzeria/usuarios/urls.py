from django.urls import path
from .views import save_cliente


urlpatterns = [
    path('save_cliente', save_cliente, name='save_cliente')
]