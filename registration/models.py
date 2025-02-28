from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribe = models.CharField(max_length= 15)
    desktop = models.BooleanField(default= False)
    
    def __str__(self):
        return self.user.username