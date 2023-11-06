from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    #food/
    path('', views.greet, name = 'greet'),
    #food/item/
    path('item/', views.item, name = 'item'),
    #food/offer_water/
    path('offer_water/', views.offer_water, name = 'offer_water'),
    #food/1
    path('<int:itemId>', views.details, name = 'details'),
    #food/add by using forms
    path('add', views.create_item, name = 'create_item'),
    #update item
    path('update/<int:itemId>', views.update_item, name = 'update_item'),
    # delete item
    path('delete/<int:itemId>', views.delete_item, name = 'delete_item'),
]