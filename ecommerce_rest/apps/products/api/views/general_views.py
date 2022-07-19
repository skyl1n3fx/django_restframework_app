from apps.base.api import GeneraListAPIView
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer 

class MeasureUnitListAPIView(GeneraListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicadorListAPIView(GeneraListAPIView):
    serializer_class = IndicadorSerializer

class CategoryProductListAPIView(GeneraListAPIView):
    serializer_class = CategoryProductSerializer

