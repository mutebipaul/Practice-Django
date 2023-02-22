from django.shortcuts import render
from .forms import pizzaform

def home(request):
    return render(request,'home.html')

def order(request):
    form = pizzaform()
    return render(request,'order.html',{pizzaform})
