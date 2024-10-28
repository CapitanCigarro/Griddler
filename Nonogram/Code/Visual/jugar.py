import pygame
from Griddler.Nonogram.Code.Logic import Nonogram
from Griddler.Nonogram.Code.Logic import Cell
from Griddler.Nonogram.Code.Logic import CellStateEnum


class Jugar:
    def __init__(self, app):
        self.app = app
        self.nonograma = Nonogram(10, 10)  # Ejemplo de un nonograma de 10x10
        self.botones = [
            Boton("Retroceder", (50, 50), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), self.ir_a_menu)
        ]

    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.ir_a_menu()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                boton.manejar_evento(evento)
            # Manejar clics en el nonograma
            pos = pygame.mouse.get_pos()
            self.nonograma.manejar_clic(pos)

    def dibujar(self, ventana):
        ventana.fill((255, 255, 255))
        for boton in self.botones:
            boton.dibujar(ventana)
        self.nonograma.dibujar(ventana)


class Boton:
    def __init__(self, texto, pos, tamano, colores, accion):
        self.texto = texto
        self.pos = pos
        self.tamano = tamano
        self.colores = colores
        self.accion = accion
        self.rect = pygame.Rect(pos, tamano)
        self.fuente = pygame.font.Font(None, 36)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.accion()

    def dibujar(self, ventana):
        color_fondo = self.colores[0]
        color_texto = self.colores[1]
        pygame.draw.rect(ventana, color_fondo, self.rect)
        texto_superficie = self.fuente.render(self.texto, True, color_texto)
        ventana.blit(texto_superficie, self.rect.topleft)
