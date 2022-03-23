from statistics import mode
from unicodedata import category, name
from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    pages = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class BookItem(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    image = models.URLField(default='')
