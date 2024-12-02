import pygame
from .panel import Panel
from .boton import Boton

class Tutorial(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.fondo_imagen = pygame.image.load("Nonogram/Imagenes/NivelFondo.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (800, 600))
    
    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)
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

        
    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

    #
