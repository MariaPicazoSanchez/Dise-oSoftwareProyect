import json
from laberinto import Bomba, Este, Habitacion, Juego, Laberinto, Norte, Oeste, Puerta, Sur, Pared, Armario

class LaberintoBuilder:
        def __init__(self):
            self.juego = None
            self.laberinto = None

        def fabricarArmario(self, unNum, unCont):
            arm = Armario()
            arm.num = unNum
            arm.agregarOrientacion(self.fabricarNorte())
            arm.agregarOrientacion(Este().default())
            arm.agregarOrientacion(Sur().default())
            arm.agregarOrientacion(Oeste().default())

            for each in arm.orientaciones:
                arm.ponerEn(each, self.fabricarPared())

            pt = self.fabricarPuertaLado1(arm, unCont)
            arm.ponerEn(Este().default(), pt)

            unCont.agregarHijo(arm)
        def fabricarBomba(self, unCont):
            bom = Bomba()
            unCont.agregarHijo(bom)

        def fabricarEste(self):
            return Este()

        def fabricarNorte(self):
            return Norte()

        def fabricarOeste(self):
            return Oeste()

        def fabricarSur(self):
            return Sur()

        def fabricarHabitacion(self, unNum):
            hab = Habitacion()
            hab.num = unNum
            hab.agregarOrientacion(self.fabricarNorte())
            hab.agregarOrientacion(Este().default())
            hab.agregarOrientacion(Sur().default())
            hab.agregarOrientacion(Oeste().default())

            for each in hab.orientaciones:
                hab.ponerEn(each, self.fabricarPared())

            self.laberinto.agregarHabitacion(hab)
            return hab

        def fabricarJuego(self):
            self.juego = Juego()
            self.juego.laberinto = self.laberinto
            self.juego.abricarLaberinto()

        def fabricarLaberinto(self):
            self.laberinto = Laberinto()
            
        def fabricarPared(self):
            return Pared()
        
        def fabricarPuertaLados(self, unaHab, otraHab):
            puerta = Puerta()
            puerta.lado1 = unaHab
            puerta.lado2 = otraHab

            return puerta

        def fabricarPuertaN1_or1_n2_or2(self, unNum, unaOrString, otroNum, otraOrString):
            lado1 = self.laberinto.obtenerHabitacion(unNum)
            lado2 = self.laberinto.obtenerHabitacion(otroNum)
            or1 = getattr(self, 'fabricar' + unaOrString)()
            or2 = getattr(self, 'fabricar' + otraOrString)()

            pt = self.fabricarPuertaLado1(lado1, lado2)

            lado1.ponerEn(or1, pt)
            lado2.ponerEn(or2, pt)

class Director:
    def __init__(self, builder, diccionario):
        self.builder = builder
        self.diccionario = diccionario

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()

    def fabricarLaberintoRecursivo(self, unDic, padre):
        con = None
        if unDic['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(unDic['num'])
        elif unDic['tipo'] == 'armario':
            con = self.builder.fabricarArmario(unDic['num'], padre)
        # Add more conditions for other types if needed

    def iniBuilder(self):
        self.builder = LaberintoBuilder()

    def leerArchivo(self, unArchivo):
        with open(unArchivo, 'r') as file:
            self.diccionario = json.load(file)

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        


    


director=Director()
