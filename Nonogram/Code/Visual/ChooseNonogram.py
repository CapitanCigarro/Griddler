import pygame

from .jugar import Jugar

from .levelButton import LevelButton

#from Code.Visual.ventana import Aplicacion
from .panel import Panel


class ChooseNonogram(Panel):
    
    def __init__(self, app, size : str, levels : int, nonogram) -> None:
        grid : int
        
        match size:
            case "15x15":
                grid = 15
                
            case "10x10":
                grid = 10
            
            case "5x5":
                grid = 5
                
        super().__init__()
        self.app = app
        pygame.font.init()
        self.font = pygame.font.Font(None, 74)
        self.size = size
        self.levelsButtons = []
        print(levels)
        for i in range(levels):
            action = app.cambiar_panel
            relatedNonogram = Jugar(self.app, nonogram.getgridActual(grid, i))
            level = LevelButton(str(i + 1), (20 + i * 50 + i * 10, 20 + (i // 10) * 50 + (i // 10) * 10),
                                (50, 50), ((80, 80, 80), (255, 255, 255)), action, relatedNonogram, app)
            self.levelsButtons.append(level)
        
        
    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE: 
                self.app.cambiar_panel(self.app.menu)
        
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for level in self.levelsButtons:
                level.manejar_evento(evento)
            
    def dibujar(self, ventana):
        ventana.fill((80, 80, 80))
        for level in self.levelsButtons:
            level.draw(ventana)
        
    def ir_a_menu(self):
        self.app.cambiar_panel(self.app.menu)