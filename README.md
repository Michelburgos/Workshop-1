
# Workshop #1
## Visión General  
Este proyecto resuelve el reto de ingeniería de datos propuesto, que consiste en analizar un conjunto de datos de 50,000 registros de candidatos que participaron en procesos de selección. El objetivo principal es migrar los datos a una base de datos relacional, aplicar lógica de negocio para identificar candidatos "contratados" (HIRED) y generar visualizaciones clave que muestren métricas específicas.  

El proyecto se centra en:  
- **Migración de datos**: Carga de datos desde un archivo CSV a una base de datos relacional (MySQL).  
- **Análisis de datos**: Filtrado de candidatos contratados (con puntajes >= 7 en ambas evaluaciones).  
- **Visualizaciones**: Creación de gráficos para mostrar métricas clave, como contrataciones por tecnología, año, seniority y país, utilizando Power BI.  

Las tecnologías utilizadas en este proyecto incluyen:  
- **Python**: Para el manejo y análisis de datos.  
- **Jupyter Notebook**: Para el análisis interactivo de datos.  
- **MySQL**: Como base de datos relacional para almacenar y consultar los datos.  
- **Power BI**: Para la creación de visualizaciones interactivas y dashboards.  



## Tabla de Contenidos  
1. [Prerrequisitos](#prerrequisitos)  
2. [Instalación](#instalación)  
3. [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)  
4. [Uso](#uso)  
5. [Visualizaciones en Power BI](#visualizaciones-en-power-bi)  
6. [Documentación](#documentación)  


## Prerrequisitos  
Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:  
- **Python**: 3.8+  
- **Jupyter Notebook**: Para ejecutar el análisis interactivo.  
- **MySQL**: Servidor de base de datos instalado y configurado.  
- **Power BI Desktop**: Para la creación de visualizaciones.  
- **Librerías de Python**: Instaladas mediante `requirements.txt`.  

---

## Instalación  
1. Clona el repositorio:  
   ```bash  
   git clone https://github.com/Michelburgos/Workshop-1.git 
   cd Workshop-1

2. Crea el entorno virtual:
    ```bash
    python -m venv venv

3. Activa el entorno virtual:
- Ve a la carpeta de venv
    ```bash
    cd venv
- Ve a la carpeta de Scripts
    ```bash
    cd Scripts
- Desde Scripts activa el entorno virtual con: 
    ```bash
    activate
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

## Configuración de la Base de Datos  
En la carpeta raíz del proyecto, crea un archivo `.env` con la siguiente estructura:  

        DB_USER=tu_usuario          
        DB_PASSWORD=tu_contraseña   
        DB_HOST=direccion_host      # Dirección del host (generalmente localhost)
        DB_NAME=nombre_de_la_database  
        DB_PORT=puerto_mysql        # Puerto de MySQL (generalmente 3306)

Despues de tener el archivo `.env` cambia la ruta en el archivo connection_mysql.py por la ruta de tu archivo `.env` 

    dotenv_path = "C:/ruta del archivo .env"

Ejecuta el archivo connection_mysql.py para conectarse a la base de datos
```bash
python connection_mysql.py

## Uso

