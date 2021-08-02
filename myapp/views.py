from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewList
# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello, world!</h1>")


def item_by_id(id):
    item = Item.objects.get(pk=id)
    return HttpResponse(f"Item: {item.title}, published on {item.datetime_found}")


def home(response):
    return render(response, "myapp/home.html", {})


def base(response):
    return render(response, "myapp/base.html", {})


def itemlist(response, list_id):
    ls = ToDoList.objects.get(id=list_id)
    return render(response, "myapp/itemlist.html", {"ls": ls})


def create(response):
    global t
    if response.method == "POST":
        form = CreateNewList(response.POST)  # Takes POST and uses data for form
        if form.is_valid():  # is_valid() checks class-fields for valid input
            n = form.cleaned_data["name"]  # Clean and un-enc data, specify field "name"
            t = ToDoList(name=n)  # Use data to create new ToDoList
            t.save()
        return HttpResponseRedirect("itemlist/%i" % t.id)  # Redirect to page that shows the list
    else:
        form = CreateNewList()
    return render(response, "myapp/create.html", {"form": form})
