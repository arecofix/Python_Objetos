import os
class persona:
    def __init__ (self,nombre,id,dni):
      self.__nombre = nombre
      self.__identificaciones = id
      self.__dni = dni

    def tarea(self):
      pass

class director (persona):

    @property
    def nombre (self):
      return self.__nombre
    @nombre.setter
    def nombre (self,nuevo):
      self.__nombre = nuevo
    @property
    def identificaciones(self):
      return self.__identificaciones
    @identificaciones.setter
    def identificaciones(self,nuevo):
       self.__identificaciones = nuevo
