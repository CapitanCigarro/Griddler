import pygame
import sys
from .menu import Menu
from .jugar import Jugar
from .elegirTamaño import elegirTamaño
from .opciones import Opciones
from .tutorial import Tutorial

pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Nonograma")


class Aplicacion:
    def __init__(self):
        # Aqui iran las distintas escenas
        self.menu = Menu(self)
        self.jugar: Jugar
        self.elegirTamaño = elegirTamaño(self)
        self.opciones = Opciones(self)
        self.tutorial = Tutorial(self)
        self.panel_actual = self.menu

    def cambiar_panel(self, nuevo_panel):
        self.panel_actual = nuevo_panel

    def ejecutar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.K_F11:
                    self.ventana = pygame.display.set_mode((self.ancho, self.alto), pygame.FULLSCREEN )
                self.panel_actual.manejar_evento(evento)

            self.panel_actual.dibujar(ventana)
            pygame.display.flip()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
