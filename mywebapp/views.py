from django.shortcuts import render,redirect,get_object_or_404
from .models import InvoiceStatusTable, POTable,POTable2
from django.db.models import Sum
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .forms import InvoiceStatusTableForm,POTableForm,VendorForm,IssueTicketForm,POTableForm2
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os

# Create your views here.


def home(req):
    invoices=InvoiceStatusTable.objects.all()
    po_records=POTable2.objects.all()
    # print(po_records[0].purchase_order_no)
    # invoices2=InvoiceStatusTable.objects.filter(payment_status='Pending')
    sum_of_pending_amount = InvoiceStatusTable.objects.filter(payment_status='Pending').aggregate(Sum('amount'))['amount__sum']
    count_of_pending_invoices = InvoiceStatusTable.objects.filter(payment_status='Pending').count() or 0
    count_of_records_with_null_invoice = POTable.objects.filter(invoice_no__isnull=True).count()

    if sum_of_pending_amount is None:
        sum_of_pending_amount = 0

    # if req.method == 'POST':
    #     form = InvoiceStatusTableForm(req.POST, req.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(req,('Duplicate Record . Invoice No DN32309172 already exists.  Kindly please check')) ##PO Amount, Invoice Amount Mismatch !!
    #         return redirect('home')  # Redirect to the home page after successful form submission
    # else:
    #     form = InvoiceStatusTableForm()


    return render(req,'index.html',{"invoices":invoices,"po_records":po_records,"sum_of_pending_amount":sum_of_pending_amount,"count_of_pending_invoices":count_of_pending_invoices,"count_of_records_with_null_invoice":count_of_records_with_null_invoice,'request': req})
    # return render(req,'index.html',{})


def invoicedashboard(req):
    return render(req,'invoicedashboard.html',{})



def login_user(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            messages.success(req,('LogIn Successfull'))
            return redirect('home')
        else:
            messages.success(req,('LogIn Failed.. Please check the Credentials...!!'))
            return redirect('login')
    else:
        return render(req,'login.html',{})

def logout_user(req):
    logout(req)
    messages.success(req,('You have been Logged out Successfully'))
    return redirect('login')

def register_user(req):
    form=SignUpForm()
    if req.method=='POST':
        form=SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(req,user)
            messages.success(req,('You have been Registered Successfully'))
            return redirect('home')
        else:
            messages.success(req,('whoops!! Error in registering !!Please try again'))
            return redirect('register')
    else:
        return render(req,'register.html',{'form':form})




# def add_email(req):
#     if req.method == 'POST':
#         form = EmailForm(req.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(req,('Email Record added Successfully'))
#             return redirect('home')  # Change 'home' to the appropriate URL
#         else:
#             messages.success(req,('Please check the details you have entered'))
#     else:
#         form = EmailForm()
#     return render(req, 'add_email.html', {'form': form})



# def add_client(req):
#     args = {}
#     if req.method == 'POST':
#         form = ClientForm(req.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(req,('Client Record added Successfully'))
#             return redirect('home')  # Change 'home' to the appropriate URL
#         else:
#             messages.success(req,('Please check the details you have entered'))
#     else:
#         form = ClientForm()
#     args['form'] = form
#     return render(req, 'add_client.html', {'form': form})



def add_invoice(req):
    args = {}
    if req.method == 'POST':
        form = InvoiceStatusTableForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,('Invoice Record added Successfully'))
            return redirect('home')  # Change 'home' to the appropriate URL
        else:
            messages.success(req,('Please check the details you have entered'))
            # return redirect('add_invoice')
    else:
        form = InvoiceStatusTableForm()
    args['form'] = form
    return render(req, 'add_invoice.html', {'form': form})

def upload_invoice(req):
    args = {}
    if req.method == 'POST':
        form = InvoiceStatusTableForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,('Invoice Record added Successfully'))
            return redirect('home')  # Change 'home' to the appropriate URL
        else:
            messages.success(req,('Please check the details you have entered'))
            # return redirect('add_invoice')
    else:
        form = InvoiceStatusTableForm()
    args['form'] = form
    return render(req, 'upload_invoice.html', {'form': form})

