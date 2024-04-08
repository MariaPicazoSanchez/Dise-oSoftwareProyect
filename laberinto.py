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
    
    def crearPuertaLados(self,side1,side2):
        door=Puerta()
        door.lado1=side1
        door.lado2=side2
        return door  
    def crearPuerta(self):
        return Puerta() 
    def crearHab(self, id):
        return Habitacion(id)

    def crearLaberinto(self):
        return Laberinto()
    
    def fabLab2HabFM(self):
        self.laberinto = self.crearLaberinto()
        room1 = self.crearHab(1)
        room2 = self.crearHab(2)
        door = self.crearPuertaLados(room1,room2)
        room1.sur=door
        room2.norte=door

        room1.este=self.crearPared()
        room1.oeste=self.crearPared()
        room1.norte=self.crearPared()
        room2.sur=self.crearPared()
        room2.este=self.crearPared()
        room2.oeste=self.crearPared()

        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)
        return self.laberinto
    
    def fabLab2Hab(self):
        self.laberinto = self.crearLaberinto()
        room1 = self.crearHab(1)
        room2 = self.crearHab(2)
        self.laberinto.agregarHabitacion(room1)
        self.laberinto.agregarHabitacion(room2)

        door=Puerta()
        door.lado1=room1
        door.lado2=room2
        room1.sur = door
        room2.norte = door

        room1.este=self.crearPared()
        room1.oeste=self.crearPared()
        room1.norte=self.crearPared()
        room2.sur=self.crearPared()
        room2.este=self.crearPared()
        room2.oeste=self.crearPared()
        return self.laberinto
    
    def fabLab2Hab2BombasFM(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        puerta = self.crearPuertaLados(hab1, hab2)
        
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

    def fabLab2HabFMD(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        puerta = self.crearPuertaLados(hab1, hab2)
        
        bm1 = self.fabricarBomba()
        bm1.em=self.crearPared()
        
        hab1.norte = self.crearPared()
        hab1.este = bm1
        hab1.oeste = self.crearPared()
        
        bm2 = self.fabricarBomba()
        bm2.em=self.crearPared()
        
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
       
    def fabLab4Hab4BichosFM(self):
        hab1 = self.crearHab(1)
        hab2 = self.crearHab(2)
        hab3 = self.crearHab(3)
        hab4 = self.crearHab(4)
           
        p12 = self.crearPuertaLados(hab1, hab2)
        p13 = self.crearPuertaLados(hab1, hab3)
        p34 = self.crearPuertaLados(hab3, hab4)
        p24 = self.crearPuertaLados(hab2, hab4)
            
        hab1.sur = p12
        hab2.norte = p12
            
        hab1.este = p13
        hab3.oeste = p13
            
        hab2.este = p24
        hab4.oeste = p24
            
        hab3.sur = p34
        hab4.norte = p34

        hab1.norte = self.crearPared()
        hab1.oeste = self.crearPared()
        hab2.oeste = self.crearPared()
        hab2.sur = self.crearPared()
        hab3.norte = self.crearPared()
        hab3.este = self.crearPared()
        hab4.sur = self.crearPared()
        hab4.este = self.crearPared()
            
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
    
    def abrirPuertas(self):
       self.laberinto.recorrer(lambda each: each.abrirPuertas())
    def activarBombas(self):
        self.laberinto.recorrer(lambda each: each.activar() if each.esBomba() else None)
    def agregarBicho(self, unBicho):
            self.bichos.append(unBicho)
            unBicho.juego = self

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
        proceso = threading.Thread(target=unBicho.actua)
        self.hilos[unBicho] = proceso
        proceso.start()

    def terminarHilo(self, unBicho):
        proceso = self.hilos.get(unBicho)
        if proceso:
            proceso.join()
            del self.hilos[unBicho]

    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)
    def agregarPersonaje(self, unNombre):
        self.person=Personaje()
        self.person.nombre=unNombre
        self.laberinto.entrarAlguien(self.person)
        self.person.juego=self

    def buscarBicho(self):
        pass
        #por implementar
    def bichoBuscarPersonaje(self,unBicho):
        unCont=unBicho.posicion
        if unCont == self.person.posicion:
            self.person.esAtacadoPor(unBicho)
    def lanzarTodosHilos(self):
        for bicho in self.bichos:
            self.lanzarHilo(bicho)
    def terminarTodosHilos(self):
        for bicho in self.bichos:
            self.terminarHilo(bicho)
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
       #este metodo no se ha implementado
       """  if alguien.posicion.este:
            if alguien.posicion.esPuerta and alguien.posicion.abierta:
                print("Entraste a la habitacion que esta al este")
            else: 
                print("La puerta esta cerrada") """
       pass
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
        #este metodo no se ha implementado
        """ if alguien.posicion.oeste:
            if alguien.posicion.oeste.abierta:
                print("Entraste a la habitacion que esta al oeste")
            else: 
                print("La puerta esta cerrada") """
        pass
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
        #este metodo no se ha implementado
        """ if alguien.posicion.norte:
            if alguien.posicion.norte.abierta:
                print("Entraste a la habitacion que esta al norte")
            else: 
                print("La puerta esta cerrada") """
        pass
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
       #este metodo no se ha implementado
       """ if alguien.posicion.sur:
            if alguien.posicion.sur.abierta:
                print("Entraste a la habitacion que esta al sur")
            else: 
                print("La puerta esta cerrada") """
       pass

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
        self.orientaciones = []
        self.este =None
        self.oeste =None
        self.norte =None 
        self.sur =None
        self.num=num
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
        self.este.entrarAlguien(alguien)
    def irAlOeste(self, alguien):
        self.oeste.entrarAlguien(alguien)
    def irAlNorte(self, alguien):
        self.norte.entrarAlguien(alguien)
    def irAlSur(self, alguien):
        self.sur.entrarAlguien(alguien)
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
        self.abierta = False
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta esta cerrada")

    def entrarAlguien(self, alguien):
        if self.abierta:
            print(self.printOn(), "abierta")
            if alguien.posicion == self.lado1:
                self.lado2.entrarAlguien(alguien)
            else:
                self.lado1.entrarAlguien(alguien)
        else:
            print(self.printOn(), "cerrada")
    
    def abrirPuertas(self):
        self.abierta = True
        print("Puerta abierta",self)
    def cerrarPuertas(self):    
        self.abierta = False
        print("Puerta cerrada",self)
    def esPuerta(self):   
        return True 
    def recorrer(self, unBloque):
        unBloque(self)
    def printOn(self):
        print('Puerta: ', self.lado1.num,'-', self.lado2.num)

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
    def entrar(self, alguien):
        pass
    def recorrer(self, unBloque):
        unBloque(self)

class Decorator(Hoja):
    def __init__(self):
        super().__init__()
        self.em=None
    def entrarAlguien(self, alguien):
        return self.em.entrarAlguien(alguien)
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
                print("No puedes atravesar la bomba")
    def entrarAlguien(self, alguien):
        self.entrar(alguien)
class Tunel(Hoja):
    def __init__(self):
        self.laberinto=None

    def entrar(self, alguien):
        print(alguien.nombre,"has entrado a un nuevo laberinto")
    
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
    def atacar(self, unBicho):
        unBicho.atacar()
class Ente():
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion =  None
        self.juego = None
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
    def __init__(self):
        super().__init__()
        self.modo = None
        #self.caminarAleatorio()
        
    def actua(self):
        self.modo.actua(self)

    def print_on(self):
        print(f"Bicho-{self.modo}")

    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)

    def atacar(self):
        self.juego.bichoBuscarPersonaje(self)

class Personaje(Ente):
    def __init__(self):
        super().__init__()
        self.nombre=None
        self.vidas=10
        self.poder=1

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
game.crearLaberinto()

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