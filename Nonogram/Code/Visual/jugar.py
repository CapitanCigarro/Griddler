import pygame

from .boton import Boton
from ..Logic.Grid import Grid
from ..Logic.Cell import CellStateEnum
from ..Logic.Level import Level
from ..Logic.LectorNiveles import LectorNiveles
from ..Logic.GameModeEnum import GameModeEnum
from ..Logic.NoLivesRemainigException import NoLivesRemainingException
from ..Logic.NoCluesRemainingException import NoCluesRemainingException


class Jugar:
    def __init__(self, app, grid: Grid, modo:GameModeEnum):
        self.app = app
        self.grid = grid
        self.modo = modo
        self.levelnonograma = Level(self.grid, self.modo)
        self.max_area_size = 450
        self.cell_size = self.calcular_tamano_celdas()
        window_width, window_height = app.ventana.get_size()
        self.start_x = window_width // 2 - self.max_area_size // 2
        self.start_y = window_height - self.max_area_size-30
        self.botones = []
        self.ventana_nonograma_emergente = False
        self.nonograma_completado = False
        self.fondo_imagen = pygame.image.load(
            "Imagenes/NivelFondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))
        self.callSave = False
       # grid.printLists()
        self.modo_pista_activado = False
        if modo == GameModeEnum.ZEN:
            self.use_clue_button = Boton("Usar Pista", (window_width - 150, 30),
                                         (120, 50), ((0, 0, 0), (255, 255, 255)), self.activar_modo_pista)
            self.use_clue_button.changefontsize(30)
            self.botones.append(self.use_clue_button)

    def modo_creativo(self, ln: LectorNiveles, l: list, ls: int):
        self.modo = GameModeEnum.CREATIVO
        self.fondo_imagen = pygame.image.load(
            "Imagenes/CrearNivelFondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))
        self.actualLector = ln
        width, height = self.app.ventana.get_size()
        self.saveButton = Boton("Guardar e ir al menu", (width/2-145, 30),
                                (300, 50), ((0, 0, 0), (255, 255, 255)), self.save_action)
        self.saveButton.changefontsize(30)
        self.list_to_save = l
        self.list_size = ls
        self.botones.append(self.saveButton)

    def save_action(self):
        isempty = 1
        for r in range(self.list_size):
            for c in range(self.list_size):
                value = self.levelnonograma.getCurrentGrid().getCell(r, c).CurrentState().value
                if value == 1:
                    self.list_to_save[r][c] = 1
                    isempty = 0
                else:
                    self.list_to_save[r][c] = 0
        if isempty == 1:
            print("No es posible guardar un nivel vacío!")
        else:
            if self.callSave == False:
                self.actualLector.addnivel(self.list_to_save)
                print("Nivel guardado!")
            self.callSave = True
        self.ir_a_menu()

    def calcular_tamano_celdas(self):
        rows = self.grid.getGridRows()
        cols = self.grid.getGridColumns()
        return max(self.max_area_size // rows, self.max_area_size // cols)

    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.ir_a_menu()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                boton.manejar_evento(evento)
            pos = pygame.mouse.get_pos()
            self.manejar_clic(pos)
        if self.modo == GameModeEnum.CREATIVO:
            self.saveButton.manejar_evento(evento)

    def activar_modo_pista(self):
        self.modo_pista_activado = True

    def manejar_clic(self, pos):
        if not self.nonograma_completado:
            x, y = pos
            col = (x - self.start_x) // self.cell_size
            row = (y - self.start_y) // self.cell_size

            if 0 <= row < self.grid.getGridRows() and 0 <= col < self.grid.getGridColumns():
                try:
                    if self.modo_pista_activado:
                        if pygame.mouse.get_pressed()[0]:
                            self.levelnonograma.useClue(row, col)
                            self.modo_pista_activado = False
                            print(f"Pista usada en la celda ({row}, {col})")
                            self.levelnonograma.getCurrentGrid().printLists()
                            return

                    if pygame.mouse.get_pressed()[0]:
                        if self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.EMPTY:
                            self.levelnonograma.changeCell(
                                row, col, CellStateEnum.PAINTED)

                            self.levelnonograma.getCurrentGrid().printLists()
                        elif (self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.PAINTED or CellStateEnum.MARKED) and self.levelnonograma.getGameMode() != GameModeEnum.LIVES:
                            self.levelnonograma.changeCell(
                                row, col, CellStateEnum.EMPTY)

                            self.levelnonograma.getCurrentGrid().printLists()
                    elif pygame.mouse.get_pressed()[2]:
                        if self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.EMPTY:
                            self.levelnonograma.changeCell(
                                row, col, CellStateEnum.MARKED)

                            self.levelnonograma.getCurrentGrid().printLists()
                        elif (self.levelnonograma.getCurrentGrid().getCell(row, col).CurrentState() == CellStateEnum.MARKED or CellStateEnum.PAINTED) and self.levelnonograma.getGameMode() == GameModeEnum.ZEN:
                            self.levelnonograma.changeCell(
                                row, col, CellStateEnum.EMPTY)

                            self.levelnonograma.getCurrentGrid().printLists()

                    if self.levelnonograma.getScore() == (self.grid.getGridRows() * self.grid.getGridColumns()):
                        if self.modo == GameModeEnum.CREATIVO:
                            return
                        print("¡Felicidades! Has completado el nonograma.")
                        self.ventana_nonograma_emergente = True
                        self.nonograma_completado = True
                except NoLivesRemainingException:
                    print("No quedan vidas.")
                    self.ventana_nonograma_emergente = True
                    self.nonograma_completado = True

                except NoCluesRemainingException:
                    self.modo_pista_activado = False
                    self.ventana_nonograma_emergente = True

    def mostrar_ventana_emergente(self):
        ancho_ventana = 600
        alto_ventana = 150
        ventana_emergente = pygame.Surface((ancho_ventana, alto_ventana))
        ventana_emergente.fill((255, 255, 255))
        pygame.draw.rect(ventana_emergente, (0, 0, 0),
                         ventana_emergente.get_rect(), 2)

        font = pygame.font.Font(None, 36)
        if self.modo == GameModeEnum.LIVES:
            if self.levelnonograma.getLives() <= 0:
                text_surface = font.render("¡Has perdido!", True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(ancho_ventana // 2, 50))
                ventana_emergente.blit(text_surface, text_rect)

                text_surface = font.render("No quedan vidas.", True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(ancho_ventana // 2, 100))
                ventana_emergente.blit(text_surface, text_rect)

                self.ventana.blit(ventana_emergente, (self.ventana.get_width(
                ) // 2 - ancho_ventana // 2, self.ventana.get_height() // 2 - alto_ventana // 2))
                pygame.display.flip()

            else:
                text_surface = font.render("¡Felicidades!", True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(ancho_ventana // 2, 50))
                ventana_emergente.blit(text_surface, text_rect)

                text_surface = font.render(
                    "Has completado el nonograma.", True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(ancho_ventana // 2, 100))
                ventana_emergente.blit(text_surface, text_rect)
                self.ventana.blit(ventana_emergente, (self.ventana.get_width(
                ) // 2 - ancho_ventana // 2, self.ventana.get_height() // 2 - alto_ventana // 2))
                pygame.display.flip()
        elif self.nonograma_completado:
            text_surface = font.render("¡Felicidades!", True, (0, 0, 0))
            text_rect = text_surface.get_rect(
                center=(ancho_ventana // 2, 50))
            ventana_emergente.blit(text_surface, text_rect)

            text_surface = font.render(
                "Has completado el nonograma.", True, (0, 0, 0))
            text_rect = text_surface.get_rect(
                center=(ancho_ventana // 2, 100))
            ventana_emergente.blit(text_surface, text_rect)

            self.ventana.blit(ventana_emergente, (self.ventana.get_width(
            ) // 2 - ancho_ventana // 2, self.ventana.get_height() // 2 - alto_ventana // 2))
            pygame.display.flip()
        elif self.levelnonograma.getRemainingClues() == 0:
            text_surface = font.render(
                "No hay más pistas para usar.", True, (0, 0, 0))
            text_rect = text_surface.get_rect(
                center=(ancho_ventana // 2, 50))
            ventana_emergente.blit(text_surface, text_rect)

            self.ventana.blit(ventana_emergente, (self.ventana.get_width(
            ) // 2 - ancho_ventana // 2, self.ventana.get_height() // 2 - alto_ventana // 2))
            pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False

    def dibujar(self, ventana):
        self.ventana = ventana
        ventana.fill((255, 255, 255))

        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width / 2 - 400, height / 2 - 300))
        font = pygame.font.Font(None, 25)

        # Mostrar el contador de pistas
        if self.modo == GameModeEnum.ZEN:
            pistas_texto = f"Pistas restantes: {self.levelnonograma.getRemainingClues()}"
            pistas_surface = font.render(pistas_texto, True, (255, 255, 255))
            pistas_rect = pistas_surface.get_rect()
            pistas_rect.topleft = (10, 10)
            ventana.blit(pistas_surface, pistas_rect)

        # Mostrar el número de vidas restantes en el modo LIVES
        if self.modo == GameModeEnum.LIVES:
            vidas_texto = f"Vidas restantes: {self.levelnonograma.getLives()}"
            vidas_surface = font.render(vidas_texto, True, (255, 255, 255))
            vidas_rect = vidas_surface.get_rect()
            vidas_rect.topleft = (10, 40)
            ventana.blit(vidas_surface, vidas_rect)

        for row_idx, row in enumerate(self.grid.getRowsList()):
            for num_idx, num in enumerate(row):
                text_surface = font.render(str(num), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.right = self.start_x - 10 - num_idx * 20
                text_rect.centery = self.start_y + row_idx * \
                    self.cell_size + self.cell_size // 2
                ventana.blit(text_surface, text_rect)

        for col_idx, col in enumerate(self.grid.getColumnsList()):
            for num_idx, num in enumerate(col):
                text_surface = font.render(str(num), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.centerx = self.start_x + col_idx * \
                    self.cell_size + self.cell_size // 2
                text_rect.bottom = self.start_y + \
                    10 - (len(col) - num_idx) * 17
                ventana.blit(text_surface, text_rect)

        for row_idx, row in enumerate(self.levelnonograma.getCurrentGrid().getCellsList()):
            for col_idx, cell in enumerate(row):
                # self.levelnonograma.getCurrentGrid().printLists()
                if cell.CurrentState() == CellStateEnum.MARKED:
                    color = (255, 0, 0)
                    rect = pygame.Rect(self.start_x + col_idx * self.cell_size, self.start_y +
                                       row_idx * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.line(ventana, color, rect.topleft,
                                     rect.bottomright, 2)
                    pygame.draw.line(
                        ventana, color, rect.bottomleft, rect.topright, 2)
                else:
                    color = (255, 255, 255) if cell.CurrentState(
                    ) == CellStateEnum.EMPTY else (0, 0, 0)
                    rect = pygame.Rect(self.start_x + col_idx * self.cell_size, self.start_y +
                                       row_idx * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(ventana, color, rect)
                    pygame.draw.rect(ventana, (200, 200, 200), rect, 1)

        for boton in self.botones:
            boton.dibujar(ventana)

        if self.ventana_nonograma_emergente:
            self.mostrar_ventana_emergente()

        self.ventana_nonograma_emergente = False
