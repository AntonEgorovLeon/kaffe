from django import forms
from .models import Client,Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('id_product','Note',)
        # formset = ProductFormSetInit

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('user','Birthdate','Phone','Social_status','Sex',)
