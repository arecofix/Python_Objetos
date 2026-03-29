#Fecha de nacimiento
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año

print("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")
fecha = input()
dia, mes, año = fecha.split("/")
print(f"Su fecha de nacimiento es: {dia} de {mes} de {año}")