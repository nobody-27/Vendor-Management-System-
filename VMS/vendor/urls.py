from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/',views.VendorProfileView.as_view(),name="vendor_create"),
    path('vendors/<str:vendor_code>/',views.VendorProfileView.as_view(),name="vendor_get"),
    
    path('purchase_orders/',views.PurchaseOrderView.as_view(),name="purchase_orders"),
    path('purchase_orders/<str:po_number>/',views.PurchaseOrderView.as_view(),name="purchase_orders")

    


]

