#definir cuenta de manera que no pueda instanciarse
#osea que es aftracta

from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self, dni:int, saldo, limite, descubierto, cajadeahorro, cuentacorriente) -> None:
        self.__dni = dni
        self.__saldo:float = 0
        self.__limite = limite
        self.__descubierto = descubierto
        self.__cajadeahorro = cajadeahorro
        self.__retirar = retirar

        def depositar(self, monto:float) -> None:
          if monto <= 0:
            raise ValueError("Monto Invalido")

          self.__saldo += monto

        @property
        def Saldo(self) -> float:
          return self.__saldo

        @property
        def dni(self) -> int:
          return self.__dni

        @abstractmethod
        def retirar(self, monto):
          pass

        @abstractmethod
        def dinero_disponible(self):
          pass


        class CajaDeAhorro(Cuenta):
          def __init__(self, dni: int) -> None:
            super().__init__(dni)


            def retirar(self, monto):
              if self.saldo < monto:
                raise ValueError("No tealcanza")
                self._saldo -= monto

            def reservar(self, monto):

              if self.__saldo < monto:
                raise ValueError("Saldo Insuficiente para reservar")

                self.__reserva += monto

                self.___saldo -= monto

            def retirar_reserva(self, monto):

              if self.__reserva < monto:
                raise ValueError("Saldo Insuficiente para reservar")

                self.__reserva -= monto

                self.___saldo += monto

        dinero_disponible = saldo + descubierto



        cuentacorriente = saldo + descubierto

        def depositar(self, destinatario: cuenta) -> None:
            if self.__saldo > 0:
            saldo.depositar(self)
            self.__depositar = saldo

        def retirar(self, retirar: cuenta) -> None:
            if self.__saldo > 0:
            saldo.retirar(self)
            self.__retirar = saldo retirar

        def dinerodisponible(self, saldo: cuenta) -> None:
            if self.__saldo > 0:
            saldo.depositar(self)
            self.__depositar = saldo
