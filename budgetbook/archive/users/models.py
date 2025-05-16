from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class UserList(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name