def vendor_master_details(req):
    args = {}
    if req.method == 'POST':
        form = VendorForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req,('vendor Record Updated Successfully'))
            return redirect('home')  # Change 'home' to the appropriate URL
        else:
            messages.success(req,('Vendor Record Updated Successfully'))
            return redirect('home')
            # return redirect('add_invoice')
    else:
        form = VendorForm()
    args['form'] = form
    return render(req, 'vendor_details.html', {'form': form})


def Issue_tickets(req):
    if req.method == 'POST':
        form = IssueTicketForm(req.POST, req.FILES)
        if form.is_valid():
            ticket = form.save()  # Save the form instance
            ticket_id = ticket.ticket_id  # Retrieve the ticket_id
            # Now you can send the ticket_id in a message
            messages.success(req, f'Raised ticket successfully . Please note your ticket no 2393')
            return redirect('issue_tickets')  # Change 'home' to the appropriate URL
        else:
            messages.error(req, 'Raised ticket successfully . Please note your ticket no 2393')
            return redirect('issue_tickets')
    else:
        form = IssueTicketForm()
    return render(req, 'issue_tickets.html', {'form': form})



# def payment_status(request):
#     if request.method == 'POST':
#         invoice_no = request.POST.get('invoice_no')
#         try:
#             invoice = InvoiceStatusTable.objects.get(invoice_no=invoice_no)
#             payment_status = invoice.payment_status
#             return render(request, 'payment_status.html', {'payment_status': payment_status})
#         except InvoiceStatusTable.DoesNotExist:
#             error_message = "Invoice not found"
#             return render(request, 'payment_status.html', {'error_message': error_message})
#     return render(request, 'payment_status.html')

def payment_status(request):
    if request.method == 'POST':
        invoice_no = request.POST.get('invoice_no')
        invoices = InvoiceStatusTable.objects.filter(invoice_no=invoice_no)
        if invoices.exists():
            # If there are multiple entries with the same invoice number,
            # you can choose how to handle them here.
            # For example, you can take the first one or iterate over them.
            payment_status = invoices[0].payment_status
            return render(request, 'payment_status.html', {'payment_status': payment_status})
        else:
            error_message = "Invoice not found"
            return render(request, 'payment_status.html', {'error_message': error_message})
    return render(request, 'payment_status.html')



def update_invoice(request, invoice_id):
    invoice = get_object_or_404(InvoiceStatusTable, id=invoice_id)
    if request.method == 'POST':
        form = InvoiceStatusTableForm(request.POST, request.FILES, instance=invoice)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully.')
            return redirect('home')  # Redirect to a success page or a different URL
    else:
        form = InvoiceStatusTableForm(instance=invoice)
    return render(request, 'update_invoice.html', {'form': form})

def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(InvoiceStatusTable, id=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        messages.success(request,'Record Deleted Successfully.')
        return redirect('home') 
    

def display_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(InvoiceStatusTable, id=invoice_id)
    # Render the PDF using a template or library like ReportLab
    pdf_content = render_to_string('invoice_pdf_template.html', {'invoice': invoice})
    response = FileResponse(pdf_content, as_attachment=True, filename=f'invoice_{invoice.invoice_no}.pdf')
    return response

def preview_pdf(request, invoice_id):
    invoice = get_object_or_404(InvoiceStatusTable, pk=invoice_id)
    pdf_path = os.path.join(settings.MEDIA_ROOT, str(invoice.upload_invoice))
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    # return render(request, 'pdf_preview.html', {'pdf_path': pdf_path})

def preview_pdf2(request, po_id):
    po = get_object_or_404(POTable2, pk=po_id)
    pdf_path = os.path.join(settings.MEDIA_ROOT, str(po.link))
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    # return render(request, 'pdf_preview.html', {'pdf_path': pdf_path})


def add_PO2(req):
    args = {}
    if req.method == 'POST':
        form = POTableForm2(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            # messages.success(req,('Invoice Record added Successfully'))
            print('PO Record added Successfully')
            return redirect('home')  # Change 'home' to the appropriate URL
        else:
            print('Please check the details you have entered')
            # pass
            # messages.success(req,('Please check the details you have entered'))
            # return redirect('add_invoice')
    else:
        form = POTableForm2()
    args['form'] = form
    return render(req, 'add_PO2.html', {'form': form})