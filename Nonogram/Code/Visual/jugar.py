import pygame
from Griddler.Nonogram.Code.Logic.Nonogram import Nonogram
from Griddler.Nonogram.Code.Logic.Grid import Grid
from Griddler.Nonogram.Code.Logic.Cell import CellStateEnum
from Griddler.Nonogram.Code.Logic.Level import Level
from .boton import Boton
from Griddler.Nonogram.SavedNonograms.NonogramsEnum import NonogramsEnum


class Jugar:
    def __init__(self, app):
        self.app = app
        # Crear un objeto Grid usando la propiedad grid del enum
        self.grid = Grid(NonogramsEnum.KITCHENFLOOR.value)
        # self.nonograma = Nonogram(self.grid)  # Pasar el Grid a Nonogram
        self.levelnonograma = Level(self.grid)
        self.cell_size = 75  # Tamaño de cada celda en píxeles
        self.start_x = 100
        self.start_y = 100
        self.botones = []
        self.ventana_nonograma_emergente = False
        self.nonograma_completado = False

    def ir_a_menu(self):
        # self.reiniciar_nonograma()
        self.app.cambiar_panel(self.app.menu)

    # def reiniciar_nonograma(self):
    #     self.grid = Grid(NonogramsEnum.KITCHENFLOOR.value)
    #     self.nonograma = Level(self.grid)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.ir_a_menu()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                boton.manejar_evento(evento)
            pos = pygame.mouse.get_pos()
            self.manejar_clic(pos)

    def manejar_clic(self, pos):
        if not self.nonograma_completado:
            x, y = pos
            col = (x - self.start_x) // self.cell_size
            row = (y - self.start_y) // self.cell_size

            # Verifica que el clic esté dentro de los límites del nonograma
            if 0 <= row < self.grid.getGridRows() and 0 <= col < self.grid.getGridColumns():
                # Determina qué tipo de clic se realizó
                if pygame.mouse.get_pressed()[0]:
                    if self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.EMPTY:
                        self.levelnonograma.changeCell(
                            row, col, CellStateEnum.PAINTED)
                    elif self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.PAINTED:
                        self.levelnonograma.changeCell(
                            row, col, CellStateEnum.EMPTY)
                elif pygame.mouse.get_pressed()[2]:  # Clic derecho
                    self.levelnonograma.changeCell(
                        row, col, CellStateEnum.MARKED)

                # Verifica si se completó el nonograma
                if self.levelnonograma.getScore() == (self.grid.getGridRows() * self.grid.getGridColumns()):
                    print("¡Felicidades! Has completado el nonograma.")
                    self.ventana_nonograma_emergente = True
                    self.nonograma_completado = True

    def mostrar_ventana_emergente(self):
        # Ajusta el tamaño de la ventana emergente
        ancho_ventana = 600  # Aumenta el ancho de la ventana
        alto_ventana = 150
        ventana_emergente = pygame.Surface((ancho_ventana, alto_ventana))
        ventana_emergente.fill((255, 255, 255))
        pygame.draw.rect(ventana_emergente, (0, 0, 0),
                         ventana_emergente.get_rect(), 2)

        font = pygame.font.Font(None, 36)
        text_surface = font.render("¡Felicidades!", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(ancho_ventana // 2, 50))
        ventana_emergente.blit(text_surface, text_rect)

        text_surface = font.render(
            "Has completado el nonograma.", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(ancho_ventana // 2, 100))
        ventana_emergente.blit(text_surface, text_rect)

        self.ventana.blit(ventana_emergente, (self.ventana.get_width(
        ) // 2 - ancho_ventana // 2, self.ventana.get_height() // 2 - alto_ventana // 2))
        pygame.display.flip()

        # Espera a que el usuario presione una tecla o haga clic para cerrar la ventana emergente
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False

    def dibujar(self, ventana):
        self.ventana = ventana
        ventana.fill((255, 255, 255))

        # Fuente para los números
        font = pygame.font.Font(None, 24)

        # Dibuja las guías de filas en el margen izquierdo
        for row_idx, row in enumerate(self.grid.getRowsList()):
            for num_idx, num in enumerate(row):
                text_surface = font.render(str(num), True, (0, 0, 0))
                text_rect = text_surface.get_rect()
                text_rect.right = self.start_x - 5 - num_idx * 20
                text_rect.centery = self.start_y + row_idx * \
                    self.cell_size + self.cell_size // 2
                ventana.blit(text_surface, text_rect)

        # Dibuja las guías de columnas en el margen superior
        for col_idx, col in enumerate(self.grid.getColumnsList()):
            for num_idx, num in enumerate(col):
                text_surface = font.render(str(num), True, (0, 0, 0))
                text_rect = text_surface.get_rect()
                text_rect.centerx = self.start_x + col_idx * \
                    self.cell_size + self.cell_size // 2
                text_rect.bottom = self.start_y - 5 - num_idx * 20
                ventana.blit(text_surface, text_rect)

        # Dibuja el nonograma
        for row_idx, row in enumerate(self.grid.getCellsList()):
            for col_idx, cell in enumerate(row):
                if cell.CurrentState() == CellStateEnum.MARKED:
                    # Dibuja una "X"
                    color = (255, 0, 0)  # Color rojo para la "X"
                    rect = pygame.Rect(self.start_x + col_idx * self.cell_size, self.start_y + row_idx *
                                       self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.line(ventana, color, rect.topleft,
                                     rect.bottomright, 2)
                    pygame.draw.line(
                        ventana, color, rect.bottomleft, rect.topright, 2)
                else:
                    # Color para celdas vacías y pintadas
                    color = (255, 255, 255) if cell.CurrentState(
                    ) == CellStateEnum.EMPTY else (0, 0, 0)
                    rect = pygame.Rect(self.start_x + col_idx * self.cell_size, self.start_y + row_idx *
                                       self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(ventana, color, rect)
                    pygame.draw.rect(ventana, (200, 200, 200),
                                     rect, 1)  # Bordes de las celdas
        # Dibuja los botones
        for boton in self.botones:
            boton.dibujar(ventana)

        # Si el nonograma está completado, muestra la ventana emergente
        if self.ventana_nonograma_emergente:
            self.mostrar_ventana_emergente()

        self.ventana_nonograma_emergente = False
