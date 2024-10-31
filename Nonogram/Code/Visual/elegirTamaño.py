import pygame
from .boton import Boton
from .jugar import Jugar
from .panel import Panel
from .selectorNumero import Selector
from ..Logic.Nonogram import Nonogram


class elegirTamaño(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.nonogram = Nonogram()
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.botones = [
            Boton("15x15", (300, 350), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_jugar15x15),
            Boton("10x10", (300, 450), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_jugar10x10),
            Boton("5x5", (300, 550), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_jugar5x5)
        ]
        self.selectores = [
            Selector(550,350,self.nonogram.gettotallevels(15)),
            Selector(550, 450, self.nonogram.gettotallevels(10)),
            Selector(550, 550, self.nonogram.gettotallevels(5))
        ]
        self.boton_retroceder = Boton("Retroceder", (50, 50), (200, 50),
                                      ((80, 80, 80), (255, 255, 255)), self.ir_a_menu)
        self.mostrar_boton_retroceder = True

    def ir_a_jugar15x15(self):
        self.mostrar_boton_retroceder = False  # El botón de retroceder desaparece
        self.app.cambiar_panel(Jugar(self.app,self.nonogram.getgridActual(15,self.selectores[0].getvalor())))
    def ir_a_jugar10x10(self):
        self.mostrar_boton_retroceder = False  # El botón de retroceder desaparece
        self.app.cambiar_panel(Jugar(self.app,self.nonogram.getgridActual(10,self.selectores[1].getvalor())))
    def ir_a_jugar5x5(self):
        self.mostrar_boton_retroceder = False  # El botón de retroceder desaparece
        self.app.cambiar_panel(Jugar(self.app,self.nonogram.getgridActual(5, self.selectores[2].getvalor())))

    def ir_a_menu(self):
        self.mostrar_boton_retroceder = True  # El botón de retroceder aparece
        self.app.cambiar_panel(self.app.menu)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if not self.mostrar_boton_retroceder:
                    # Retrocede al menú si el botón no está visible
                    self.app.cambiar_panel(self.app.menu)
                else:
                    self.ir_a_menu()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                boton.manejar_evento(evento)
            for selector in self.selectores:
                selector.manejar_evento(evento)
            if self.mostrar_boton_retroceder:
                self.boton_retroceder.manejar_evento(evento)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        for boton in self.botones:
            boton.dibujar(ventana)
        for selector in self.selectores:
            selector.dibujar(ventana)
        if self.mostrar_boton_retroceder:
            self.boton_retroceder.dibujar(ventana)
