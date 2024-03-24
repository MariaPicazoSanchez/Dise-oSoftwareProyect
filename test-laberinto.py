import unittest
from laberinto import Juego, Laberinto, Habitacion

class TestJuego(unittest.TestCase):
    def setUp(self):
        self.juego=Juego()
        self.laberinto=Laberinto()
        self.juego.fabLab4Hab4BichosFM()
        

    def testHabitaciones(self):
        hab1 = self.juego.obtenerHabitacion(1)
        self.assertEqual(hab1.num, 1)
        self.assertTrue(isinstance(hab1, Habitacion))  
        self.assertTrue(hab1.sur.esPuerta())
        self.assertTrue(hab1.este.esPuerta())
        self.assertTrue(hab1.norte.esPared())
        self.assertTrue(hab1.oeste.esPared())

    def testInicial(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.laberinto)
        self.assertEqual(self.juego.laberinto.numeroHabitaciones(), 4)
        self.assertEqual(len(self.juego.bichos), 4)

if __name__ == '__main__':
    unittest.main()