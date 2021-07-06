from datetime import date, datetime
import calendar
from django.apps import apps
from django.db.models.functions import ExtractWeekDay
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
# def customer_list(request):
#     table = CustomerTable(Customer.objects.all())
#     return render(request, 'employees/index.html', {'table': table})


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    # query customer take to find customer record whose user matches this user
    # if that finds no results, redirect them to finishing register
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'employees/index.html', context)

def registration(request):
    request.user
    try:
        new_employee = Employee.objects.get(user_id=User.id)
        context = {
            'new_employee' : new_employee
        }
        print("Employee.name has already been registered.")
        return render(request, 'employee/index.html', context)
    except:
        if request.method == 'POST':
            name = request.POST.get('name')
            route = request.POST.get('route')
            user = request.user
            new_employee = Employee(name=name, route=route, user=user)
            new_employee.save()
            return HttpResponseRedirect(reverse('employees:index'))
        else:
            return render(request, 'employees/register.html')

def daily_filter(request, does_pickup=None):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.filter(zip_code=employee.route)
    my_date = date.today()
    does_pickup = False
    create_route = [does_pickup == True]
    for Customer in customers:
        if ExtractWeekDay(Customer.weekly_pickup_day) == calendar.day_name[my_date.weekday()] or ExtractWeekDay(Customer.onetime_pickup) == calendar.day_name[my_date.weekday()]:
            does_pickup = True
        else:
            does_pickup = False
    suspended_accounts = Customer.objects.filter(datetime.date.today > Customer.start_suspension) and Customer.objects.filter(datetime.date.today < Customer.end_suspension)
    create_route.remove(suspended_accounts)
    context = {
        'create_route': create_route
    }
    return render(request, 'employees/Daily Route.html', context)

def lookup(request, does_pickup=None):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.filter(zip_code=employee.route)
    does_pick = False
    create_route = [does_pickup == True]
    for Customer in customers:
        if ExtractWeekDay(Customer.weekly_pickup_day) == datetime.date.today() or ExtractWeekDay(
                Customer.onetime_pickup) == datetime.date.today():
            does_pickup = True
        else:
            does_pickup = False
    # suspended_accounts = Customer.objects.filter(
    #         datetime.date.weekday(now) > Customer.start_suspension and Customer.objects.filter(
    #             datetime.date.weekday(now) < Customer.end_suspension)
    # create_route.remove(suspended_accounts)
    context = {
        'create_route': create_route
    }
    return render(request, 'employees/Daily Route.html', context)

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
