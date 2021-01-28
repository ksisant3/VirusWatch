import mysql.connector

USERNAME = 'admin'
PASSWORD = 'viruswatch'
SERVER = 'test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com'
DATABASE = 'Test_DB'

def get_files():
    mydb = mysql.connector.connect(
        host=SERVER,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT file_name FROM user_file")

    filenames = cursor.fetchall()

    outList = set()

    for filename in filenames:
        outList.add(filename)

    return {'files': outList}