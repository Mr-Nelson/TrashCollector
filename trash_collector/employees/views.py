from django.db.models.sql import AND
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse

from .models import Employee
import datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    # query customer take to find customer record whose user matches this user
    # if that finds no results, redirect them to finishing register
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

def registration(request):
    new_employee = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        route = request.POST.get('route')
        new_employee = Employee(name=name, route=route)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/register.html')
def daily_filter(request):
<<<<<<< HEAD
    request.user

=======
    # request.user
>>>>>>> b8bc34b88a1b35f6217ac408f7ddd0080528464f
    # create_route = Employee.objects.filter(route=request) == Customer.objects.filter(zip_code=request)
    # suspended_accounts = Customer.objects.exclude(datetime.datetime.now() > Customer.start_suspension) AND Customer.objects.exclude(datetime.datetime.now() < Customer.end_suspension)
    # does_pickup = False
<<<<<<< HEAD

    # create_route = Employee.objects.filter(route=request) == Customer.objects.filter(zip_code=request)
    # suspended_accounts = Customer.objects.exclude(datetime.datetime.now() > Customer.start_suspension) AND Customer.objects.exclude(datetime.datetime.now() < Customer.end_suspension)
    # does_pickup = False
    pass

    if Customer.weekly_pickup_day == datetime.datetime.now or Customer.onetime_pickup == datetime.datetime.now:
        return True
    else:
        return False
=======
    # if Customer.weekly_pickup_day == datetime.datetime.now or Customer.onetime_pickup == datetime.datetime.now:
    #     return True
    # else:
    #     return False
>>>>>>> b8bc34b88a1b35f6217ac408f7ddd0080528464f
    # context = {
    #     'create_route' : create_route, 'suspended_accounts' : suspended_accounts, 'does_pickup' : does_pickup
    # }
    # create_route = Employee.objects.filter(route=request) == Customer.objects.filter(zip_code=request)
    # suspended_accounts = Customer.objects.exclude(datetime.datetime.now() > Customer.start_suspension) AND Customer.objects.exclude(datetime.datetime.now() < Customer.end_suspension)
    # does_pickup = False
    # if Customer.weekly_pickup_day == datetime.datetime.now or Customer.onetime_pickup == datetime.datetime.now:
    #     return True
    # else:
    #     return False
    # context = {
    #     'create_route' : create_route, 'suspended_accounts' : suspended_accounts, 'does_pickup' : does_pickup
    # }
    # return render(request, 'employees/daily.html', context)
    pass
#     filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are today's date (utilize NOW command)
def lookup(request):
    # request.user
    # lookup_route = Employee.objects.filter(route)
    # lookup_date = request.datetime()
    pass
#       filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are specific date (utilize Datefield)
def confirm_pickup(request):
    # is_complete = False
    # try Customer.zip_code == .route:
    #     is_complete = True
    # except Customer.zip_code += .route:
    #     is_complete = False
    # return render(request, 'employees:confirm_pickup')
    pass
#       utilizing boolean phrase is_complete
def charge_pickup(request):
    # if request.confirm_pickup == True:
    #     Customer.balance += 5
    pass
#       connected with boolean is_complete = True
