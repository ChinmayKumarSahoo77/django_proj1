from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Item

# Create your views here.

"""
#Render Using HTTPResponse 
def greet(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'itemList': item_list,
    }
    return HttpResponse(template.render(context,request))
"""

def greet(request):
    """
    Render template using django render
    """
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'itemList': item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("<h1>Here is the item list view</h1>")

def offer_water(request):
    return HttpResponse("<h3>Do you need water?</h3>")
