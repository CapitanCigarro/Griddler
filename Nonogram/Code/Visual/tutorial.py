import pygame
from .panel import Panel
from .boton import Boton

class Tutorial(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        window_width, window_height = app.ventana.get_size()
        self.botones = [
            Boton("SIGUIENTE", (440, 540), (350, 50), ((0, 0, 0), (255, 255, 255)), self.ir_a_tutorial1)
        ]
        self.fondo_imagen = pygame.image.load("Nonogram/Imagenes/Tutorial_fondo.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (800, 600))
    
    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.app.cambiar_panel(self.app.menu)
        for boton in self.botones:
            boton.manejar_evento(evento)
    def ir_a_tutorial1(self):
        self.app.cambiar_panel(self.app.tutorial1)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80)) 
        width, height =  ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400,height/2-300))

        self.fuente_tutorial=pygame.font.Font(None,20)
        texto = "En este juego resolverás rompecabezas pintando y tachando celdas para formar una imagen oculta"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 20))
        texto= "Haz clic **izquierdo** para pintar una celda, y haz **clic derecho** para tachar una celda (indicar que está vacía)"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 35))
        texto= "Cada número indica cuántas celdas consecutivas debes pintar en esa fila o columna."
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 50))
        texto= "Por ejemplo, '3' significa que hay un bloque de 3 celdas pintadas."
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 65))
        texto= "Si hay varios números, como '2 1', habrá un bloque de 2 celdas y otro de 1, separados por al menos 1 celda vacía"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 80))
        texto= "Si necesitas ayuda, apretas el botón de pista, y luego apretas una casilla, revelando esta ultima"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 95))

        

        self.imagen1= pygame.image.load("Nonogram/Imagenes/Tutorial1.png")
        self.imagen2= pygame.image.load("Nonogram/Imagenes/Tutorial2.png")

        self.fondo_imagen1 = pygame.transform.scale(self.imagen1, (380, 285))
        self.fondo_imagen2 = pygame.transform.scale(self.imagen2, (380, 285))
        
        ventana.blit(self.fondo_imagen1,(10,200))
        ventana.blit(self.fondo_imagen2,(410,200))

        texto= "Rellenas primero los de 5 ya que es el tamaño maximo"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (10, 170))
        texto= "Rellenas los 3 bloques continuos que se señala arriba"
        ventana.blit(self.fuente_tutorial.render(texto,True,(255, 255, 255)), (410, 170))

        for boton in self.botones:
            boton.dibujar(ventana)

        
    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

