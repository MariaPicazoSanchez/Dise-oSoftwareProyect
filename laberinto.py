import random
import time
from orientaciones import Este, Oeste, Norte, Sur, Orientation, NorEste, NorOeste, SurEste, SurOeste
from juego import Juego
from estados import Cerrada, Abierta,Vivo, Muerto


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
    def entrarAlguien(self, alguien):
        pass

class Contenedor(ElementoMapa):
    def __init__(self,num=None):
        self.hijos =[]
        self.num=num
        self.forma = None
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo) if hijo in self.hijos else print("No se puede eliminar EM")

    def agregarOrientacion(self, unaOrientacion):
        self.forma.agregarOrientacion(unaOrientacion)

    def caminarAleatorio(self, unBicho):
        if self.orientaciones:
            numOr = len(self.obtenerOrientaciones().length)
            numAl = random.randint(1, numOr)
            orAl = self.obtenerOrientaciones()[numAl-1]
            orAl.caminar(unBicho)

    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
        self.forma.recorrer(unBloque)

    def irAlEste(self, alguien):
        self.este.entrarAlguien(alguien)
    def irAlOeste(self, alguien):
        self.oeste.entrarAlguien(alguien)
    def irAlNorte(self, alguien):
        self.norte.entrarAlguien(alguien)
    def irAlSur(self, alguien):
        self.sur.entrarAlguien(alguien)
    def irAlNorEste(self, alguien):
        self.noreste.entrarAlguien(alguien)
    def irAlNorOeste(self, alguien):
        self.noroeste.entrarAlguien(alguien)
    def irAlSurEste(self,alguien):
        self.sureste.entrarAlguien(alguien)
    def irAlSurOeste(self, alguien):
        self.suroeste.entrarAlguien(alguien)

    def ponerElementoEn(self, unaOrientacion, elemento):
        self.forma.ponerElementoEn(unaOrientacion, elemento)

    #FALTA POR CAMBIAR
    def recorrerEn(self, unBloque, unCont):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
        for each in self.orientaciones:
            each.recorrerEn(unBloque, self)
    
    def obtenerOrientaciones(self):
        return self.forma.orientaciones

class Armario(Contenedor):
    def __init__(self, num=None):
        super().__init__(num)
        
    def entrar(self, alguien):
        print("Entraste al armario ", str(alguien.nombre))
        alguien.poscion = self
    def printOn(self):
        print('Armario', str(self.num))

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        pass
    def agregarHabitacion(self, room):
        self.agregarHijo(room)
    
    def entrarAlguien(self,alguien):
        hab=self.obtenerHabitacion(1)
        hab.entrarAlguien(alguien) 
   
    def numeroHabitaciones(self):
        return len(self.hijos)

    def obtenerHabitacion(self, unNum):
        return self.hijos[unNum-1]
    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)

class Habitacion(Contenedor):
    def __init__(self,num):
        super().__init__(num)
    
    def entrar(self):
        print("Entraste a la habitacion ", self.num)

    def entrarAlguien(self, alguien):
        print("Entraste a la habitacion ", alguien.nombre)
        alguien.posicion = self
        
    def esHabitacion(self):
        return True
    def printOn(self):
        print('Hab', self.num)
class Puerta(ElementoMapa):
    def __init__(self):
        self.lado1 = None
        self.lado2 = None
        self.estado = Cerrada()

    def entrarAlguien(self, alguien):
        if self.estaAbierta():
            print(self.printOn(), "abierta")
            if alguien.posicion == self.lado1:
                self.lado2.entrarAlguien(alguien)
            else:
                self.lado1.entrarAlguien(alguien)
        else:
            print(self.printOn(), "cerrada")
    
    def abrirPuertas(self):
        self.estado.abrirPuertas(self)
    def cerrarPuertas(self):    
        self.estado.cerrarPuertas(self)
    def esPuerta(self):   
        return True 
    def recorrer(self, unBloque):
        unBloque(self)
    def printOn(self):
        print('Puerta: ', self.lado1.num,'-', self.lado2.num)
    def estaAbierta(self):
        return self.estado.estaAbierta()
    

