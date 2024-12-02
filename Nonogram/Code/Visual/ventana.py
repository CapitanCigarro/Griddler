import pygame
import sys
from .menu import Menu
from .jugar import Jugar
from .elegirTamaño import elegirTamaño
from .opciones import Opciones
from .tutorial import Tutorial
from .tutorial1 import tutorial1


pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

class Aplicacion:
    def __init__(self):
        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("Nonograma")
        # Aqui iran las distintas escenas
        self.menu = Menu(self)
        self.tutorial1 = tutorial1(self)
        self.jugar: Jugar
        self.elegirTamaño = elegirTamaño(self)
        self.opciones = Opciones(self,self.ventana)
        self.tutorial = Tutorial(self)
        self.panel_actual = self.menu
        self.panel_anterior = self.menu

    def cambiar_panel(self, nuevo_panel):
        self.panel_anterior = self.panel_actual
        self.panel_actual = nuevo_panel

        if nuevo_panel == self.elegirTamaño:
            self.panel_actual.__init__(self)

    def ejecutar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.K_F11:
                    self.ventana = pygame.display.set_mode((self.ancho, self.alto), pygame.FULLSCREEN )
                self.panel_actual.manejar_evento(evento)

            self.panel_actual.dibujar(self.ventana)
            pygame.display.flip()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
