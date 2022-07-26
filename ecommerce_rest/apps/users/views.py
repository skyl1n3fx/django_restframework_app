from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Create your views here.

from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def sendEmail(email):
    context = {'mail': "こんにちはホセ、私は私のロシアのバンカーから挨拶を送ります。" }
    template = get_template('correo.html')
    content = template.render(context)

    correo = EmailMultiAlternatives(
        'Este es un correo de prueba 死神',
        'x4leqxinn',
        settings.EMAIL_HOST_USER,
        [email]
        #cc=[] copia a 
    )

    correo.attach_alternative(content, 'text/html')
    correo.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('txtMail')
        sendEmail(mail)

    return render(request,'index.html',{})



from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import (
    CustomTokenObtainPairSerializer,
    CustomUserSerializer
    )
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')

        user = authenticate(
            username = username,
            password = password
            )


        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response(
                    {
                        'token' : login_serializer.validated_data.get('access'),
                        'refresh-token' : login_serializer.validated_data.get('refresh'),
                        'user' : user_serializer.data,
                        'message' : 'Inicio de sesión éxitoso.'
                    }, status = status.HTTP_200_OK
                )
            return Response({'error' : 'Contraseña o Nombre de usuario incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error' : 'Contraseña o Nombre de usuario incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id = request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message' : 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error' : 'No existe este usuario.'})

