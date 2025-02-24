# database.py
import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL.
    """
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'raise_on_warnings': True
    }
    return mysql.connector.connect(**config)