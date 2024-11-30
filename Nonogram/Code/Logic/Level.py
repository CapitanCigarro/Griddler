
from Grid import Grid
from CellStateEnum import CellStateEnum
from NoCluesRemainingException import NoCluesRemainingException
import GameModeEnum

class Level:
    __currentGrid : Grid
    __score : int
    __remainingClues : int
    __gameMode : GameModeEnum

    def __init__(self, expected : Grid, mode : GameModeEnum) -> None:
        self.__currentGrid = expected
        self.__score = 0
        self.__remainingClues = 3
        self.__gameMode = mode
        for i in range(self.__currentGrid.getGridRows()):
            for j in range(self.__currentGrid.getGridColumns()):
                if self.__currentGrid.getCell(i, j).isSolved():
                    self.__score += 1


    def getScore(self) -> int:
        return self.__score

    def changeCell(self, i : int, j : int, state : CellStateEnum) -> None:
        if self.__gameMode == GameModeEnum.ZEN:
            self.__score += self.__currentGrid.getCell(i, j).setCurrentState(state)

    def useClue(self, i : int, j : int) -> None:
        if self.__gameMode == GameModeEnum.ZEN:
            if self.__remainingClues > 0:
                clue_cell = self.__currentGrid.getCell(i, j)
                if not clue_cell.isSolved():
                    if clue_cell.getExpectedState() == CellStateEnum.PAINTED:
                        self.__score += clue_cell.setCurrentState(CellStateEnum.PAINTED)
                    else:
                        self.__score += clue_cell.setCurrentState(CellStateEnum.MARKED)
                    self.__remainingClues -= 1
            else:
                raise NoCluesRemainingException("No quedan pistas para usar")
        
    def getGameMode(self) -> GameModeEnum:
        return self.__gameMode
    def setGameMode(self, change : GameModeEnum) -> None:
        self.__gameMode = change

