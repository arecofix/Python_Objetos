"""
Servicios de la aplicación.

Los servicios contienen la lógica de negocio
de la aplicación, manteniendo las rutas limpias.
"""

from app.models.estudiante import Estudiante, Materia


class EstudianteService:
    """Servicio para gestionar estudiantes."""
    
    # Base de datos simulada en memoria
    _estudiantes = {}
    _contador = 0
    
    @classmethod
    def crear_estudiante(cls, nombre, email, carrera):
        """
        Crea un nuevo estudiante.
        
        Args:
            nombre (str): Nombre del estudiante
            email (str): Email del estudiante
            carrera (str): Carrera que cursa
            
        Returns:
            Estudiante: Instancia del estudiante creado
        """
        cls._contador += 1
        estudiante = Estudiante(
            id_estudiante=str(cls._contador),
            nombre=nombre,
            email=email,
            carrera=carrera
        )
        cls._estudiantes[str(cls._contador)] = estudiante
        return estudiante
    
    @classmethod
    def obtener_estudiante(cls, id_estudiante):
        """
        Obtiene un estudiante por ID.
        
        Args:
            id_estudiante (str): ID del estudiante
            
        Returns:
            Estudiante: El estudiante encontrado o None
        """
        return cls._estudiantes.get(id_estudiante)
    
    @classmethod
    def obtener_todos_estudiantes(cls):
        """
        Obtiene todos los estudiantes.
        
        Returns:
            list: Lista de todos los estudiantes
        """
        return list(cls._estudiantes.values())
    
    @classmethod
    def actualizar_estudiante(cls, id_estudiante, nombre=None, email=None, carrera=None):
        """
        Actualiza un estudiante existente.
        
        Args:
            id_estudiante (str): ID del estudiante
            nombre (str, optional): Nuevo nombre
            email (str, optional): Nuevo email
            carrera (str, optional): Nueva carrera
            
        Returns:
            Estudiante: El estudiante actualizado o None
        """
        estudiante = cls._estudiantes.get(id_estudiante)
        if not estudiante:
            return None
        
        if nombre:
            estudiante.nombre = nombre
        if email:
            estudiante.email = email
        if carrera:
            estudiante.carrera = carrera
        
        return estudiante
    
    @classmethod
    def eliminar_estudiante(cls, id_estudiante):
        """
        Elimina un estudiante.
        
        Args:
            id_estudiante (str): ID del estudiante
            
        Returns:
            bool: True si se eliminó, False si no existe
        """
        if id_estudiante in cls._estudiantes:
            del cls._estudiantes[id_estudiante]
            return True
        return False


class MateriaService:
    """Servicio para gestionar materias."""
    
    # Base de datos simulada en memoria
    _materias = {}
    _contador = 0
    
    @classmethod
    def crear_materia(cls, nombre, profesor, creditos):
        """
        Crea una nueva materia.
        
        Args:
            nombre (str): Nombre de la materia
            profesor (str): Nombre del profesor
            creditos (int): Número de créditos
            
        Returns:
            Materia: Instancia de la materia creada
        """
        cls._contador += 1
        materia = Materia(
            id_materia=str(cls._contador),
            nombre=nombre,
            profesor=profesor,
            creditos=creditos
        )
        cls._materias[str(cls._contador)] = materia
        return materia
    
    @classmethod
    def obtener_materia(cls, id_materia):
        """
        Obtiene una materia por ID.
        
        Args:
            id_materia (str): ID de la materia
            
        Returns:
            Materia: La materia encontrada o None
        """
        return cls._materias.get(id_materia)
    
    @classmethod
    def obtener_todas_materias(cls):
        """
        Obtiene todas las materias.
        
        Returns:
            list: Lista de todas las materias
        """
        return list(cls._materias.values())
