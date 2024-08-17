from django.shortcuts import render


def nuestros_locales(request):
    return render(request, 'nuestros_locales/locales.html', {})


