import pygame
from .boton import Boton
from .panel import Panel


class Jugar(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80)) 
        texto = self.fuente.render("Buena suerte", True, (255, 255, 255))
        ventana.blit(texto, (220, 30))