import pygame
import sys
from .boton import Boton
from .panel import Panel


class Menu(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        window_width, window_height = app.ventana.get_size()
        self.botones = [
            Boton("Jugar", (window_width//2 - 100, 350), (200, 55),
                  ((0, 0, 0), (255, 255, 255)), self.ir_a_elegirTamaño),
            Boton("Tutorial", (window_width//2 - 100, 450), (200, 55),
                  ((0, 0, 0), (255, 255, 255)), self.ir_a_tutorial),
            Boton("Opciones", (window_width//2 - 100, 550), (200, 55),
                  ((0, 0, 0), (255, 255, 255)), self.ir_a_opciones),
        ]
        self.botonSalir = Boton("Salir", (0, 0), (200, 50),
                                ((0, 0, 0), (255, 255, 255)), self.salir)
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 100)
        self.fondo_imagen = pygame.image.load("Imagenes/Menu fondo.png")
        self.fondo_imagen = pygame.transform.scale(
            self.fondo_imagen, (800, 600))

    # Estas definiciones seran cuando cree class jugar, tutorial y opciones
    def ir_a_jugar(self):
        self.app.cambiar_panel(self.app.jugar)

    def ir_a_elegirTamaño(self):
        self.app.cambiar_panel(self.app.elegirTamaño)

    def ir_a_tutorial(self):
        self.app.cambiar_panel(self.app.tutorial)

    def ir_a_opciones(self):
        self.app.cambiar_panel(self.app.opciones)

    def manejar_evento(self, evento):
        for boton in self.botones:
            boton.manejar_evento(evento)
        self.botonSalir.manejar_evento(evento)

    def salir(self):
        pygame.quit()
        sys.exit()

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400, height/2-300))
        count = 0
        for boton in self.botones:
            boton.updatePosX((width//2 - 96, height//2 + 80 * count + 45))
            boton.dibujar(ventana)
            count += 1
        self.botonSalir.dibujar(ventana)
        texto = self.fuente.render("Nonograma", True, (255, 255, 255))
        ventana.blit(texto, (width / 2 - 193, height/2-145))
