from apps.base.api import GeneraListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializers


class ProductListAPIView(GeneraListAPIView):
    serializer_class = ProductSerializers