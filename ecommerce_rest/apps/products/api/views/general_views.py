from rest_framework import generics

from apps.products.models import MeasureUnit, Indicador, CategoryProduct
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer 

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)


class IndicadorListAPIView(generics.ListAPIView):
    serializer_class = IndicadorSerializer

    def get_queryset(self):
        return Indicador.objects.filter(state = True)


class CategoryProductListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state = True)

