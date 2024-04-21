import unittest
from builder import LaberintoBuilder, Director, LaberintoBuilderHexagonal
from laberinto import Habitacion

class TestLaberinto(unittest.TestCase):
    def setUp(self):
        self.director = Director()
        self.director.procesar(r'C:\Users\maria\Documents\2 Ing\Diseño software\DiferentesLaberintos\1erLaberinto\laberintoHex4hab4bichos.json')
        self.dic = self.director.diccionario
        self.juego = self.director.obtener_juego()
        self.juego.agregarPersonaje('Pepito')


    def comprobarArmarioEn(self, num, unCont):
        arm = next((each for each in unCont.hijos if each.esArmario), None)
        assert arm is not None and arm.esArmario, f"No se encontró el armario {num} en el contenedor"
        return arm
    def comprobarBombaEn(self, unContenedor):
        bomba = next((each for each in unContenedor.hijos if each.es_bomba), None)
        assert bomba is not None and bomba.esBomba, "El contenedor no contiene una bomba"
    def comprobarHabitacion(self, num):
        hab = self.juego.obtenerHabitacion(num)
        self.assertEqual(hab.num, num)
        return hab
    def comprobarLaberintoRecursivo(self, unDic, padre):
        nada = True
        
        # Contenedores
        if unDic['tipo'] == 'habitacion':
            nada = False
            con = self.comprobarHabitacion(unDic['num'])
        elif unDic['tipo'] == 'armario':
            nada = False
            con = self.comprobarArmario(unDic['num'], padre)
        
        # Hojas
        elif unDic['tipo'] == 'bomba':
            nada = False
            self.comprobarBombaEn(padre)
        elif unDic['tipo'] == 'tunel':
            nada = False
            self.comprobarTunelEn(padre)
        
        lista = unDic.get('hijos', None)
        if lista is not None:
            for each in lista:
                self.comprobarLaberintoRecursivo(each, con)
        
        if nada:
            self.assertFalse(True)

    def comprobarPuertaDe(self, unNum, unaOr, otroNum, otraOr):
        unaHab = self.juego.obtenerHabitacion(unNum)
        otraHab = self.juego.obtenerHabitacion(otroNum)

        self.assertEqual(unaHab.num, unNum)
        self.assertEqual(otraHab.num, otroNum)

        or1 = getattr(self.director.builder, f'fabricar{unaOr}')()
        or2 = getattr(self.director.builder, f'fabricar{otraOr}')()

        pt1 = unaHab.obtenerElemento(or1)
        pt2 = otraHab.obtenerElemento(or2)

        self.assertTrue(pt1.esPuerta())
        self.assertTrue(pt2.esPuerta())
        self.assertEqual(pt1, pt2)

        self.assertFalse(pt1.estaAbierta())

    def comprobarTunelEn(self, unContenedor):
        tunel = next((each for each in unContenedor.hijos if each.es_tunel), None)
        assert tunel is not None and tunel.esTunel, "El contenedor no contiene un túnel"
    
    def testLaberinto(self):
        for each in self.dic['laberinto']:
            self.comprobarLaberintoRecursivo(each, 'root')

        if 'puertas' in self.dic:
            for cada in self.dic['puertas']:
                self.comprobarPuertaDe(cada[0], cada[1], cada[2], cada[3])
                
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
