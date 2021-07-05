from django.urls import path
from django.views.generic import RedirectView

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registration, name="registration"),
    path('edit_weekly_pickup_day/', views.create_edit_pickup, name="edit_weekly_pickup_day"),
    path('onetime_pickup/', views.onetime_pickup, name="onetime_pickup"),
    path('pickup_suspension/', views.pickup_suspension, name="pickup_suspension")
]
