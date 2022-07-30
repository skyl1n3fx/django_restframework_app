from rest_framework import serializers
from apps.users.models import User

# Importamos los grupos
from django.contrib.auth.models import Group

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

        # Buscamos el Grupo de permisos y se lo asignamos al usuario.
        group = Group.objects.get(id=1) 
        user.groups.add(group)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email', 'name', 'last_name')


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 128, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 128, min_length = 6, write_only = True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Debe ingresar ambas contraseñas iguales.'})
        return data


# Creamos un serializer para sólo lectura
class UserListSerializer(serializers.ModelSerializer):

    # Mostrar una relación foránea como JSON 
    # tipo = TipoSerializer(read_only = True)
    # Le indicamos los tipos de usuarios aceptados
    # tipo_id = serializers.PrimaryKeyRelatedField(queryset=Tipo.objects.all(), source="tipo")

    class Meta:
        model = User

    def to_representation(self,instance):
        print(instance)
        # super().to_representation(instance) llama a cada uno de los valores (fields)
        return {
            'id' : instance['id'],
            'nombre_usuario' : instance['username'],
            'correo' : instance['email'],
            'foto' : instance['image'],
            'contrasenia' : instance['password']
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