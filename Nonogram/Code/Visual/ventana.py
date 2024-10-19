import pygame
import sys
from .menu import Menu
from .jugar import Jugar

pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

ventana = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Nonograma")


class Aplicacion:
    def __init__(self):
        # Aqui iran las distintas escenas
        self.menu = Menu(self)
        self.jugar = Jugar(self)
        # self.tutorial = Tutorial(self)
        # self.opciones = Opciones(self)
        self.panel_actual = self.menu

    def cambiar_panel(self, nuevo_panel):
        self.panel_actual = nuevo_panel

    def ejecutar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.panel_actual.manejar_evento(evento)

            self.panel_actual.dibujar(ventana)
            pygame.display.flip()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
