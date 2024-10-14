from .menu import Menu 
import pygame 

class Ventana:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Juego')

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def iniciar(self):
        menu = Menu(self)  
        menu.iniciar()    