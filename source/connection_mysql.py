import os
from dotenv import load_dotenv
import mysql.connector

dotenv_path = "C:/Users/Michel Burgos/OneDrive/Documentos/GitHub/Workshop-1/credential.env"
load_dotenv(dotenv_path)

# Obtener las variables de entorno
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')


def get_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL.
    """
    try:
        conexion = mysql.connector.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            database=db_name,
            port=int(db_port),
            use_pure=True  # Forzar el uso de TCP/IP
        )
        
        if conexion.is_connected():
            print("✅ Conexión a la base de datos exitosa.")
            return conexion
            
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None