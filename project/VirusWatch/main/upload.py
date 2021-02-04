from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime
import mysql.connector
from .database import Database

# ASSUMES REQUEST HAS VALID FORM
# RETURNS TRUE ON SUCCESS
def upload_file(request):

    fileSystem = FileSystemStorage()
    file = request.FILES['document']

    # GET GROUP NAME AND ID
    # (HARDCODED FOR NOW)
    groupID = 1
    groupName = 'TEMP GROUP'

    groupPath = os.path.join(fileSystem.location, groupName)

    # CHECK IF GROUP FOLDER DOESN'T EXIST
    if not os.path.exists(groupPath):

        # CREATE IT
        os.makedirs(groupPath)

    filePath = os.path.join(groupPath, file.name)

    # SAVE FILE TO GROUP FOLDER
    # IF FILE IS DUPLICATE, FILEPATH 
    # IS UPDATED TO NEW FILE PATH
    filePath = fileSystem.save(filePath, file)

    # OPEN DB CONNECTION
    conn = Database.open_db_conn()

    # SAVE FILE PATH, UPLOAD DATE, UPLOADER NAME TO USER_FILE
    cursor = conn.cursor()

    # SQL
    sql = """ INSERT INTO user_file
              (file_name, user_id, group_id) 
              VALUES
              (%s,%s,%s);
          """

    # EXCECUTE SQL AND COMMIT CHANGES
    cursor.execute(sql, (file.name, request.user.id, groupID))
    conn.commit()

    # CLOSE CONNECITON
    cursor.close()
    conn.close()

    # RETURN TRUE
    return True

