#!/bin/bash

# Variables de rutas
APP_DIR="/app"
VENV_DIR="$APP_DIR/venv"

# Crear el directorio de trabajo si no existe
mkdir -p "$APP_DIR"

# Copiar los archivos de herramientas desde /tmp/app a /app
cp -r /tmp/app/* "$APP_DIR/"

# Crear el entorno virtual en /app/venv
python3 -m venv "$VENV_DIR"

# Activar el entorno virtual
source "$VENV_DIR/bin/activate"

# Actualizar pip e instalar dependencias
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r "$APP_DIR/requirements.txt"

# Mostrar mensaje de éxito
echo "✅ Entorno virtual configurado correctamente en $VENV_DIR"

# Iniciar la aplicación (puedes cambiar este comando según sea necesario)
exec "$@"
