#!/bin/bash
# ============================================================================
# Script de Ejecución - Universidad API Flask
# ============================================================================
# Este script inicia la aplicación Flask en modo desarrollo
# Uso: ./run.sh
# ============================================================================

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              INICIANDO UNIVERSIDAD API - FLASK                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Activar entorno virtual
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✅ Entorno virtual activado"
else
    echo "❌ Entorno virtual no encontrado"
    echo "Ejecuta primero: python -m venv .venv"
    exit 1
fi

echo ""
echo "🚀 Iniciando aplicación en modo desarrollo..."
echo "📌 URL: http://127.0.0.1:5000"
echo "🔍 Health: http://127.0.0.1:5000/api/health"
echo ""

# Ejecutar la aplicación
python run.py
