import random
import time
from orientaciones import Este, Oeste, Norte, Sur, Orientation, NorEste, NorOeste, SurEste, SurOeste
#from juego import Juego
from estados import Cerrada, Abierta,Vivo, Muerto
from punto import Punto

class ElementoMapa():
    def __init__(self):
        self.padre = None
        self.comandos=[]
    def agregarComando(self, unComando):
        self.comandos.append(unComando) 
    def eliminarComando(self, unComando):
        self.comandos.remove(unComando) if unComando in self.comandos else print("No se puede eliminar EM")
    def obtenerComandos(self):
        return self.comandos
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
    def esArmario(self):
        return False
    def esTunel(self):
        return False
    def aceptar(self, unVisitor):
        pass
class Contenedor(ElementoMapa):
    def __init__(self,num=None):
        self.hijos =[]
        self.num=num
        self.forma = Cuadrado()
    def visitarContenedor(self, unVisitor):
        pass
    def aceptar(self, unVisitor):
        self.visitarContenedor(unVisitor)
        for each in self.hijos:
            each.aceptar(unVisitor)
    def obtenerPunto(self):
        return self.forma.punto
    def obtenerExtend(self):
        return self.forma.extend
    def puntoSet(self, unPunto):
        if isinstance(unPunto, tuple):
            unPunto = Punto(unPunto[0], unPunto[1])
        self.forma.punto = unPunto
    def extendSet(self, unExtend):
        self.forma.extend = unExtend
    def calcularPosicion(self):
        self.forma.calcularPosicion()
    def obtenerComandos(self):
        lista = []
        for each in self.hijos:
            lista.append(each.obtenerComandos())
        lista.append(self.forma.obtenerComandos())
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo) if hijo in self.hijos else print("No se puede eliminar EM")

    def agregarOrientacion(self, unaOrientacion):
        self.forma.agregarOrientacion(unaOrientacion)

    def caminarAleatorio(self, unBicho):
        numOr = len(self.obtenerOrientaciones())
        numAl = random.randint(0, numOr - 1)
        orAl = self.obtenerOrientaciones()[numAl-1]
        orAl.caminar(unBicho)

    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
        self.forma.recorrer(unBloque)

    def irAlEste(self, alguien):
        self.forma.irAlEste(alguien)
    def irAlOeste(self, alguien):
        self.forma.irAlOeste(alguien)
    def irAlNorte(self, alguien):
        self.forma.irAlNorte(alguien)
    def irAlSur(self, alguien):
        self.forma.irAlSur(alguien)
    def irAlNorEste(self, alguien):
        self.forma.irAlNorEste(alguien)
    def irAlNorOeste(self, alguien):
        self.forma.irAlNorOeste(alguien)
    def irAlSurEste(self,alguien):
        self.forma.irAlSurEste(alguien)
    def irAlSurOeste(self, alguien):
        self.forma.irAlSurOeste(alguien)

    def ponerElementoEn(self, unaOrientacion, elemento):
        self.forma.ponerElementoEn(unaOrientacion, elemento)
    def recorrerEn(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
        for each in self.forma.orientaciones:
            each.recorrerEn(unBloque, self)
    
    def obtenerOrientaciones(self):
        return self.forma.orientaciones
    
    def obtenerElemento(self, unaOrientacion):
        return self.forma.obtenerElemento(unaOrientacion)

class Armario(Contenedor):
    def __init__(self, num=None):
        super().__init__(num)
        pass
    def entrarAlguien(self, alguien):
        print("Entraste al armario ", str(alguien.nombre))
        alguien.poscion = self
    def printOn(self):
        print('Armario', str(self.num))
    def esArmario(self):
        return True

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, room):
        self.agregarHijo(room)
    
    def entrarAlguien(self,alguien):
        hab=self.obtenerHabitacion(1)
        hab.entrarAlguien(alguien) 
   
    def numeroHabitaciones(self):
        return len(self.hijos)

    def obtenerHabitacion(self, unNum):
        for room in self.hijos:
            if room.num == unNum:
                return room
        return None
        
    def recorrer(self, unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)
    def aceptar(self, unVisitor):
        for each in self.hijos:
            each.aceptar(unVisitor)
class Habitacion(Contenedor):
    def __init__(self,num):
        super().__init__(num)
    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
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
        super().__init__()
        self.lado1 = None
        self.lado2 = None
        self.estado = Cerrada()
        self.visitada=False
    def calcularPosicionDesdeEn(self, unCont, unPunto):
        if self.visitada:
            return self
        self.visitada=True
        if unCont.num == self.lado1.num:
            self.lado2.puntoSet(unPunto)
            self.lado2.calcularPosicion()
        else:
            self.lado1.puntoSet(unPunto)
            self.lado1.calcularPosicion()

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
    def calcularPosicionDesdeEn(self, unCont, unPunto):
        pass
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
        self.potencia=10
    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)
    def activar(self,alguien):
        self.activa=True
        print("Bomba activada")
        self.explotar(alguien)
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
    def explotar(self, alguien):
        # Si la explosión no está activa, salimos
        if not self.activa:
            return None
        # Buscamos todos los bichos en la posición de alguien
        lista = alguien.juego.buscarTodosBichos()
        # Si encontramos bichos, los atacamos con la potencia de la explosión
        if lista:
            for each in lista:
                each.esAtacadoPor(self.potencia)

