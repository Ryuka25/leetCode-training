import mysql.connector
from .config import *

class Database:

    database = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWD,
        database=DB_NAME
    )

    _cursor = database.cursor()
    
    def getCursor():
        if (Database._cursor):
            return Database._cursor