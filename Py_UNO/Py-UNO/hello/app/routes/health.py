"""
Rutas de salud de la aplicación.

Endpoints para verificar el estado de la aplicación.
"""

from flask import Blueprint, jsonify
from app.config import Config

health_bp = Blueprint('health', __name__, url_prefix='/api/health')


@health_bp.route('/', methods=['GET'])
def health_check():
    """
    Verifica el estado de la aplicación.
    
    Returns:
        dict: Estado de la aplicación
    """
    return jsonify({
        'status': 'healthy',
        'app_name': Config.APP_NAME,
        'version': Config.APP_VERSION,
        'environment': 'development'
    }), 200
