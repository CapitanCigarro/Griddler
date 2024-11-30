from math import factorial

from select import select

from .boton import Boton
import pygame

class LevelButton:
    
    def __init__(self, number, position, size, colour, action, relatedNonogram, app,imag:bool):
        self.with_imagen = imag
        self.position = position
        self.size = size
        self.number = number
        self.colour = colour
        self.firstcolor =colour
        self.seconcolor = ((100,0,0),(255,255,255))
        self.action = action
        self.app = app
        self.nonogram = relatedNonogram
        x,y = position
        if imag == True:
            imagoffset = 25
        else:
            imagoffset = 0
        self.rect = pygame.Rect((x+imagoffset,y+imagoffset), (size))
        self.text = pygame.font.Font(None, 74)
        self.fondo_imagen = pygame.image.load("Imagenes/BotonNiveles.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (100, 100))

    def draw(self, ventana):
        color_fondo, color_texto = self.colour
        if self.with_imagen == True:
            ventana.blit(self.fondo_imagen, self.position)
        pygame.draw.rect(ventana, color_fondo, self.rect)
        texto_renderizado = self.text.render(self.number, True, color_texto)
        ventana.blit(texto_renderizado, texto_renderizado.get_rect(
            center=self.rect.center))
        
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.app.cambiar_panel(self.nonogram)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colour = self.seconcolor
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colour = self.firstcolor
