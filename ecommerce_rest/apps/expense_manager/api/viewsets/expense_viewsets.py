from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.expense_manager.api.serializers.expense_serializer import *

# ModelViewset me crea todos los métodos automáticos.
# Generic viewset debo declararlos yo

class ExpenseViewSet(viewsets.GenericViewSet):
    serializer_class = ExpenseSerializer