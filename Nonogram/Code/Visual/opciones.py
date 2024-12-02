import pygame
from .panel import Panel
from .boton import Boton


class Opciones(Panel):
    def __init__(self, app, ventana):
        super().__init__()
        self.ventana = ventana
        self.app = app
        self.pantallacom=True
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        self.musicaOn = True
        self.canciones = [
            "Musica/C418Sweden.mp3",
            "Musica/CornfieldChase.mp3",
            "Musica/lofi.mp3"
        ]
        
        # Inicializar música
        pygame.mixer.init()
        pygame.mixer.music.load(self.canciones[1])  
        pygame.mixer.music.set_volume(0.05)  
        pygame.mixer.music.play(-1)

        # Slider de volumen
        self.slider_rect = pygame.Rect(50, 350, 200, 10)  
        self.handle_rect = pygame.Rect(50, 340, 20, 30) 
        self.volumen = 5

        self.botones = [
            Boton("C418Sweden", (400, 200), (350, 50), ((0, 0, 0), (255, 255, 255)),
                  lambda: self.cambiarMusica(self.canciones[0])),
            Boton("CornfieldChase", (400, 300), (350, 50), ((0, 0, 0), (255, 255, 255)),
                  lambda: self.cambiarMusica(self.canciones[1])),
            Boton("Lofi", (400, 400), (350, 50), ((0, 0, 0), (255, 255, 255)),
                  lambda: self.cambiarMusica(self.canciones[2])),
            Boton("Activar/Desactivar Musica", (400, 500), (350, 50), ((0, 0, 0), (255, 255, 255)),
                  self.pausarMusica),
            Boton("Pantalla completa", (10, 200), (350, 50), ((0, 0, 0), (255, 255, 255)),
                  lambda: self.pantallaCompleta())      
        ]

        # Fondo
        self.fondo_imagen = pygame.image.load("Imagenes/Opcion fondo.png")
        self.fondo_imagen = pygame.transform.scale(self.fondo_imagen, (800, 600))

    def pantallaCompleta(self):
        if self.pantallacom:
            pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
            self.pantallacom=False
        else:
            self.ventana = pygame.display.set_mode((800, 600))
            self.pantallacom=True


    def cambiarMusica(self, musica):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volumen / 100) 

    def pausarMusica(self):
        if self.musicaOn:
            self.musicaOn = False
            pygame.mixer.music.stop()
        else:
            self.musicaOn = True
            pygame.mixer.music.play(-1)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                self.app.cambiar_panel(self.app.menu)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(evento.pos):
                self.slider_dragging = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            self.slider_dragging = False
        elif evento.type == pygame.MOUSEMOTION:
            if hasattr(self, 'slider_dragging') and self.slider_dragging:
                x = max(self.slider_rect.left, min(evento.pos[0], self.slider_rect.right - self.handle_rect.width))
                self.handle_rect.x = x
                self.volumen = int(((x - self.slider_rect.left) / self.slider_rect.width) * 100)
                pygame.mixer.music.set_volume(self.volumen / 100)

        for boton in self.botones:
            boton.manejar_evento(evento)

    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        width, height = ventana.get_size()
        ventana.blit(self.fondo_imagen, (width / 2 - 400, height / 2 - 300))
        texto = self.fuente.render("Opciones", True, (255, 255, 255))
        ventana.blit(texto, (50, 30))

        pygame.draw.rect(ventana, (200, 200, 200), self.slider_rect)  
        pygame.draw.rect(ventana, (100, 100, 255), self.handle_rect)  
        texto_volumen = self.fuente.render(f"Volumen: {self.volumen}", True, (255, 255, 255))
        ventana.blit(texto_volumen, (50, 380))

        for boton in self.botones:
            boton.dibujar(ventana)
