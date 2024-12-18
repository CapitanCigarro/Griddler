from ..Logic.Cell import Cell


class Grid:

    __gridSize: int
    __gridRows: int
    __gridColumns: int

    __cellsList: list[list[Cell]]
    __rowsList: list[list[int]]
    __columnsList: list[list[int]]

    def __init__(self, grid: list[list[int]]) -> None:
        self.__gridRows = len(grid)  # How many rows
        self.__gridColumns = len(grid[0])  # How many columns
        self.__gridSize = self.__gridRows * self.__gridRows
        self.__cellsList = []
        self.__rowsList = []
        self.__columnsList = []
        self.__initializeLists(grid)

        # self.printLists()

    def __initializeLists(self, grid: list[list[int]]) -> None:
        rangeVar = self.__gridRows if self.__gridRows > self.__gridColumns else self.__gridColumns

        rowsBool = True
        columnsBool = True

        for i in range(rangeVar):
            rowList = []
            columnList = []

            if i < self.__gridRows:
                self.__cellsList.append([])

            for j in range(rangeVar):
                if i < self.__gridRows:
                    if j < self.__gridColumns:
                        rowList.append(grid[i][j])

                else:
                    rowsBool = False

                if i < self.__gridColumns:
                    if j < self.__gridRows:
                        columnList.append(grid[j][i])

                else:
                    columnsBool = False

                if j < self.__gridColumns and i < self.__gridRows:
                    self.__cellsList[i].append(Cell(grid[i][j]))

            if rowsBool:
                self.__rowsList.append(self.__countNumbers(rowList))

            if columnsBool:
                self.__columnsList.append(self.__countNumbers(columnList))

    def __countNumbers(self, numbers: list) -> list:
        """
        method to get the numbers that show in the puzzle
        """
        ret = []

        aux = 0

        for i in numbers:
            if i == 1:
                aux += 1
            elif aux != 0:
                ret.append(aux)
                aux = 0

        if aux != 0:
            ret.append(aux)

        return ret

    def printLists(self) -> None:
        print("Rows List:", self.__rowsList)
        print("Columns List:", self.__columnsList)

        for i in range(len(self.__cellsList)):
            a = "["  # Inicializa la variable 'a'
            for j in range(len(self.__cellsList[i])):
                if j != len(self.__cellsList[i]) - 1:
                    a += f"{str(self.__cellsList[i][j])}, "
                else:
                    a += f"{str(self.__cellsList[i][j])}"
            a += "]"
            print(a)  # Imprime la lista de celdas

    def getCell(self, row: int, column: int) -> Cell:
        return self.__cellsList[row][column]

    def getGridSize(self) -> int:
        return self.__gridSize

    def getGridRows(self) -> int:
        return self.__gridRows

    def getGridColumns(self) -> int:
        return self.__gridColumns

    def getCellsList(self) -> list[list[Cell]]:
        return self.__cellsList

    def getRowsList(self) -> list[list[int]]:
        return self.__rowsList

    def getColumnsList(self) -> list[list[int]]:
        return self.__columnsList
