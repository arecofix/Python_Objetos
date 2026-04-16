#Caja de Ahorros Imagina que acabas de abrir una nueva caja de ahorros en USD que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu caja de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales

print("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: ")
cantidad = float(input())
interes = 0.04
ahorros_año1 = cantidad * (1 + interes)
ahorros_año2 = ahorros_año1 * (1 + interes)
ahorros_año3 = ahorros_año2 * (1 + interes)
print(f"Cantidad de ahorros tras el primer año: {ahorros_año1:.2f} USD")
print(f"Cantidad de ahorros tras el segundo año: {ahorros_año2:.2f} USD")
print(f"Cantidad de ahorros tras el tercer año: {ahorros_año3:.2f} USD")

