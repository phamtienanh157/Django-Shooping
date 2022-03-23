from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Store
# Create your views here.


def getListBooks(request):
    data = {'Books': Book.objects.all()}
    return render(request, 'pages/home.html', data)


def getBookById(request, id):
    book = Book.objects.get(id=id)
    data = {'book': book}
    return render(request, 'pages/itemDetails.html', data)
