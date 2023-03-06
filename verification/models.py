from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=200, null=True, blank=True)
    phone_number=models.CharField(max_length=15)
    otp=models.CharField(max_length=100, null=True, blank=True)
    uid=models.CharField(default=f'{uuid.uuid4}', max_length=200)

    def __str__(self):
        return self.username