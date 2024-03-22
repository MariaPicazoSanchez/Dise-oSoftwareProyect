import json
from laberinto import Bomba, Este, Habitacion, Juego, Laberinto, Norte, Oeste, Puerta, Sur, Pared, Armario,Contenedor

class LaberintoBuilder:
        def __init__(self):
            self.juego = None
            self.laberinto = None

        def fabricarArmarioEn(self, unNum, unCont):
            arm = Armario(unNum)
            arm.agregarOrientacion('Norte')
            arm.agregarOrientacion('Este')
            arm.agregarOrientacion('Sur')
            arm.agregarOrientacion('Oeste')

            for orientacion in arm.orientaciones:
                arm.orientaciones[orientacion].poner_en(orientacion, self.fabricarPared(self))
            pt = self.fabricarPuerta(arm, unCont)
           

            unCont.agregarHijo(arm)
            return arm
        
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
        "suponiendo que python lee los ficheros json igual que en smallTalk"
        def fabricarBichoPosicion(self, strModo, posicion):
            hab = self.juego.obtenerHabitacion(posicion)
            if hab is not None:
                if strModo == 'Agresivo':
                    self.fabricarBichoAgresivo(hab)
                elif strModo == 'Perezoso':
                    self.fabricarBichoPerezoso(hab)

        def fabricarHabitacion(self, unNum):
            hab = Habitacion()
            hab.num = unNum
            hab.agregarOrientacion(self.fabricarNorte())
            hab.agregarOrientacion(Este().default())
            hab.agregarOrientacion(Sur().default())
            hab.agregarOrientacion(Oeste().default())

            for each in hab.orientaciones:
                hab.ponerEn(each, self.fabricarPared(self))

            self.laberinto.agregarHabitacion(hab)
            return hab

        def fabricarJuego(self):
            self.juego = Juego()
            self.juego.laberinto = self.laberinto
            self.juego.crearLaberinto()

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

            pt = self.fabricarPuertaLados(lado1, lado2)

            lado1.ponerEn(or1, pt)
            lado2.ponerEn(or2, pt)
        def obtenerJuego(self):
            return self.juego

class Director:
    def __init__(self):
        self.builder = LaberintoBuilder()
        self.diccionario = None

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()

    def fabricarLaberintoRecursivo(self, unDic, padre):
        con = None
        if unDic['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(unDic['num'])
        elif unDic['tipo'] == 'armario':
            con = self.builder.fabricarArmarioEn(unDic['num'], padre)
        

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

    def fabricarBichos(self):
        #
        bichos = self.diccionario.get('bichos',None)
        if bichos is not None:
            for bicho in bichos:
                modo = bicho.get('modo')
                posicion = bicho.get('posicion')
                self.builder.fabricarBichoPosicion(modo, posicion)
        


    


director=Director()
unCont = Contenedor()
armario = director.builder.fabricarArmarioEn(1, unCont)
