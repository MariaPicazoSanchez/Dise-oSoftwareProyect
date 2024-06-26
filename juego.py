#"consola para saber como funcionan los hilos"
import copy
import time
import threading
from laberinto import Bicho, ParedBomba, Agresivo, Habitacion, Personaje, Pared, Puerta, Bomba, Laberinto, Perezoso
from orientaciones import Este, Oeste, Norte, Sur, SurEste, SurOeste, NorEste, NorOeste
from estados import Muerto
from laberinto import Cuadrado, Hexagono


class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []
        self.hilos = {}
        self.person=None
        self.prototipo=None
        self.fase = Inicial()

    def fabricarPared(self):
        return Pared()
    
    def fabricarForma(self):
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    
    def fabricarPuertaLados(self,side1,side2):
        door=Puerta()
        door.lado1=side1
        door.lado2=side2
        return door  
    def fabricarPuerta(self):
        return Puerta() 
    def fabricarHab(self, unNum):
        hab = Habitacion(unNum)
        hab.forma = Cuadrado()

        # hab.agregarOrientacion(self.fabricarNorte())
        # hab.agregarOrientacion(self.fabricarEste())
        # hab.agregarOrientacion(self.fabricarSur())
        # hab.agregarOrientacion(self.fabricarOeste())
        

        for each in hab.forma.orientaciones:
            hab.ponerElementoEn(each, self.fabricarPared())

        #self.laberinto.agregarHabitacion(hab)
        return hab
    def fabricarHabHexagonal(self,unNum):
        hab=Habitacion(unNum)
        hab.forma=Hexagono()
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarNorEste())
        hab.agregarOrientacion(self.fabricarNorOeste())
        hab.agregarOrientacion(self.fabricarSurEste())
        hab.agregarOrientacion(self.fabricarSurOeste())
        for each in hab.forma.orientaciones:
            hab.forma.ponerElementoEn(each,self.fabricarPared())
        #self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabLab2HabFM(self):
        self.laberinto = self.fabricarLaberinto()
        room1 = self.fabricarHab(1)
        room2 = self.fabricarHab(2)
        door = self.fabricarPuertaLados(room1,room2)
        room1.ponerElementoEn(Sur(),door)
        room2.ponerElementoEn(Norte(),door)

        # ACUERDATE DE CAMBIAR EL CREAR POR FABRICAR
        # Commented out for now
        # room1.este = self.crearPared()
        # room1.oeste = self.crearPared()
        # room1.norte = self.crearPared()
        # room2.sur = self.crearPared()
        # room2.este = self.crearPared()
        # room2.oeste = self.crearPared()

        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)
        #return self.laberinto
    
    def fabLab2Hab(self):
        self.laberinto = self.fabricarLaberinto()
        room1 = self.fabricarHab(1)
        room2 = self.fabricarHab(2)
        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)

        door=Puerta()
        door.lado1=room1
        door.lado2=room2
        room1.sur = door
        room2.norte = door

        room1.este=self.fabricarPared()
        room1.oeste=self.fabricarPared()
        room1.norte=self.fabricarPared()
        room2.sur=self.fabricarPared()
        room2.este=self.fabricarPared()
        room2.oeste=self.fabricarPared()
        #return self.laberinto
    
    def fabLab2Hab2BombasFM(self):
        hab1 = self.fabricarHab(1)
        hab2 = self.fabricarHab(2)
        puerta = self.fabricarPuertaLados(hab1, hab2)
        
        hab1.norte = self.fabricarPared()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        bm1 = self.fabricarBomba()
        bm2 = self.fabricarBomba()
        
        hab1.agregarHijo(bm1)
        hab2.agregarHijo(bm2)
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def fabLab2HabFMD(self):
        hab1 = self.fabricarHab(1)
        hab2 = self.fabricarHab(2)
        puerta = self.fabricarPuertaLados(hab1, hab2)
        
        bm1 = self.fabricarBomba()
        bm1.em=self.fabricarPared()
        
        hab1.norte = self.fabricarPared()
        hab1.este = bm1
        hab1.oeste = self.fabricarPared()
        
        bm2 = self.fabricarBomba()
        bm2.em=self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.este = bm2
        hab2.oeste = self.fabricarPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = self.fabricarLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
       
    def fabLab4Hab4BichosFM(self):
        hab1 = self.fabricarHab(1)
        hab2 = self.fabricarHab(2)
        hab3 = self.fabricarHab(3)
        hab4 = self.fabricarHab(4)
           
        p12 = self.fabricarPuertaLados(hab1, hab2)
        p13 = self.fabricarPuertaLados(hab1, hab3)
        p34 = self.fabricarPuertaLados(hab3, hab4)
        p24 = self.fabricarPuertaLados(hab2, hab4)
            
        hab1.sur = p12
        hab2.norte = p12
            
        hab1.este = p13
        hab3.oeste = p13
            
        hab2.este = p24
        hab4.oeste = p24
            
        hab3.sur = p34
        hab4.norte = p34

        # ACUERDATE DE CAMBIAR EL CREAR POR FABRICAR
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.sur = self.fabricarPared()
        hab3.norte = self.fabricarPared()
        hab3.este = self.fabricarPared()
        hab4.sur = self.fabricarPared()
        hab4.este = self.fabricarPared()
            
        self.laberinto = self.fabricarLaberinto()
            
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
            
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))
       
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarSurEste(self):
        return SurEste()
    def fabricarSurOeste(self):
        return SurOeste()
    def fabricarNorEste(self):
        return NorEste()
    def fabricarNorOeste(self):
        return NorOeste()
    
    def abrirPuertas(self):
       self.laberinto.recorrer(lambda each: each.abrirPuertas())
    def activarBombas(self):
        #self.laberinto.recorrer(lambda each: each.activar() if each.esBomba() else None)
        self.fase.activarBombasEn(self)
    def agregarBicho(self, unBicho):
            self.bichos.append(unBicho)
            unBicho.juego = self
    def agregarPersonaje(self, unNombre):
        self.fase.agregarPersonajeEn(unNombre, self)
    
    def puedeAgregarPersonaje(self, unNombre):
        self.person=Personaje(unNombre)
        self.laberinto.entrarAlguien(self.person)
        self.person.juego = self

    def cerrarPuertas(self):
        self.laberinto.recorrer(lambda each: each.cerrarPuertas())
    def desactivarBombas(self):
        self.laberinto.recorrer(lambda each: each.desactivar() if each.esBomba() else None)

    def eliminarBicho(self, unBicho):
        if unBicho in self.bichos:
            self.bichos.remove(unBicho)
        else:
            print("No existe ese bicho")

    def fabricarBichoAgresivo(self, Habitacion):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.juego = self
        bicho.posicion = Habitacion
        bicho.vidas = 5
        bicho.poder = 2
        return bicho
    def fabricarBichoPerezoso(self, Habitacion):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.juego = self
        bicho.posicion = Habitacion
        bicho.vidas = 3
        bicho.poder = 1
        return bicho
    def fabricarBomba(self):
        return Bomba()
    
    def lanzarHilo(self, unBicho):
        def proceso():
            while unBicho.estaVivo():
                unBicho.actua()

        hilo = threading.Thread(target=proceso)
        hilo.start()
        self.hilos[unBicho] = hilo

    def terminarHilo(self, unBicho):
        unBicho.vidas = 0
        unBicho.estado=Muerto()
        if(self.comprobarTodosMuertos()):
            self.ganaPersonaje()

    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)
  
    def buscarTodosBichos(self):
        posicion = self.person.obtenerPosicion()
        lista = [bicho for bicho in self.bichos if bicho.obtenerPosicion() == posicion and bicho.estaVivo()]
        
        for bicho in lista:
            bicho.esAtacadoPor(self.person)
        
        return lista
    def buscarTodosBichosPosicion(self, posicion):
        lista = [bicho for bicho in self.bichos if bicho.obtenerPosicion() == posicion and bicho.estaVivo()]
        
        for bicho in lista:
            bicho.esAtacadoPor(self.person)
        
        return lista


    def buscarBicho(self):
        posicion = self.person.obtenerPosicion()
        
        for bicho in self.bichos:
            if bicho.obtenerPosicion() == posicion and bicho.estaVivo():
                bicho.esAtacadoPor(self.person.vidas)
                return bicho
        
        return None



    def bichoBuscarPersonaje(self, unBicho):
        unCont = unBicho.obtenerPosicion()
        if self.person is None:
            return None
        if self.person.obtenerPosicion() == unCont:
            return self.person
        else:
            return None


    def lanzarTodosHilos(self):
        # print("-----------------------------------")
        # print("COMIENZA EL JUEGO")
        # for bicho in self.bichos:
        #     self.lanzarHilo(bicho)
        self.fase.lanzarTodosHilosEn(self)
    
    def lanzarTodosHilosTest(self):
        self.fase.lanzarTodosHilosEn(self)

    def puedeLanzarTodosHilos(self):
        print("-----------------------------------")
        print("COMIENZA EL JUEGO")
        for bicho in self.bichos:
            self.lanzarHilo(bicho)

    def puedeLanzarTodosHilosTest(self):
        print("-----------------------------------")
        print("COMIENZA EL JUEGO")

    def terminarTodosHilos(self):
        #for bicho in self.bichos:
        #    self.terminarHilo(bicho)
        self.fase.terminarTodosHilosEn(self)

    def puedeTerminarTodosHilos(self):
        for bicho in self.bichos:
            self.terminarHilo(bicho)

    def finJuego(self):
        print("El juego ha terminado.")
        self.fase= Final()
    def muerePersonaje(self):
        self.person.estado=Muerto()
        self.terminarTodosHilos()
        
    def comprobarTodosMuertos(self):
        for bicho in self.bichos:
            if bicho.estaVivo():
                return False
        return True
    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)
    def ganaPersonaje(self):
        if self.person.estaVivo():
            print("El personaje ha ganado")
        self.finJuego()

    def puedeActivarBombas(self):
        for each in self.laberinto:
            if each.esBomba():
                each.activar(self.person)

