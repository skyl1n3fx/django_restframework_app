from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


# Importamos nuestro modelo base  
from apps.base.models import BaseModel

class RoleUser(BaseModel):
    
    description = models.CharField('Descripción',max_length=50, blank=False, null=False,unique=True)

    class Meta:
        verbose_name = "Rol de Usuario"
        verbose_name_plural = "Roles de Usuario"

    def __str__(self):
        return self.description

    


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', default='', max_length=255, null=True, blank = True) # Modelo con campo Image
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    role = models.ForeignKey(RoleUser, on_delete = models.CASCADE, verbose_name = 'Rol Usuario', null = True)
    historical = HistoricalRecords()
    objects = UserManager()


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
