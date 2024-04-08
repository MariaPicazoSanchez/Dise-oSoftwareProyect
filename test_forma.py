import unittest
from forma import Forma,Cuadrado
from laberinto import Contenedor, Personaje, Este

class TestCuadrado(unittest.TestCase):
    def setUp(self):
        self.cuadrado = Cuadrado()

    def test_agregarOrientacion_a_Forma(self):
        forma = Forma()
        orientacion = Este()
        forma.agregarOrientacion(orientacion)

        self.assertIn(orientacion, forma.orientaciones)

    def test_irAlEste_en_Cuadrado(self):
        cuadrado = Cuadrado()
        alguien = Personaje()
        alguien.nombre = "Juan"
        cuadrado.este = Contenedor()

        cuadrado.irAlEste(alguien)

        self.assertIn(alguien, cuadrado.este.orientaciones)

if __name__ == '__main__':
    unittest.main()