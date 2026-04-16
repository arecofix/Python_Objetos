"""
Rutas API de la aplicación.

Endpoints para gestionar estudiantes y materias.
"""

from flask import Blueprint, request, jsonify
from app.services.universidad_service import EstudianteService, MateriaService
from app.utils.decorators import validate_json

api_bp = Blueprint('api', __name__, url_prefix='/api')


# ============================================================================
# Rutas para Estudiantes
# ============================================================================

@api_bp.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    """
    Obtiene todos los estudiantes.
    
    Returns:
        dict: Lista de estudiantes
    """
    estudiantes = EstudianteService.obtener_todos_estudiantes()
    return jsonify({
        'status': 'success',
        'data': [est.to_dict() for est in estudiantes],
        'total': len(estudiantes)
    }), 200


@api_bp.route('/estudiantes/<id_estudiante>', methods=['GET'])
def obtener_estudiante(id_estudiante):
    """
    Obtiene un estudiante específico.
    
    Args:
        id_estudiante (str): ID del estudiante
        
    Returns:
        dict: Datos del estudiante
    """
    estudiante = EstudianteService.obtener_estudiante(id_estudiante)
    if not estudiante:
        return jsonify({
            'status': 'error',
            'message': 'Estudiante no encontrado'
        }), 404
    
    return jsonify({
        'status': 'success',
        'data': estudiante.to_dict()
    }), 200


@api_bp.route('/estudiantes', methods=['POST'])
@validate_json
def crear_estudiante():
    """
    Crea un nuevo estudiante.
    
    Returns:
        dict: Datos del estudiante creado
    """
    data = request.get_json()
    
    # Validar campos requeridos
    campos_requeridos = ['nombre', 'email', 'carrera']
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({
            'status': 'error',
            'message': f'Campos requeridos: {", ".join(campos_requeridos)}'
        }), 400
    
    estudiante = EstudianteService.crear_estudiante(
        nombre=data['nombre'],
        email=data['email'],
        carrera=data['carrera']
    )
    
    return jsonify({
        'status': 'success',
        'message': 'Estudiante creado exitosamente',
        'data': estudiante.to_dict()
    }), 201


@api_bp.route('/estudiantes/<id_estudiante>', methods=['PUT'])
@validate_json
def actualizar_estudiante(id_estudiante):
    """
    Actualiza un estudiante existente.
    
    Args:
        id_estudiante (str): ID del estudiante
        
    Returns:
        dict: Datos del estudiante actualizado
    """
    data = request.get_json()
    
    estudiante = EstudianteService.actualizar_estudiante(
        id_estudiante=id_estudiante,
        nombre=data.get('nombre'),
        email=data.get('email'),
        carrera=data.get('carrera')
    )
    
    if not estudiante:
        return jsonify({
            'status': 'error',
            'message': 'Estudiante no encontrado'
        }), 404
    
    return jsonify({
        'status': 'success',
        'message': 'Estudiante actualizado exitosamente',
        'data': estudiante.to_dict()
    }), 200


@api_bp.route('/estudiantes/<id_estudiante>', methods=['DELETE'])
def eliminar_estudiante(id_estudiante):
    """
    Elimina un estudiante.
    
    Args:
        id_estudiante (str): ID del estudiante
        
    Returns:
        dict: Confirmación de eliminación
    """
    if EstudianteService.eliminar_estudiante(id_estudiante):
        return jsonify({
            'status': 'success',
            'message': 'Estudiante eliminado exitosamente'
        }), 200
    
    return jsonify({
        'status': 'error',
        'message': 'Estudiante no encontrado'
    }), 404


# ============================================================================
# Rutas para Materias
# ============================================================================

@api_bp.route('/materias', methods=['GET'])
def obtener_materias():
    """
    Obtiene todas las materias.
    
    Returns:
        dict: Lista de materias
    """
    materias = MateriaService.obtener_todas_materias()
    return jsonify({
        'status': 'success',
        'data': [mat.to_dict() for mat in materias],
        'total': len(materias)
    }), 200


@api_bp.route('/materias/<id_materia>', methods=['GET'])
def obtener_materia(id_materia):
    """
    Obtiene una materia específica.
    
    Args:
        id_materia (str): ID de la materia
        
    Returns:
        dict: Datos de la materia
    """
    materia = MateriaService.obtener_materia(id_materia)
    if not materia:
        return jsonify({
            'status': 'error',
            'message': 'Materia no encontrada'
        }), 404
    
    return jsonify({
        'status': 'success',
        'data': materia.to_dict()
    }), 200


@api_bp.route('/materias', methods=['POST'])
@validate_json
def crear_materia():
    """
    Crea una nueva materia.
    
    Returns:
        dict: Datos de la materia creada
    """
    data = request.get_json()
    
    # Validar campos requeridos
    campos_requeridos = ['nombre', 'profesor', 'creditos']
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({
            'status': 'error',
            'message': f'Campos requeridos: {", ".join(campos_requeridos)}'
        }), 400
    
    materia = MateriaService.crear_materia(
        nombre=data['nombre'],
        profesor=data['profesor'],
        creditos=data['creditos']
    )
    
    return jsonify({
        'status': 'success',
        'message': 'Materia creada exitosamente',
        'data': materia.to_dict()
    }), 201
