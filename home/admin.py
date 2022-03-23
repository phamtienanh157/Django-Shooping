from atexit import register
from django.contrib import admin
from .models import Book, Author, Publisher, Category, BookItem
# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'price']
# admin.site.register(Book, BookAdmin)

myModels = [Book, Author, Publisher, Category, BookItem]
admin.site.register(myModels)
