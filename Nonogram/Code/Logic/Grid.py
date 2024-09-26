from Cell import Cell

class Grid:
    gridSize : int
    gridRows : int
    gridColumns : int
    
    cellsList : list
    rowsList : list
    columnsList : list
    
    def __init__(self, grid : list) -> None:
        self.gridRows = len(grid) # How many rows
        self.gridColumns = len(grid[0]) # How many columns
        self.gridSize = self.gridRows * self.gridRows
        self.cellsList = []
        self.rowsList = []
        self.columnsList = []
        self.__initializeLists(grid)
        
        
    def __initializeLists(self, grid : list) -> None:
        rangeVar = self.gridRows if self.gridRows > self.gridColumns else self.gridColumns
        
        rowsBool = True
        columnsBool = True
        
        for i in range(rangeVar):
            rowList = []
            columnList = []
            
            if i < self.gridRows:
                self.cellsList.append([])
            
            for j in range(rangeVar):
                if i < self.gridRows:
                    if j < self.gridColumns:
                        rowList.append(grid[i][j])
                        
                else:
                    rowsBool = False   
                
                if i < self.gridColumns:
                    if j < self.gridRows:
                        columnList.append(grid[j][i])
                
                else:
                    columnsBool = False        
                    
                if j < self.gridColumns and i < self.gridRows:
                    self.cellsList[i].append(Cell(grid[i][j]))
            
            if rowsBool:
                self.rowsList.append(self.__countNumbers(rowList))
            
            if columnsBool:
                self.columnsList.append(self.__countNumbers(columnList))
    
                    
    def __countNumbers(self, numbers : list) -> list:        
        """
        method to get the numbers that show in the puzzle
        """
        ret = []
        
        aux = 0
        
        for i in numbers:
            if i == 1:
                aux +=1
            elif aux != 0:
                ret.append(aux)
                aux = 0
                
        if aux != 0:
            ret.append(aux)
        
        return ret
    
    def __str__(self) -> str:
        a = """\nCells = 
"""
        b = """\nColumns = 
"""
        c = """\nRows = 
"""
        
        for i in range(len(self.cellsList)):
            a += "["
            for j in range(len(self.cellsList[i])):
                if j != len(self.cellsList[i]) - 1:
                    a += f"{str(self.cellsList[i][j])}, "
                
                else:
                    a+= f"{str(self.cellsList[i][j])}"
                
            a +="]\n"
            
            if i < len(self.columnsList):
                b += str(f"{self.columnsList[i]}\n")
                
            if i < len(self.rowsList):
                c += str(f"{self.rowsList[i]}\n")
        
        return f"""
                Columns = {self.gridColumns}
                Rows = {self.gridRows}
                Cells Amount = {self.gridSize}""" + a + b + c
                