from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView
from apps.products.api.views.products_views  import (
   ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductDestroyAPIView
   )

urlpatterns = [
   path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
   path('indicator/',IndicadorListAPIView.as_view(), name='indicador'),
   path('category-product/',CategoryProductListAPIView.as_view(), name='category_product'),
   path('product/list',ProductListAPIView.as_view(), name='product_list'),
   path('product/create',ProductCreateAPIView.as_view(), name='product_create'),
   path('product/retrieve/<int:pk>',ProductRetrieveAPIView.as_view(), name='product_retrieve'),
   path('product/destroy/<int:pk>',ProductDestroyAPIView.as_view(), name='product_destroy'),
]
