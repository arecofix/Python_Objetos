# 🎓 Universidad API - Flask con Clean Architecture

## ✅ Estado del Proyecto

Tu proyecto Flask ha sido **configurado completamente** con todas las mejores prácticas:

- ✅ **Clean Code**: Código legible, bien documentado y mantenible
- ✅ **Clean Architecture**: Separación clara de responsabilidades
- ✅ **Escalable**: Estructura lista para crecer sin refactorización
- ✅ **Ágil**: Fácil de modificar y extender
- ✅ **Optimizado**: Configuración y dependencias minimalistas

---

## 🚀 Cómo Iniciar la Aplicación

### Opción 1: Script Automático (Recomendado)
```powershell
# Ejecutar en PowerShell
.\start.bat
```

### Opción 2: Manualmente
```powershell
# 1. Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# 2. Ejecutar la aplicación
python run.py
```

### Opción 3: Script PowerShell
```powershell
.\_run.ps1
```

---

## 🌐 URLs de la Aplicación

Una vez ejecutada, accede a:

| Recurso | URL |
|---------|-----|
| **Health Check** | http://127.0.0.1:5000/api/health |
| **Todos los Estudiantes** | http://127.0.0.1:5000/api/estudiantes |
| **Todas las Materias** | http://127.0.0.1:5000/api/materias |

---

## 📋 Ejemplos de Uso (PowerShell/curl)

### Crear un Estudiante
```powershell
$body = @{
    nombre = "María García"
    email = "maria@example.com"
    carrera = "Ingeniería Informática"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/estudiantes" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

### Obtener Todos los Estudiantes
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/estudiantes" | Select-Object -ExpandProperty Content
```

### Crear una Materia
```powershell
$body = @{
    nombre = "Bases de Datos"
    profesor = "Ing. López"
    creditos = 3
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/materias" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

---

## 📁 Estructura del Proyecto

```
poo/
├── app/                           # Código principal
│   ├── __init__.py               # Factory de la aplicación
│   ├── config.py                 # Configuración por ambiente
│   ├── models/                   # Entidades del negocio
│   │   └── estudiante.py
│   ├── routes/                   # Endpoints del API
│   │   ├── health.py
│   │   └── api.py
│   ├── services/                 # Lógica de negocio
│   │   └── universidad_service.py
│   ├── utils/                    # Funcionalidades transversales
│   │   └── decorators.py
│   └── templates/                # Plantillas HTML
├── .venv/                        # Entorno virtual (no commitar)
├── .env                          # Variables de entorno
├── .gitignore                    # Archivos a ignorar
├── requirements.txt              # Dependencias
├── run.py                        # Punto de entrada
├── start.bat                     # Script para iniciar (Windows)
├── test_api.py                   # Pruebas de endpoints
├── _run.ps1                      # Script PowerShell
├── _setup.ps1                    # Script de configuración
└── README.md                     # Documentación
```

---

## 🏗️ Arquitectura Implementada

### Capas de la Aplicación

```
┌─────────────────────────────────────┐
│      ROUTES (API/HTTP Layer)        │  ← Recibe requests
├─────────────────────────────────────┤
│      SERVICES (Business Logic)      │  ← Procesa datos
├─────────────────────────────────────┤
│         MODELS (Data Layer)         │  ← Define entidades
├─────────────────────────────────────┤
│       CONFIG & UTILS (Support)      │  ← Funciones auxiliares
└─────────────────────────────────────┘
```

### Principios Aplicados

1. **Separación de Responsabilidades**
   - Routes: Manejo de HTTP
   - Services: Lógica de negocio
   - Models: Estructuras de datos

2. **DRY (Don't Repeat Yourself)**
   - Decoradores reutilizables
   - Servicios centralizados

3. **SOLID**
   - Single Responsibility: Cada clase tiene un propósito
   - Open/Closed: Extensible sin modificar código existente

4. **Configuración por Ambiente**
   - Development, Production, Testing

---

## 🔧 Variables de Entorno

El archivo `.env` contiene:

```
FLASK_APP=run.py
FLASK_ENV=development        # Cambiar a 'production' si es necesario
FLASK_DEBUG=True             # Cambiar a False en producción
SECRET_KEY=your-secret-key   # ⚠️ Cambiar en producción
```

---

## 📚 Endpoints API Detallados

### Health Check
```
GET /api/health
Response: { "status": "healthy", "version": "1.0.0" }
```

### Estudiantes

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/estudiantes` | Obtener todos |
| GET | `/api/estudiantes/{id}` | Obtener uno |
| POST | `/api/estudiantes` | Crear nuevo |
| PUT | `/api/estudiantes/{id}` | Actualizar |
| DELETE | `/api/estudiantes/{id}` | Eliminar |

**Body para POST:**
```json
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "carrera": "Ingeniería Informática"
}
```

### Materias

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/materias` | Obtener todas |
| GET | `/api/materias/{id}` | Obtener una |
| POST | `/api/materias` | Crear nueva |

**Body para POST:**
```json
{
  "nombre": "Python Avanzado",
  "profesor": "Dr. Gonzalez",
  "creditos": 4
}
```

---

## 🆘 Solución de Problemas

### ❌ "Módulo app no encontrado"
```powershell
# Verifica que estés en el directorio correcto
cd c:\Users\Ezequiel\Desktop\Utilidades\Universidad\poo
```

### ❌ Puerto 5000 en uso
```powershell
# Cambiar puerto en run.py (última línea)
app.run(host='127.0.0.1', port=5001, debug=True)
```

### ❌ Entorno virtual no activado
```powershell
.\.venv\Scripts\Activate.ps1
# Deberías ver (.venv) al inicio del prompt
```

---

## 📦 Próximos Pasos (Escalabilidad)

Para convertir esto en una aplicación de producción:

1. **Base de Datos Real**
   ```bash
   pip install SQLAlchemy flask-sqlalchemy postgresql
   ```

2. **Validación de Datos**
   ```bash
   pip install Marshmallow flask-marshmallow
   ```

3. **Autenticación**
   ```bash
   pip install flask-jwt-extended
   ```

4. **Testing**
   ```bash
   pip install pytest pytest-flask
   ```

5. **Logging**
   - Configurar Python logging
   - Usar herramientas como Sentry

6. **API Documentation**
   ```bash
   pip install flasgger
   ```

7. **Docker**
   - Crear `Dockerfile` y `docker-compose.yml`

8. **CI/CD**
   - GitHub Actions
   - Deploy a Heroku, AWS, etc.

---

## 🎯 Características de Clean Code Implementadas

- ✅ **Nombres Descriptivos**: Variables y funciones claras
- ✅ **Funciones Pequeñas**: Una única responsabilidad
- ✅ **Docstrings**: Documentación en cada función
- ✅ **DRY**: Reutilización de código
- ✅ **Manejo de Errores**: Centralizado y consistente
- ✅ **Logging**: Fácil de debuggear

---

## 💡 Tips Importantes

1. **Activar siempre el entorno virtual** antes de trabajar
2. **No commitar** la carpeta `.venv`
3. **Cambiar SECRET_KEY** antes de producción
4. **Usar variables de entorno** para datos sensibles
5. **Código siempre documentado** con docstrings

---

## 📞 Soporte

Toda la documentación está en los archivos:
- `README.md` - Documentación técnica
- Comentarios en el código - Explicaciones detalladas

---

**¡Tu aplicación está lista para usarse! 🚀**

Ejecuta `python run.py` y accede a http://127.0.0.1:5000/api/health
