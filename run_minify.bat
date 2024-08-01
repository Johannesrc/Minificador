@echo off

:: Nombre del entorno virtual
set VENV_DIR=env

:: Comprobar si el entorno virtual existe
if not exist %VENV_DIR% (
    python -m venv %VENV_DIR%
    echo Entorno virtual creado en %VENV_DIR%
) else (
    echo Entorno virtual ya existe en %VENV_DIR%
)

:: Activar el entorno virtual
call %VENV_DIR%\Scripts\activate

:: Función para instalar dependencias si no están ya instaladas
pip list | findstr htmlmin >nul
if %ERRORLEVEL% neq 0 (
    echo Instalando htmlmin...
    pip install htmlmin
) else (
    echo htmlmin ya esta instalado.
)

pip list | findstr csscompressor >nul
if %ERRORLEVEL% neq 0 (
    echo Instalando csscompressor...
    pip install csscompressor
) else (
    echo csscompressor ya esta instalado.
)

pip list | findstr jsmin >nul
if %ERRORLEVEL% neq 0 (
    echo Instalando jsmin...
    pip install jsmin
) else (
    echo jsmin ya esta instalado.
)

:: Ejecutar el script de minificación
python main.py

:: Desactivar el entorno virtual
call %VENV_DIR%\Scripts\deactivate
