from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 15
# Create your views here.
def index(request):
    return HttpResponse("This is a site to cal tax")
def anyNumber(request, number):
    return HttpResponse(f'The total is  {number * ((tax_rate/100)+1)}')
def taxRate(request):
    return render(request, "app/taxrate.html",{
        "tax": tax_rate
    })