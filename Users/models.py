from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# Create your models here.

class User(AbstractUser):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Exp = models.CharField(max_length=10, default='0')
    groups = models.ForeignKey(Group, on_delete='Cascade', null=True)
    user_permissions = models.ForeignKey(Permission, on_delete='Cascade', null=True)

    class Meta:
        db_table = "users"

