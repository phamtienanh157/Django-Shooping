from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Store
# Create your views here.


def renderView(request):
    return render(request, 'pages/home.html')

def createStores(request):
    # Create model
    store_corporate = Store(name='Corporate', address='624 Broadway', city='San Diego', state='CA',
                            email='corporate@coffeehouse.com')
    store_downtown = Store(name='Downtown', address='Horton Plaza', city='San Diego', state='CA',
                           email='downtown@coffeehouse.com')
    store_uptown = Store(name='Uptown', address='240 University Ave',
                         city='San Diego', state='CA', email='uptown@coffeehouse.com')
    store_midtown = Store(name='Midtown', address='784 W Washington St', city='San Diego',
                          state='CA', email='midtown@coffeehouse.com')

    # Create store list
    store_list = [store_corporate, store_downtown, store_uptown, store_midtown]

    # Call bulk_create to create records in a single call
    Store.objects.bulk_create(store_list)

    return render(request, 'pages/home.html')

def readStores(request):
    # Query with all() method or equivalent SQL: 'SELECT * FROM ...'
    all_stores = Store.objects.all()

    # Query with include() method or equivalent SQL: 'SELECT....WHERE city = "San Diego"'
    san_diego_stores = Store.objects.filter(city='San Diego')

    # Query with exclude() method or equivalent SQL: 'SELECT....WHERE NOT (city = "San Diego")'
    non_san_diego_stores = Store.objects.exclude(city='San Diego')

    # Query with include() and exclude() methods or equivalent SQL: 'SELECT....WHERE STATE = 'CA' AND NOT(city="San Diego")'
    ca_stores_without_san_diego = Store.objects.filter(
        state='CA').exclude(city='San Diego')

    return render(request, 'pages/home.html')

def readPerformance(request):
    store_items = Store.objects.filter(city='San Diego').only('name')
    store_items.query.get_loaded_field_names()

    # All Store records with no city
    store_items = Store.objects.defer('city').all()
    store_items.query.get_loaded_field_names()

    # Item names on the breakfast menu
    store_items = Store.objects.filter(city='San Diego').values('name')
    # Outputs: <QuerySet [{'name': 'Oatmeal'}, {'name': 'Oman'}]>

    # All Store records with no email
    all_stores = Store.objects.values_list('email','name','city').all()
    # Outputs: <QuerySet [('corporate@coffeehouse.com', 'Corporate', 'San Diego'),
    # ('downtown@coffeehouse.com', 'Downtown', 'San Diego'), ('uptown@coffeehouse.com',
    # 'Uptown', 'San Diego'), ('midtown@coffeehouse.com', 'Midtown', 'San Diego')]>
    return render(request, 'pages/home.html')

def updateStores(request):
    Store.objects.all().update(email="contact@coffeehouse.com")

    # select_for_update
    store_list = Store.objects.select_for_update().exclude(state='CA')

    # Loop over each store and invoke save() on each entry
    for store in store_list:
        # Add complex update logic here for each store
        # save() method called on each member to update
        store.save()
    return render(request, 'pages/home.html')


def deleteStores(request):
    Store.objects.filter(city='San Diego').delete()

    return render(request, 'pages/home.html')


