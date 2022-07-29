from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.expense_manager.api.serializers.expense_serializer import *

from apps.expense_manager.models import *

from apps.expense_manager.api.serializers.general_serializers import *

from rest_framework.decorators import action

from apps.products.models import Product

from apps.base.utils import format_date

# Si queremos enviar el usuario mediante el envio del Token JWT
from rest_framework_simplejwt.authentication import JWTAuthentication

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

    @action(methods=['GET'],detail=False)
    def get_vouchers(self,request):
        data = Voucher.objects.filter(state = True)
        data = VoucherSerializer(data, many = True).data
        return Response(data)

    @action(methods=[ 'get'], detail=False)
    def get_payment_type(self, request):
        data = PaymentType.objects. filter(state=True).order_by('id')
        data = PaymentTypeSerializer(data, many=True).data
        return Response(data)

    @action(methods=[ 'get'], detail=False)
    def get_products(self, request):
        data = Product.objects.filter(state=True).order_by('id')
        data = ProductSerializer(data, many=True).data
        return Response(data)

    def format_data(self,data):
        # Creamos una instancia del JWT
        JWT_authenticator = JWTAuthentication()
        # Decode del token
        # Devuelve 2 cosas (Usuario y Token)
        user, _ = JWT_authenticator.authenticate(self.request)
        data['user'] = user.id
        data['date'] = format_date(data['date'])
        return data

    def create(self, request):
        try:
            data = self.format_data(request.data)
        except:
            # Formato mal enviado.
            print('Formato mal enviado.')
            data = None
        finally:
            serializer = self.serializer_class(data = data)
            
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Factura registrada correctamente.'}, status = status.HTTP_201_CREATED)
        return Response(
            {
                'message' : 'No se pudo crear la factura.',
                'errors' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)