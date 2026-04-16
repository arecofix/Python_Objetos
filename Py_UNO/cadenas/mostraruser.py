#Mostrar n veces username
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido

print("Ingrese su nombre: ")
nombre = input()
print("Ingrese un número entero: ")
num = int(input())
for i in range(num):
    print(nombre)

    