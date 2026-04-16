#Producto
#Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales

print("Ingrese el nombre del producto: ")
nombre = input()
print("Ingrese el precio del producto: ")
precio = float(input())
print("Ingrese el número de unidades: ")
unidades = int(input())

coste_total = precio * unidades

print(f"{nombre}: ${precio:6.2f} x {unidades:3d} = ${coste_total:8.2f}")