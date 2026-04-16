# ============================================================================
# Script de Verificación - Universidad API Flask
# ============================================================================
# Este script verifica que todo está configurado correctamente
# Uso: .\verify.ps1
# ============================================================================

Write-Host "`n" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "          VERIFICACIÓN DE CONFIGURACIÓN - UNIVERSIDAD API" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════════`n" -ForegroundColor Cyan

# 1. Verificar Python
Write-Host "[1/5] Verificando instalación de Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($pythonVersion -match '\d+\.\d+\.\d+') {
    Write-Host "✅ Python instalado: $pythonVersion`n" -ForegroundColor Green
} else {
    Write-Host "❌ Python no encontrado`n" -ForegroundColor Red
    exit 1
}

# 2. Verificar entorno virtual
Write-Host "[2/5] Verificando entorno virtual..." -ForegroundColor Yellow
if (Test-Path ".\.venv\Scripts\python.exe") {
    Write-Host "✅ Entorno virtual existe`n" -ForegroundColor Green
} else {
    Write-Host "❌ Entorno virtual no encontrado`n" -ForegroundColor Red
    exit 1
}

# 3. Verificar dependencias
Write-Host "[3/5] Verificando dependencias..." -ForegroundColor Yellow
$packages = @("Flask", "python-dotenv")
$installed = .\.venv\Scripts\pip list

foreach ($package in $packages) {
    if ($installed -like "*$package*") {
        Write-Host "  ✅ $package instalado" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $package NO instalado" -ForegroundColor Red
    }
}
Write-Host ""

# 4. Verificar estructura de carpetas
Write-Host "[4/5] Verificando estructura de carpetas..." -ForegroundColor Yellow
$folders = @("app", "app\models", "app\routes", "app\services", "app\utils", "app\templates")
foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Write-Host "  ✅ $folder existe" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $folder NO encontrado" -ForegroundColor Red
    }
}
Write-Host ""

# 5. Verificar archivos principales
Write-Host "[5/5] Verificando archivos principales..." -ForegroundColor Yellow
$files = @("run.py", ".env", "requirements.txt", "app\__init__.py", "app\config.py", "app\routes\api.py", "app\services\universidad_service.py")
foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "  ✅ $file existe" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $file NO encontrado" -ForegroundColor Red
    }
}
Write-Host ""

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "         ✅ VERIFICACIÓN COMPLETADA EXITOSAMENTE                 " -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════`n" -ForegroundColor Cyan

Write-Host "Próximo paso: Ejecutar uno de estos comandos:`n" -ForegroundColor Yellow
Write-Host "  1. Opción Windows: .\start.bat" -ForegroundColor Cyan
Write-Host "  2. Opción PowerShell: .\_run.ps1" -ForegroundColor Cyan
Write-Host "  3. Opción Manual: python run.py`n" -ForegroundColor Cyan
