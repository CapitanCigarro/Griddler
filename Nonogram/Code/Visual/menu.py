import pygame
from .boton import Boton
from .panel import Panel
from .jugar import Jugar


class Menu(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.botones = [
            Boton("Jugar", (300, 350), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_elegirTamaño),
            Boton("Tutorial", (300, 450), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_tutorial),
            Boton("Opciones", (300, 550), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_opciones)
        ]
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 100)

    # Estas definiciones seran cuando cree class jugar, tutorial y opciones
    def ir_a_jugar(self):
        self.app.cambiar_panel(self.app.jugar)

    def ir_a_elegirTamaño(self):
        self.app.cambiar_panel(self.app.elegirTamaño)

    def ir_a_tutorial(self):
        self.app.cambiar_panel(self.app.tutorial)

    def ir_a_opciones(self):
        self.app.cambiar_panel(self.app.opciones)

    def manejar_evento(self, evento):
        for boton in self.botones:
            boton.manejar_evento(evento)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        for boton in self.botones:
            boton.dibujar(ventana)

        texto = self.fuente.render("Nonograma", True, (255, 255, 255))
        ventana.blit(texto, (220, 200))
