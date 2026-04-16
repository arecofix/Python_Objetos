#Teléfono sin prefijo ni extensión
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +54, y la extensión tiene cuatro dígitos (por ejemplo +54-9115847-1056). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión

print("Ingrese un número de teléfono con el formato +54-XXXXXXXX-XXXX: ")
telefono = input()
print(f"El número de teléfono sin prefijo ni extensión es: {telefono[4:-4]}")
