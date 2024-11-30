import csv


class LectorNiveles:
    __rutaArchivo: str
    levels: list[list[list[int]]]

    def __init__(self, ruta: str):
        self.levels = [[]]
        self.__rutaArchivo = ruta

        with open(self.__rutaArchivo, newline='') as csvfile:
            values = csv.reader(csvfile, delimiter=';', quotechar='|')
            level = []

            for y in values:
                aux = [int]
                posx = 0
                for x in y:
                    if x == '':
                        break
                    if posx == 0:
                        aux[0] = int(x)
                    else:
                        aux.append(int(x))
                    posx += 1
                if len(aux) == 1:
                    self.levels.append(level)
                    level = []
                    continue
                level.append(aux)

    def getniveles(self, n: int):
        if len(self.levels) > n + 1:
            return self.levels[n+1]

    def gettotalniveles(self) -> int:
        # se elimina 1 por len(), ya que [0] nunca será nivel
        return len(self.levels) - 1

    def getsizeniveles(self) -> int:
        if len(self.levels) > 1:
            return len(self.levels[1])

    def addnivel(self,nivel:list):
        self.levels.append(nivel)
        self.saveLevels()

    def saveLevels(self):
        with open(self.__rutaArchivo, mode='w', newline='') as csvfile:
            wr = csv.writer(csvfile,delimiter=';')
            for i in range(self.gettotalniveles()):
                wr.writerows(self.levels[i+1])
                wr.writerow([None] * self.getsizeniveles())