class JuegoBombas(Juego):
    def __init__(self):
        super().__init__()
        
    def fabricarPared(self):
        return ParedBomba()

class Fase:
    def __init__(self):
        pass
    def esFinal(self):
        return False
    def esInicial(self):
        return False
    def esJugando(self):
        return False
    def agregarPersonajeEn(self, unaCadena, unJuego):
        pass
    def lanzarTodosHilosEn(self, unJuego):
        pass
    def terminarTodosHilosEn(self, unJuego):
        pass
    def activarBombasEn(self, unJuego):
        pass
    def lanzarTodosHilosTestEn(self, unJuego):
        pass

class Inicial(Fase):
    def __init__(self):
        super().__init__()
    def esInicial(self):
        return True
    def agregarPersonajeEn(self, unaCadena, unJuego):#revisar porque da bucle infinito
        #unJuego.agregarPersonaje(unaCadena)#lo que tenemos en pharo
        unJuego.puedeAgregarPersonaje(unaCadena)

    def lanzarTodosHilosEn(self, unJuego):
        unJuego.puedeLanzarTodosHilos()
        unJuego.fase = Jugando()

    def lanzarTodosHilosTestEn(self, unJuego):
        unJuego.puedeLanzarTodosHilosTest()
        unJuego.fase = Jugando()

    def terminarTodosHilosEn(self, unJuego):
        print("No se puede terminar los hilos en la fase inicial")
    
    def activarBombasEn(self, unJuego):
        print("El juego no ha comenzado")
    
