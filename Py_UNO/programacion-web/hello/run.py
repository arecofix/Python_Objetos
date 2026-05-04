"""
Punto de entrada de la aplicación Flask.

Este script inicia la aplicación en modo desarrollo.
"""

import os
from app import create_app
from app.config import config_by_name

# Obtener configuración del ambiente
config_name = os.getenv('FLASK_ENV', 'development')
config_class = config_by_name.get(config_name, config_by_name['default'])

# Crear aplicación
app = create_app(config_class)


if __name__ == '__main__':
    """
    Punto de entrada principal de la aplicación.
    
    La aplicación se ejecuta en:
    - Host: 127.0.0.1 (localhost)
    - Puerto: 5000
    - Debug: Habilitado en desarrollo (auto-recarga)
    """
    print(f"\n{'='*60}")
    print(f"  Iniciando Universidad API")
    print(f"{'='*60}")
    print(f"  Ambiente: {config_name}")
    print(f"  URL: http://127.0.0.1:5000")
    print(f"  Health: http://127.0.0.1:5000/api/health")
    print(f"{'='*60}\n")
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
