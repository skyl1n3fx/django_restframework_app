from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, CategoryProductSerializer

# Subir imagen
from drf_extra_fields.fields import Base64ImageField


class ProductSerializers(serializers.ModelSerializer):
    # Sobreescribimos al atributo Image, para que acepte codificación base 64
    #image = Base64ImageField(required=False)
    '''
    # Método 1 de mostrar relaciones en un serializer
    measure_unit = MeasureUnitSerializer()
    category = CategoryProductSerializer()

    # Método 2 es mostrar la clase Meta 
    measure_unit = serializers.StringRelatedField()
    '''
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')

    # Método 3 
    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'stock' : instance.stock.get('quantity__sum') if instance.stock.get('quantity__sum') is not None else 0,
            'name' : instance.name,
            'description' : instance.description,
            'image' : instance.image.url if instance.image != '' else '',
            'measure_unit' : instance.measure_unit.description if instance.measure_unit is not None else '',
            'category' : {
                'id' : instance.category.id,
                'description' : instance.category.description
            } if instance.category is not None else ''
        }
        
    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una Unidad de Medida.")
        return value

    def validate_category(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una Categoria de producto.")
        return value


    def validate(self,data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError(
                    {
                        "measure_unit" : "Debe ingresar una unidad de Medida."
                    }
                )
        if 'category' not in data.keys():
            raise serializers.ValidationError({"category":"Debe ingresar una Categoria de producto."})
        return data