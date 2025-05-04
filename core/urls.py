from django.urls import path
from .views import home, statistics

urlpatterns = [
    path('', home, name='home'),
    path('statistics/', statistics, name='statistics'),
]
