from django.contrib import admin
from django.urls import path, include

# Configs para servir las imágenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('products/',include('apps.products.api.urls')),
    path('productos/',include('apps.products.api.routers')),
]

# Si estamos en DEBUG, los archivos se servirán en MEDIA_URL y MEDIA_ROOT
# URL para acceder a las fotos
# http://localhost:8000/usuario/archivos/perfil/00d71a0b-d4b3-4281-8f32-eb167dcff825.jpg

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)