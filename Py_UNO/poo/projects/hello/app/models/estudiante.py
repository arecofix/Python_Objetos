"""
Modelos de datos para la aplicación.

Aquí se definen las clases que representan
las entidades del negocio.
"""


class Estudiante:
    """Modelo que representa un estudiante."""
    
    def __init__(self, id_estudiante, nombre, email, carrera):
        """
        Inicializa un estudiante.
        
        Args:
            id_estudiante (str): Identificador único del estudiante
            nombre (str): Nombre completo del estudiante
            email (str): Correo electrónico
            carrera (str): Carrera que cursa
        """
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.email = email
        self.carrera = carrera
    
    def to_dict(self):
        """
        Convierte el estudiante a diccionario.
        
        Returns:
            dict: Representación en diccionario del estudiante
        """
        return {
            'id': self.id_estudiante,
            'nombre': self.nombre,
            'email': self.email,
            'carrera': self.carrera
        }


class Materia:
    """Modelo que representa una materia."""
    
    def __init__(self, id_materia, nombre, profesor, creditos):
        """
        Inicializa una materia.
        
        Args:
            id_materia (str): Identificador único de la materia
            nombre (str): Nombre de la materia
            profesor (str): Nombre del profesor
            creditos (int): Número de créditos
        """
        self.id_materia = id_materia
        self.nombre = nombre
        self.profesor = profesor
        self.creditos = creditos
    
    def to_dict(self):
        """
        Convierte la materia a diccionario.
        
        Returns:
            dict: Representación en diccionario de la materia
        """
        return {
            'id': self.id_materia,
            'nombre': self.nombre,
            'profesor': self.profesor,
            'creditos': self.creditos
        }
