from django.http import HttpResponse
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import pandas as pd
from sqlalchemy import create_engine
import tkinter as tk
import os
from datetime import datetime

USERNAME = 'admin'
PASSWORD = 'viruswatch'
SERVER = 'test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com:3306'
DATABASE = 'Test_DB'

def upload_file(request):

    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid() and handle_uploaded_file(request.FILES['document']):
        return True
    return False

def handle_uploaded_file(file):
    
    try: 
        fileSystem = FileSystemStorage()
        fileSystem.save(file.name, file)

        root = tk.Tk()
        root.withdraw()

        file_path = os.path.join(fileSystem.location, file.name)

        engine = create_engine('mysql+mysqldb://'+ USERNAME +':'+PASSWORD+'@'+SERVER+'/'+DATABASE)

        dataframe = pd.read_excel(file_path)

        table_name = datetime.now().strftime("%H:%M:%S") + '_' + file.name

        dataframe.to_sql(table_name, con=engine)

        fileSystem.delete(file.name)

        return True

    except:
        return False