from abc import ABC

class Material(ABC):
    def __init__(self,titulo: str, autor: str, anio:int):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__ (self) -> str:
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"
    def __repr__(self) -> str:
        return self.__str__()
class Libro(Material):
    def __init__(self,titulo: str, autor: str, anio:int, genero: str):
        super().__init__(titulo,autor,anio)
        self.genero = genero
    def __str__(self) -> str:
        return f"Libro: {super().__str__()}, Genero: {self.genero}"
class Revista(Material):
    def __init__(self,titulo: str, autor: str, anio:int, numero_edicion: int):
        super().__init__(titulo,autor,anio)
        self.numero_edicion = numero_edicion
    def __str__(self) -> str:
        return f"Revista: {super().__str__()}, Número de edición: {self.numero_edicion}"
class DVD(Material):
    def __init__(self,titulo: str, autor: str, anio:int, duracion: int):
        super().__init__(titulo,autor,anio)
        self.duracion = duracion
    def __str__(self) -> str:
        return f"DVD: {super().__str__()}, Duración: {self.duracion}"

class Usuario:
    def __init__(self, nombre:str):
        self.nombre:str = nombre
        self.material_prestado: list[Material] = []
    def prestar (self,material: Material):
        self.material_prestado.append(material)
    def devolver (self, material: Material):
        self.material_prestado.remove(material)
    def listar_material(self) -> str:
        s = ""
        for m in self.material_prestado:
          s = s + m.__str__() + "\n"
        return s
    def __str__(self) -> str:
        return f"Usuario: {self.nombre}, Materiales prestados:\n {self.listar_material()}"




def main():
    libro = Libro("El vado de los zorros", "Anna Starobinets", 2025, "Ficción")
    revista = Revista("Cifras", "Editorial Cúspide", 2026, 4678)
    dvd = DVD("Matilda", "Autor de Matilda", 1996, 2)
    luisito = Usuario("Luisito")

    luisito.prestar(libro)
    luisito.prestar(revista)
    luisito.prestar(dvd)

    luisito.listar_material()
    def mostrar_informacion(material : "Material"):
        print(material.__str__())
    mostrar_informacion(libro)
    mostrar_informacion(dvd)
    mostrar_informacion(revista)

if __name__ == "__main__":
     main()
