from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def display(request):
    return render(request,'main.html')

def mobile(request):
    products = Product.objects.filter(category = 1)
    return render(request,'products.html', {'products' : products})

def laptop(request):
    products = Product.objects.filter(category = 2)
    return render(request,'products.html', {'products' : products})

def productform(request):
    form = ProductForm()
    return render(request,'form.html', {'form':form})