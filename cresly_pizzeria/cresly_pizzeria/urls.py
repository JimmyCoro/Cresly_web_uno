
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('menu.urls')),
    path('', include('usuarios.urls')),
    path('', include('nuestros_locales.urls')),


]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
