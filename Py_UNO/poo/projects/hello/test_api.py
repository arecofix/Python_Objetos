"""
Test de endpoints de la aplicación Flask.

Este script prueba todos los endpoints de la API.
Requisito: Tener la aplicación ejecutándose en http://127.0.0.1:5000
"""

import urllib.request
import urllib.error
import json
import time

# Colores para terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def test_api():
    """Ejecuta todas las pruebas de los endpoints."""
    
    base_url = "http://127.0.0.1:5000"
    
    print(f"\n{BLUE}╔════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BLUE}║         PRUEBAS DE LA APLICACIÓN UNIVERSIDAD API               ║{RESET}")
    print(f"{BLUE}╚════════════════════════════════════════════════════════════════╝{RESET}\n")
    
    # 1. Prueba de Health Check
    print(f"{YELLOW}[1/6] Prueba de Health Check...{RESET}")
    try:
        response = urllib.request.urlopen(f"{base_url}/api/health")
        data = json.loads(response.read().decode())
        print(f"{GREEN}✅ Health Check OK{RESET}")
        print(f"   Estado: {data['status']}")
        print(f"   Versión: {data['version']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    # 2. Crear estudiante
    print(f"{YELLOW}[2/6] Creando estudiante...{RESET}")
    try:
        data = {
            "nombre": "Juan Pérez",
            "email": "juan@example.com",
            "carrera": "Ingeniería Informática"
        }
        req = urllib.request.Request(
            f"{base_url}/api/estudiantes",
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        estudiante_id = result['data']['id']
        print(f"{GREEN}✅ Estudiante creado{RESET}")
        print(f"   ID: {estudiante_id}")
        print(f"   Nombre: {result['data']['nombre']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    # 3. Obtener todos los estudiantes
    print(f"{YELLOW}[3/6] Obteniendo estudiantes...{RESET}")
    try:
        response = urllib.request.urlopen(f"{base_url}/api/estudiantes")
        data = json.loads(response.read().decode())
        print(f"{GREEN}✅ Estudiantes obtenidos{RESET}")
        print(f"   Total: {data['total']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    # 4. Crear materia
    print(f"{YELLOW}[4/6] Creando materia...{RESET}")
    try:
        data = {
            "nombre": "Python Avanzado",
            "profesor": "Dr. Gonzalez",
            "creditos": 4
        }
        req = urllib.request.Request(
            f"{base_url}/api/materias",
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        materia_id = result['data']['id']
        print(f"{GREEN}✅ Materia creada{RESET}")
        print(f"   ID: {materia_id}")
        print(f"   Nombre: {result['data']['nombre']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    # 5. Obtener todas las materias
    print(f"{YELLOW}[5/6] Obteniendo materias...{RESET}")
    try:
        response = urllib.request.urlopen(f"{base_url}/api/materias")
        data = json.loads(response.read().decode())
        print(f"{GREEN}✅ Materias obtenidas{RESET}")
        print(f"   Total: {data['total']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    # 6. Obtener un estudiante específico
    print(f"{YELLOW}[6/6] Obteniendo estudiante específico...{RESET}")
    try:
        response = urllib.request.urlopen(f"{base_url}/api/estudiantes/{estudiante_id}")
        data = json.loads(response.read().decode())
        print(f"{GREEN}✅ Estudiante obtenido{RESET}")
        print(f"   Nombre: {data['data']['nombre']}")
        print(f"   Email: {data['data']['email']}\n")
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}\n")
        return
    
    print(f"{BLUE}╔════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║            ✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE      ║{RESET}")
    print(f"{BLUE}╚════════════════════════════════════════════════════════════════╝{RESET}\n")


if __name__ == "__main__":
    print(f"\n{YELLOW}Esperando 2 segundos para asegurar que el servidor esté listo...{RESET}")
    time.sleep(2)
    test_api()
