from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, Product_Form

def display(request):
    return render(request,'main.html')

def mobile(request):
    products = Product.objects.filter(category = 1)
    return render(request,'products.html', {'products' : products})

def laptop(request):
    products = Product.objects.filter(category = 2)
    return render(request,'products.html', {'products' : products})

def productform(request):
    form = Product_Form

    if request.method == 'POST':
        form = Product_Form(request.POST)
        if form.is_valid():
            form.save()
            return display(request)
    return render(request,'form.html', {'form':form})