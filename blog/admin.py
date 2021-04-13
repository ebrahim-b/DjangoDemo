from django.contrib import admin
from .models import Product

class AdminShow(admin.ModelAdmin):
    list_display = ['name', 'model']

admin.site.register(Product, AdminShow)
