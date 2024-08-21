from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # Ruta raíz para la app 'inicio'
    path('menu/', include('menu.urls')),  # Ruta para la app 'menu'
    path('usuarios/', include('usuarios.urls')),  # Ruta para la app 'usuarios'
    path('locales/', include('nuestros_locales.urls')),  # Ruta para la app 'nuestros_locales'
    path('carrito/', include('carrito.urls')),  # Ruta para la app 'nuestros_locales'

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
