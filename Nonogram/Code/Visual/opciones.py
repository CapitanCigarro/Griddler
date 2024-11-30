import pygame
from .panel import Panel
from .boton import Boton
from .selectorNumero import Selector

class Opciones(Panel):
    def __init__(self, app,ventana):
        super().__init__()
        self.ventana=ventana
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.pantalla_completa = False

        self.botones = [
            Boton("Pantalla completa", (150, 250), (350, 50), ((0, 0, 0), (255, 255, 255)), self.toggle_fullscreen),
            Boton("Aplicar Resolución", (150, 350), (350, 50), ((0, 0, 0), (255, 255, 255)), self.aplicar_resolucion)
        ]
        self.resoluciones = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
        self.resolucion_selector = Selector(640, 350, len(self.resoluciones) - 1)
        self.fondo_imagen = pygame.image.load("Imagenes/Opcion fondo.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (800, 600))

    def manejar_evento(self, evento):
        self.resolucion_selector.manejar_evento(evento)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)
        # Llama a los eventos de los botones
        for boton in self.botones:
            boton.manejar_evento(evento)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height =  ventana.get_size()
        ventana.blit(self.fondo_imagen, (width/2-400,height/2-300))
        texto = self.fuente.render("Opciones", True, (255, 255, 255))
        ventana.blit(texto, (50, 30))

        # Dibuja los botones
        for boton in self.botones:
            boton.dibujar(ventana)

        resolucion_actual = self.resoluciones[self.resolucion_selector.getvalor()]
        texto_resolucion = self.fuente.render(f"Resolución: {resolucion_actual[0]} x {resolucion_actual[1]}", True, (255, 255, 255))
        ventana.blit(texto_resolucion, (20, 150))
        self.resolucion_selector.dibujar(ventana)

    def toggle_fullscreen(self):
        if self.pantalla_completa:
            # Cambiar a modo ventana
            self.ventana = pygame.display.set_mode((800, 800))  # O cualquier resolución que desees
            self.pantalla_completa = False
        else:
            # Cambiar a pantalla completa
            self.ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.pantalla_completa = True

    def aplicar_resolucion(self):
        nueva_resolucion = self.resoluciones[self.resolucion_selector.getvalor()]
        
        pygame.display.set_mode((nueva_resolucion[0], nueva_resolucion[1]))