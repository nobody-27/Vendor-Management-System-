from django.contrib import admin
from .models import Vendor,PurchaseOrder
# Register your models here.

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'address','on_time_delivery_rate','vendor_code')
    readonly_fields = ('vendor_code','on_time_delivery_rate')


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number','vendor','order_date','delivery_date','items','quantity')
    readonly_fields = ('po_number',)
