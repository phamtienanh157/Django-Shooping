from atexit import register
from django.contrib import admin
from .models import Store
# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'email']
admin.site.register(Store, StoreAdmin)

