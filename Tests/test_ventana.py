import unittest
from unittest.mock import Mock
import pygame
from Nonogram.Code.Visual.ventana import Aplicacion


class TestAplicacion(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.app = Aplicacion()

    def tearDown(self):
        pygame.quit()

    def test_inicializacion(self):
        self.assertIsNotNone(self.app.menu)
        self.assertEqual(self.app.panel_actual, self.app.menu)

    def test_cambiar_panel(self):
        nuevo_panel = Mock()
        self.app.cambiar_panel(nuevo_panel)
        self.assertEqual(self.app.panel_actual, nuevo_panel)


if __name__ == "__main__":
    unittest.main()
