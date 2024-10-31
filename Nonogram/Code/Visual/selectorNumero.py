import pygame
from pygame.display import update

from Nonogram.Code.Visual.boton import Boton

class Selector:
    __pos = (0,0)
    __tam = (50,50)

    __max = 0
    __valor = 0
    __colores =((80, 80, 80), (255, 255, 255))

    def __init__(self,x:int,y:int,max:int):
        self.__pos = (x,y)
        self.__posText = (x+50,y)
        self.__max = max
        self.rect = pygame.Rect(self.__posText, self.__tam)

        self.botonrestar = Boton("<",(x,y),self.__tam,self.__colores,self.restar)
        self.botonsumar = Boton(">",(x+100,y),self.__tam,self.__colores,self.sumar)
        self.fuente = pygame.font.Font(None, 54)

    def restar(self):
        if self.__valor > 0:
            self.__valor -= 1
            self.dibujartexto(self.ventana)

    def sumar(self):
        if self.__valor < self.__max:
            self.__valor += 1
            self.dibujartexto(self.ventana)

    def getvalor(self):
        return self.__valor

    def manejar_evento(self,evento):
        self.botonsumar.manejar_evento(evento)
        self.botonrestar.manejar_evento(evento)

    def dibujar(self,ventana):
        self.ventana = ventana
        self.botonsumar.dibujar(ventana)
        self.botonrestar.dibujar(ventana)
        self.dibujartexto(ventana)

    def dibujartexto(self,ventana):
        texto_renderizado = self.fuente.render(str(self.__valor), True, (255,255,255))
        self.ventana.blit(texto_renderizado, texto_renderizado.get_rect(
            center=self.rect.center))
