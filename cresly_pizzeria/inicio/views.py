from django.shortcuts import render
from .views import *
from usuarios.forms import  ClienteForm

# Create your views here.
def inicio(request):
    data = {}
    formulario = ClienteForm()
    data['formulario'] = formulario
    return render(request, 'inicio/inicio.html', data)