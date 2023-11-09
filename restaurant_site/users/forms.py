from django import forms  # used to create django form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm): #inheriting user UserCreationForm
    email = forms.EmailField() #adding one field with name email and type is EmailField
    
    class Meta:
        # A meta cls is nothing but which provides the info about this class it self.
        # Meta class holds info. about RegisterForm class
        
        model = User #the model which it belongs to
        fields = ['username', 'email', 'password1', 'password2'] # Field need to be displayed on the form
