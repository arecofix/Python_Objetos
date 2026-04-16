#Carrito de compras
#Escribir un programa que pregunte por consola por los productos de un carrito de compras, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta

print("Ingrese los productos del carrito de compras, separados por comas: ")
productos = input()
for producto in productos.split(","):
    print(producto)