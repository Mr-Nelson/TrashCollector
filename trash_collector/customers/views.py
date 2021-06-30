from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # query cutsomer take to find custeomr reccord whose user matches this user
    # if that finds no results, redirect them to finsihin register
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')

def registration(request):
    pass
#       input types name, address, zipcode
def monthly_statement(request):
    pass
#       utilize boolean statement from employees.views.charge_pickup function
def create_edit_pickup(request):
    pass
#     create/edit format from previous project (possibly two functions)
def onetime_pickup(request):
    pass
#       create format for onetime_pickup object
def pickup_suspension(request):
    pass
#       if statement involving boolean user input