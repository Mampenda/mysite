from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('item/<int:id>', views.item_by_id, name='item_by_id'),
    path('itemlist/<int:list_id>', views.itemlist, name='itemlist'),
    path('create/', views.create, name='create'),
    path('create/itemlist/<int:list_id>', views.itemlist, name='itemlist'),
]
