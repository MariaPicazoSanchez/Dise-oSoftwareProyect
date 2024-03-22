import random
import threading
import time


class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.hilos = {}
        self.person=None

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self,side1,side2):
        door=Puerta(side1,side2)
        return door  
    
    def crearHab(self, id):
        return Habitacion(id)

    def crearLaberinto(self):
        return Laberinto()
    
    def make2RoomsMazeFM(self):
        self.laberinto = self.crearLaberinto()
        room1 = self.crearHab(1)
        room2 = self.crearHab(2)
        door = self.crearPuerta(room1,room2)
        room1.sur=door
        room2.norte=door
        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)
        return self.laberinto
    
    def make2RoomsMaze(self):
        self.laberinto = self.crearLaberinto()
        room1 = self.crearHab(1)
        room2 = self.crearHab(2)
        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)

        door=Puerta(room1,room2)
        room1.sur = door
        room2.norte = door
        return self.laberinto
    
    def make2Rooms2BombasFM(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        puerta = self.crearPuerta(hab1, hab2)
        
        hab1.norte = self.crearPared()
        hab1.este = self.crearPared()
        hab1.oeste = self.crearPared()
        
        hab2.sur = self.crearPared()
        hab2.este = self.crearPared()
        hab2.oeste = self.crearPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        bm1 = self.fabricarBomba()
        bm2 = self.fabricarBomba()
        
        hab1.agregarHijo(bm1)
        hab2.agregarHijo(bm2)
        
        self.maze = self.crearLaberinto()
        
        self.maze.agregarHabitacion(hab1)
        self.maze.agregarHabitacion(hab2)

    def make2RoomsFMD(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        puerta = self.crearPuerta(hab1, hab2)
        
        bm1 = self.fabricarBomba()
        bm1.em(self.crearPared())
        
        hab1.norte = self.crearPared()
        hab1.este = bm1
        hab1.oeste = self.crearPared()
        
        bm2 = self.fabricarBomba()
        bm2.em(self.crearPared())
        
        hab2.sur = self.crearPared()
        hab2.este = bm2
        hab2.oeste = self.crearPared()
        
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto = self.crearLaberinto()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
       
    def make4Rooms4BichosFM(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        hab3 = self.crearHab(3)
        hab4 = self.crearHab(4)
           
        p12 = self.crearPuerta(hab1, hab2)
        p13 = self.crearPuerta(hab1, hab3)
        p34 = self.crearPuerta(hab3, hab4)
        p24 = self.crearPuerta(hab2, hab4)
            
        hab1.sur = p12
        hab2.norte = p12
            
        hab1.este = p13
        hab3.oeste = p13
            
        hab2.este = p24
        hab4.oeste = p24
            
        hab3.sur = p34
        hab4.norte = p34
            
        self.laberinto = self.crearLaberinto()
            
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)
            
        self.agregarBicho(self.fabricarBichoAgresivo(hab1))
        self.agregarBicho(self.fabricarBichoAgresivo(hab3))
        self.agregarBicho(self.fabricarBichoPerezoso(hab2))
        self.agregarBicho(self.fabricarBichoPerezoso(hab4))
       
    def crearEste(self):
        return Este
    def crearOeste(self):
        return Oeste
    def crearNorte(self):
        return Norte
    def crearSur(self):
        return Sur
    def abrirPuerta(self):
        for each in self.recorrer():
            each.abrirPuertas()
    def activarBombas(self):
        for each in self.recorrer():
            if each.esBomba():
                each.activar()
    def agregarBicho(self, unBicho):
            self.bichos.append(unBicho)

    def cerrarPuertas(self):
        for each in self.recorrer():
            each.cerrarPuertas()
    def desactivarBombas(self):
        for each in self.recorrer():
            if each.esBomba():
                each.desactivar()
    def eliminarBicho(self, Bicho):
        if Bicho in self.bichos:
            self.bichos.remove(Bicho)
        else:
            print("No existe ese bicho")

    def fabricarBichoAgresivo(self, Habitacion):
        bicho = Bicho(Agresivo(), 5, 2, Habitacion)
        return bicho
    def fabricarBichoPerezoso(self, Habitacion):
        bicho = Bicho(Perezoso(), 3, 1, Habitacion)
        return bicho
    def fabricarBomba(self):
        return Bomba()
    def fabricarPuertaLados(self, lado1, lado2):
        puerta = self.crearPuerta(lado1, lado2)
        return puerta
    def lanzarHilo(self, unBicho):
        proceso = threading.Thread(target=unBicho.actua)
        self.hilos[unBicho] = proceso
        proceso.start()

    def terminarHilo(self, unBicho):
        proceso = self.hilos.get(unBicho)
        if proceso:
            proceso.join()
            del self.hilos[unBicho]

    def obtenerHabitacion(self, unNum):
        return self.maze.obtenerHabitacion(unNum)
    def agregarPersonaje(self, unNombre):
        self.person=Personaje(3, 2, 1, unNombre)
        self.laberinto.entrarAlguien(self.person)
        self.person.juego=self

    def buscarBicho(self):
        pass
        #por implementar
    
class Orientation:
    def __init__(self):
        pass
    def caminar(self, Bicho):
        pass
    def ponerElementoEn(self, EM, Contenedor):
        pass
    def recorrer(self,unBloque):
        pass
class Este(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlEste()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
        if alguien.posicion.este:
            if alguien.posicion.este.abierta:
                print("Entraste a la habitacion que esta al este")
            else: 
                print("La puerta esta cerrada")
class Oeste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlOeste()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.oeste=EM
    def entrar(self, alguien):
        if alguien.posicion.oeste:
            if alguien.posicion.oeste.abierta:
                print("Entraste a la habitacion que esta al oeste")
            else: 
                print("La puerta esta cerrada")
class Norte(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlNorte()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
        if alguien.posicion.norte:
            if alguien.posicion.norte.abierta:
                print("Entraste a la habitacion que esta al norte")
            else: 
                print("La puerta esta cerrada")
class Sur(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlSur()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
       if alguien.posicion.sur:
            if alguien.posicion.sur.abierta:
                print("Entraste a la habitacion que esta al sur")
            else: 
                print("La puerta esta cerrada")

class ElementoMapa():
    def __init__(self):
        self.padre = None
        pass
    def entrar(self):
        pass
    def recorrer(self, unBloque):
        pass
    def esBomba(self):
        return False
    def esHabitacion(self):
        return False
    def esPared(self):
        return False
    def esPuerta(self):
        return False
    def abrirPuertas(self):
        pass
    def cerrarPuertas(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos =[]
        self.orientaciones = []
        self.este =None
        self.oeste =None
        self.norte =None
        self.sur =None
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)

    def caminarAleatorio(self, unBicho):
        if self.orientaciones:
            numOr = len(self.orientaciones)
            numAl = random.randint(1, numOr)
            orAl = self.orientaciones[numAl-1]
            orAl.caminar(unBicho)

    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
    def irAlEste(self, alguien):
        self.este.entrar(alguien)
    def irAlOeste(self, alguien):
        self.oeste.entrar(alguien)
    def irAlNorte(self, alguien):
        self.norte.entrar(alguien)
    def irAlSur(self, alguien):
        self.sur.entrar(alguien)
    def ponerEn(self, unaOrientacion, elemento):
        if isinstance(unaOrientacion, Este):
            unaOrientacion.ponerElemento(elemento, self)
        elif isinstance(unaOrientacion, Oeste):
            unaOrientacion.ponerElemento(elemento, self)
        elif isinstance(unaOrientacion, Norte):
            unaOrientacion.ponerElemento(elemento, self)
        elif isinstance(unaOrientacion, Sur):
            unaOrientacion.ponerElemento(elemento, self)

    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)

    def recorrerEn(self, unBloque, unCont):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
        for each in self.orientaciones:
            each.recorrerEn(unBloque, self)

class Armario(Contenedor):
    def __init__(self, num=None):
        super().__init__(num)
        self.num = num

class Laberinto(Contenedor):
    def __init__(self):
        self.rooms = []
        
    def agregarHabitacion(self, room):
        self.rooms.append(room)
    
    def entrar(self):
        hab=self.rooms[0]
        hab.entrar() 
    def entrarAlguien(self, alguien):
        hab=self.rooms[0]
        hab.entrarAlguien(alguien)

    def numeroHabitaciones(self):
        return len(self.rooms)

    def obtenerHabitacion(self, unNum):
        return self.rooms[unNum-1]

class Habitacion(Contenedor):
    def __init__(self,num=None, norte=Norte(), sur=Sur(), este=Este(), oeste=Oeste()):
        super().__init__()
        self.num = num
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
    
    def entrar(self):
        print("Entraste a la habitacion ", self.num)

    def entrarAlguien(self, alguien):
        print("Entraste a la habitacion ", alguien.nombre)
        alguien.posicion = self
        
    def esHabitacion(self):
        return True
    def printOn(self):
        print('Hab')
        print(str(self.num))
class Puerta(ElementoMapa):
    def __init__(self, side1, side2):
        self.lado1 = side1
        self.lado2 = side2
        self.abierta = False
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta esta cerrada")
    def abrirPuertas(self):
        self.abierta = True
    def cerrarPuertas(self):    
        self.abierta = False
    def esPuerta(self):   
        return True 
    def recorrer(self, unBloque):
        unBloque(self)
    def printOn(self):
        print('Puerta: ', self.lado1, self.lado2)

class Pared(ElementoMapa):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("No puedes atravesar la pared")
    def esPared(self):
        return True
    def recorrer(self, unBloque):
        unBloque(self)
class Hoja(ElementoMapa):
    def __init__(self):
        pass
    def accept(self, visitor):
        visitor.visitHoja(self)
    def recorrer(self, unBloque):
        unBloque(self)

class Decorator(Hoja):
    def __init__(self):
        self.em=None
class Bomba(Decorator):
    def __init__(self):
        self.activa=False
    def activar(self):
        self.activa=True
        print("Bomba activada")
    def desactivar(self):
        self.activa=False
        print("Bomba desactivada")
    def esBomba(self):
        return True
    def entrar(self, alguien):
        if self.activa:
            print("La bomba ha explotado")
            # quitar vidas a alguien: en función del poder de la bomba
        else:
            if self.em is not None:
                self.em.entrar()
            else:
                print("No puedes atravesar la bomba")


class ParedBomba(Pared):
    def __init__(self):
        return self
    def entrar(self):
        if isinstance(self, Bomba) and self.activa:
            print("¡Boom! Te has chocado con una pared-bomba")
            # Perform explosion logic here
        else:
            super().entrar()
    
class JuegoBombas(Juego):
    def __init__(self):
       # return self
        pass
    def crearPared(self):
        return ParedBomba()
class Modo():
    def __init__(self):
        pass
    def actua(self, Bicho):
        self.dormir(Bicho)
        self.caminar(Bicho)
        self.atacar(Bicho)
    def dormir(self, unBicho):
        print(unBicho.__class__.__name__, "duerme")
        time.sleep(2)
    def caminar(self, unBicho):
        unBicho.caminarAleatorio()
class Ente():
    def __init__(self, vidas, poder, habitacion, contenedor):
        self.vidas = vidas
        self.poder = poder
        self.habitacion = habitacion
        self.posicion = contenedor
    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)
        
    def irAlOeste(self):
        self.posicion.irAlOeste(self)
       
    def irAlSur(self):
        self.posicion.irAlSur(self)
    def atacar(self):
        pass
class Bicho(Ente):
    def __init__(self, modo=Modo(), vidas=1, poder=2, habitacion=None, contenedor=None):
        super().__init__(vidas, poder, habitacion, contenedor)
        self.modo = modo
        self.caminarAleatorio()
        
    def actua(self):
        self.modo.actua(self)

    def print_on(self):
        print(f"Bicho-{self.modo}")

    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)

    def atacar(self):
        self.juego.buscarPersonaje()

class Personaje(Ente):
    def __init__(self, vidas, poder, habitacion,nombre=None, contenedor=None):
        super().__init__(vidas, poder, habitacion, contenedor)
        self.nombre=nombre
    def atacar(self):
        self.juego.buscarBicho()
    
    def esAtacadoPor(self,unBicho):
        self.vidas-=unBicho.poder
        if self.vidas<=0:
            print("Has muerto")
            self.juego.terminarHilo()
        else:
            print("Tienes ", self.vidas, "vidas")
    
class Agresivo(Modo):
    def __init__(self):
        super().__init__()
    def printOn(self):
        print("Agresivo")
class Perezoso(Modo):
    def __init__(self):
        super().__init__()
    def printOn(self):
        print("Perezoso")
game=Juego()
game=JuegoBombas()
game.make2RoomsMaze()
game.make2RoomsMazeFM()
game.agregarPersonaje("Pepito")
game.laberinto.entrar() 

bicho = Bicho(Agresivo(), 3, 5,Habitacion(1),Habitacion(1))
bicho.irAlEste()  # Llamando a actua después de cambiar la posición
bicho.caminarAleatorio()
bicho.irAlNorte()  # Llamando a actua después de cambiar la posición
bicho.irAlOeste()  # Llamando a actua después de cambiar la posición
bicho.irAlSur()  # Llamando a actua después de cambiar la posición

#las orientaciones(entrar) les falta el metodo entrar el que esta me lo he inventado