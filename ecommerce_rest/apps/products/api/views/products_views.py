from rest_framework import generics
from rest_framework.response import Response
# Para usar status codes
from rest_framework import status


from apps.base.api import GeneraListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializers


class ProductListAPIView(GeneraListAPIView):
    serializer_class = ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializers

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente.'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)