# from .Cell import CellStateEnum
# from .Cell import Cell
from Code.Logic.Level import Level
from Code.Logic.LectorNiveles import LectorNiveles
from Code.Logic.Grid import Grid

class Nonogram:
    __nivelActual: Level
    __lectorNivel5x5 : LectorNiveles
    __lectorNivel10x10 : LectorNiveles
    __lectorNivel15x15 : LectorNiveles

    def __init__(self):
        self.__lectorNivel5x5 = LectorNiveles("../../SavedNonograms/Levels5x5.csv")
        self.__lectorNivel10x10 = LectorNiveles("../../SavedNonograms/Levels10x10.csv")
        self.__lectorNivel15x15 = LectorNiveles("../../SavedNonograms/Levels15x15.csv")

    def getgridActual(self,tam:int,sel:int) -> Grid:
        if tam == 5:
            return Grid(self.__lectorNivel5x5.getniveles(sel))
        if tam == 10:
            return Grid(self.__lectorNivel10x10.getniveles(sel))
        if tam == 15:
            return Grid(self.__lectorNivel15x15.getniveles(sel))

    def gettotallevels(self,tam:int) -> int:
        if tam == 5:
            return self.__lectorNivel5x5.gettotalniveles()
        if tam == 10:
            return self.__lectorNivel10x10.gettotalniveles()
        if tam == 15:
            return self.__lectorNivel15x15.gettotalniveles()