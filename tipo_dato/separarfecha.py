#Separar fecha Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato aaaammdd. Se pide informar por separado el día, el mes y el año de la fecha ingresada

print("Ingrese una fecha en formato aaaammdd: ")
fecha = int(input())
año = fecha // 10000
mes = (fecha % 10000) // 100
día = fecha % 100
print(f"El año es: {año}")
print(f"El mes es: {mes}")
print(f"El día es: {día}")

