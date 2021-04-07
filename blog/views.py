from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return render(request,'main.html')

def mobile(request):
    mobiles = {
        'product1': 'apple',
        'product2': 'samsung'
    }
    return render(request,'products.html', context=mobiles)

def laptop(request):
    laptops = {
        'product1': 'asus',
        'product2': 'hp'
    }
    return render(request,'products.html', context=laptops)