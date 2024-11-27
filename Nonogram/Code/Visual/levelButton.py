from .boton import Boton
import pygame

class LevelButton:
    
    def __init__(self, number, position, size, colour, action, relatedNonogram, app):
        self.position = position
        self.size = size
        self.number = number
        self.colour = colour
        self.action = action
        self.app = app
        self.nonogram = relatedNonogram
        self.rect = pygame.Rect((position), (size))
        self.text = pygame.font.Font(None, 74)
        
    def draw(self, ventana):
        color_fondo, color_texto = self.colour
        pygame.draw.rect(ventana, color_fondo, self.rect)
        texto_renderizado = self.text.render(self.number, True, color_texto)
        ventana.blit(texto_renderizado, texto_renderizado.get_rect(
            center=self.rect.center))
        
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.app.cambiar_panel(self.nonogram)
                