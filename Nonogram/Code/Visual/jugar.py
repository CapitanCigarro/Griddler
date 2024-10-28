import pygame
from Griddler.Nonogram.Code.Logic.Nonogram import Nonogram
from Griddler.Nonogram.Code.Logic.Grid import Grid
from Griddler.Nonogram.Code.Logic.Cell import CellStateEnum
from .boton import Boton


class Jugar:
    def __init__(self, app):
        self.app = app
        # Crear una lista bidimensional y pasarla a Grid
        grid_data = [[0] * 10 for _ in range(10)]
        grid = Grid(grid_data)  # Crear un objeto Grid
        self.nonograma = Nonogram(grid)  # Pasar el Grid a Nonogram
        self.cell_size = 30  # Tamaño de cada celda en píxeles
        self.botones = [
        ]

    # Resto de tu código ...

    # Resto de tu código ...

    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.ir_a_menu()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                boton.manejar_evento(evento)
            # Detectar clic en el nonograma
            pos = pygame.mouse.get_pos()
            self.manejar_clic(pos)

    def manejar_clic(self, pos):
        """
        Cambia el estado de una celda cuando se hace clic.

        Parameters
        ----------
        pos : tuple
            Posición del clic en la ventana.
        """
        x, y = pos
        col = x // self.cell_size
        row = y // self.cell_size

        # Verifica que el clic esté dentro de los límites del nonograma
        if 0 <= row < self.nonograma.grid.gridRows and 0 <= col < self.nonograma.grid.gridColumns:
            # Cambia el estado de la celda en el modelo lógico
            current_cell = self.nonograma.grid.cellsList[row][col]
            new_state = CellStateEnum.PAINTED if current_cell.currentState == CellStateEnum.EMPTY else CellStateEnum.EMPTY
            current_cell.setCurrentState(new_state)

    def dibujar(self, ventana):
        ventana.fill((255, 255, 255))

        # Dibuja los botones
        for boton in self.botones:
            boton.dibujar(ventana)

        # Dibuja el nonograma
        for row_idx, row in enumerate(self.nonograma.grid.cellsList):
            for col_idx, cell in enumerate(row):
                color = (255, 255, 255) if cell.currentState == CellStateEnum.EMPTY else (
                    0, 0, 0)
                rect = pygame.Rect(col_idx * self.cell_size, row_idx *
                                   self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(ventana, color, rect)
                pygame.draw.rect(ventana, (200, 200, 200),
                                 rect, 1)  # Bordes de las celdas
