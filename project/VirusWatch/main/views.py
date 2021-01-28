from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from django.contrib.auth import authenticate, login
from .upload import upload_file
from .download import get_files


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

def upload(response):
    if response.method == 'POST':
        if upload_file(response):
            return HttpResponse("<h1>file uploaded successfully</h1>")
        else:
            return HttpResponse("<h1>file uploaded failed</h1>") 

    return render(response, "main/upload.html")

def view_uploads(response):
    return render(response, "main/view-uploads.html", get_files())

