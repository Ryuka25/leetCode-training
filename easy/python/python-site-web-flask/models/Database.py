import mysql.connector
from .config import *

class Database:

    database = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD, database=DB_NAME)
    _instance = database.cursor()
    
    def getInstance():
        if (Database._instance):
            return Database._instance