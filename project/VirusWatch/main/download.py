import mysql.connector
from .database import Database

def get_files(userID):
    db = Database()

    sql = """SELECT file_name
             FROM user_file 
             WHERE user_id= %s"
    """

    filenames = db.excecute_sql_select(sql,(str(userID),))

    outList = []

    for filename in filenames:
        outList.append(filename)

    print(type(outList[0]))

    return {'files': outList}
