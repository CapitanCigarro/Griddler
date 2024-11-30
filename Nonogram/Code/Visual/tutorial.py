import pygame
from .panel import Panel
from .boton import Boton

class Tutorial(Panel):
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
        
    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)