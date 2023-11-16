from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import UserProfile

# We are creating this function to make the creation of user profile automatic.
# To make it automatic we are making use of Django singnal using Signal dispatcher

@receiver(post_save, sender = User)
def build_profile(sender, instance, created, **kwargs):
    """
    function to build the profile
    sender - Who send the signal - (here User)
    instance - instance which is being saved (instance of UserProfile)  
    created - receives boolean value and tells wheather user created or not
    **kwargs - To pass additional keyword argument

    @receiver(post_save, sender = User)
    post_save - signal type
    sender = User - Who is sending the signal

    Whenever it receives a 'post_save' signal from 'User', then only this function will be executed
    """
    if created:
        UserProfile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    """
    Function to save the profile
    """
    instance.userprofile.save()
    #'userprofile' in above line is the Profile model name.