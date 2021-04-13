from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(min_length=5)
    model = forms.CharField()