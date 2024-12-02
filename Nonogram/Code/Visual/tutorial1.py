import pygame
from .boton import Boton
from .panel import Panel


class tutorial1(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 100)
        self.fondo_imagen = pygame.image.load("Imagenes/Tutorial_fondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.app.cambiar_panel(self.app.tutorial)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400, height/2-300))

        self.imagen3 = pygame.image.load("Imagenes/Tutorial3.png")
        self.imagen4 = pygame.image.load("Imagenes/Tutorial4.png")

        self.fondo_imagen3 = pygame.transform.scale(self.imagen3, (380, 285))
        self.fondo_imagen4 = pygame.transform.scale(self.imagen4, (380, 285))

        ventana.blit(self.fondo_imagen3, (10, 200))
        ventana.blit(self.fondo_imagen4, (410, 200))
