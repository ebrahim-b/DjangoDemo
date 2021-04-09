from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def display(request):
    return render(request,'main.html')

def mobile(request):
    products = Product.objects.filter(category = 1)
    return render(request,'products.html', {'products' : products})

def laptop(request):
    products = Product.objects.filter(category = 2)
    return render(request,'products.html', {'products' : products})