class Jugando(Fase):
    def __init__(self):
        super().__init__()
    def esJugando(self):
        return True
    def agregarPersonajeEn(self, unaCadena, unJuego):
        print("No se puede agregar un personaje en la fase jugando")
    def lanzarTodosHilosEn(self, unJuego):
        print("El juego ya ha comenzado")
    def lanzarTodosHilosTestEn(self, unJuego):
        print("El juego ya ha comenzado")
    def terminarTodosHilosEn(self, unJuego):
        unJuego.puedeTerminarTodosHilos()
    def activarBombasEn(self, unJuego):
        unJuego.puedeActivarBombas()

        
class Final(Fase):
    def __init__(self):
        super().__init__()
    def esFinal(self):
        return True
    def agregarPersonajeEn(self, unaCadena, unJuego):
        print("El juego ha terminado. No se puede agregar un personaje")
    def lanzarTodosHilosEn(self, unJuego):
        print("El juego ya ha terminado. No se pueden lanzar hilos")
    def lanzarTodosHilosTestEn(self, unJuego):
        print("El juego ya ha terminado.")
    def terminarTodosHilosEn(self, unJuego):
        print("Ya ha terminado el juego")
    def activarBombasEn(self, unJuego):
        print("El juego ha terminado. No se pueden activar bombas.")


#game=Juego()
#game.fabLab4Hab4BichosFM()
#game.agregarPersonaje("Juan")
#bichoA1=game.bichos[0]
#game.abrirPuertas()
#game.lanzarTodosHilos()
#time.sleep(5)
#game.terminarTodosHilos()