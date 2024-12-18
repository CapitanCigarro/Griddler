import pygame

from .boton import Boton
from .jugar import Jugar

from .levelButton import LevelButton

# from Code.Visual.ventana import Aplicacion
from .panel import Panel
from ..Logic.GameModeEnum import GameModeEnum
from ..Logic.Grid import Grid
from ..Logic.Level import Level


class ChooseNonogram(Panel):

    def __init__(self, app, size: str, levels: int, nonogram, mode:GameModeEnum) -> None:
        grid: int

        match size:
            case "15x15":
                grid = 15

            case "10x10":
                grid = 10

            case "5x5":
                grid = 5

        super().__init__()
        self.app = app
        pygame.font.init()
        self.font = pygame.font.Font(None, 74)
        self.size = size
        self.levelsButtons = []
        action = app.cambiar_panel
        for i in range(levels):
            relatedNonogram = Jugar(self.app, nonogram.getgridActual(grid, i),mode)
            level = LevelButton(str(i + 1), (20 + (i % 7) * 100 + (i % 7) * 10, 60 + (i // 7) * 100 + (i // 7) * 10),
                                (50, 50), ((0, 0, 0), (255, 255, 255)), action, relatedNonogram, app, True)
            self.levelsButtons.append(level)

        # Creador de nivel
        emptyList = []
        for i in range(grid):
            emptyList.append([0]*grid)
        emptyNonogram = Jugar(self.app, Grid(emptyList),GameModeEnum.CREATIVO)
        emptyNonogram.modo_creativo(
            nonogram.getlectornivel(grid), emptyList, grid)
        width, height = app.ventana.get_size()
        createLevelButton = LevelButton("Crear", (width - 200, height - 50),
                                        (200, 50), ((0, 0, 0), (255, 255, 255)), action, emptyNonogram, app, False)
        self.levelsButtons.append(createLevelButton)
        self.fondo_imagen = pygame.image.load("Imagenes/Niveles fondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))

        self.boton_retroceder = Boton("Retroceder", (0, 0), (200, 50),
                                      ((0, 0, 0), (255, 255, 255)), self.ir_atras)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.app.cambiar_panel(self.app.menu)

        for level in self.levelsButtons:
            level.manejar_evento(evento)
        self.boton_retroceder.manejar_evento(evento)

    def ir_atras(self):
        self.app.cambiar_panel(self.app.panel_anterior)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400, height/2-300))
        for level in self.levelsButtons:
            level.draw(ventana)

        self.boton_retroceder.dibujar(ventana)

    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)
