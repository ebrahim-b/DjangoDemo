from django.urls import path
from .views import display,mobile,laptop

urlpatterns = [
    path('',display),
    path('mobile/',mobile),
    path('laptop/',laptop),
]