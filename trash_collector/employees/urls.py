from django.urls import path
from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.registration, name="registration"),
    path('filter/', views.daily_filter, name="daily"),
    path('lookup/', views.lookup, name="lookup"),
    path('confirm/', views.confirm_pickup, name="confirm"),
    path('charge/', views.charge_pickup, name="charge")
]