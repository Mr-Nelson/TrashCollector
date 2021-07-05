from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
from django.contrib.auth.models import AbstractUser
from accounts.models import User
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    try:
        customer = Customer.objects.get(pk=user.id)
        context = {
            'customer': customer
        }
        return render(request, 'customer/index.html', context)
    except:
        return HttpResponseRedirect(reverse('customers:registration'))
    # is_customer = user.groups.filter(name="Customers").exists
    # if is_customer:
    #     return render(request, "accounts/register.html")
    # else:

    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    # print(user)
    # return render(request, 'customers/index.html')

    # # query customer take to find customer record whose user matches this user
    # # if that finds no results, redirect them to finishing register
    # # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # # This will allow you to later query the database using the logged-in user,
    # # thereby finding the customer/employee profile that matches with the logged-in user.
    # # print(user)


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        user_registration = Customer(name=name,
                            address=address,
                            zip_code=zip_code,
                            weekly_pickup_day=weekly_pickup_day)
        user_registration.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/register.html")
    pass

def monthly_statement(request):
    pass
#       utilize boolean statement from employees.views.charge_pickup function
def create_edit_pickup(request, customer):
    # if request.method == 'POST':
        # if Customer.weekly_pickup_day == None:
        #     weekly_pickup_day = request.POST.get('name')
        #     new_weekly_pickup_day = Customer(weekly_pickup_day=weekly_pickup_day)
        #     new_weekly_pickup_day.save()
        #     return HttpResponseRedirect(reverse('customers:index'))
        # else:
    edit_weekly_pickup_day =User.objects.get(pk=customer)
    context = {
            'edit_weekly_pickup_day': edit_weekly_pickup_day
    }
    if request.method == 'POST':
        edit_weekly_pickup_day.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        edit_weekly_pickup_day.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/edit_weekly_pickup.html", context)
    # else:
    #     return render(request, "customers/edit_weekly_pickup.html")
    #     create/edit format from previous project (possibly two functions)


def onetime_pickup(request):
    if request.method == 'POST':
        onetime_pickup = request.POST.get('onetime_pickup')
        new_onetime_pickup = Customer(onetime_pickup=onetime_pickup)
        new_onetime_pickup.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/onetime_pickup.html")
        pass
    #       create format for onetime_pickup object
def pickup_suspension(request):
    if start_suspension == True:
        pass
#       if statement involving boolean user input