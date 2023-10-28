from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greet(request):
    # print("Welcome to our website")
    return HttpResponse("Welcome to our restaurant website...")