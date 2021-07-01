from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse

from .models import Employee
from .models import Customer
import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    # This line will get the Customer model from the other app, it can now be used to query the db
    # query customer take to find customer record whose user matches this user
    # if that finds no results, redirect them to finishing register
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        route = request.POST.get('route')
        new_user = Employee(name=name, route=route)
        new_user.save()
        return HttpResponseRedirect(reverse('employees:index'))
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

#     filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are today's date (utilize NOW command)
def lookup(request):
    request.user
    lookup_route = Employee.objects.filter(route)
    lookup_date = request.datetime()

#       filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are specific date (utilize Datefield)
def confirm_pickup(request):
    is_complete = False
    try Customer.address = '':
        is_complete = True
    except Customer.address = None
        is_complete = False
    return render(request, 'employees:confirm_pickup')

#       utilizing boolean phrase is_complete
def charge_pickup(request):
    if request.confirm_pickup == True:
        Customer.balance += 5

#       connected with boolean is_complete = True