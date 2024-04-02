from django.contrib import admin
from .models import InvoiceStatusTable, POTable
# Register your models here.


admin.site.register(InvoiceStatusTable)
admin.site.register(POTable)