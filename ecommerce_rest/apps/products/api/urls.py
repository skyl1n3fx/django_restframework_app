from django.urls import path

from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView,CategoryList
from apps.products.api.views.products_views  import (
   ProductListAPIView, ProductDestroyAPIView, ProductUpdateAPIView,
   ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
   )

urlpatterns = [
   #path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
   #path('indicator/',IndicadorListAPIView.as_view(), name='indicador'),
   #path('category-product/',CategoryProductListAPIView.as_view(), name='category_product'),
   path('product/list',ProductListAPIView.as_view(), name='product_list'),
   path('product/',ProductListCreateAPIView.as_view(), name='product_create'),
   path('product/retrieve-update-destroy/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
   path('product/destroy/<int:pk>',ProductDestroyAPIView.as_view(), name='product_destroy'),
   path('product/update/<int:pk>',ProductUpdateAPIView.as_view(), name='product_update'),
   path('uwu/',CategoryList.as_view(), name='category_list'),
]
