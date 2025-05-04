from django.db import models
from users.models import CustomUser

class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.full_name