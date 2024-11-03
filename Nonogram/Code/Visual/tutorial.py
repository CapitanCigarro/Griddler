import pygame
from .panel import Panel
from .boton import Boton

class Tutorial(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.botones = [
            Boton("Pantalla completa", (300, 350), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0)),
            Boton("Tutorial", (300, 450), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0)),
            Boton("Opciones", (300, 550), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0))
        ]
    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)
    def dibujar(self, ventana):
        ventana.fill((80, 80, 80)) 
        texto = self.fuente.render("Buena suerte", True, (255, 255, 255))
        ventana.blit(texto, (220, 30))
        for boton in self.botones:
            boton.dibujar(ventana)
    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)