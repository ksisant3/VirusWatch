from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from .upload import *
from .download import get_files
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.conf import settings
import mimetypes

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

        File(name=response.FILES['document'].name,file=response.FILES['document'],
             user=response.user).save()
        return HttpResponse("<h1>file uploaded successfully</h1>")

    return render(response, "main/upload.html")

@login_required()
def view_uploads(response):

    return render(response, "main/view-uploads.html",
                 {'files':File.objects.filter(user = response.user.id)})



def download(request,file_name):
    f = File.objects.get(user = request.user.id, name = file_name )
    response = HttpResponse(f.file.open(mode='rb'))
    file_mimetype = mimetypes.guess_type(f.file.name)
    response['Content-Type'] = file_mimetype
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    response['X-Sendfile'] = file_name
    return response