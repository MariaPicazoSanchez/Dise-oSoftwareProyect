import unittest
from laberinto import Maze, Game, Room

class TestJuego(unittest.TestCase):
    def setUp(self):
        self.juego=Game()
        self.maze=Maze()
        self.juego.make4Rooms4BichosFM()
        

    def testHabitaciones(self):
        hab1 = self.juego.obtenerHabitacion(1)

        self.assertEqual(hab1.num, 1)
        self.assertTrue(isinstance(hab1, Room))  
        self.assertTrue(hab1.sur.esPuerta())
        self.assertTrue(hab1.este.esPuerta())
        self.assertTrue(hab1.norte.esPared())
        self.assertTrue(hab1.oeste.esPared())

    def testInicial(self):
        self.assertIsNotNone(self.juego)
        self.assertIsNotNone(self.juego.maze)
        self.assertEqual(self.juego.maze.numeroHabitaciones(), 4)
        self.assertEqual(len(self.juego.bichos), 4)

if __name__ == '__main__':
    unittest.main()