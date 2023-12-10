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
