import pygame
import sys
from Nonogram.Code.Visual.menu import Menu
from Nonogram.Code.Visual.jugar import Jugar
from Nonogram.Code.Visual.elegirTamaño import elegirTamaño

pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Nonograma")


class Aplicacion:
    def __init__(self):
        # Aqui iran las distintas escenas
        self.menu = Menu(self)
        self.jugar : Jugar
        self.elegirTamaño = elegirTamaño(self)
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