from django.shortcuts import render
from django.shortcuts import render
from usuarios.forms import RegisterForm, LoginForm

def inicio(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    return render(request, 'inicio/inicio.html', {
        'register_form': register_form,
        'login_form': login_form
    })

