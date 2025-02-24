import os
from dotenv import load_dotenv
import mysql.connector

# Cargar variables de entorno desde el archivo .env
load_dotenv('credential.env')

# Obtener las variables de entorno
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

def get_connection(): 
# Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name,
            port=int(db_port)  # Asegúrate de convertir el puerto a entero
        )
        
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa.")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
