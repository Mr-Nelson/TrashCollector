from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
def daily_filter(request):
    pass
#     filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are todays date (utilize NOW command)
def lookup(request):
    pass
#       filter customers in zip_code:route, non-suspended account, pickup day & onetime pickup are specific date (utilize Datefield)
def confirm_pickup(request):
    pass
#       utilizing boolean phrase is_complete
def charge_pickup(request):
    pass
#       connected with boolean is_complete = True