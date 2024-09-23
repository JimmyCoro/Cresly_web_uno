from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm

def login(request):
    if request.method == 'POST':
        print(request.POST)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso. ¡Bienvenido!'})
                messages.success(request, 'Inicio de sesión exitoso. ¡Bienvenido!')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
        # Devolver errores del formulario como JSON si es una solicitud AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = LoginForm()
    
    return render(request, 'base.html', {'login_form': form, 'modal_open': True})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Ajusta según tu modelo de usuario
            user.save()
            # Devolver una respuesta JSON en caso de éxito
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Registro exitoso. ¡Bienvenido!'})
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
        else:
            # Devolver una respuesta JSON en caso de error
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            # Si no es AJAX, podrías manejarlo de otra manera o redirigir
    else:
        form = RegisterForm()

    # Si no es AJAX, puedes devolver algo básico o simplemente no hacer nada
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def logout_view(request):
    logout(request)
    return redirect('/')  