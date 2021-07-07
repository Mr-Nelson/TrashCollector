from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

class EmployeeAdmin(UserAdmin):
    """Overrides default Admin model to allow for custom user creation in Admin interface"""
    pass


# Registering our custom user in the admin interface
admin.site.register(User, UserAdmin)
