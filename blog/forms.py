from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(min_length=5)
    model = forms.CharField()


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"