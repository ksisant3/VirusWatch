from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from django.contrib.auth import authenticate, login


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})
    
def home(response):
    return render(response, "main/home.html", {})

def create(response):
    return render(response, "main/create.html", {})

def thanks(response):
    return render(response, "main/thanks.html", {})

