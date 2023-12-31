"""
URL configuration for restaurant_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('food.urls')),
    path('register/', user_view.register, name = 'register'),
    path('login/', auth_view.LoginView.as_view(template_name = "users/login.html"), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = "users/logout.html"), name = 'logout'),
    #.as_view() bcoz of class view
    # template_name = "users/login.html" -> tell django to look for template in specified location
    path('profile/', user_view.profile_page, name='profile'),
]

# Search how to manage static files in django
# Copy the code from following section and add it to urls.py of main project:
# Serving files uploaded by a user during development
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
