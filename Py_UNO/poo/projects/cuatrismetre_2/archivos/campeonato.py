import csv
class Campeonato:

  def __init__(self) -> None:
    self. __partidos:dict[str,list[int]] = {}

    @property
    def partidos(self): -> dict[str,list[int]]:
      return self.__partidos

    def cargar_partidos (self, partidos.csv):
        with open(partidos.csv, "r") as
            lector = csv.reader(file)
            for partido in lector:
              k1 = partido[0]
              k2 = partido[2]
                equipo1 = self.partidos.get(k1, {0,0,0,0,0,0,0,0})

                equipo2 = self.partidos.get(k2, {0,0,0,0,0,0,0,0})

                ##partidos jguados
                equipo1[0]+=1
                equipo2[0]+=1

                if partido[1] > partids[3]:
                    ##partidosganados
                    equipo1[1] += 1
                    equipo1[7] += 3
                    equipo2[3] += 1
                    equipo1[4] +=
                    equipo2[5]

                elif partido[2] > partido[3]:
                    equipo2[1] += 1
                    equipo1[7] += 3
                    equipo1[3] += 1
                    equipo1[4] += int(partido[1]) - int(partido[3])
                    equipo2[5] += int(partido[3]) - int(partido[1])
                else:
                  ##Empatados
                  equipo1[2] +=1
                  equipo2[2] +=1
                  equipo1[7] += 1
                  equipo2[7] += 1

            self.partidos[k1] = equipo1
            self.partidos[k2] = equipo2

            file.close()

            def imprimir_tabla(self, tabla):
              with (tabla, "w") as tabla:
                for seleccion, resultadaos in self.partidos.items():
                  tabla.write(f"{seleccion} {resultados})

def main():
  mundial = Campeonato()
  mundial.cargar_partidos("partidos.csv")
  print(mundial.__partidos)











def main():
  pass

if __name__ == "__main__":
  main()
dict
