from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST) # retriving the form data
        if form_data.is_valid(): # validate form data
            form_data.save() # saving form_data
            user_name = form_data.cleaned_data.get('username') # get username from form_data
            # using message.success() trying to print the message
            messages.success(request, f'Welcome {user_name}, your have logged in successfully.')
            return redirect('login') #render list of food page
        
    else:
        # create the form if method is not POST
        form_data = RegisterForm()
    return render(request, 'users/register.html', {'form': form_data})