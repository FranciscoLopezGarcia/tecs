#!/bin/bash

set -e  # Salir si hay error

echo "Creando entorno virtual..."
python3 -m venv venv

echo "Activando entorno virtual e instalando dependencias..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Listo! Para activar el entorno más tarde ejecutá:"
echo "source venv/bin/activate"
