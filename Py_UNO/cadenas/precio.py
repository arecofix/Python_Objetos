#Precio
#Escribir un programa que pregunte por consola el precio de un producto en pesos con dos decimales y muestre por pantalla el número de pesos y el número de centavos del precio introducido

print("Ingrese el precio del producto en pesos con dos decimales: ")
precio = float(input())
pesos = int(precio)
centavos = int((precio - pesos) * 100)
print(f"El precio es de {pesos} pesos y {centavos} centavos.")