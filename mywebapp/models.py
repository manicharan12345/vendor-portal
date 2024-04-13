from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class InvoiceStatusTable(models.Model):
    invoice_no = models.CharField('Invoice No',max_length=100)
    po_no = models.CharField('PO No',max_length=100,blank=True, null=True)
    invoice_date = models.DateField('Invoice Date',blank=True, null=True)
    invoice_due_date = models.DateField('Invoice  due Date',blank=True, null=True)
    amount=models.DecimalField(default=0,max_digits=20,decimal_places=2,blank=True, null=True)
    payment_status = models.CharField(default='Pending',max_length=50,blank=True, null=True)
    payment_date = models.DateField('Payment Date',blank=True, null=True)
    upload_invoice = models.FileField(upload_to='invoice_copies/', blank=True, null=True,)

    def __str__(self):
        return f"{self.invoice_no}"


class VendorMasterTable(models.Model):
    vendor_id = models.CharField('Vendor ID', max_length=100)
    Vendor_Name = models.CharField('Name', max_length=100)
    Vendor_Address = models.CharField('Address', max_length=255, blank=True, null=True)
    Contact_no = models.CharField('Contact Person', max_length=20, blank=True, null=True)
    gst_details = models.CharField('GST Details', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.vendor_id} - {self.Vendor_Name}"



class IssueTicket(models.Model):
    ticket_id = models.CharField('Ticket ID', max_length=100, primary_key=True)
    date = models.DateField('Date')
    vendor_id = models.CharField('Vendor ID', max_length=100,blank=True, null=True)
    ticket_category = models.CharField('Ticket Category', max_length=100)
    description = models.TextField('Description')
    severity = models.CharField('Severity', max_length=50)

    def __str__(self):
        return f"{self.ticket_id} - {self.vendor_id}"


class POTable(models.Model):
    purchase_order_no = models.CharField('Purchase order no',max_length=100)
    purchase_order_date = models.DateField('Purchase order date')
    vendor_name = models.CharField('Vendor Name',max_length=100)
    po_amount=models.DecimalField(default=0,max_digits=20,decimal_places=2)
    grn_no = models.CharField('GRN No',max_length=100)
    invoice_no = models.CharField('Invoice No',max_length=100,blank=True, null=True)
    invoice_date = models.DateField('Invoice Date',blank=True, null=True)
    link = models.FileField(upload_to='invoice_copies/', blank=True, null=True,)

    def __str__(self):
        return f"{self.purchase_order_no}"

class POTable2(models.Model):
    purchase_order_no = models.CharField('Purchase order no',max_length=100)
    purchase_order_date = models.DateField('Purchase order date')
    po_amount=models.DecimalField(default=0,max_digits=20,decimal_places=2)
    link = models.FileField(upload_to='invoice_copies/', blank=True, null=True,)

    def __str__(self):
        return f"{self.purchase_order_no}"
