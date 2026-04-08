import os
import dotenv
import mysql.connector
from dotenv import load_dotenv


from mysql.connector import Error

# os.getenv("PATH") #this gets us environment variables

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("PASSWORD"),
        port = os.getenv("PORT"),
        database = os.getenv("DB"),
        autocommit=True #works to auto commit
    )