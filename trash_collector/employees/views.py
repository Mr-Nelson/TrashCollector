from datetime import date, datetime
import calendar
from django.apps import apps
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

import customers.models
from customers.models import Customer

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
        new_employee = Employee.objects.get(user_id=user.id)
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
    now_calendar = date.today()
    create_route = []
    now_weekday = calendar.day_name[my_date.weekday()]
    int_weekday = date.today().weekday()
    for cust in customers:
        start_date = cust.start_suspension
        end_date = cust.end_suspension
        customer_weekday = cust.weekly_pickup_day
        if now_calendar.__lt__(start_date) and now_calendar.__gt__(end_date):
            if cust.onetime_pickup is not None:
                customer_onetime = datetime.weekday(cust.onetime_pickup)
            else:
                customer_onetime = None
            if customer_weekday == now_weekday or customer_onetime == int_weekday:
                create_route.append(cust)
    context = {
        'create_route': create_route
    }
    return render(request, 'employees/Daily Route.html', context)


def lookup(request, does_pickup=None):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.filter(zip_code=employee.route)
    create_route = []
    context = {
        'create_route': create_route
    }
    if request.method == 'POST':
        my_date = request.POST.get('select date')
        # now_calendar = my_date
        # now_weekday = calendar.weekday(datetime.now())
        # int_weekday = my_date.weekday(my_date)
        for cust in customers:
            if cust.weekly_pickup_day == my_date:
                create_route.append(cust)
        # if my_date is not None:
        #     datetimeobj = datetime.strptime(my_date, "%Y-%m-%d")
        #     now_calendar = datetimeobj.date()
        #     int_weekday = datetimeobj.weekday()
        #     now_weekday = calendar.day_name[int_weekday]
        #     for cust in customers:
        #         start_date = cust.start_suspension
        #         end_date = cust.end_suspension
        #         customer_weekday = cust.weekly_pickup_day
        #         if now_calendar.__lt__(start_date) and now_calendar.__gt__(end_date):
        #             if cust.onetime_pickup is not None:
        #                 customer_onetime = datetime.weekday(cust.onetime_pickup)
        #             else:
        #                 customer_onetime = None
        #             if customer_weekday == now_weekday or customer_onetime == int_weekday:
        #                 create_route.append(cust)
        return render(request, 'employees/Daily Route.html', context)
    else:
        return render(request, 'employees/Route Lookup.html', context)


def confirm_pickup(request, user_id):
    charge_customer = Customer.objects.get(pk=user_id)
    context = {
        'charge_customer': charge_customer
    }
    if request.method == 'POST':
        charge_customer.balance += 10
        charge_customer.save()
        return HttpResponseRedirect(reverse('employees:daily'))
    else:
        return render(request, "employees/pickup_confirmation.html", context)
    #       create format for onetime_pickup object
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

def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    trash_collector = apps.get_model('trash_collector.trash_collector')
    api_key = trash_collector.GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return lat, lng