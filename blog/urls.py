from django.urls import path
from .views import display,mobile,laptop,productform, deleteModel, updateModel

urlpatterns = [
    path('',display),
    path('mobile/',mobile),
    path('laptop/',laptop),
    path('form/',productform),
    path('delete/<int:id>',deleteModel),
    path('update/<int:id>',updateModel),
]