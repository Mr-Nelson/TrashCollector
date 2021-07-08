from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
import customers.models


class User(AbstractUser):
    """Our custom user model that adds a new field to the default django user model"""
    is_employee = models.BooleanField(default=False)

    def __repr__(self):
        return self.username, self.pk, self.objects,

    def __str__(self):
        return self.username, self.pk, self.objects,

    def __int__(self):
        return self.username, self.pk, self.objects,

