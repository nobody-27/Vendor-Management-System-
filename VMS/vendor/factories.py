from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence,PostGenerationMethodCall,sequence,SubFactory
import itertools


class VendorFactory(DjangoModelFactory):
    name = Faker('name')
    address = Faker('address')
    contact_details = Faker('msisdn')

    class Meta:
        model = 'vendor.Vendor'

def home():
    data = {
        'item_name':lambda a: a + "sam"


    }

from datetime import datetime,timedelta
    
    
class PurchaseOrder(DjangoModelFactory):
    
    vendor = SubFactory(VendorFactory)
    order_date = Faker('date_between_dates')
    delivery_date = Faker(f'date_between_dates(date_start={datetime.utcnow()},date_end={datetime.utcnow() + timedelta(days=13)})')
    quantity = Faker('msisdn')

    class Meta:
        model = 'vendor.PurchaseOrder'
