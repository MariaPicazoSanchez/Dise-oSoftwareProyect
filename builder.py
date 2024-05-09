import json
from laberinto import Bomba, Habitacion,Bicho,Agresivo, Perezoso, Tunel, Laberinto, Puerta, Pared, Armario,Contenedor
from juego import Juego
from orientaciones import Este, Oeste, Sur, Norte, SurEste, SurOeste, NorEste, NorOeste
from laberinto import Cuadrado, Hexagono
from comandos import Abrir
import keyboard
class LaberintoBuilder:
        def __init__(self):
            self.juego = None
            self.laberinto = None

        def fabricarArmarioEn(self, unNum, unCont):
            arm = Armario(unNum)
            arm.forma = self.fabricarForma()
            arm.forma.num = unNum
            for orientacion in arm.obtenerOrientaciones():
                arm.ponerElementoEn(orientacion, self.fabricarPared())

            pt = self.fabricarPuertaLados(arm, unCont)
            orAl = arm.forma.obtenerOrientacionAleatoria()
            arm.ponerElementoEn(orAl, pt)
           
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
        def fabricarBichoPosicion(self, strModo, unaHab):
            hab = self.juego.obtenerHabitacion(unaHab)
            if hab is not None:
                if strModo == 'Agresivo':
                    self.fabricarBichoAgresivo(hab)
                elif strModo == 'Perezoso':
                    self.fabricarBichoPerezoso(hab)

        def fabricarHabitacion(self, unNum):
            hab = Habitacion(unNum)
            hab.forma = self.fabricarForma()
            hab.forma.num = unNum
            #hab.agregarOrientacion(self.fabricarNorte())
            #hab.agregarOrientacion(self.fabricarEste())
            #hab.agregarOrientacion(self.fabricarSur())
            #hab.agregarOrientacion(self.fabricarOeste())

            for each in hab.obtenerOrientaciones():
                hab.ponerElementoEn(each, self.fabricarPared())

            self.laberinto.agregarHabitacion(hab)
            return hab

        def fabricarJuego(self):
            self.juego = Juego()
            self.juego.prototipo = self.laberinto
            self.juego.laberinto = self.juego.clonarLaberinto()
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
            pt.agregarComando(Abrir(pt))
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
            bicho.juego = self
            bicho.vidas=10
            bicho.poder=3
            bicho.posicion = unaHab
            self.juego.agregarBicho(bicho)
        def fabricarBichoPerezoso(self, unaHab):
            bicho = Bicho()
            bicho.modo = Perezoso()
            bicho.juego = self
            bicho.vidas=5
            bicho.poder=1
            bicho.posicion = unaHab
            self.juego.agregarBicho(bicho)
        def fabricarForma(self):
            forma=Cuadrado()
            forma.agregarOrientacion(self.fabricarNorte())
            forma.agregarOrientacion(self.fabricarEste())
            forma.agregarOrientacion(self.fabricarSur())
            forma.agregarOrientacion(self.fabricarOeste())

            return forma
class Director:
    def __init__(self):
        self.builder = LaberintoBuilder()
        self.diccionario = None

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.diccionario.get('laberinto', []):
            self.fabricarLaberintoRecursivoEn(each, 'root')


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
        for each in self.diccionario.get('hijos', []):
            self.fabricarLaberintoRecursivoEn(each, con)


    def iniBuilder(self):
        forma = self.diccionario.get('forma')
        if forma == 'cuadrado':
            self.builder = LaberintoBuilder()
        elif forma == 'hexagono':
            self.builder = LaberintoBuilderHexagonal()

    def leerArchivo(self, unArchivo):
        try:
            with open(unArchivo) as file:
                self.diccionario = json.load(file)
        except FileNotFoundError:
            print(f'No se encontró el archivo', unArchivo)

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def fabricarBichos(self):
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
    def fabricarForma(self):
        forma=Hexagono()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarNoreste())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarSuroeste())
        forma.agregarOrientacion(self.fabricarNoroeste())
        return forma
    
    def fabricarNoroeste(self):
        return NorOeste()

    def fabricarNoreste(self):
        return NorEste()

    def fabricarSuroeste(self):
        return SurOeste()

    def fabricarSureste(self):
        return SurEste()

   
    


# director=Director()
# unCont = Contenedor()
# armario = director.builder.fabricarArmarioEn(1, unCont)


def main(): #stdscr
 
    director=Director()
    director.procesar('C:\\Users\\maria\\Documents\\2 Ing\\Diseño software\\DiferentesLaberintos\\1erLaberinto\\laberinto2habTunel2Bichos.json')
    game=director.obtenerJuego()
    game.agregarPersonaje("Pepe")
    person=game.person
    game.abrirPuertas()
    game.lanzarTodosHilos()
    while True:
        if keyboard.is_pressed('q'):
            break  # Exit the program
        elif keyboard.is_pressed("w"): #curses.KEY_UP:
            person.irAlNorte()
        elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
            person.irAlSur()
        elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
            person.irAlOeste()
        elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
            person.irAlEste()
        elif keyboard.is_pressed("enter"):#curses.KEY_ENTER or key in [10, 13]:
            person.atacar()
    game.terminarTodosHilos()
#main()