from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(unique=True,default=uuid.uuid4,editable=False,primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13,unique=True)
    balance = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'