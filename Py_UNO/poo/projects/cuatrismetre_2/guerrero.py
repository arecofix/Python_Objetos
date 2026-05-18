# guerrero.py


class Guerrero:
    def __init__(
        self,
        nombre: str,
        energia: int,
        salud: int,
        costo_ataque: int,
        danio: int,
        energia_max: int,
    ):
        self.nombre = nombre
        self.energia = energia
        self.salud = salud
        self.costo_ataque = costo_ataque
        self.danio = danio
        self.energia_max = energia_max

    def atacar(self, otro: "Guerrero") -> None:
        """Ataca a otro guerrero si tiene suficiente energía
        y no está derrotado."""
        pass

    def recibir_racion(self) -> None:
        """Recupera energía al recibir una ración de agua."""
        pass

    def esta_derrotado(self) -> bool:
        """Devuelve True si la salud llegó a 0 o menos."""
        pass

    def estado(self) -> str:
        """Devuelve un string con nombre, salud y energía."""
        pass


class Soldado(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=100, salud=200, costo_ataque=10, danio=10, energia_max=100
        )


class Orco(Guerrero):
    def __init__(self, nombre: str):
        super().__init__(
            nombre, energia=120, salud=250, costo_ataque=15, danio=20, energia_max=120
        )


def main():
    pass


if __name__ == "__main__":
    main()
