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
        password = os.getenv("PASS"),
        port = os.getenv("PORT"),
        database = os.getenv("DB"),
        autocommit=True #works to auto commit
    )

def select_messages() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True) #essentially resultset from jdbc
        
        sql = "SELECT * FROM database"
        cursor.execute(sql) #data lives in cursor (cursor already the result)
        
        for row in cursor:
            print(row)
            
        conn.close() #this happens automatically because we wrote "with"
        
def get_message_by_id(id: int) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True) #set setting to dictionary
        sql = "SELECT * FROM database WHERE id = %s", {id}
        cursor.execute(*sql)
        return cursor[0]
        
            
def create_message(message: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO database (message)"
        cursor.execute(sql)
        conn.commit()
        # queries not in auto-commit mode
        #remember ACID database rules
        #atomicity, consistency, isolation, 
        
create_message("hi")