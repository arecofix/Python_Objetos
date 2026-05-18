"""
class ObraEdificio
cada clase debera tener superficie a cimentar
superficie qu ya a sido cimentada m cuadrados sin decimales
precisamos los siguientes metodos: Constructor osea el __Init__
metodo cimentando es un metodo que recibe los metros cuadrados que se estan cimentando en ese momento
si la suma de la superficie previamente cimentada
resta por cimentar
terminado = bool osea si la superficie total fue cimentada

guardar superficie a cimetar y la que ya esta cimentada

"""

class ObraEdificio:
    def __init__(self, superficie_total):
        self.superficie_a_cimentar = superficie_total
        self.superficie_cimentada = 0
        self.terminada = False

        def __init__(self) -> None:
          if self.__superficie_a_cimentar <= self.__superficie_cimentada:
            raise ValueError("supericie a cimentar no puede ser mayor a superficie cimentada")

        print("Ingrese superficie a cimentar")

        if self.__superficie_cimentada == 100:
          terminada = True

        
