from django.shortcuts import render, redirect
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


def deleteModel(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect('/')

def updateModel(request, id):
    product = Product.objects.get(id=id)

    form = Product_Form(instance = product)

    if request.method == 'POST':
        form = Product_Form(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'form.html', {'form':form})
