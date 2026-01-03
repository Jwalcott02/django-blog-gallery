from django import forms
from .models import Product

##This form handles user input using Django’s ModelForm, automatically generating fields from the model.

class ProductForm(forms.ModelForm):
    class Meta:
       model = Product
       fields = ['name','description','image']