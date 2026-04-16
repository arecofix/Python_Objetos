#Vocal MAY
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase, pero con la vocal introducida en mayúscula

print("Ingrese una frase: ")
frase = input()
print("Ingrese una vocal: ")
vocal = input()
print(f"La frase con la vocal en mayúscula es: {frase.replace(vocal, vocal.upper())}")