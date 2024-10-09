from ..Nonogram.Code.Logic.Cell import Cell
from ..Nonogram.Code.Logic.CellStateEnum import CellStateEnum

# TODO get this to work

import unittest

class TestCell(unittest.TestCase):
    emptyCell = Cell(CellStateEnum.EMPTY)
    paintedCell = Cell(CellStateEnum.PAINTED)
    def testCorrect(self):
        self.assertEqual(self.emptyCell.setCurrentState(CellStateEnum.EMPTY), 1)
        self.assertEqual(self.emptyCell.setCurrentState(CellStateEnum.MARKED), 0)
        self.assertEqual(self.paintedCell.setCurrentState(CellStateEnum.PAINTED,1))





if __name__ == '__main__':
    unittest.main()