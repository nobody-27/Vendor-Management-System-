from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class VenderProfile(APIView):
    
    def get(self,request):
        """
        List all vendors.
        """
        # GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
        return
    
    def post(self,request):
        """
        : Create a new vendor..
        """
        pass

    def put(self,request):
        return

    def delete(self,request):
        pass


class Purchase(APIView):
    
