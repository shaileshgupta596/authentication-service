from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.dispatch import receiver

from authapi.choices import UserTypeChoices

class User(AbstractUser):  

    user_type = models.CharField(max_length=20, choices=UserTypeChoices.choices, default=UserTypeChoices.USER)

    def __str__(self):
        return self.username
