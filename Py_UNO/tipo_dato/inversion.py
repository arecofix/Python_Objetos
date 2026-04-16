#Inversión
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión

print("Ingrese la cantidad a invertir: ")
cantidad = float(input())
print("Ingrese el interés anual (en porcentaje): ")
interes = float(input())
print("Ingrese el número de años: ")
fecha = int(input())
capital = cantidad * (1 + interes / 100) ** fecha
print(f"El capital obtenido en la inversión es: {capital:.2f}")
