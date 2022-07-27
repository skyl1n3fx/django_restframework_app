from django.urls import path
from apps.users.views import index

urlpatterns = [
    path('email/',index, name = 'email'),
]
