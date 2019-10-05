from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True, max_length=40, blank=False, null=True)

    def __str__(self):
        return self.username