class Pared(ElementoMapa):
    def __init__(self):
        pass 
    def entrar(self):
        print("No puedes atravesar la pared")
    def entrarAlguien(self, alguien):
        if isinstance(alguien,Bicho):
            print(alguien.__class__.__name__,"no puede atravesar la pared")
        else:
            print(alguien.nombre,"no puedes atravesar la pared")
    def esPared(self):
        return True
    def recorrer(self, unBloque):
        unBloque(self)
class Hoja(ElementoMapa):
    def __init__(self):
        pass
    def entrarAlguien(self, alguien):
        pass
    def recorrer(self, unBloque):
        unBloque(self)

class Decorator(Hoja):
    def __init__(self):
        super().__init__()
        self.em=None

class Bomba(Decorator):
    def __init__(self):
        super().__init__()
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
                print("La bomba ha explotado")
    #POR PREGUNTAR EL ELSE DEBERIA SER ENTRARalGUIEN
    def entrarAlguien(self, alguien):
        if self.activa:
            print("La bomba ha explotado")
        else:
            self.em.entrar()
class Tunel(Hoja):
    def __init__(self):
        self.laberinto=None

    def entrarAlguien(self, alguien):
        print(alguien.nombre," has entrado a un nuevo laberinto")
    
class ParedBomba(Pared):
    def __init__(self):
        pass
    def entrar(self):
        if isinstance(self, Bomba) and self.activa:
            print("¡Boom! Te has chocado con una pared-bomba")
            # Perform explosion logic here
        else:
            super().entrar()
    
class JuegoBombas(Juego):
    def __init__(self):
        super().__init__()
        
    def fabricarPared(self):
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
    def atacar(self, unBicho):
        unBicho.atacar()
class Ente():
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.juego = None
        self.estado = Vivo()
    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)
        
    def irAlOeste(self):
        self.posicion.irAlOeste(self)
       
    def irAlSur(self):
        self.posicion.irAlSur(self)
    def irAlNorEste(self):
        self.posicion.irAlNorEste(self)

    def irAlNorOeste(self):
        self.posicion.irAlNorOeste(self)

    def irAlSurEste(self):
        self.posicion.irAlSurEste(self)

    def irAlSurOeste(self):
        self.posicion.irAlSurOeste(self)

    def atacar(self):
        self.estado.atacar(self)
    def esAtacadoPor(self, alguien):
        self.vidad=self.vidas-alguien.poder
        if self.vidas<=0:
            print("Muere" + self.__class__.__name__)
            self.muero()
        else:
            print("Te han atacado, vidas restantes ", self.vidas)
    def estaVivo(self):
        return self.estado.estaVivo()
    def muero(self):
        pass
    def puedeAtacar(self):
        pass

class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None
        #self.caminarAleatorio()
        
    def actua(self):
        self.modo.actua(self)

    def printOn(self):
        print(f"Bicho-{self.modo}")

    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)

    def puedeAtacar(self):
        self.juego.bichoBuscarPersonaje(self)
    def muero(self):
        self.juego.terminalHilo(self)

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nombre=None
        super.vidas=20
        super.poder=1

    def puedeAtacar(self):
        self.juego.buscarBicho()
    def muero(self):
        self.juego.muerePersonaje(self)
    
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
game.fabricarLaberinto()

game.fabLab2Hab()
game.fabLab2Hab2BombasFM()
game.fabLab2HabFM()
game.fabLab2HabFMD() #no va bien
game.agregarPersonaje("Pepito")
game.laberinto.entrar() 
game.abrirPuertas()
tunel = Tunel()
tunel.entrar(game.person)
bicho = Bicho()
bicho.modo = Agresivo()
bicho.posicion = game.laberinto.hijos[0]
bicho.irAlEste()  # Llamando a actua después de cambiar la posición
bicho.caminarAleatorio()
bicho.irAlNorte()  # Llamando a actua después de cambiar la posición
bicho.irAlOeste()  # Llamando a actua después de cambiar la posición
bicho.irAlSur()  # Llamando a actua después de cambiar la posición
game.cerrarPuertas()
#las orientaciones(entrar) les falta el metodo entrar el que esta me lo he inventado