# ============================================================================
# Script de Configuración e Instalación - Universidad API Flask
# ============================================================================
# Este script automatiza toda la configuración de la aplicación
# Uso: .\_setup.ps1
# ============================================================================

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                CONFIGURACIÓN INICIAL - UNIVERSIDAD API          ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# ============================================================================
# 1. CONFIGURAR POWERSHELL
# ============================================================================
Write-Host "📋 [1/5] Verificando permisos de PowerShell..." -ForegroundColor Yellow

$ExecutionPolicy = Get-ExecutionPolicy -Scope CurrentUser
if ($ExecutionPolicy -eq "RemoteSigned") {
    Write-Host "✅ Permisos ya configurados correctamente`n" -ForegroundColor Green
} else {
    Write-Host "⚙️  Configurando permisos..." -ForegroundColor Yellow
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Write-Host "✅ Permisos configurados (RemoteSigned)`n" -ForegroundColor Green
}

# ============================================================================
# 2. CREAR ENTORNO VIRTUAL
# ============================================================================
Write-Host "📋 [2/5] Creando entorno virtual (.venv)..." -ForegroundColor Yellow

if (Test-Path ".\.venv") {
    Write-Host "✅ Entorno virtual ya existe`n" -ForegroundColor Green
} else {
    python -m venv .venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Entorno virtual creado exitosamente`n" -ForegroundColor Green
    } else {
        Write-Host "❌ Error creando entorno virtual" -ForegroundColor Red
        exit 1
    }
}

# ============================================================================
# 3. ACTIVAR ENTORNO VIRTUAL
# ============================================================================
Write-Host "📋 [3/5] Activando entorno virtual..." -ForegroundColor Yellow

& .\.venv\Scripts\Activate.ps1
Write-Host "✅ Entorno virtual activado`n" -ForegroundColor Green

# ============================================================================
# 4. INSTALAR DEPENDENCIAS
# ============================================================================
Write-Host "📋 [4/5] Instalando dependencias de PyPI..." -ForegroundColor Yellow

python -m pip install --upgrade pip -q
pip install -r requirements.txt -q

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencias instaladas exitosamente`n" -ForegroundColor Green
} else {
    Write-Host "❌ Error instalando dependencias" -ForegroundColor Red
    exit 1
}

# ============================================================================
# 5. INFORMACIÓN FINAL
# ============================================================================
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║              ✅ CONFIGURACIÓN COMPLETADA EXITOSAMENTE          ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

Write-Host "📌 PRÓXIMOS PASOS:" -ForegroundColor Green
Write-Host "   1. Ejecutar la aplicación: ( python run.py )`n" -ForegroundColor White

Write-Host "🌐 ENLACES ÚTILES:" -ForegroundColor Green
Write-Host "   • API Principal:  http://127.0.0.1:5000/api" -ForegroundColor Cyan
Write-Host "   • Health Check:   http://127.0.0.1:5000/api/health" -ForegroundColor Cyan
Write-Host "   • Estudiantes:    http://127.0.0.1:5000/api/estudiantes" -ForegroundColor Cyan
Write-Host "   • Materias:       http://127.0.0.1:5000/api/materias`n" -ForegroundColor Cyan

Write-Host "📚 MÁS INFORMACIÓN:" -ForegroundColor Green
Write-Host "   Consulta README.md para documentación completa`n" -ForegroundColor White
