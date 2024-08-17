from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cliente

def save_cliente(request):

    print(request.GET)
    if request.method == 'POST':
        correo = request.POST['correo']  # acceder a valores del diccionario POSt lo mismo
        password = request.POST['password']
        apellido = request.POST['apellido']
        nombre = request.POST.get('nombre', 'no hay valor')  # acceder a valores del diccionario
        print(request.POST)
        print(correo, nombre, apellido, password)

        usuario1 = User(username=correo, password=password)
        usuario1.set_password(password)
        usuario1.save()

        cliente1 = Cliente(nombre=nombre, apellido=apellido, correo=correo, usuario=usuario1)
        cliente1.save()

        return redirect('inicio')
    else:
        return HttpResponse(f"PETICION GET")