from django.db import models
import random
import string
import time
import uuid
# Create your models here.

def generate_vendor_code():
    timestamp = str(int(time.time()))
    random_chars  = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase,k=6))
    if Vendor.objects.filter(vendor_code=timestamp+random_chars).exists():
        return generate_vendor_code
    return timestamp+random_chars

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=200,default=generate_vendor_code,unique=True)
    on_time_delivery_rate = models.FloatField(default=float(0.0))
    quality_rating_avg = models.FloatField(default=float(0.0))
    average_response_time = models.FloatField(default=float(0.0))
    fulfillment_rate = models.FloatField(default=float(0.0))

    def __str__(self) -> str:
        return self.name

STATUS = ( 
    ("PENDING,", "pending"),
    ("COMPLETED,", "completed"),
    ("CANCELED","canceled")
) 

def generate_purchaser_code():
    code = uuid.uuid1().hex[0:]
    if PurchaseOrder.objects.filter(po_number=code).exists():
        return generate_purchaser_code
    return code

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100,default=generate_purchaser_code,unique=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(help_text="order placed")
    delivery_date = models.DateTimeField()
    items = models.JSONField(null=True)
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS,max_length=50,default=STATUS[0][0])
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.order_date)
    

class HistoryPerformance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return self.vendor.name