from .Grid import Grid
from .Cell import Cell, CellStateEnum


class Nonogram:
    """
    Nonogram game class to manage the puzzle grid and logic.

    Attributes
    ----------
    grid : Grid
        Represents the nonogram's grid with cells.

    Methods
    -------
    check_solution() -> bool
        Checks if the current grid state matches the solution.

    update_cell(row: int, col: int, state: CellStateEnum) -> int
        Updates the cell state and returns the points based on correctness.
    """

    def __init__(self, grid: Grid):
        """
        Initialize Nonogram with a given Grid object.

        Parameters
        ----------
        grid : Grid
            An instance of the Grid class representing the puzzle.
        """
        self.grid = grid

    def check_solution(self) -> bool:
        """
        Checks if all cells in the grid match the expected states.

        Returns
        -------
        bool
            True if the solution is correct, False otherwise.
        """
        for row in range(self.grid.gridRows):
            for col in range(self.grid.gridColumns):
                cell = self.grid.cellsList[row][col]
                if cell.expectedState != cell.currentState:
                    return False
        return True

    def update_cell(self, row: int, col: int, state: CellStateEnum) -> int:
        """
        Updates a cell state in the grid and checks correctness.

        Parameters
        ----------
        row : int
            Row of the cell to update.
        col : int
            Column of the cell to update.
        state : CellStateEnum
            The new state to set for the cell.

        Returns
        -------
        int
            Points awarded or deducted based on the cell update.
        """
        cell = self.grid.cellsList[row][col]
        return cell.setCurrentState(state)
