from django.urls import path
from . import views

urlpatterns = [
    path('', views.getListBooks),
    path('<int:id>', views.getBookById)
]
