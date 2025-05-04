from django.urls import path
from .views import create_client, client_list

urlpatterns = [
    path('create/', create_client, name='create_client'),
    path('list/', client_list, name='client_list'),
]