from rest_framework import generics

from rest_framework.response import Response
# Para usar status codes
from rest_framework import status

from apps.products.api.serializers.product_serializers import ProductSerializers
from apps.base.api import GeneraListAPIView

# Para los viewset
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers       
    # from rest_framework.parsers import JSONParser
    # parser_classes = (JSONParser) 
    # Por defecto DRF permite JSONPARSER, FORMPARSER, MULTIPARTPARSER
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    def list(self,request):
        for key, value in request.__dict__.items():
            print(key)
        product_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(product_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        '''
            from apps.base.utils import validate_files
            # Procesamos la información antes de validarla
            data =  validate_files(request.data,'image')
        '''
        serializer = self.serializer_class(data = request.data) # Aquí enviariamos el resultado de data
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente.'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message' : 'Ola olvidona'}, status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product: 
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


class ProductListAPIView(GeneraListAPIView):
    serializer_class = ProductSerializers

# De generics ListCreate API View permite método POST y GET
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = ProductSerializers.Meta.model.objects.filter(state = True)

    '''
    def get_queryset(self):
        # Es más escalable

    '''

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente.'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers

    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    # Podemos sobreescribir el método GET
    '''
    def get(self, request,pk = None):
    '''


    def patch(self, request,pk = None):
        
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message' : 'El producto se actualizó correctamente bb<3'}, status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product: 
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


# Eliminar 

# No se debe realizar una eliminación como tal en la base de datos 
# Se debe realizar una eliminación lógica
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    # Sobreescribimos el método delete
    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product: 
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self, request,pk = None):
        
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response({'Error' :  '¡No existe un producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)