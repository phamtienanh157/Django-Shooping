from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookItem
# Create your views here.


def renderHome(request):
    return render(request, 'pages/home.html')
