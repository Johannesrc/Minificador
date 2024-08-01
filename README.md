# Minificador de Proyecto en Python

Este proyecto es una aplicación en Python diseñada para minificar archivos HTML, CSS, JS y PHP dentro de un proyecto. La aplicación permite crear una copia del proyecto en una ruta especificada por el usuario, con todos los archivos minificados.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener las siguientes bibliotecas instaladas:

- `htmlmin`
- `csscompressor`
- `jsmin`

## Instalación y Uso

### Opción 1: Manualmente en un Entorno Virtual

#### 1. Crear y Activar un Entorno Virtual

1. Abre una terminal en el directorio del proyecto.
2. Crea un entorno virtual ejecutando:

   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```bash
     env\Scripts\activate
     ```
   - En macOS y Linux:
     ```bash
     source env/bin/activate
     ```

#### 2. Instalar Dependencias

Con el entorno virtual activado, instala las dependencias necesarias:

```bash
pip install htmlmin csscompressor jsmin
```

#### 3. Ejecutar el Script

Con el entorno virtual activado, ejecuta el script principal:

```bash
python main.py
```

### Opción 2: Usando Scripts de Automatización

Puedes utilizar los scripts proporcionados (`run_minify.sh` para Unix/Linux/macOS o `run_minify.bat` para Windows) para automatizar todo el proceso de creación del entorno virtual, instalación de dependencias, ejecución del script y desactivación del entorno virtual.

#### En Unix/Linux/macOS

1. Asegúrate de que el script `run_minify.sh` tiene permisos de ejecución:

   ```bash
   chmod +x run_minify.sh
   ```

2. Ejecuta el script:

   ```bash
   ./run_minify.sh
   ```

#### En Windows

1. Simplemente ejecuta el archivo `run_minify.bat` haciendo doble clic o desde la terminal:

   ```cmd
   run_minify.bat
   ```

## Descripción

La aplicación proporciona una interfaz gráfica simple para seleccionar la ruta del proyecto de origen y la ruta de destino donde se guardará la copia del proyecto con los archivos minificados.

### Características

- **Minificación de Archivos**: Minifica archivos HTML, CSS, JS y PHP.
- **Copia del Proyecto**: Crea una copia del proyecto en una ubicación especificada por el usuario.
- **Interfaz Gráfica**: Incluye una interfaz gráfica de usuario fácil de usar basada en `tkinter`.

### Minificación de PHP

La minificación de PHP maneja tanto PHP puro como archivos PHP que contienen HTML. Las características de minificación incluyen:

- Eliminación de comentarios y espacios innecesarios en el código PHP.
- Minificación de contenido HTML y JavaScript embebido dentro de archivos PHP.

## Uso de la Aplicación

1. Clona este repositorio o descarga los archivos.
2. Ejecuta el script `main.py` (o utiliza los scripts de automatización):
   ```bash
   python main.py
   ```
3. En la interfaz gráfica, selecciona la ruta del proyecto de origen y la ruta del proyecto de destino.
4. Haz clic en "Minificar" para crear una copia del proyecto con los archivos minificados en la ruta especificada.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, envía un pull request o abre un issue para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo los términos de la Licencia Pública General de GNU. Consulta el archivo LICENSE para obtener más detalles.
