from statistics import mode
from unicodedata import category, name
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    pages = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class BookItem(models.Model):
    book = models.OneToOneField(
        Book, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    image = models.URLField(default='')

    def __str__(self):
        return f"{self.book.title}"
