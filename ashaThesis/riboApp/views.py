from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    #can make a dictionary here like my_dict={}
    # then in the render command put {"name":ls.name}
    ls = ToDoList.objects.get(id=id)
    return render(response, "riboApp/base.html", {})

def view1(response):
    return HttpResponse("<h1>Another cool page :)</h1>")

def home(response):
    return render(response, "riboApp/home.html", {})

def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
