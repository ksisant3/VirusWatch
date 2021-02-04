import mysql.connector
from .database import Database

def get_files():
    conn = Database.open_db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT file_name FROM user_file")

    filenames = cursor.fetchall()

    outList = set()

    for filename in filenames:
        outList.add(filename)

    conn.close()
    cursor.close()

    return {'files': outList}