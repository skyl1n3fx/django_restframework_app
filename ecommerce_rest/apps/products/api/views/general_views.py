from rest_framework import viewsets

from apps.base.api import GeneraListAPIView
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer 
from apps.products.models import *

from rest_framework.response import Response
from rest_framework import status

# ModelViewSet

# No genera todos los endpoints
# ViewSet
# GenericViewSet

class MeasureUnitListAPIView(viewsets.GenericViewSet):
    '''
    Hola desde Unidad de Medida
    '''
    
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        '''
        Retorna todas las Unidades de Medida


        params 
        name :  Nombre de la Unidad de medida

        '''
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)

class IndicadorListAPIView(viewsets.GenericViewSet):
    model = Indicador
    serializer_class = IndicadorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        '''
        Retorna todos los Indicadores


        params 
        name :  Nombre del Indicador

        '''
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)


class CategoryProductListAPIView(viewsets.GenericViewSet):
    model = CategoryProduct
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state = True)

    def list(self, request):
        '''
        Retorna todos las Unidades de Medida


        params 
        name :  Nombre de la Unidad de medida

        '''
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Categoría Registrada Correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(
            {
                'message' : 'Categoria no se pudo crear.',
                'error' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk = None):
        if self.get_object().exists():                
            serializer = self.serializer_class(instance=self.get_object().get(),data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Categoría actualizada correctamente!'}, status = status.HTTP_200_OK)
        return Response(
            {
                'message' : 'Categoria no se pudo actualizar.',
                'error' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST
        )


    def destroy(self,request,pk = None):
        if self.get_object().exists():
            # Eliminación lógica
            serializer = self.get_object().get()
            serializer.state = False
            serializer.save()
            return Response({'message' : 'Categoría eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'message' : 'Categoría no encontrada.'}, status = status.HTTP_400_BAD_REQUEST)