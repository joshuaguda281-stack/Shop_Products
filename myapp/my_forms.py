from django import forms

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'cost', 'discount', 'for_sale', 'category', 'description', 'price']
