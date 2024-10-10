import unittest
import pygame
from Nonogram.Code.Visual.boton import Boton


class TestBoton(unittest.TestCase):

    def setUp(self):
        # Inicializar Pygame y crear ventana de prueba
        pygame.init()
        self.ventana = pygame.display.set_mode((200, 200))

        # Variables de prueba
        self.texto = "Test"
        self.pos = (50, 50)
        self.tamano = (100, 50)
        self.colores = [(255, 0, 0), (255, 255, 255)]
        self.llamada_accion = False

        # Acción que será llamada cuando el botón se presione
        def accion():
            self.llamada_accion = True

        # Crear botón de prueba
        self.boton = Boton(self.texto, self.pos,
                           self.tamano, self.colores, accion)

    def test_dibujar_boton(self):
        # Prueba que se dibuje el botón
        self.boton.dibujar(self.ventana)
        # Simplemente verificamos que el rectángulo haya sido dibujado correctamente
        self.assertEqual(self.boton.rect.topleft, self.pos)
        self.assertEqual(self.boton.rect.size, self.tamano)

    def test_manejar_evento_click(self):
        # Crear un evento de clic dentro del área del botón
        evento = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
                                    'pos': (75, 75), 'button': 1})
        self.boton.manejar_evento(evento)

        # Verificar si la acción fue ejecutada
        self.assertTrue(self.llamada_accion)

    def test_no_ejecuta_accion_si_no_hay_click(self):
        # Crear un evento de clic fuera del área del botón
        evento = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
                                    'pos': (10, 10), 'button': 1})
        self.boton.manejar_evento(evento)

        # Verificar que la acción no fue ejecutada
        self.assertFalse(self.llamada_accion)


if __name__ == '__main__':
    unittest.main()
