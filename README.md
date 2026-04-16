# 🔧 Arecofix Local-Engine

Un motor de gestión robusto para servicios técnicos y e-commerce con arquitectura **Offline-First / Local-First**. 

---

## 🏛️ Descripción del Proyecto
`local-engine` es el núcleo de gestión para **Arecofix**, diseñado para operar de manera autónoma sin conexión a internet mediante una arquitectura híbrida:
- **Operación Local:** Almacenamiento y procesamiento en el equipo del usuario (SQLite).
- **Sincronización Inteligente:** Detección de conectividad para sincronización de datos con la nube (**Supabase/PostgreSQL**).

Este repositorio también sirve como entorno académico para la carrera de **Licenciatura en Informática**, implementando las mejores prácticas de la industria y patrones de diseño de vanguardia.

---

## 🚀 Stack Tecnológico
- **Back-end:** [Python 3.x](https://www.python.org/), [Flask](https://flask.palletsprojects.com/) (REST API), [SQLAlchemy](https://www.sqlalchemy.org/) (ORM).
- **Motor Local:** [SQLite](https://www.sqlite.org/).
- **Front-end / Desktop:** [Angular](https://angular.io/) empaquetado con [Tauri](https://tauri.app/) (para generar ejecutables nativos `.exe`).
- **Nube:** [Supabase](https://supabase.com/) (PostgreSQL).

---

## 📂 Estructura del Repositorio
- **/Back-end:** Lógica central en Python (POO), base de datos local y API de comunicación.
- **/Front-end:** Interfaz de usuario en Angular y configuración de Tauri para despliegue de escritorio.
- **/Py_UNO:** Espacio de colaboración para trabajos prácticos universitarios (enfoque académico-educativo).

---

## 🛠️ Guía de Instalación Rápida

### 1. Back-end (Python & Flask)
Para configurar el entorno local:
```bash
cd Back-end
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
pip install flask flask-sqlalchemy
python app.py
```

### 2. Front-end (Angular & Tauri)
Requiere Node.js y Rust (para Tauri):
```bash
cd Front-end
npm install
npm install @tauri-apps/api @tauri-apps/cli
# Ejecutar en modo desarrollo
npm run tauri dev
```

### 3. Universidad (Py_UNO)
Entorno para prácticas grupales y colaborativas:
```bash
cd Py_UNO
# Consultar instrucciones específicas de los trabajos prácticos.
```

---

## 📊 Arquitectura de Datos & Patrones
El proyecto se basa en los principios de **Clean Architecture** y **Programación Orientada a Objetos (POO)**:
- **Persistencia:** Implementamos el patrón Repository para abstraer la fuente de datos (Local vs Remote).
- **Escalabilidad:** Separación de responsabilidades entre el core de negocio y los servicios de infraestructura.
- **Modelado:** Uso de modelos robustos que representan fielmente las entidades de negocio.

---

*Desarrollado por [Ezequiel] como parte de Arecofix y formación académica.*
