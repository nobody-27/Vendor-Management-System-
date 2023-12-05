from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence,PostGenerationMethodCall,sequence


class VendorFactory(DjangoModelFactory):
    name = Faker('name')
    address = Faker('address')
    contact_details = Faker('msisdn')

    class Meta:
        model = 'vendor.Vendor'