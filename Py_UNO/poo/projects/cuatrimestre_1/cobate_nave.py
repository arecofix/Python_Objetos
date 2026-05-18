#Combate de Naves Espaciales
#Queremos simular un combate entre distintos tipos de naves espaciales. Todas comparten ciertas características básicas, pero cada una ataca de manera diferente según su naturaleza. Esto nos permitirá trabajar con herencia y sobreescritura de métodos.
#Clase base: Nave
#Atributos:
#nombre → identificador de la nave.
#salud → puntos de vida de la nave.
#danio → puntos de salud que provoca en su oponente cuando ataca
#Métodos:
#atacar(otra) → será redefinido en las subclases.
#recibir_danio(atacante) → resta salud a la nave de acuerdo a quien la ataca (no puede bajar de 0).
#esta_destruida() → devuelve True si la salud llega a 0 o menos.
#estado() → devuelve un string con nombre y salud actual.

class Nave(ABC):
  def __init__(self, nombre, salud, danio) -> None:
    self.__nombre = nombre
    self.__salud = salud
    self.__danio = danio

    @abstractmethod
    def atacar(self, enemigo:Nave) -> None:
        pass

    @property
    def salud(self) -> int:
      return self.__salud
    @salud.setter
    def salud(self, nueva_salud):
      self.__salud = nueva_salud

    def recibir_danio(self, atacante:Nave):
      self.__salud -= atacante.__danio

    def esta_destruida(self)->bool:
      return self.__salud <= 0


    def estado(self)->str:
      return f"Nombre3: {self.__nombre}, salud {self.__salud}"

class Caza(Nave):
  def __init__(self, nombre) -> None:
    super().__init__(nombre, 100, 15)

    def atacar(self, enemigo: Nave) -> None:
      enemigo.recibir_danio(self)

class Bombardero(Nave):
  def __init__(self, nombre, salud, danio):
    super().__init__(nombre, 150, 25)

    def ataqcar(self, enemigo: Nave) -> None:
      enemigo.recibir_danio(self)
      self.__salud -= 5


class Crucero(Nave):
  def __init__(self, nombre, salud, danio):
    super().__init__(nombre, 300, 40)

    def atacar(self, enemigo: Nave) -> None:
      if self.__salud > 50:
        enemigo.recibir_danio(self)
      self.__salud -= 5

      

def main():
  pass
