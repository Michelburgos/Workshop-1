# Workshop 1  

## Visión General  
Este proyecto aborda un reto de ingeniería de datos que implica el análisis de un conjunto de datos con 50,000 registros de candidatos en procesos de selección. Su principal objetivo es migrar los datos a una base de datos relacional, aplicar lógica de negocio para identificar candidatos "contratados" (HIRED) y generar visualizaciones clave con métricas relevantes.  

El proyecto se enfoca en:  
- **Migración de datos**: Cargar datos desde un archivo CSV a una base de datos relacional (MySQL).  
- **Análisis de datos**: Filtrar candidatos contratados (con puntajes >= 7 en ambas evaluaciones).  
- **Visualizaciones**: Crear gráficos para mostrar métricas clave como contrataciones por tecnología, año, seniority y país, utilizando Power BI.  

Las tecnologías utilizadas en este proyecto incluyen:  
- **Python**: Para manipulación y análisis de datos.  
- **Jupyter Notebook**: Para análisis interactivo de datos.  
- **MySQL**: Base de datos relacional para almacenamiento y consultas.  
- **Power BI**: Para la creación de dashboards interactivos.  

## Tabla de Contenidos  
1. [Prerrequisitos](#prerrequisitos)  
2. [Instalación](#instalación)  
3. [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)  
4. [Uso](#uso)  
5. [Visualizaciones en Power BI](#visualizaciones-en-power-bi)  
6. [Documentación](#documentación)  

---

## Prerrequisitos  
Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:  
- **Python**: Versión 3.8 o superior.  
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
   ```  

2. Crea un entorno virtual:  
   ```bash  
   python -m venv venv  
   ```  

3. Activa el entorno virtual:  
   - En Windows:  
     ```bash  
     venv\Scripts\activate  
     ```  
   - En macOS/Linux:  
     ```bash  
     source venv/bin/activate  
     ```  

4. Instala las dependencias necesarias:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## Configuración de la Base de Datos  
1. Crea un archivo `.env` en la carpeta raíz del proyecto con la siguiente estructura:  

   ```ini  
   DB_USER=tu_usuario  
   DB_PASSWORD=tu_contraseña  
   DB_HOST=localhost  # Dirección del servidor MySQL  
   DB_NAME=nombre_de_la_base_de_datos  
   DB_PORT=3306  # Puerto de MySQL (por defecto 3306)  
   ```  

2. Asegúrate de modificar la ruta del archivo `.env` en `connection_mysql.py`:  
   ```python  
   dotenv_path = "C:/ruta/del/archivo/.env"  
   ```  

3. Ejecuta el siguiente comando para comprobar la conexión a la base de datos:  
   ```bash  
   python connection_mysql.py  
   ```  

---

## Uso  
### Ejecución de los Notebooks  
Para ejecutar correctamente el análisis, sigue este orden en los notebooks:  

1. **`001.ipynb`**: Extrae los datos del archivo CSV y los carga en la base de datos.  
2. **`002.ipynb`**: Realiza el análisis exploratorio de datos.  
3. **`003.ipynb`**: Transforma los datos y los carga en una nueva tabla dentro de la base de datos.  

🔹 **Nota**: Asegúrate de seleccionar el kernel correcto en Jupyter Notebook antes de ejecutar cada notebook. Debes elegir `venv` para utilizar el entorno virtual creado.  

---

## Visualizaciones en Power BI  
### Conectar Power BI con MySQL  
#### Instalación del conector  
Como utilizamos MySQL, es necesario instalar **MySQL Connector/NET**.  

1. Descarga **MySQL Connector/NET** desde la página oficial:  
   🔗 [MySQL Connector/NET](https://dev.mysql.com/downloads/connector/net/)  
2. Instala la versión compatible con tu sistema operativo (32 o 64 bits).  

#### Configuración de la conexión en Power BI  
1. Abre **Power BI Desktop**.  
2. Ve a **Obtener datos** > **Base de datos** > **MySQL**.  
3. En el campo **Servidor**, ingresa:  
   - `localhost` si MySQL está en tu máquina.  
   - `IP_DEL_SERVIDOR` o `NOMBRE_DEL_SERVIDOR` si es remoto.  
   - Si es necesario, especifica el puerto en el formato: `servidor:puerto` (Ej: `192.168.1.10:3306`).  
4. Selecciona el método de autenticación:  
   - **Base de datos** → Ingresa tu usuario y contraseña de MySQL.  
   - **Windows** → Si MySQL permite autenticación con Windows (menos común).  
5. Haz clic en **Conectar** y selecciona la base de datos y las tablas necesarias.  

#### Creación de Visualizaciones  
Una vez conectada la base de datos en Power BI, puedes comenzar a construir visualizaciones con los datos extraídos y transformados. Algunas métricas sugeridas incluyen:  
- Contrataciones por tecnología.  
- Contrataciones por año.  
- Distribución de candidatos por seniority.  
- Análisis de contratación por país.  

---


