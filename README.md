# Workshop 1  

Por Michel Dahiana Burgos Santos

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
   dotenv_path = "C:/ruta del archivo .env"  
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
## 1. Instalación de MySQL Connector/ODBC
Power BI no tiene un conector nativo para MySQL, por lo que es necesario instalar **MySQL Connector/ODBC**.

### Pasos:
1. Descargar el conector desde la página oficial de MySQL:
   - [Descargar MySQL Connector/ODBC](https://dev.mysql.com/downloads/connector/odbc/)
2. Instalar el conector en el sistema.
3. Durante la instalación, asegurarse de seleccionar la opción **Unicode Driver** para mejor compatibilidad.

---

## 2. Configuración de una Fuente de Datos ODBC (DSN)
Después de instalar el conector, se debe configurar una fuente de datos ODBC en Windows.

### Pasos:
1. Abrir el **Administrador de Orígenes de Datos ODBC** en Windows (buscar "ODBC" en el menú de inicio).
2. Seleccionar la pestaña **DSN del sistema** y hacer clic en **Agregar**.
3. Elegir **MySQL ODBC Unicode Driver** y hacer clic en **Finalizar**.
4. En la ventana de configuración, ingresar los datos de conexión:
   - **Data Source Name (DSN)**: Nombre para identificar la conexión (ejemplo: `MySQL_PowerBI`).
   - **Server**: IP o nombre del servidor donde está MySQL (ejemplo: `localhost` o `192.168.1.100`).
   - **User**: Usuario de MySQL (ejemplo: `root`).
   - **Password**: Contraseña del usuario de MySQL.
   - **Database**: Nombre de la base de datos a la que se conectará Power BI.
5. Hacer clic en **Test** para verificar la conexión.
6. Si todo está correcto, guardar la configuración.

---

## 3. Conectar Power BI a MySQL
Una vez configurado el DSN en ODBC, Power BI puede conectarse a la base de datos.

### Pasos:
1. Abrir **Power BI**.
2. Hacer clic en **Obtener datos**.
3. Seleccionar la opción **ODBC** en la lista de conectores.
4. En la ventana emergente, elegir el DSN configurado previamente (`MySQL_PowerBI`).
5. Ingresar credenciales si es necesario y hacer clic en **Conectar**.
6. Aparecerá una lista de bases de datos y tablas disponibles en MySQL.
7. Seleccionar la base de datos y las tablas que se desean importar.
8. Hacer clic en **Cargar** para traer los datos a Power BI.


#### Creación de Visualizaciones  
Una vez conectada la base de datos en Power BI, puedes comenzar a construir visualizaciones con los datos extraídos y transformados. Algunas métricas sugeridas incluyen:  
- Contrataciones por tecnología.  
- Contrataciones por año.  
- Distribución de candidatos por seniority.  
- Análisis de contratación por país.  

---


