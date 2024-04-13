import unittest
from builder import LaberintoBuilder, Director, LaberintoBuilderHexagonal
from laberinto import Habitacion

class TestLaberintoBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = LaberintoBuilder()

    def test_fabricarHabitacion(self):
        habitacion = self.builder.fabricarHabitacion(1)
        self.assertIsNotNone(habitacion)
        # Agrega más aserciones para verificar otros aspectos de la creación de habitaciones

    def test_fabricarPuertaLados(self):
        habitacion1 = Habitacion()
        habitacion2 = Habitacion()
        puerta = self.builder.fabricarPuertaLados(habitacion1, habitacion2)
        self.assertIsNotNone(puerta)
        self.assertEqual(puerta.lado1, habitacion1)
        self.assertEqual(puerta.lado2, habitacion2)
        # Agrega más aserciones para verificar otros aspectos de la creación de puertas

    # Agrega más tests para otros métodos de LaberintoBuilder

class TestDirector(unittest.TestCase):
    def setUp(self):
        self.director = Director()

    def test_fabricarJuego(self):
        self.director.fabricarJuego()
        juego = self.director.obtenerJuego()
        self.assertIsNotNone(juego)
        # Agrega más aserciones para verificar otros aspectos de la creación del juego

    def test_fabricarLaberinto(self):
        self.director.fabricarLaberinto()
        laberinto = self.director.builder.laberinto
        self.assertIsNotNone(laberinto)
        # Agrega más aserciones para verificar otros aspectos de la creación del laberinto

    # Agrega más tests para otros métodos de Director

if __name__ == '__main__':
    unittest.main()
