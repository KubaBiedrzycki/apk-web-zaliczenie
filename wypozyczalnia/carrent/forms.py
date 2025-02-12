from django import forms
from .models import Car, Client

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'hp', 'drive', 'condition']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'age', 'drivingLicense', 'drivingLicenseUntill']