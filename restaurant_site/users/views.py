from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method == "POST":
        form_data = UserCreationForm(request.POST) # retriving the form data
        if form_data.is_valid(): # validate form data
            user_name = form_data.cleaned_data.get('username') # get username from form_data
            # using message.success() trying to print the message
            messages.success(request, f'Welcome {user_name}, your account is created successfully.')
            return redirect('food:greet') #render list of food page
        
    else:
        # create the form if method is not POST
        form_data = UserCreationForm()
    return render(request, 'users/register.html', {'form': form_data})