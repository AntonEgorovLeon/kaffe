from django import forms
from .models import Client,Sale, Visit

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('Note',)
        # formset = ProductFormSetInit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('Note',)
        # formset = ProductFormSetInit

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('user','Birthdate','Phone','Social_status','Sex',)
