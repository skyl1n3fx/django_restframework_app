from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.expense_manager.api.serializers.expense_serializer import *

from apps.expense_manager.models import *

from apps.expense_manager.api.serializers.general_serializers import *

from rest_framework.decorators import action

# ModelViewset me crea todos los métodos automáticos.
# Generic viewset debo declararlos yo

class ExpenseViewSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer

    @action(methods=['GET'],detail=False, url_path = 'search-supplier')
    def search_supplier(self,request):
        # Recibimos el query param de la petición GET
        ruc_or_business_name = request.query_params.get('ruc_or_business_name','')
        print(ruc_or_business_name)
        supplier = Supplier.objects.filter(
            Q(ruc__iexact=ruc_or_business_name) |
            Q(business_name__iexact=ruc_or_business_name)
        ).first()
        if supplier:
            # Una vez lo encontramos debesmos serializarlo.
            supplier_serializer = SupplierSerializer(supplier)
            return Response(supplier_serializer.data,status = status.HTTP_200_OK)
        return Response({'message':'No se ha entrado un proveedor.'}, status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def new_supplier(self,request):
        data_supplier = request.data
        data_supplier = SupplierRegisterSerializer(data=data_supplier)
        if data_supplier.is_valid():
            data_supplier = data_supplier.save()
            return Response({
                'message' : 'Proveedor registrado correctamente!',
                'supplier' : data_supplier
            }, status=status.HTTP_201_CREATED)
        return Response({'error':data_supplier.errors}, status = status.HTTP_400_BAD_REQUEST)
