import os
from dotenv import load_dotenv
import mysql.connector

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

# Mostrar las variables de entorno cargadas
print("Variables de entorno cargadas:")
print(f"Usuario: {db_user}")
print(f"Contraseña: {db_password}")
print(f"Host: {db_host}")
print(f"Base de datos: {db_name}")
print(f"Puerto: {db_port}")

# Conectar a la base de datos
try:
    conexion = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name,
        port=db_port
    )
    
    if conexion.is_connected():
        print("Conexión a la base de datos exitosa.")
        
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")