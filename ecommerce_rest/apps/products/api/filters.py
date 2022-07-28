import django_filters
from apps.products.models import *

class CategoryFilter(django_filters.FilterSet):

    # description = django_filters.CharFilter(lookup_expr = 'icontains')
    
    class Meta:
        model = CategoryProduct
        #fields = ('description',)
        
        fields = {
            'id' : ['gt','lt','contains','exact'],
            'description' : ['exact' ,'contains']
        }
            
        
        