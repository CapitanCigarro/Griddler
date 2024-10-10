import pygame
from .boton import Boton
from .panel import Panel


class Menu(Panel):
    def __init__(self, app):
        super().__init__()
        self.app = app
