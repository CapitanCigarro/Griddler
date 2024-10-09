from typing import Any
from CellStateEnum import CellStateEnum


class Cell:
        
    """
    Logic Cell class
    
    Attributes
    ----------
    
    __expectedState : int
        Expected state for this cell, 0 for EMPTY, 1 for PAINTED
    
    currentState : CellStateEnum
        Current state of this cell (default CellStateEnum.EMPTY)
        
    Methods
    -------
    
    setCurrentState(__expectedState : CellStateEnum) -> int
        sets and compares state of cell
    
    """
            
    __expectedState : CellStateEnum
    __currentState : CellStateEnum
    
    def __init__(self, expectedState : int) -> None:
        self.__expectedState = CellStateEnum(expectedState)
        self.__currentState = CellStateEnum.EMPTY
        
    def setCurrentState(self, state : CellStateEnum) -> int:
        """
        sets state and compares to expected
        
        Parameters
        ----------
        state : CellStateEnum
            state that cell will change to
            
        Returns
        -------
            int
            corresponding to points, if correct will return 1 point, if wrong -1
        
        """
        
        aux = {CellStateEnum.EMPTY, CellStateEnum.MARKED}
        if self.__currentState in aux and state in aux:
            self.__currentState = state
            return 0
        
        if self.__currentState == state:
            return 0
        
        self.__currentState = state
        
        if self.__expectedState in aux and state in aux:
            return 1
        
        if self.__expectedState == CellStateEnum.PAINTED and state == CellStateEnum.PAINTED:
            return 1
        
        if self.__expectedState not in aux and state in aux:
            return -1
        
        if self.__expectedState in aux and state not in aux:
            return -1
        
    def __str__(self) -> str:
        return self.__currentState.name    
    
    def getExpectedState(self) -> CellStateEnum:  
        return self.__expectedState
    
    def CurrentState(self) -> CellStateEnum:
        return self.__currentState
    
# TODO delete this

""" emptyCell = Cell(CellStateEnum.EMPTY)
emptyCell.setCurrentState(CellStateEnum.PAINTED)
paintedCell = Cell(CellStateEnum.PAINTED)
def testCorrect():
    print(f"1 == {emptyCell.setCurrentState(CellStateEnum.EMPTY)}\n")
    print(f"0 == {emptyCell.setCurrentState(CellStateEnum.MARKED)}\n")
    print(f"1 == {paintedCell.setCurrentState(CellStateEnum.PAINTED)}\n")
    
def testIncorrect():
    print(f"-1 == {emptyCell.setCurrentState(CellStateEnum.PAINTED)}")
    print(f"0 == {emptyCell.setCurrentState(CellStateEnum.PAINTED)}")
    print(f"-1 == {paintedCell.setCurrentState(CellStateEnum.EMPTY)}")
    print(f"0 == {paintedCell.setCurrentState(CellStateEnum.MARKED)}")
    
testCorrect()
testIncorrect() """
