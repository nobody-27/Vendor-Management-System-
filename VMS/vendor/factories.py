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


@Faker.override_default_locale('en_US')
class PurchaseOrder(DjangoModelFactory):
    vendor = SubFactory(VendorFactory)
    order_date = Faker('date_between_dates')
    delivery_date = Faker('date_between_dates')
    quantity = Faker('msisdn')
    # item = Faker()

    class Meta:
        model = 'vendor.PurchaseOrder'
