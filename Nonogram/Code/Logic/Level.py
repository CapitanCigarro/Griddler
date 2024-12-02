from .Grid import Grid
from .CellStateEnum import CellStateEnum
from .NoCluesRemainingException import NoCluesRemainingException
from .GameModeEnum import GameModeEnum
from .NoLivesRemainigException import NoLivesRemainingException


class Level:
    __currentGrid: Grid
    __score: int
    __remainingClues: int
    __gameMode: GameModeEnum
    __lives: int

    def __init__(self, expected: Grid, mode: GameModeEnum) -> None:
        self.__currentGrid = expected
        self.__score = 0
        self.__remainingClues = 3
        self.__lives = 3
        self.__gameMode = mode
        for i in range(self.__currentGrid.getGridRows()):
            for j in range(self.__currentGrid.getGridColumns()):
                if self.__currentGrid.getCell(i, j).isSolved():
                    self.__score += 1

    def getScore(self) -> int:
        return self.__score

    def changeCell(self, i: int, j: int, state: CellStateEnum) -> None:
        if self.__gameMode == GameModeEnum.LIVES:
            if state == self.__currentGrid.getCell(i, j).getExpectedState():
                self.__score += self.__currentGrid.getCell(
                    i, j).setCurrentState(state)
            else:
                self.__lives -= 1
                if self.__currentGrid.getCell(i, j).getExpectedState() == CellStateEnum.PAINTED:
                    self.__score += self.__currentGrid.getCell(
                        i, j).setCurrentState(CellStateEnum.PAINTED)
                else:
                    self.__score += self.__currentGrid.getCell(
                        i, j).setCurrentState(CellStateEnum.MARKED)
                if self.__lives <= 0:
                    raise NoLivesRemainingException("No quedan vidas")
        else:
            self.__score += self.__currentGrid.getCell(
                i, j).setCurrentState(state)

    def useClue(self, i: int, j: int) -> None:
        if self.__gameMode == GameModeEnum.ZEN:
            if self.__remainingClues > 0:
                clue_cell = self.__currentGrid.getCell(i, j)
                if clue_cell.getExpectedState() == CellStateEnum.PAINTED:
                    self.__score += clue_cell.setCurrentState(
                        CellStateEnum.PAINTED)
                else:
                    self.__score += clue_cell.setCurrentState(
                        CellStateEnum.MARKED)
                self.__remainingClues -= 1
            else:
                raise NoCluesRemainingException("No quedan pistas para usar")

    def getGameMode(self) -> GameModeEnum:
        return self.__gameMode

    def setGameMode(self, change: GameModeEnum) -> None:
        self.__gameMode = change

    def getRemainingClues(self) -> int:
        return self.__remainingClues

    def getCurrentGrid(self) -> Grid:
        return self.__currentGrid

    def getLives(self) -> int:
        return self.__lives
