# ============================================================================
# Script de Ejecución - Universidad API Flask
# ============================================================================
# Este script inicia la aplicación Flask en modo desarrollo
# Uso: .\_run.ps1
# ============================================================================

Write-Host "`n" -ForegroundColor Cyan
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║           🎓 UNIVERSIDAD API - FLASK - INICIANDO              ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# Activar entorno virtual
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    Write-Host "🔌 Activando entorno virtual..." -ForegroundColor Yellow
    & .\.venv\Scripts\Activate.ps1
    Write-Host "✅ Entorno virtual activado`n" -ForegroundColor Green
} else {
    Write-Host "❌ Entorno virtual no encontrado" -ForegroundColor Red
    Write-Host "Ejecuta primero: ._setup.ps1" -ForegroundColor Yellow
    exit 1
}

Write-Host "🚀 Iniciando aplicación en modo desarrollo...`n" -ForegroundColor Green

Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                    ENLACES DISPONIBLES                         ║" -ForegroundColor Cyan
Write-Host "╠════════════════════════════════════════════════════════════════╣" -ForegroundColor Cyan
Write-Host "║ 📌 API Principal:    http://127.0.0.1:5000/api                 ║" -ForegroundColor White
Write-Host "║ 🔍 Health Check:     http://127.0.0.1:5000/api/health          ║" -ForegroundColor White
Write-Host "║ 👥 Estudiantes:      http://127.0.0.1:5000/api/estudiantes     ║" -ForegroundColor White
Write-Host "║ 📚 Materias:         http://127.0.0.1:5000/api/materias        ║" -ForegroundColor White
Write-Host "╠════════════════════════════════════════════════════════════════╣" -ForegroundColor Cyan
Write-Host "║ ✋ Presiona CTRL+C para detener el servidor                    ║" -ForegroundColor Yellow
Write-Host "║ 📖 Documentación: Lee README.md o INICIO_RAPIDO.md             ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# Ejecutar la aplicación
& .\.venv\Scripts\python.exe run.py
