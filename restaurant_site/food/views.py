from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Item
from .forms import CreateForm

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

def details(request,itemId):
    item_details = Item.objects.get(id = itemId)
    context = {
        "itemDetails": item_details,
    }
    return render(request, 'food/details.html', context)

def create_item(request):
    form_data = CreateForm(request.POST or None)
    
    if form_data.is_valid():
        form_data.save()
        return redirect('food:greet')

        

    return render(request, 'food/create_form.html', {'form_data': form_data})

def update_item(request, itemId):
    item_id = Item.objects.get(id = itemId)

    form_data = CreateForm(request.POST or None, instance = item_id)

    if form_data.is_valid():
        form_data.save()
        return redirect('food:greet')

    # render tamplate
    return render(request, 'food/create_form.html', {'form_data':form_data, 'itemId': item_id})

def delete_item(request, itemId):
    item_id = Item.objects.get(id = itemId)

    if request.method == 'POST':
        item_id.delete()
        return redirect('food:greet')

    return render(request, 'food/delete_item.html', {'item': item_id})

