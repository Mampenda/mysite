from django.contrib import admin
from .models import Item, ToDoList, ListItem

admin.site.register(Item)
admin.site.register(ToDoList)
admin.site.register(ListItem)
