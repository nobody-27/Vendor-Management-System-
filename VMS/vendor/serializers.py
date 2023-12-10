from rest_framework import serializers
from .models import Vendor,PurchaseOrder

class Vendorserializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name','contact_details','address',)
    
    def to_representation(self, obj):
        data = super(Vendorserializer, self).to_representation(obj)
        data['vendor_code'] = obj.vendor_code
        data['on_time_delivery_rate'] = obj.on_time_delivery_rate
        return data
        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            'vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date'
        
        )


