from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm
from django import forms
from .models import InvoiceStatusTable, POTable,VendorMasterTable,IssueTicket,POTable2



class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):

        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer.letters,digits and @/./+/_ only .</small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted"><li>Your password can\'t be too similar to your other personal information</li><li>Your password must contain atleast 8 characters</li><li>Your password can\'t be too commonly used password</li><li>Your password can\'t be entirly numeric</li></ul>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Passsword'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before ,for verification</small></span>'





class InvoiceStatusTableForm(forms.ModelForm):
    class Meta:
        model = InvoiceStatusTable
        fields = ['invoice_no', 'po_no','invoice_date', 'invoice_due_date','amount', 'payment_status', 'payment_date','upload_invoice']
        widgets = {
            'invoice_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice No'}),
            'po_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PO No'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'invoice_due_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment Status'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'upload_invoice': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class VendorForm(forms.ModelForm):
    class Meta:
        model = VendorMasterTable
        fields = ['vendor_id', 'Vendor_Name', 'Vendor_Address', 'Contact_no', 'gst_details']
        labels = {
            'vendor_id': 'Vendor ID',
            'Vendor_Name': 'Name',
            'Vendor_Address': 'Address',
            'Contact_no': 'Contact Person',
            'gst_details': 'GST Details',
        }
        widgets = {
            'vendor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
            'Vendor_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'Vendor_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Address'}),
            'Contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Person'}),
            'gst_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GST Details'}),
        }

class IssueTicketForm(forms.ModelForm):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    severity = forms.ChoiceField(choices=SEVERITY_CHOICES, label='Severity')

    class Meta:
        model = IssueTicket
        fields = ['ticket_id', 'date', 'vendor_id', 'ticket_category', 'description', 'severity']
        labels = {
            'ticket_id': 'Ticket ID',
            'date': 'Date',
            'vendor_id': 'Vendor ID',
            'ticket_category': 'Ticket Category',
            'description': 'Description',
        }
        widgets = {
            'ticket_id': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'vendor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'ticket_category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class POTableForm(forms.ModelForm):
    class Meta:
        model = POTable
        fields = ['purchase_order_no', 'purchase_order_date', 'vendor_name', 'po_amount', 'grn_no', 'invoice_no', 'invoice_date', 'link']
        widgets = {
            'purchase_order_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purchase Order No'}),
            'purchase_order_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'po_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'grn_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GRN No'}),
            'invoice_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice No'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'link': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class POTableForm2(forms.ModelForm):
    class Meta:
        model = POTable2
        fields = ['purchase_order_no', 'purchase_order_date','po_amount', 'link']
        widgets = {
            'purchase_order_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purchase Order No'}),
            'purchase_order_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'po_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'link': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

