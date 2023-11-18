from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Item
from .forms import CreateForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'itemList': item_list,
    }
    # Rendering template using django render
    return render(request, 'food/index.html', context)

"""
    Implementing django 'Class Based' 'List' view inplace of above greet() function view
    FYI:
    django 'List' view is used to show the list of item and it's a (generic view)inbuilt Class Based view
 """

class ItemListClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'itemList'

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

# class Based Detail View for getting details of specific item
class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/details.html'

def create_item(request):
    form_data = CreateForm(request.POST or None)
    
    if form_data.is_valid():
        form_data.save()
        return redirect('food:greet')

    return render(request, 'food/create_form.html', {'form_data': form_data})

# class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    # Fields which are required to show in form
    template_name = 'food/create_form.html'

    # Create a function to accept form
    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
"""
In Django, when you create or update an object using a form, you can customize the behavior by overriding certain methods in your class-based views. The `form_valid` method is one of these methods.

Here's an explanation of what this `form_valid` function does:

1. **`form_valid` Method:**
   - The `form_valid` method is called when the form is successfully validated. This happens when the user submits the form with valid data.
   - This method is part of the Django `CreateView` class, and you've overridden it in your `CreateItem` class.

2. **`form` Argument:**
   - The `form` argument is the instance of the form that has been successfully validated.

3. **Updating `form.instance.user_name`:**
   - `form.instance` represents the instance of the model associated with the form. In this case, it's an instance of the `Item` model because your view is a `CreateView` for the `Item` model.
   - `self.request.user` represents the user who made the request (the user who is currently logged in). You're assigning this user to the `user_name` field of the `Item` model instance.

4. **`super().form_valid(form)` Call:**
   - This line calls the `form_valid` method of the parent class (`CreateView`) using the `super()` function.
   - This is important because the parent class's `form_valid` method likely contains logic that is necessary for the view to function properly. By calling `super().form_valid(form)`, you ensure that the default behavior of the parent class is executed.

5. **Return Statement:**
   - The `return super().form_valid(form)` line is used to return the result of the parent class's `form_valid` method. This is usually necessary to maintain the expected flow of the view.

In summary, the `form_valid` method in your example is responsible for updating the `user_name` field of the `Item` model instance with the currently logged-in user and then calling the `form_valid` method of the parent class to ensure that any default behavior is executed.
"""

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

