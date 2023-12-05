from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/',views.VendorProfileView.as_view(),name="vendor_create"),
    path('vendors/<int:vendor>/',views.VendorProfileView.as_view(),name="vendor_get"),
    
    path('purchase_orders/',views.PurchaseOrderView.as_view(),name="purchase_order"),
    path('purchase_orders/<int:po_id>/',views.PurchaseOrderView.as_view(),name="purchase_orders")

    


]

