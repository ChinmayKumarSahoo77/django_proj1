from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greet(request):
    return HttpResponse("Welcome to our restaurant website...")

def item(request):
    return HttpResponse("<h1>Here is the item list view</h1>")

def offer_water(request):
    return HttpResponse("<h3>Do you need water?</h3>")
