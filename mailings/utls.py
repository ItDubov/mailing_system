from django.urls import path
from .views import create_mailing, mailing_list

urlpatterns = [
    path('create/', create_mailing, name='create_mailing'),
    path('list/', mailing_list, name='mailing_list'),
]
