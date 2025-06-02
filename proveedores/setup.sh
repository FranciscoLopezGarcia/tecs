#!/bin/bash

# Directorio del entorno virtual
VENV_DIR=".venv"

# Crear entorno si no existe
if [ ! -d "$VENV_DIR" ]; then
    echo "🧪 Creando entorno virtual..."
    python3 -m venv $VENV_DIR
fi

# Activar entorno
source $VENV_DIR/bin/activate

# Instalar dependencias
echo "📦 Instalando dependencias desde requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Entorno listo y dependencias instaladas."
echo "👉 Ejecutá tu script con: source $VENV_DIR/bin/activate && python main.py <archivo>"
