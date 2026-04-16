#Cociente y Resto
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente

print("Ingrese primer valor")
valor1 = int(input())   
print("Ingrese segundo valor")
valor2 = int(input())
cociente = valor1 // valor2
resto = valor1 % valor2
print(f"La división de {valor1} entre {valor2} da un cociente de {cociente} y un resto de {resto}")