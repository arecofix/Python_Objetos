"""
Configuración de la aplicación Flask.

Este módulo gestiona la configuración de la aplicación
según el ambiente (desarrollo, producción, pruebas).
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


class Config:
    """Configuración base para la aplicación."""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    TESTING = False
    
    # Información de la aplicación
    APP_NAME = 'Universidad API'
    APP_VERSION = '1.0.0'
    
    # Configuración de sesión
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hora


class DevelopmentConfig(Config):
    """Configuración para ambiente de desarrollo."""
    
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Configuración para ambiente de producción."""
    
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Configuración para ambiente de pruebas."""
    
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


# Seleccionar configuración según el ambiente
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
