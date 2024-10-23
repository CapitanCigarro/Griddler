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
        for i in range(self.__currentGrid.getGridRows()):
            for j in range(self.__currentGrid.getGridColumns()):
                if self.__currentGrid.getCell(i, j).isSolved():
                    self.__score += 1


    def getScore(self) -> int:
        return self.__score

    def changeCell(self, i : int, j : int, state : CellStateEnum) -> None:
        self.__score += self.__currentGrid.getCell(i, j).setCurrentState(state)

    def useClue(self, i : int, j : int) -> None:
        if self.__remainingClues > 0:
            clue_cell = self.__currentGrid.getCell(i, j)
            if not clue_cell.isSolved():
                if clue_cell.getExpectedState() == CellStateEnum.PAINTED:
                    self.__score += clue_cell.setCurrentState(CellStateEnum.PAINTED)
                else:
                    self.__score += clue_cell.setCurrentState(CellStateEnum.MARKED)
                self.__remainingClues -= 1