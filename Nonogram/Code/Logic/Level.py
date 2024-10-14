from Grid import Grid
from  CellStateEnum import CellStateEnum

class Level:
    __currentGrid : Grid
    __score : int

    def __init__(self, expected : Grid) -> None:
        self.__currentGrid = expected
        __score = 0

    def getScore(self) -> int:
        return self.__score

    def changeCell(self, i : int, j : int, state : CellStateEnum) -> None:
        self.__score = self.__currentGrid.getCell(i, j).setCurrentState(state)