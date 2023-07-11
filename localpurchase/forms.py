from django import forms
from .models import LocalPurchaseModel, LPBillSubmissionModel
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget

class DTForm(forms.Form):
    date_input = forms.DateField(widget=AdminDateWidget)

class LocalPurchaseForm(forms.ModelForm):
    class Meta:
        model = LocalPurchaseModel
        fields = ("ref_no","indentor_name","your_email","requested_by","purpose","item_to_purchase",
                  "date_of_purchase","vendor_details","localtion_of_purchase","coa",
                  "approximate_distance","assigned_to","any_other_details" )
        labels = {
            'ref_no' : 'Reference No.',
            'indentor_name' : 'Name of the Indentor',
            'your_email':'Enter your email',
            'requested_by': 'Requested by',
            'coa':'CoA'


        }
        todays_date = date.today()
        yr = todays_date.year
        mnt = todays_date.month
        widgets = {
            'ref_no': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'indentor_name': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'requested_by': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'purpose': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'item_to_purchase': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'date_of_purchase': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'coa': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'vendor_details': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'localtion_of_purchase': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'approximate_distance': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'assigned_to': forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'any_other_details': forms.Textarea(attrs={'class':'form-control','row':'3'})
        }

class LPBillSubmissionForm(forms.ModelForm):
    class Meta:
        model = LPBillSubmissionModel
        fields = '__all__'
        labels = {
        'coa' : 'CoA',
        }
        widgets = {
        'bill_date' :  forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd '}
            )
        }
