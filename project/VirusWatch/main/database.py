import mysql.connector
import os
from datetime import datetime

USERNAME = 'admin'
PASSWORD = 'viruswatch'
SERVER = 'test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com'
DATABASE = 'Test_DB'

class Database:

    def __init__(self):
        self.conn = mysql.connector.connect(
                host=SERVER,
                user=USERNAME,
                password=PASSWORD,
                database=DATABASE
        )

    def __del__(self):
        self.conn.close()

    def excecute_sql_select(self, sql_string, tupl = None):
        cursor = self.conn.cursor()

        if tupl is None:
            cursor.execute(sql_string)
        else:
            cursor.execute(sql_string,tupl)

        row = cursor.fetchone()

        output = []

        while row is not None:
            output.append(row)
            row = cursor.fetchone()

        cursor.close()

        return output

    def excecute_sql_insert(self, sql_string, tuple = None):

        cursor = self.conn.cursor()

        if tuple is not None:

            cursor.execute(sql_string, tuple)

        else:

            cursor.execute(sql_string)

        self.conn.commit()

        cursor.close()

        return True


