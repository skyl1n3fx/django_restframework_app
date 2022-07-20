from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView
from apps.products.api.views.products_views  import ProductListAPIView, ProductCreateAPIView

urlpatterns = [
   path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
   path('indicator/',IndicadorListAPIView.as_view(), name='indicador'),
   path('category-product/',CategoryProductListAPIView.as_view(), name='category_product'),
   path('product/list',ProductListAPIView.as_view(), name='product_list'),
   path('product/create',ProductCreateAPIView.as_view(), name='product_create'),
]
