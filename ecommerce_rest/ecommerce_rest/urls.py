from django.contrib import admin
from django.urls import path, include, re_path

# Configs para servir las imágenes
from django.conf import settings
from django.conf.urls.static import static


# Importamos en nuestro archivo de rutas
# para Drf 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

from apps.users.views import Login, Logout

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

schema_view = get_schema_view(
  openapi.Info(
    title="Documentación de API",
    default_version='v0.1',
    description="Documentación pública de API de Monas Xinas",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="developerpeperu@gmail.com"),
    license=openapi.License(name="Shinigami License"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(),name='logout'),
    path('login/',Login.as_view(),name='login'),
    #path('refresh-token/',UserToken.as_view(), name = 'refresh_token'),
    path('usuario/', include('apps.users.api.routers')),
    path('products/',include('apps.products.api.urls')),
    path('productos/',include('apps.products.api.routers')),
    # Implementamos las rutas de JWT.
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    # Ruta de redirección por url erronéa
    re_path(r'^(?P<path>.*)/$', include('apps.products.api.routers'), name='uwu'),
]

# Se debe realizar la consulta implementando en la petición en los HEADERS
# Para JWT
# Authorization :  Bearer {TOKEN}

# Si estamos en DEBUG, los archivos se servirán en MEDIA_URL y MEDIA_ROOT
# URL para acceder a las fotos
# http://localhost:8000/usuario/archivos/perfil/00d71a0b-d4b3-4281-8f32-eb167dcff825.jpg

'''
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''


from django.views.static import serve

urlpatterns += [
  re_path(r'media/^(?P<path>.*)$', serve, {
    'document_root' : settings.MEDIA_ROOT
  }),
]