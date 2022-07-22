from rest_framework import viewsets

from apps.base.api import GeneraListAPIView
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer 
from apps.products.models import *

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
    
    def list(self, request):
        '''
        Retorna todos las Unidades de Medida


        params 
        name :  Nombre de la Unidad de medida

        '''
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)
