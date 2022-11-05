from django import forms
from burgery.models import Product

class AddNewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'