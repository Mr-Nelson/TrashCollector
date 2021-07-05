import django_tables2 as tables
from trash_collector.customers import apps
from trash_collector.customers.models import Customer


class CustomerTable(tables.Table):
    Customer = apps.get_model('customers.Customer')
    class Meta:
        model =Customer
        sequence = ('name', 'address', 'zip_code', 'balance')
        exclude = (
        'customer_id', 'user_id', 'weekly_pickup_day', 'onetime_pickup', 'start_suspension', 'end_suspension')

class RouteTable(tables.Table):
    Customer = apps.get_model('customers.Customer')
    class Meta:
        model = Customer
        sequence = ('name', 'address', 'zip_code')
        exclude = ('customer_id', 'user_id', 'weekly_pickup_day', 'onetime_pickup', 'start_suspension', 'end_suspension', 'balance')