from django.urls import path

from . import views

urlpatterns = [
    path('', views.greet, name = 'greet'),
    path('item/', views.item, name = 'item'),
    path('offer_water/', views.offer_water, name = 'offer_water'),
]