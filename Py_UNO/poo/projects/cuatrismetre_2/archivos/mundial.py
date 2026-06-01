import csv

with open("partidos.csv", mode='r' encording='utf-8') as archivo:
  lector_dict = csv.DictReader(archivo)

    for fila in lector_dict:
      print(fila['Nombre'], fila['Puntaje'])

      
