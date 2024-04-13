import json
from laberinto import Bomba, Habitacion,Bicho,Agresivo, Perezoso, Tunel, Laberinto, Puerta, Pared, Armario,Contenedor
from juego import Juego
from orientaciones import Este, Oeste, Sur, Norte, SurEste, SurOeste, NorEste, NorOeste
from forma import Cuadrado, Hexagono
class LaberintoBuilder:
        def __init__(self):
            self.juego = None
            self.laberinto = None

        def fabricarArmarioEn(self, unNum, unCont):
            arm = Armario(unNum)
            arm = Cuadrado()
            arm.agregarOrientacion(self.fabricarNorte())
            arm.agregarOrientacion(self.fabricarEste())
            arm.agregarOrientacion(self.fabricarSur())
            arm.agregarOrientacion(self.fabricarOeste())

            for orientacion in arm.obtenerOrientaciones():
                arm.ponerElementoEn(orientacion, self.fabricarPared())
            pt = self.fabricarPuertaLados(arm, unCont)
            arm.ponerElementoEn(self.fabricarEste(), pt)
           

            unCont.agregarHijo(arm)
            return arm
        
        def fabricarBombaEn(self, unCont):
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
        
        #"suponiendo que python lee los ficheros json igual que en smallTalk"
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
            hab.forma = Cuadrado()
            hab.agregarOrientacion(self.fabricarNorte())
            hab.agregarOrientacion(self.fabricarEste())
            hab.agregarOrientacion(self.fabricarSur())
            hab.agregarOrientacion(self.fabricarOeste())

            for each in hab.obtenerOrientaciones():
                hab.ponerEn(each, self.fabricarPared())

            self.laberinto.agregarHabitacion(hab)
            return hab

        def fabricarJuego(self):
            self.juego = Juego()
            self.juego.laberinto = self.laberinto
           #self.juego.fabricarLaberinto()

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

            lado1.ponerElementoEn(or1, pt)
            lado2.ponerElementoEn(or2, pt)
        def obtenerJuego(self):
            return self.juego
        def fabricarTunelEn(self, unCont):
            tunel =Tunel()
            unCont.agregarHijo(tunel)
        def fabricarBichoAgresivo(self, unaHab):
            bicho = Bicho()
            bicho.modo = Agresivo()
            bicho.vidas=10
            bicho.poder=3
            bicho.posicion = unaHab
            self.juego.agregarBicho(bicho)
        def fabricarBichoPerezoso(self, unaHab):
            bicho = Bicho()
            bicho.modo = Perezoso()
            bicho.vidas=5
            bicho.poder=1
            bicho.posicion = unaHab
            self.juego.agregarBicho(bicho)


class Director:
    def __init__(self):
        self.builder = LaberintoBuilder()
        self.diccionario = None

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        (self.diccionario['laberinto'] or []).forEach(lambda each: self.fabricarLaberintoRecursivo(each, 'root'))

        # recorrer la colección de puertas, para poner las puertas
        for each in self.diccionario.get('puertas', []):
            self.builder.fabricarPuertaN1_or1_n2_or2(each[0], each[1], each[2], each[3])
    
    
    def fabricarLaberintoRecursivoEn(self, unDic, padre):
        con = None
        if unDic['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(unDic['num'])
        if unDic['tipo'] == 'armario':
            con = self.builder.fabricarArmarioEn(unDic['num'], padre)
        if unDic['tipo'] == 'bomba':
            con = self.builder.fabricarBombaEn(padre)
        if unDic['tipo'] == 'tunel':
            con = self.builder.fabricarTunelEn(padre)
        (self.diccionario.get('hijos') or []).forEach(lambda each: self.fabricarLaberintoRecursivo(each, con))

    def iniBuilder(self):
        forma = self.diccionario.get('forma')
        if forma == 'cuadrado':
            self.builder = LaberintoBuilder()
        elif forma == 'hexagono':
            self.builder = LaberintoBuilderHexagonal()

    def leerArchivo(self, unArchivo):
        with open(unArchivo, 'r') as file:
            self.diccionario = json.load(file)

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def fabricarBichos(self):
        #
        bichos = self.diccionario.get('bichos',None)
        if bichos is not None:
            for bicho in bichos:
                modo = bicho.get('modo')
                posicion = bicho.get('posicion')
                self.builder.fabricarBichoPosicion(modo, posicion)
    def obtenerJuego(self):
        return self.builder.obtenerJuego()

class LaberintoBuilderHexagonal(LaberintoBuilder):
    def __init__(self):
        super().__init__()

    def fabricarNoroeste(self):
        return NorOeste()

    def fabricarNoreste(self):
        return NorEste()

    def fabricarSuroeste(self):
        return SurOeste()

    def fabricarSureste(self):
        return SurEste()

    def fabricarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num = unNum
        hab.forma = Hexagono()
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarNoreste())
        hab.agregarOrientacion(self.fabricarSureste())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarSuroeste())
        hab.agregarOrientacion(self.fabricarNoroeste())

        for each in hab.orientaciones:
            hab.ponerEn(each, self.fabricarPared())

        self.laberinto.agregarHabitacion(hab)
        return hab
    


director=Director()
unCont = Contenedor()
armario = director.builder.fabricarArmarioEn(1, unCont)
