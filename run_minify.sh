#!/bin/bash

# Nombre del entorno virtual
VENV_DIR="env"

# Crear el entorno virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    echo "Entorno virtual creado en $VENV_DIR"
else
    echo "Entorno virtual ya existe en $VENV_DIR"
fi

# Activar el entorno virtual
source "$VENV_DIR/bin/activate"

# Comprobar e instalar dependencias si es necesario
install_dependency_if_missing() {
    local package=$1
    if ! pip list | grep -F "$package" > /dev/null; then
        echo "Instalando $package..."
        pip install "$package"
    else
        echo "$package ya está instalado."
    fi
}

install_dependency_if_missing "htmlmin"
install_dependency_if_missing "csscompressor"
install_dependency_if_missing "jsmin"

# Ejecutar el script de minificación
python main.py

# Desactivar el entorno virtual
deactivate
