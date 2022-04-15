from statistics import mode
from unicodedata import category, name
from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

