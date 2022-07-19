from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView

urlpatterns = [
   path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
   path('indicator/',IndicadorListAPIView.as_view(), name='indicador'),
   path('category-product/',CategoryProductListAPIView.as_view(), name='category_product'),
]
