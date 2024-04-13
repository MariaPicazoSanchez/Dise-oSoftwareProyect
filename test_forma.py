import unittest
from forma import Forma,Cuadrado, Hexagono
from laberinto import Contenedor, Personaje
from orientaciones import Este

class TestForma(unittest.TestCase):
    def setUp(self):
        pass

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

    def test_irAlEste(self):
        hexagono = Hexagono()
        hexagono.este = Forma()
        with self.assertRaises(AttributeError):
            hexagono.irAlEste("alguien")
            
if __name__ == '__main__':
    unittest.main()