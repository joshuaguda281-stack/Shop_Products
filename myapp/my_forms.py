from django import forms
from django.contrib.auth.forms import UserCreationForm

from myapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'cost', 'discount', 'for_sale', 'category', 'description', 'price', 'picture']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')
