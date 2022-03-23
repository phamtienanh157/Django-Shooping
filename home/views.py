from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookItem
# Create your views here.


def getListBooks(request):
    data = {'Books': BookItem.objects.all()}
    return render(request, 'pages/home.html', data)


def getBookById(request, id):
    book = BookItem.objects.get(id=id)
    data = {'bookItem': book}
    return render(request, 'pages/itemDetails.html', data)
