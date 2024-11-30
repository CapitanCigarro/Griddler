import pygame


class Boton:
    def __init__(self, texto, pos, tamano, colores, accion):
        self.texto = texto
        self.pos = pos
        self.tamano = tamano
        self.colores = colores
        self.firstcolor = colores
        self.seconcolor = ((100,0,0),(255,255,255))
        self.accion = accion
        self.rect = pygame.Rect(pos, tamano)
        self.fuente = pygame.font.Font(None, 50)

    def changefontsize(self,size):
        self.fuente = pygame.font.Font(None,size)

    def dibujar(self, ventana):
        color_fondo, color_texto = self.colores
        pygame.draw.rect(ventana, color_fondo, self.rect)
        texto_renderizado = self.fuente.render(self.texto, True, color_texto)
        ventana.blit(texto_renderizado, texto_renderizado.get_rect(
            center=self.rect.center))

    def updatePosX(self,pos):
        self.rect = pygame.Rect(pos, self.tamano)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.rect.collidepoint(evento.pos):
                self.accion()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colores = self.seconcolor
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colores = self.firstcolor
