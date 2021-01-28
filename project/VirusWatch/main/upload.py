from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import pandas as pd
from sqlalchemy import create_engine
import tkinter as tk
import os
from datetime import datetime
import mysql.connector


USERNAME = 'admin'
PASSWORD = 'viruswatch'
SERVER = 'test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com:3306'
DATABASE = 'Test_DB'

def upload_file(request):

    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid() and handle_uploaded_file(request.FILES['document']):
        add_filename(request.FILES['document'].name)
        return True
    return False

def add_filename(filename):
    mydb = mysql.connector.connect(
        host="test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com",
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )

    mycursor = mydb.cursor()

    sql= "INSERT INTO user_file(file_name) VALUES('" + filename + "');"
    val = (filename)
    print(sql)
    mycursor.execute(sql)

    mydb.commit()
    mycursor.close()

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