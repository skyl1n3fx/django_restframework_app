from rest_framework import serializers

from apps.expense_manager.models import *  

class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        exclude = ('state' , 'created_date' , ' modified_date' , 'deleted_date')