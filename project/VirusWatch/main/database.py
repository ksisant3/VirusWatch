import mysql.connector
import os
from datetime import datetime

USERNAME = 'admin'
PASSWORD = 'viruswatch'
SERVER = 'test-db.ctvd1ztjykvr.us-east-1.rds.amazonaws.com'
DATABASE = 'Test_DB'

class Database:

    @staticmethod
    def open_db_conn():
            return mysql.connector.connect(
                host=SERVER,
                user=USERNAME,
                password=PASSWORD,
                database=DATABASE
        )