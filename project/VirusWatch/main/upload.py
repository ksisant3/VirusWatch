from django.core.files.storage import FileSystemStorage
#import os
from os import path, makedirs
from datetime import datetime
import mysql.connector
from .database import Database

# ASSUMES REQUEST HAS VALID FORM
# RETURNS TRUE ON SUCCESS
def upload_file(request):

    fileSystem = FileSystemStorage()
    file = request.FILES['document']
    fileName = file.name

    # GET GROUP NAME AND ID
    # (HARDCODED FOR NOW)
    groupID = 1
    groupName = 'TEMP GROUP'

    appFileDir = path.join(fileSystem.location,'files')

    groupDir = path.join(appFileDir, groupName)

    # CHECK IF GROUP FOLDER DOESN'T EXIST
    if not path.exists(groupDir):

        makedirs(groupDir)

    if path.exists(path.join(groupDir,fileName)):

        fileName = find_unique_filename(fileName, groupDir)

    fileDir = path.join(groupDir, fileName)

    # SAVE FILE TO GROUP FOLDER
    # IF FILE IS DUPLICATE, FILEPATH 
    # IS UPDATED TO NEW FILE PATH
    fileSystem.save(fileDir, file)

    # OPEN DB CONNECTION
    db = Database()

    # SAVE FILE PATH, UPLOAD DATE, UPLOADER NAME TO USER_FILE
    sql = """ INSERT INTO user_file
              (file_name, user_id, group_id) 
              VALUES
              (%s,%s,%s);
          """

    # EXCECUTE SQL AND COMMIT CHANGES
    db.excecute_sql_insert(sql, (fileName, request.user.id, groupID))

    # RETURN TRUE
    return True

def find_unique_filename(fileName,directory):
    count = 1
    if fileName[-4:-3] == '.':
        while path.exists(path.join(directory,fileName[:-4] + 
                         '(' + str(count) + ')' + fileName[-4:])):
            count+=1

        return fileName[:-4] + '(' + str(count) + ')' + fileName[-4:]

    elif fileName[-5:-4] == '.':
        while path.exists(path.join(directory,fileName[:-5] +
                         '(' + str(count) + ')' + fileName[-5:])):
            count+=1

        return fileName[:-5] + '(' + str(count) + ')' + fileName[-5:]

    else:
        raise Exception("excel file name not valid")