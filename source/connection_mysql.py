import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

dotenv_path = "C:/Users/Michel Burgos/OneDrive/Documentos/GitHub/Workshop-1/credential.env"
load_dotenv(dotenv_path)

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

def get_sqlalchemy_engine():
    """Crea y devuelve un engine de SQLAlchemy para conectar con MySQL"""
    try:
        engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
        
        # Verificar conexión con un simple ping
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # 🔹 Se usa text() para evitar el error

        print("✅ Conexión a la base de datos exitosa.")
        return engine
    
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return None

