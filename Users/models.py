from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

# Create your models here.

class Users(AbstractUser):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Exp = models.CharField(max_length=10, default='0')

    class Meta:
        db_table = "users"
