import unittest
from Code.Logic.Level import Level
from Code.Logic.Grid import Grid
from Code.Logic.CellStateEnum import CellStateEnum

example_grid = Grid([
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
    ])
example_empty_grid = Grid([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ])

level_1 = Level(example_grid, example_empty_grid)

def test_score():
    level_1.changeCell(0, 3, CellStateEnum.PAINTED)
    assertEqual(level_1.getScore(), 1)