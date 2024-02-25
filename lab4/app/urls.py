from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:number>", views.anyNumber, name="anyNumber"),
    path("taxrate/", views.taxRate, name="taxRate"),
    
]