import pygame

from .panel import Panel
from .boton import Boton

class Opciones(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 74)
        ancho=800
        alto=800
        self.botones = [
            Boton("Pantalla completa", (300, 350), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0)),
            Boton("Tutorial", (300, 450), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0)),
            Boton("Opciones", (300, 550), (200, 50),
                  ((80, 80, 80), (255, 255, 255)), print(0))
        ]

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)


    def dibujar(self, ventana):
        ventana.fill((80, 80, 80)) 
        texto = self.fuente.render("Buena suerte", True, (255, 255, 255))
        ventana.blit(texto, (220, 30))
        for boton in self.botones:
            boton.dibujar(ventana)
        

    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)

    def cambiar_resolucion(self, ancho, alto):
        """Cambia la resolución de la ventana del juego."""
        self.ancho, self.alto = ancho, alto
        self.ventana = pygame.display.set_mode((self.ancho, self.alto), pygame.FULLSCREEN if self.pantalla_completa else 0)
        print(f"Resolución cambiada a: {self.ancho}x{self.alto}")

    def cambiar_volumen(self, nuevo_volumen):
        """Ajusta el volumen de la música."""
        self.volumen = max(0.0, min(1.0, nuevo_volumen))  # Asegura que el volumen esté entre 0 y 1
        pygame.mixer.music.set_volume(self.volumen)
        print(f"Volumen cambiado a: {self.volumen}")

    def iniciar_musica(self, ruta_musica):
        """Inicia la reproducción de la música."""
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1)  # Repetición indefinida

    def pausar_reanudar_musica(self):
        """Pausa o reanuda la música según su estado actual."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Música pausada")
        else:
            pygame.mixer.music.unpause()
            print("Música reanudada")

    def detener_musica(self):
        """Detiene la música."""
        pygame.mixer.music.stop()
        print("Música detenida")