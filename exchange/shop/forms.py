from shop.models import Products
from django import forms


class Productform(forms.ModelForm):
    class Meta:
        model=Products
        exclude=['user']