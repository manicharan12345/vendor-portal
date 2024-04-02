from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    # path('add_email/', views.add_email, name='add_email'),
    # path('add_client/', views.add_client, name='add_client'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('upload_invoice/', views.upload_invoice, name='upload_invoice'),
    path('add_vendor_details/', views.vendor_master_details, name='add_vendor_details'),
    path('issue_tickets/', views.Issue_tickets, name='issue_tickets'),
    path('payment_status/', views.payment_status, name='payment_status'),
    path('update_invoice/<str:invoice_id>/',views.update_invoice, name='update_invoice'),
    path('delete_invoice/<int:invoice_id>/', views.delete_invoice, name='delete_invoice'),
    path('invoicedashboard/', views.invoicedashboard, name='invoicedashboard'),
]
