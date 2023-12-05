from typing import Any
from django.core.management.base import BaseCommand
from ...factories import VendorFactory,PurchaseOrder


class Command(BaseCommand):
    help = 'Generate fake data and seed to models with them, default ara 100'

    def add_arguments(self, parser) -> None:
        parser.add_argument('--amount',type=int,help="The amount of fake data you want")


    def __generate_vendor(self,amount:int):
        for _ in range(amount):
            VendorFactory()
            PurchaseOrder()
    
    
    def handle(self, *args, **option) -> str | None:
        amount = option.get('amount',10)
        self.__generate_vendor(10)