class Tunel(Hoja):
    def __init__(self):
        self.laberinto=None
    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)
    def entrarAlguien(self, alguien):
        print(f"{alguien.nombre} accede a un nuevo laberinto")
        if self.laberinto is None:
            self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrarAlguien(alguien)

    def esTunel(self):
        return True
    
class ParedBomba(Pared):
    def __init__(self):
        pass
    def entrar(self):
        print("Te has chocado con una pared bomba")
    

class Modo():
    def __init__(self):
        self.color = None
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
        self._vidas = None
        self.poder = None
        self.juego = None
        self.estado = Vivo()
        self.posicion = None

    @property
    def vidas(self):
        return self._vidas

    @vidas.setter
    def vidas(self, value):
        if self._vidas == None:
            self._vidas = value
        elif self.vidas != value:
            self._vidas = value
            print(self.__class__.__name__, " te han atacado, vidas restantes:", self._vidas)
           # self.notify_observers()

    #def attach(self, observer):
       # self.observers.append(observer)
        
    #def detach(self, observer):
       # self.observers.remove(observer)

   # def notify_observers(self):
    #    for observer in self.observers:
     #       observer.update()

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
    def esAtacadoPor(self, power):
        if power > self.vidas:
            self.vidas -= power
        else:
            self.vidas = power - self.vidas
        if self.vidas > 0:
            print("Alguien ataca a", self.__class__.__name__, "vidas restantes:", str(self.vidas))
        else:
            print("Muere", self.__class__.__name__)
            self.muero()
            # self.juego.muerePersonaje()  # Descomenta esta línea si es necesario

    def estaVivo(self):
        return self.estado.estaVivo()
    def muero(self):
        pass
    def puedeAtacar(self):
        enemigo = self.buscarEnemigo()
        if enemigo is not None:
            enemigo.esAtacadoPor(self.poder)
    def buscarEnemigo(self):
        pass
    def obtenerPosicion(self):
        return self.posicion


class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None

        #self.caminarAleatorio()
        
    def actua(self):
        self.estado.actua(self)
    
    def buscarEnemigo(self):
        return self.juego.buscarPersonaje(self)

    def printOn(self):
        print(f"Bicho-{self.modo}")

    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)

    def puedeActuar(self):
        self.juego.bichoBuscarPersonaje(self)
    def muero(self):
        self.juego.terminarHilo(self)
    def addDependent(self, unObserver):
        pass

class Personaje(Ente):
    def __init__(self,unNombre):
        super().__init__()
        self.nombre=unNombre
        self.vidas=20
        self.poder=1
    def obtenerComandos(self):
        return self.posicion.obtenerComandos()
    def buscarEnemigo(self):
        return self.juego.buscarBicho()
    def muero(self):
        self.juego.muerePersonaje(self)
    def addDependent(self, unObserver):
        pass
    def puedeActuar(self):
        self.modo.actua(self)
    
class Agresivo(Modo):
    def __init__(self):
        super().__init__()
        self.color = "red"
    def printOn(self):
        print("Agresivo")
class Perezoso(Modo):
    def __init__(self):
        super().__init__()
        self.color = "green"
        
    
    def printOn(self):
        print("Perezoso")

class Forma:
    def __init__(self):
        self.orientaciones = []
        self.punto=Punto(0,0)
        self.extend=Punto(0,0)
        self.num=None
    def calcularPosicion(self):
        for each in self.orientaciones:
            each.calcularPosicionDesde(self)
    def obtenerComandos(self):
        lista = []
        for each in self.orientaciones:
            lista.append(each.obtenerComandoDe())
        return lista
    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)

    def irAlEste(self,alguien):
        pass
    def irAlOeste(self,alguien):    
        pass
    def irAlNorte(self,alguien):
        pass
    def irAlSur(self,alguien):
        pass
    def ponerElementoEn(self, unaOrientacion, unEM):
        unaOrientacion.ponerElementoEn(unEM,self)
    def recorrer(self, unBloque):
        for orientation in self.orientaciones:
            orientation.recorrer(unBloque, self)
    def obtenerElemento(self, unaOrientacion):
        return unaOrientacion.obtenerElementoDe(self)
    def obtenerOrientacionAleatoria(self):
        num_or = len(self.orientaciones)
        num_al = random.randint(0, num_or - 1)
        or_al = self.orientaciones[num_al]

        return or_al

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        
    def irAlEste(self,alguien):
        self.este.entrarAlguien(alguien)
    def irAlOeste(self,alguien):
        self.oeste.entrarAlguien(alguien)


class Hexagono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
                
    def irAlNorEste(self, alguien):
        self.noreste.entrarAlguien(alguien)
                
    def irAlNorOeste(self, alguien):
        self.noroeste.entrarAlguien(alguien)
                
    def irAlSurEste(self, alguien):
        self.sureste.entrarAlguien(alguien)
                
    def irAlSurOeste(self, alguien):
        self.suroeste.entrarAlguien(alguien)