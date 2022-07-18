from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude


# Serializados que no está basado en un modelo
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    # Custom validation
    def validate_name(self, value):
        if 'monaxina' in value:
            raise serializers.ValidationError('Error, el usuario no puede llamarse mona xina.')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Error, debe indicar un correo electrónico.')
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('El email no puede contener el nombre.')
        return value

    def validate(self, data):
        '''
        if data['name'] in data['email']:
            raise serializers.ValidationError('El mail no puede contener el nombre.')
        '''
        print('Validación general')
        return data
        
    def create(self,validated_data):
        print(validated_data)
        #return User(**validated_data)
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance


    # Sirve si queremos validar y no guardar en una Base de datos
    '''
    def save(self):
        print(self.validated_data)
        send_email()
    '''

# Si queremos hacer validaciones especificas por campo en caso de Create or Update.
# Podemos hacerlo en el método.
# Podemos crear 2 serializers para uno por caso.