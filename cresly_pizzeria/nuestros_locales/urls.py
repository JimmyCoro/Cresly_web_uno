from django.urls import path
from .views import nuestros_locales

urlpatterns = [
    path('', nuestros_locales, name='nuestros_locales')

]
