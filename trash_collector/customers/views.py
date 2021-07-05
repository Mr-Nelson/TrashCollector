from django.contrib.auth.models import User
from django.db.models.sql import AND
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
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        user_registration = Customer(name=name, user=user,
                            address=address,
                            zip_code=zip_code,
                            weekly_pickup_day=weekly_pickup_day)
        user_registration.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/register.html")
    pass

def account_info(request):
    user = request.user
    account_info_detail = Customer.objects.get(user=user)
    context = {
        'account_info_detail': account_info_detail
    }
    return render(request, 'customers/account_info.html', context)

def create_edit_pickup(request):
    user = request.user
    print(user.id)
    edit_weekly_pickup_day = Customer.objects.get(user=user)
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
    user = request.user
    print(user.id)
    new_onetime_pickup = Customer.objects.get(user=user)
    context = {
            'new_onetime_pickup': new_onetime_pickup
    }
    if request.method == 'POST':
        new_onetime_pickup.onetime_pickup = request.POST.get('onetime_pickup')
        new_onetime_pickup.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/onetime_pickup.html", context)
    #       create format for onetime_pickup object


def pickup_suspension(request):
    user = request.user
    print(user.id)
    new_pickup_suspension = Customer.objects.get(user=user)
    context = {
        'new_pickup_suspension': new_pickup_suspension
    }
    if request.method == 'POST':
        new_pickup_suspension.start_suspension = request.POST.get('start_suspension')
        new_pickup_suspension.end_suspension = request.POST.get('end_suspension')
        new_pickup_suspension.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/pickup_suspension.html", context)

