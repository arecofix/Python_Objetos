"""
Decoradores para la aplicación.

Decoradores reutilizables para manejo de validaciones,
autenticación y otras funcionalidades transversales.
"""

from functools import wraps
from flask import request, jsonify


def validate_json(f):
    """
    Decorador para validar que la solicitud contiene JSON válido.
    
    Args:
        f: Función a decorar
        
    Returns:
        function: Función decorada
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method in ['POST', 'PUT', 'PATCH']:
            if not request.is_json:
                return jsonify({
                    'status': 'error',
                    'message': 'Content-Type debe ser application/json'
                }), 400
        return f(*args, **kwargs)
    return decorated_function


def require_auth(f):
    """
    Decorador para requerir autenticación.
    
    Args:
        f: Función a decorar
        
    Returns:
        function: Función decorada
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({
                'status': 'error',
                'message': 'Autenticación requerida'
            }), 401
        return f(*args, **kwargs)
    return decorated_function
