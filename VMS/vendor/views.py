from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class VendorProfileView(APIView):
    
    def get(self,request,vendor=None):
        return Response({"vendor_id":"ALL" if vendor == None else vendor})
    
    def post(self,request):
        pass

    def put(self,request,vendor):
        return

    def delete(self,request,vendor):
        pass


class PurchaseOrderView(APIView):
    
    def get(self,request,po_id=None):
        return Response({})
    
    def post(self,request):
        return Response({})
    
    def put(self,request,po_id):
        return Response({})

    def delete(self,request,po_id):
        return Response({})
