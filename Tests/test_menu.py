import unittest
from unittest.mock import Mock, patch
import pygame
from Nonogram.Code.Visual.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.app_mock = Mock()  # Crear un mock para la aplicación
        self.menu = Menu(self.app_mock)  # Instanciar el menú
        for boton in self.menu.botones:
            boton.manejar_evento = Mock()

    def tearDown(self):
        pygame.quit()

    def test_inicializacion(self):
        # Verifica que los botones se inicialicen correctamente
        self.assertEqual(len(self.menu.botones), 3)
        self.assertEqual(self.menu.botones[0].texto, "Jugar")
        self.assertEqual(self.menu.botones[1].texto, "Tutorial")
        self.assertEqual(self.menu.botones[2].texto, "Opciones")

    def test_ir_a_jugar(self):
        self.menu.ir_a_jugar()
        self.app_mock.cambiar_panel.assert_called_once_with(
            self.app_mock.jugar)

    def test_ir_a_tutorial(self):
        self.menu.ir_a_tutorial()
        self.app_mock.cambiar_panel.assert_called_once_with(
            self.app_mock.tutorial)

    def test_ir_a_opciones(self):
        self.menu.ir_a_opciones()
        self.app_mock.cambiar_panel.assert_called_once_with(
            self.app_mock.opciones)

    @patch('pygame.event.get')
    def test_manejar_evento(self, mock_event_get):
        # Simula un evento MOUSEBUTTONDOWN con el atributo 'pos'
        mock_evento = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
            'pos': (100, 100), 'button': 1
        })
        mock_event_get.return_value = [mock_evento]

        # Llama al método manejar_evento
        self.menu.manejar_evento(mock_evento)

        # Aserciones para verificar que cada botón maneje el evento
        for boton in self.menu.botones:
            boton.manejar_evento.assert_called_with(mock_evento)


if __name__ == "__main__":
    unittest.main()
