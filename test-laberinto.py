import unittest
from laberinto import Laberinto, Habitacion, Bicho, Agresivo, Perezoso, Personaje
from juego import Juego

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

    def testFabricarBichoAgresivo(self):
        habitacion = Habitacion(1)  
        bicho = self.juego.fabricarBichoAgresivo(habitacion)
        self.assertIsInstance(bicho, Bicho)
        self.assertIsInstance(bicho.modo, Agresivo)
        self.assertEqual(bicho.juego, self.juego)
        self.assertEqual(bicho.posicion, habitacion)
        self.assertEqual(bicho.vidas, 5)
        self.assertEqual(bicho.poder, 2)

    def testFabricarBichoPerezoso(self):
        habitacion = Habitacion(1)  
        bicho = self.juego.fabricarBichoPerezoso(habitacion)
        self.assertIsInstance(bicho, Bicho)
        self.assertIsInstance(bicho.modo, Perezoso)
        self.assertEqual(bicho.juego, self.juego)
        self.assertEqual(bicho.posicion, habitacion)
        self.assertEqual(bicho.vidas, 3)
        self.assertEqual(bicho.poder, 1)

    def test_agregarPersonaje(self):
        self.juego.agregarPersonaje("Juan")
        self.assertIsInstance(self.juego.person, Personaje)
        self.assertEqual(self.juego.person.nombre, "Juan")
        #hab=self.juego.obtenerHabitacion(1)
        #self.assertIn(self.juego.person, hab.hijos)

        self.assertEqual(self.juego.person.juego, self.juego)
    

if __name__ == '__main__':
    unittest.main()