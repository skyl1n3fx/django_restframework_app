from rest_framework.test import APITestCase
from faker import Faker
from rest_framework import status

class TestSetup(APITestCase):
    
    def setUp(self):
        from apps.users.models import User

        faker = Faker()

        # Definimos cual es la ruta de mi login
        self.login_url = '/login/' #reverse
        self.user = User.objects.create_superuser(
            name = 'QATester',
            last_name = 'QATester',
            username = faker.name(),
            password = 'QATester',
            email = faker.email() # Me crea un email falso
        )
        '''
            Cuando Creamos Pruebas Unitarias se crea 
            una base de datos externa donde se realizas
            los Test Cases 
        '''

        # Simulo un cliente
        # POST, PUT, PATCH, DELETE, GET
        response = self.client.post(
            self.login_url,
            {
                'username' : self.user.username,
                'password' : 'QATester'
            },
            format = 'json'
        )

        # Verifica la igualdad de 2 valores.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Permite detener la ejecución.
        # import pdb; pdb.set_trace() 
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()
