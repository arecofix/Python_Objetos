"""
Rutas principales de la aplicación.

Endpoints iniciales de bienvenida.
"""

from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    """
    Página principal de bienvenida.
    
    Returns:
        dict: Mensaje de bienvenida
    """
    return jsonify({
        'message': 'Hola Mundo',
        'status': 'success'
    }), 200


@main_bp.route('/api', methods=['GET'])
def api_info():
    """
    Información de la API.
    
    Returns:
        dict: Información de bienvenida del API
    """
    return jsonify({
        'message': 'Bienvenido a Universidad API',
        'version': '1.0.0',
        'status': 'success',
        'endpoints': {
            'health': '/api/health',
            'estudiantes': '/api/estudiantes',
            'materias': '/api/materias'
        }
    }), 200
