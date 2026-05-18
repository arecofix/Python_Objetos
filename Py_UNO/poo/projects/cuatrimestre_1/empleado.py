class Empleado:
    def __init__(self, nombre, salario_base, dni):
        self.__nombre = nombre
        self.__salario_base = salario_base
        self.__dni = dni

    # Creamos una 'property' (getter) para poder leer el salario base desde la clase hija
    @property
    def salario_base(self):
        return self.__salario_base

    def bonificacion(self):
        return self.__salario_base * 0.05

    def salario(self):
        # Llama a self.bonificacion(), lo que permite el polimorfismo con Gerente
        return self.__salario_base + self.bonificacion()


class Gerente(Empleado):
    # Añadimos 'dni' porque la clase padre lo exige, y agregamos los ':' faltantes
    def __init__(self, nombre, salario_base, dni, depto):
        # Corregimos la indentación y pasamos el dni al padre
        super().__init__(nombre, salario_base, dni)
        self.departamento = depto

    def bonificacion(self):
        # No se puede usar super().__salario_base porque '__' lo hace estrictamente privado.
        # En su lugar, usamos la propiedad 'salario_base' que creamos en el padre.
        return self.salario_base * 0.1


def main():
    # Probando la clase Empleado
    empleado = Empleado("Carlos", 1000, "12345678A")
    print(f"Empleado: {empleado._Empleado__nombre}") # Acceso forzado solo para demostrar
    print(f"Bonificación Empleado (5%): {empleado.bonificacion()}")
    print(f"Salario final Empleado: {empleado.salario()}\n")

    # Probando la clase Gerente
    gerente = Gerente("Ana", 2000, "87654321B", "Ventas")
    print(f"Gerente del departamento de {gerente.departamento}")
    print(f"Bonificación Gerente (10%): {gerente.bonificacion()}")
    print(f"Salario final Gerente: {gerente.salario()}")

# Ejecutamos la función main
if __name__ == "__main__":
    main()
