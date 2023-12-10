from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from vendor.models import Vendor
from rest_framework import status
from .serializers import (
    Vendorserializer,
    PurchaseOrderSerializer
)
# Create your views here.

class VendorProfileView(APIView):
    serializer_class = Vendorserializer

    def get_object(self,code):
        return Vendor.objects.filter(vendor_code=code).first()

    def get(self,request,vendor_code:str = None):
        if vendor_code != None:

            if self.get_object(vendor_code):

                return Response({"message":self.serializer_class(self.get_object(vendor_code)).data},status=status.HTTP_200_OK)
            
            return Response({"message":"Record Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        return Response({"data":self.serializer_class(Vendor.objects.all(),many=True).data},status=status.HTTP_200_OK)
    
    def post(self,request):
        validate = Vendorserializer(data=request.data)
        if validate.is_valid():
            name = validate.validated_data.get('name')
            contact_details = validate.validated_data.get('contact_details')
            address = validate.validated_data.get('address')

            Vendor.objects.create(
                name = name,
                contact_details = contact_details,
                address = address
            )
            return Response({"message":"vendors saved succesfully"})

        return Response({"message":validate.errors},status=status.HTTP_200_OK)


    def put(self,request,vendor_code:str):
        if self.get_object(vendor_code):

            return
        
        

        return Response({"message":"done"},status=status.HTTP_202_ACCEPTED)
    

    def delete(self,request,vendor_code:str):
        return Response({"message":"vendor deleted successfully"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class PurchaseOrderView(APIView):
    serializer_class = PurchaseOrderSerializer

    
    def get(self,request,purchase_orders=None):

        return Response({'message':"ALL"})
    

    def post(self,request):
        return Response({},status=status.HTTP_200_OK)
    
    def put(self,request,po_id):
        return Response({})

    def delete(self,request,po_id):
        return Response({})





import random
from faker import Faker
from django.utils import timezone

fake = Faker()

# @csrf_exempt
# @api_view(['POST'])
def data_entry(request):
    try:
        for _ in range(10):
            Vendor.objects.create(
                name=fake.company(),
                contact_details=fake.address(),
                address=fake.address(),
                vendor_code=str(fake.uuid4())[:8].upper(),
                on_time_delivery_rate=random.uniform(0.7, 0.95),
                quality_rating_avg=random.uniform(3.5, 4.8),
                average_response_time=random.uniform(2.0, 4.0),
                fulfillment_rate=random.uniform(0.8, 0.95),
            )

        # Create Purchase Orders
        vendors = Vendor.objects.all()
        for _ in range(20):
            vendor = random.choice(vendors)
            status = random.choice(["PENDING", "COMPLETED", "CANCELED"])
            
            PurchaseOrder.objects.create(
                po_number=str(fake.uuid4())[:8].upper(),
                vendor=vendor,
                order_date=fake.date_time_between(start_date='-30d', end_date='now'),
                delivery_date=fake.date_time_between(start_date='now', end_date='+30d'),
                items={'item1': random.randint(5, 20), 'item2': random.randint(10, 30)},
                quantity=random.randint(5, 50),
                status=status,
                quality_rating=random.uniform(3.0, 5.0) if status == "COMPLETED" else None,
                acknowledgment_date=timezone.now() if status == "COMPLETED" else None,
            )

        # Create Historical Performance records
        for vendor in vendors:
            HistoryPerformance.objects.create(
                vendor=vendor,
                date=fake.date_time_between(start_date='-30d', end_date='now'),
                on_time_delivery_rate=random.uniform(0.7, 0.95),
                quality_rating_avg=random.uniform(3.5, 4.8),
                average_response_time=random.uniform(2.0, 4.0),
                fulfillment_rate=random.uniform(0.8, 0.95),
            )

    except Exception as e:
        return Response({'success': False, 'message': str(e)})

    return Response({'success': True, 'message': 'Data entry successful'})