from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # It creates one to one relation with User model
    # on_delete=models.CASCADE - On deleting user the profile also need to be deleted
    
    image = models.ImageField(default="profilepic.jpg", upload_to="profile_pictures")
    locations = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
