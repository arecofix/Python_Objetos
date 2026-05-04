# Aplicación Flask - Universidad API"""

















































































































































**Creado con ❤️ usando Flask**---4. Reinicia Visual Studio Code si cambias el entorno3. Comprueba que el puerto 5000 esté disponible2. Asegúrate de instalar requirements.txt1. Verifica que el entorno virtual esté activado (`(.venv)` visible)Si tienes problemas:## Ayuda- [ ] Logging avanzado- [ ] Docker para deployment- [ ] Documentación con Swagger- [ ] Testing unitario con Pytest- [ ] Validación con Marshmallow- [ ] Autenticación con JWT- [ ] Integrar base de datos real## Próximas Mejoras```FLASK_DEBUG=FalseFLASK_ENV=production```Para cambiar el modo a producción, modifica la variable `FLASK_ENV` en `.env`:## Cambiar a Producción```└── README.md            # Este archivo├── run.py               # Punto de entrada├── requirements.txt     # Dependencias├── .env                 # Variables de entorno├── .venv/               # Entorno virtual│   └── config.py        # Configuración│   ├── __init__.py      # Factory de la app│   ├── templates/       # Plantillas HTML│   ├── utils/           # Utilidades y decoradores│   ├── services/        # Lógica de negocio│   ├── routes/          # Endpoints del API│   ├── models/          # Entidades del negocio├── app/poo/```## Estructura de Carpetas```curl http://127.0.0.1:5000/api/health# Verificar salud de la appcurl http://127.0.0.1:5000/api/estudiantes# Obtener estudiantes  -d '{"nombre":"Juan","email":"juan@example.com","carrera":"Informática"}'  -H "Content-Type: application/json" `curl -X POST http://127.0.0.1:5000/api/estudiantes `# Crear estudiante```powershell## Ejemplo de uso con curl```POST /api/materias         # CrearGET  /api/materias/<id>    # Obtener unaGET  /api/materias         # Obtener todas```### Materias```DELETE /api/estudiantes/<id>      # EliminarPUT    /api/estudiantes/<id>      # ActualizarPOST   /api/estudiantes           # CrearGET    /api/estudiantes/<id>      # Obtener unoGET    /api/estudiantes           # Obtener todos```### Estudiantes```GET /api/health```### Verificar Estado## Endpoints DisponiblesLa aplicación estará disponible en: **http://127.0.0.1:5000**```python run.py```powershell### 5. Ejecutar la aplicación```pip install -r requirements.txt```powershell### 4. Instalar dependenciasDeberías ver `(.venv)` al inicio de tu terminal.```.\.venv\Scripts\Activate.ps1```powershell### 3. Activar entorno virtual```python -m venv .venv```powershell### 2. Crear entorno virtualConfirmar con `Y` y presionar Enter.```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```powershell### 1. PowerShell - Ejecutar scripts## Instalación y Configuración- PowerShell (en Windows)- pip- Python 3.8+## Requisitos- 🛡️ **Manejo de errores**: Centralizado y consistente- 📚 **Documentado**: Docstrings completos- 🚀 **Escalable**: Estructura lista para crecer- 🔧 **Configuración por ambiente**: Desarrollo, producción, testing- 📡 **API RESTful**: Endpoints bien estructurados- 🧹 **Clean Code**: Código legible y mantenible- 🏗️ **Clean Architecture**: Separación clara de responsabilidades## CaracterísticasUna aplicación Flask moderna con arquitectura limpia, siguiendo Clean Code y Clean Architecture.Documentación del Proyecto Flask con Clean Architecture.

## Estructura del Proyecto

```
poo/
├── app/
│   ├── __init__.py           # Factory de la aplicación
│   ├── config.py             # Configuración de la app
│   ├── models/
│   │   ├── __init__.py
│   │   └── estudiante.py     # Modelos de datos
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py         # Rutas de verificación
│   │   └── api.py            # Rutas principales del API
│   ├── services/
│   │   ├── __init__.py
│   │   └── universidad_service.py  # Lógica de negocio
│   ├── utils/
│   │   ├── __init__.py
│   │   └── decorators.py     # Decoradores reutilizables
│   └── templates/
│       ├── base.html
│       └── index.html
├── .venv/                    # Entorno virtual
├── .env                      # Variables de entorno
├── .gitignore                # Archivo git ignore
├── requirements.txt          # Dependencias del proyecto
├── run.py                    # Punto de entrada
└── README.md                 # Este archivo
```

## Principios de Arquitectura

### Clean Code
- ✅ Nombres descriptivos para funciones y variables
- ✅ Funciones pequeñas y enfocadas en una sola responsabilidad
- ✅ Docstrings completos para cada función
- ✅ Decoradores para reutilizar código

### Clean Architecture
- ✅ **Models**: Entidades del negocio
- ✅ **Services**: Lógica de negocio aislada
- ✅ **Routes**: Puntos de entrada del API
- ✅ **Utils**: Funcionalidades transversales

### Características

- 🔒 Manejo de errores centralizado
- 📝 Logging y debugging
- 🔧 Configuración por ambiente
- 📦 Inyección de dependencias básica
- 🎯 API RESTful siguiendo convenciones
- 🧪 Preparado para testing

## Configuración

1. Crear entorno virtual
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar aplicación: `python run.py`

## API Endpoints

### Health Check
- `GET /api/health` - Verificar estado de la aplicación

### Estudiantes
- `GET /api/estudiantes` - Obtener todos los estudiantes
- `GET /api/estudiantes/<id>` - Obtener un estudiante
- `POST /api/estudiantes` - Crear nuevo estudiante
- `PUT /api/estudiantes/<id>` - Actualizar estudiante
- `DELETE /api/estudiantes/<id>` - Eliminar estudiante

### Materias
- `GET /api/materias` - Obtener todas las materias
- `GET /api/materias/<id>` - Obtener una materia
- `POST /api/materias` - Crear nueva materia

## Ejemplos de Uso

### Crear un estudiante
```bash
curl -X POST http://127.0.0.1:5000/api/estudiantes \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez",
    "email": "juan@email.com",
    "carrera": "Ingeniería Informática"
  }'
```

### Obtener todos los estudiantes
```bash
curl http://127.0.0.1:5000/api/estudiantes
```

### Crear una materia
```bash
curl -X POST http://127.0.0.1:5000/api/materias \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Python Avanzado",
    "profesor": "Dr. Gonzalez",
    "creditos": 4
  }'
```

## Próximos Pasos para Escalabilidad

Para convertir este proyecto en una aplicación de producción, considera:

1. **Base de datos**: Integrar SQLAlchemy/PostgreSQL
2. **Validación**: Usar Marshmallow o Pydantic
3. **Autenticación**: JWT con Flask-JWT-Extended
4. **Testing**: Pytest para pruebas unitarias
5. **Logging**: Python logging configurado
6. **CORS**: Flask-CORS para solicitudes inter-origen
7. **Documentación**: Swagger/OpenAPI
8. **CI/CD**: GitHub Actions o similar
9. **Docker**: Containerización
10. **Monitoreo**: Application insights

## Licencia

Este proyecto es con fines educativos.
"""
