from django.urls import path
from .views import display,mobile,laptop,productform

urlpatterns = [
    path('',display),
    path('mobile/',mobile),
    path('laptop/',laptop),
    path('form/',productform),
]