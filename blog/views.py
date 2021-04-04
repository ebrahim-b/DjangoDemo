from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1>Tango With Django</h1>')
