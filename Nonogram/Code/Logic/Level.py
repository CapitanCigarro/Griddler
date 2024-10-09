from Grid import Grid

class Level:
    __expectedGrid : Grid
    __currentGrid : Grid
    __score : int

    def __init__(self, expected : Grid, current : Grid) -> None:
        self.__expectedGrid = expected
        self.__currentGrid = current
        __score = 0
