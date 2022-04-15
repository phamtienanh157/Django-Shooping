from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderView),
    path('create-stores', views.createStores),
    path('delete-stores', views.deleteStores),
    path('update-stores', views.updateStores),
]
