#Panadería Una panadería vende bolsas de pan a ARS 2000 cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de bolsas vendidas que no son del día. Después el programa debe mostrar el precio habitual de una bolsa de pan, el descuento que se le hace por no ser fresca y el coste final total

print("Ingrese el número de bolsas vendidas que no son del día: ")
bolsas = int(input())
precio_habitual = 2000
descuento = precio_habitual * 0.60
precio_final = precio_habitual - descuento
costo_total = precio_final * bolsas
print(f"El precio habitual de una bolsa de pan es: ARS {precio_habitual}")
print(f"El descuento por no ser fresca es: ARS {descuento}")
print(f"El coste final total es: ARS {costo_total}")
