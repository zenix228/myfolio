from django.db.models import *
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'