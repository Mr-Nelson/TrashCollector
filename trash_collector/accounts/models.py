from django.db import models
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
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

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)