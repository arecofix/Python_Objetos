"""
Aplicación Flask con Clean Architecture.

Este módulo inicializa la aplicación Flask con configuraciones
y registro de blueprints de forma escalable y mantenible.
"""

from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    """
    Factory function para crear y configurar la aplicación Flask.
    
    Args:
        config_class: Clase de configuración a utilizar (default: Config)
        
    Returns:
        Flask: Instancia configurada de la aplicación Flask
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Registrar blueprints
    register_blueprints(app)
    
    # Registrar manejadores de errores
    register_error_handlers(app)
    
    return app


def register_blueprints(app):
    """
    Registra todos los blueprints de la aplicación.
    
    Args:
        app: Instancia de la aplicación Flask
    """
    from app.routes.main import main_bp
    from app.routes.health import health_bp
    from app.routes.api import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(api_bp)


def register_error_handlers(app):
    """
    Registra manejadores de errores globales.
    
    Args:
        app: Instancia de la aplicación Flask
    """
    
    @app.errorhandler(404)
    def not_found(error):
        """Manejo de error 404."""
        return {
            'status': 'error',
            'message': 'Recurso no encontrado',
            'code': 404
        }, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Manejo de error 500."""
        return {
            'status': 'error',
            'message': 'Error interno del servidor',
            'code': 500
        }, 500
