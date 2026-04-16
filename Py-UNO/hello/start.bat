@echo off
REM Script para iniciar la aplicación Flask
cd /d "%~dp0"

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║        INICIANDO UNIVERSIDAD API - FLASK                       ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Activar entorno virtual
call .venv\Scripts\activate.bat

echo 🚀 Iniciando servidor Flask...
echo.
echo URLs disponibles:
echo   - Principal:  http://127.0.0.1:5000
echo   - Health:     http://127.0.0.1:5000/api/health
echo   - Estudiantes: http://127.0.0.1:5000/api/estudiantes
echo   - Materias:   http://127.0.0.1:5000/api/materias
echo.
echo ✋ Presiona CTRL+C para detener el servidor
echo.

REM Ejecutar la aplicación
python run.py
