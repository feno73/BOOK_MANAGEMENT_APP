import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        conn = sqlite3.connect('db/books_db.db')
        return conn
    except  Error as e:
        print("Error conectando a la bbdd: " + str(e))

