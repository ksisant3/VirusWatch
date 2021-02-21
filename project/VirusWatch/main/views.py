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
from django.contrib import messages


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})
    
def home(response):
    return render(response, "main/home.html", {})

def thanks(response):
    return render(response, "main/thanks.html", {})


def analysis(response):
    return render(response, "main/analysis.html", {})

@login_required()
def upload(response):

    if response.method == 'POST' and \
    UploadFileForm(response.POST, response.FILES).is_valid():

        File(name=response.FILES['document'].name,file=response.FILES['document'],
             user=response.user).save()

        messages.info(response, 'Your file has been uploaded successfully!')
        
    return render(response, "main/upload.html")

@login_required()
def view_uploads(response):

    return render(response, "main/view-uploads.html",
                 {'files':File.objects.filter(user = response.user.id)})



def download( request, file_id ):

    # todo: check if user is logged in
    #       and has permissions

    # get file model with id
    file_model = File.objects.get( id = file_id )

    response = HttpResponse( file_model.file.open(mode='rb') )

    file_mimetype = mimetypes.guess_type( file_model.file.name )

    response['Content-Type'] = file_mimetype

    response['Content-Disposition'] = 'attachment; filename=' + \
                                      file_model.file.name

    response['X-Sendfile'] = file_model.file.name

    return response