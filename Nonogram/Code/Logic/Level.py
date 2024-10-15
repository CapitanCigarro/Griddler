from random import random, randint

from Grid import Grid
from  CellStateEnum import CellStateEnum

class Level:
    __currentGrid : Grid
    __score : int
    __remainingClues : int

    def __init__(self, expected : Grid) -> None:
        self.__currentGrid = expected
        self.__score = 0
        self.__remainingClues = 3

    def getScore(self) -> int:
        return self.__score

    def changeCell(self, i : int, j : int, state : CellStateEnum) -> None:
        self.__score = self.__currentGrid.getCell(i, j).setCurrentState(state)

    def useClue(self) -> None:
        if self.__remainingClues > 0:
            ran_i = randint(0, self.__currentGrid.getGridRows() - 1)
            ran_j = randint(0, self.__currentGrid.getGridColumns() - 1)
            clue_cell = self.__currentGrid.getCell(ran_i, ran_j)

            if clue_cell.getExpectedState() == CellStateEnum.PAINTED:
                clue_cell.setCurrentState(CellStateEnum.PAINTED)
            else:
                clue_cell.setCurrentState(CellStateEnum.MARKED)
            self.__remainingClues -= 1