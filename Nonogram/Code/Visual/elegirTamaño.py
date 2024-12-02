from time import sleep

import pygame

from Code.Visual.ChooseNonogram import ChooseNonogram
from .boton import Boton
from .jugar import Jugar
from .panel import Panel
from .selectorNumero import Selector
from ..Logic.GameModeEnum import GameModeEnum
from ..Logic.Nonogram import Nonogram


class elegirTamaño(Panel):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.nonogram = Nonogram()
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.botones = []
        self.botones_tam = [
            Boton("15x15", (300, 350), (200, 50),
                  ((0, 0, 0), (255, 255, 255)), self.choose_15x15),
            Boton("10x10", (300, 450), (200, 50),
                  ((0, 0, 0), (255, 255, 255)), self.choose_10x10),
            Boton("5x5", (300, 550), (200, 50),
                  ((0, 0, 0), (255, 255, 255)), self.choose_5x5)
        ]
        self.botones_mode = [
            Boton("ZEN", (300, 350), (200, 50),
                  ((0, 0, 0), (255, 255, 255)), self.choose_modeZEN),
            Boton("VIDAS", (300, 550), (200, 50),
                  ((0, 0, 0), (255, 255, 255)), self.choose_modeVIDA)
        ]
        self.botones = self.botones_mode

        self.boton_retroceder = Boton("Retroceder", (50, 50), (200, 50),
                                      ((0, 0, 0), (255, 255, 255)), self.ir_atras)
        self.mostrar_boton_retroceder = True
        self.fondo_imagen = pygame.image.load("Imagenes/Tam fondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))

    def choose_modeVIDA(self):
        self.game_mode = GameModeEnum.LIVES
        self.botones = self.botones_tam
    def choose_modeZEN(self):
        self.game_mode = GameModeEnum.ZEN
        self.botones = self.botones_tam

    def choose_15x15(self):
        self.app.cambiar_panel(ChooseNonogram(
            self.app, "15x15", self.nonogram.gettotallevels(15), self.nonogram,self.game_mode))

    def choose_10x10(self):
        self.app.cambiar_panel(ChooseNonogram(
            self.app, "10x10", self.nonogram.gettotallevels(10), self.nonogram,self.game_mode))

    def choose_5x5(self):
        self.app.cambiar_panel(ChooseNonogram(
            self.app, "5x5", self.nonogram.gettotallevels(5), self.nonogram,self.game_mode))

    def ir_atras(self):
        if self.botones == self.botones_tam:
            self.botones = self.botones_mode
        else:
            self.ir_a_menu()

    def ir_a_menu(self):
        self.mostrar_boton_retroceder = True  # El botón de retroceder aparece
        self.botones = self.botones_mode
        self.app.cambiar_panel(self.app.menu)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if not self.mostrar_boton_retroceder:
                    # Retrocede al menú si el botón no está visible
                    self.app.cambiar_panel(self.app.menu)
                else:
                    self.ir_a_menu()
        for boton in self.botones:
            boton.manejar_evento(evento)
        if self.mostrar_boton_retroceder:
            self.boton_retroceder.manejar_evento(evento)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400, height/2-300))
        count = 0
        for boton in self.botones:
            boton.updatePosX((width//2 - 95, height//4 + 80 * count + 40))
            boton.dibujar(ventana)
            count += 1
        if self.mostrar_boton_retroceder:
            self.boton_retroceder.dibujar(ventana)
