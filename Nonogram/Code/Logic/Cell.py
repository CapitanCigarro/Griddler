from CellStateEnum import CellStateEnum


class Cell:
        
    """
    Logic Cell class
    
    Attributes
    ----------
    
    expectedState : CellStateEnum
        Expected state for this cell
    
    currentState : CellStateEnum
        Current state of this cell (default CellStateEnum.EMPTY)
        
    Methods
    -------
    
    setCurrentState(expectedState : CellStateEnum) -> int
        sets and compares state of cell
    
    """
            
    expectedState : CellStateEnum
    currentState : CellStateEnum
    
    def __init__(self, expectedState : CellStateEnum) -> None:
        self.expectedState = expectedState
        self.currentState = CellStateEnum.EMPTY
        
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
        if self.currentState in aux and state in aux:
            self.currentState = state
            return 0
        
        if self.currentState == state:
            return 0
        
        self.currentState = state
        
        if self.expectedState in aux and state in aux:
            return 1
        
        if self.expectedState == CellStateEnum.PAINTED and state == CellStateEnum.PAINTED:
            return 1
        
        if self.expectedState not in aux and state in aux:
            return -1
        
        if self.expectedState in aux and state not in aux:
            return -1
        
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