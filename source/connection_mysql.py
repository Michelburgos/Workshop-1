import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv('.\Workshop-1\source\credentials.env')

# Mensaje de depuración
print("Variables de entorno cargadas:")
print(f"Usuario: {os.getenv('DB_USER')}")
print(f"Contraseña: {os.getenv('DB_PASSWORD')}")
print(f"Host: {os.getenv('DB_HOST')}")
print(f"Base de datos: {os.getenv('DB_NAME')}")
print(f"Puerto: {os.getenv('DB_PORT')}")

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL.
    """
    config = {
        "user": "root",
        "password": "root",
        "host": "127.0.0.1",
        "database": "candidates_db",
        "port": 3305,
        "raise_on_warnings": True
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa.")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        raise

if __name__ == "__main__":
    # Prueba la conexión
    conexion = get_db_connection()
    if conexion:
        conexion.close()
        print("Conexión cerrada.")