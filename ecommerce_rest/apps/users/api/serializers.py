from rest_framework import serializers
from apps.users.models import User

# Subir imagen
from drf_extra_fields.fields import Base64ImageField

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializador para el nuevo login
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')

class UserSerializer(serializers.ModelSerializer):
    
    # Sobreescribimos al atributo Image, para que acepte codificación base 64
    image = Base64ImageField(required=False)
    password = serializers.CharField(min_length=3, required=False)

    class Meta:
        model = User
        fields = '__all__'
        # exclude

    def create(self,validated_data):
        # Encriptamos la contraseña
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance, validated_data)
        try:
            # Encripta la contraseña sólo si se actualiza
            updated_user.set_password(validated_data['password'])
        except Exception as ex:
            pass
        finally:
            updated_user.save()
        
        return updated_user

# Creamos un serializer para sólo lectura
class UserListSerializer(serializers.ModelSerializer):

    # Mostrar una relación foránea como JSON 
    # tipo = TipoSerializer(read_only = True)
    # Le indicamos los tipos de usuarios aceptados
    # tipo_id = serializers.PrimaryKeyRelatedField(queryset=Tipo.objects.all(), source="tipo")

    class Meta:
        model = User

    def to_representation(self,instance):
        # print(instance)
        # super().to_representation(instance) llama a cada uno de los valores (fields)
        return {
            'id' : instance['id'],
            'nombre_usuario' : instance['username'],
            'correo' : instance['email'],
            'foto' : instance['image'],
            'contrasenia' : instance['password'],
        }




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
        existe = User.objects.filter(email=value).exists()

        if existe:
            raise serializers.ValidationError('Error el email ya se encuentra registrado!')
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