from django.urls import path

from . import views

app_name = "food"
urlpatterns = [
    #food/
    #used as_view() due to ItemListClassView is a class based view
    path('', views.ItemListClassView.as_view(), name = 'greet'),
    #food/item/
    path('item/', views.item, name = 'item'),
    #food/offer_water/
    path('offer_water/', views.offer_water, name = 'offer_water'),
    
    #food/1
    path('<int:pk>/', views.ItemDetailView.as_view(), name = 'details'), 
    # Above is class based details view
    # path('<int:itemId>/', views.details, name = 'details'), - Above is class based details view

    #food/add by using forms
    path('add/', views.CreateItem.as_view(), name = 'create_item'),
    #update item
    path('update/<int:itemId>', views.update_item, name = 'update_item'),
    # delete item
    path('delete/<int:itemId>', views.delete_item, name = 'delete_item'),
]