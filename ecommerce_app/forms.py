from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    This form is used to add product into our ecommerce website
    """
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

