from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from .models import Customer
import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    # query customer take to find customer record whose user matches this user
    # if that finds no results, redirect them to finishing register
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
def daily_filter(request):
    request.user
    specific_route = Employee.objects.filter(route) == Customer.objects.filter(zipcode)
    suspended_accounts = Customer.user
    does_pickup = False
        if Customer.weekly_pickup_day == datetime.datetime.now() or Customer.onetime_pickup == datetime.datetime.now()
            return True
        else:
            return False
    context = {
        'specific_route' = specific_route, 'suspended_accounts' = suspended_accounts, 'does_pickup' = does_pickup
    }
    return render(request, 'employees/daily.html', context)
    pass
#     filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are today's date (utilize NOW command)
def lookup(request):
    request.user
    lookup_route = Employee.objects.filter(route)
    lookup_date = request.datetime()
    pass
#       filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are specific date (utilize Datefield)
def confirm_pickup(request):
    pass
#       utilizing boolean phrase is_complete
def charge_pickup(request):
    pass
#       connected with boolean is_complete = True