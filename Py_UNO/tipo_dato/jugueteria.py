#Juguetería Una juguetería tiene mucho éxito en dos de sus productos: autos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que se debe 
#calcular el peso de los autos y muñecas que saldrán en cada paquete a demanda. Cada auto pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de autos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

print("Ingrese el número de autos vendidos: ")
autos = int(input())
print("Ingrese el número de muñecas vendidas: ")
muñecas = int(input())
peso_total = autos * 112 + muñecas * 75
print(f"El peso total del paquete es: {peso_total} g")

