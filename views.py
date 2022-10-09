from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
  return render(request, 'myfirstblogspot/index.html')

def customers(request):
  return render(request, 'myfirstblogspot/customers.html')

def packages(request):
  return render(request, 'myfirstblogspot/packages.html')    

