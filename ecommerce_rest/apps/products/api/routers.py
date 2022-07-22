from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_views import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'productos',ProductViewSet, basename='productos')  
router.register(r'categorias',CategoryProductListAPIView, basename='categorias')  
router.register(r'unidades-medida',MeasureUnitListAPIView, basename='unidades-medida')  
router.register(r'indicadores',IndicadorListAPIView, basename='indicadores')  


urlpatterns = router.urls