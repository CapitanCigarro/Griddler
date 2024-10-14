import pygame

class Menu:
    def __init__(self, ventana):
        self.ventana = ventana 
        self.running = True

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.boton_rect = pygame.Rect(self.ventana.width // 2 - 100, self.ventana.height // 2 + 100, 200, 50)

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.boton_rect.collidepoint(pos):
                    print("Botón del menú presionado.")
                    self.running = False 

    def dibujar(self):
        self.ventana.screen.fill(self.BLACK)

        font = pygame.font.Font(None, 74)
        texto = font.render('Menú Principal', True, self.WHITE)
        text_rect = texto.get_rect(center=(self.ventana.width // 2, self.ventana.height // 2))
        self.ventana.screen.blit(texto, text_rect)

        pygame.draw.rect(self.ventana.screen, self.WHITE, self.boton_rect)
        pygame.display.flip()

    def iniciar(self):
        while self.running:
            self.manejar_eventos()
            self.dibujar()