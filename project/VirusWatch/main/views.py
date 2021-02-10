from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from django.contrib.auth import authenticate, login
from .upload import *
from .download import get_files
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})
    
def home(response):
    return render(response, "main/home.html", {})

def thanks(response):
    return render(response, "main/thanks.html", {})

@login_required()
def upload(response):

    if response.method == 'POST' and \
    UploadFileForm(response.POST, response.FILES).is_valid():

        if upload_file(response):
            return HttpResponse("<h1>file uploaded successfully</h1>")
        else:
            return HttpResponse("<h1>file uploaded failed</h1>") 

    return render(response, "main/upload.html")

@login_required()
def view_uploads(response):
    return render(response, "main/view-uploads.html", get_files(response.user.id))
