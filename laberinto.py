import random
import time


class Game:
    def __init__(self):
        self.maze = None
        self.bichos = []
        self.hilos = {}

    def create_wall(self):
        return Wall()
    
    def create_door(self,side1,side2):
        door=Door(side1,side2)
        return door  
    
    def create_room(self, id):
        return Room(id)

    def create_maze(self):
        return Maze()
    
    def make2RoomsMazeFM(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = self.create_door(room1,room2)
        room1.south=door
        room2.north=door
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        return self.maze
    
    def make2RoomsMaze(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

        door=Door(room1,room2)
        room1.south = door
        room2.north = door
        return self.maze
    
    def make2Rooms2BombasFM(self):
        hab1 = self.create_room(1)
        hab2 = self.create_room(2)
        puerta = self.create_door(hab1, hab2)
        
        hab1.north = self.create_wall()
        hab1.east = self.create_wall()
        hab1.west = self.create_wall()
        
        hab2.south = self.create_wall()
        hab2.east = self.create_wall()
        hab2.west = self.create_wall()
        
        puerta.side1 = hab1
        puerta.side2 = hab2
        
        hab1.south = puerta
        hab2.north = puerta
        
        bm1 = self.fabricarBomba()
        bm2 = self.fabricarBomba()
        
        hab1.agregarHijo(bm1)
        hab2.agregarHijo(bm2)
        
        self.maze = self.create_maze()
        
        self.maze.addRoom(hab1)
        self.maze.addRoom(hab2)

    def make2RoomsFMD(self):
        hab1 = self.create_room(1)
        hab2 = self.create_room(2)
        puerta = self.create_door(hab1, hab2)
        
        bm1 = self.fabricarBomba()
        bm1.em(self.create_wall())
        
        hab1.north = self.create_wall()
        hab1.east = bm1
        hab1.west = self.create_wall()
        
        bm2 = self.fabricarBomba()
        bm2.em(self.create_wall())
        
        hab2.south = self.create_wall()
        hab2.east = bm2
        hab2.west = self.create_wall()
        
        puerta.side1 = hab1
        puerta.side2 = hab2
        
        hab1.south = puerta
        hab2.north = puerta
        
        self.maze = self.create_maze()
        
        self.maze.addRoom(hab1)
        self.maze.addRoom(hab2)
    def make4Rooms4BichosFM(self):
        hab1 = self.create_room(1)
        hab2 = self.create_room(2)
        hab3 = self.create_room(3)
        hab4 = self.create_room(4)
           
        p12 = self.create_door(hab1, hab2)
        p13 = self.create_door(hab1, hab3)
        p34 = self.create_door(hab3, hab4)
        p24 = self.create_door(hab2, hab4)
            
        hab1.south = p12
        hab2.north = p12
            
        hab1.east = p13
        hab3.west = p13
            
        hab2.east = p24
        hab4.west = p24
            
        hab3.south = p34
        hab4.north = p34
            
        self.maze = self.create_maze()
            
        self.maze.addRoom(hab1)
        self.maze.addRoom(hab2)
        self.maze.addRoom(hab3)
        self.maze.addRoom(hab4)
            
        self.agregar_bicho(self.fabricarBichoAgresivo(hab1))
        self.agregar_bicho(self.fabricarBichoAgresivo(hab3))
        self.agregar_bicho(self.fabricarBichoPerezoso(hab2))
        self.agregar_bicho(self.fabricarBichoPerezoso(hab4))
        return self.maze
    def create_East(self):
        return Este
    def create_West(self):
        return Oeste
    def create_North(self):
        return Norte
    def create_South(self):
        return Sur
    def openDoor(self):
        for each in self.recorrer():
            each.abrir_puertas()
    def activar_bombas(self):
        for each in self.recorrer():
            if each.es_bomba():
                each.activar()
    def agregar_bicho(self, unBicho):
            self.bichos.append(unBicho)

    def cerrarPuertas(self):
        for each in self.recorrer():
            each.cerrar_puertas()
    def desactivarBombas(self):
        for each in self.recorrer():
            if each.es_bomba():
                each.desactivar()
    def eliminarBicho(self, Bicho):
        if Bicho in self.bichos:
            self.bichos.remove(Bicho)
        else:
            print("No existe ese bicho")

    def fabricarBichoAgresivo(self, Habitacion):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 2
        bicho.posicion = Habitacion
        return bicho
    def fabricarBichoPerezoso(self, Habitacion):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 2
        bicho.poder = 0
        bicho.posicion = Habitacion
        return bicho
    def fabricarBomba(self):
        return Bomba()
    def fabricarPuertaLados(self, lado1, lado2):
        puerta = self.create_door(lado1, lado2)
        return puerta
    def lanzarHilo(self, unBicho):
        proceso = [True]
        while proceso[0]:
            unBicho.actua()
        self.hilos[unBicho] = proceso
    def terminarHilo(self, unBicho):
        proceso = self.hilos.get(unBicho)
        if proceso is not None:
            proceso.terminate()

    def obtenerHabitacion(self, unNum):
        return self.maze.obtenerHabitacion(unNum)
    
    
class Orientation:
    def __init__(self):
        pass
    def caminar(Bicho):
        pass
    def ponerElemento(MapElement, Contenedor):
        pass
    def recorrer(Block):
        pass
class Este(Orientation):
    _instance = None
    def recorrerEn(Block,Contenedor):
        Contenedor.recorrer(Block)
    def ponerElemento(MapElement, Contenedor):
        Contenedor.este=MapElement
class Oeste(Orientation):
    def recorrerEn(Block,Contenedor):
        Contenedor.recorrer(Block)
    def ponerElemento(MapElement, Contenedor):
        Contenedor.oeste=MapElement
class Norte(Orientation):
    def recorrerEn(Block,Contenedor):
        Contenedor.recorrer(Block)
    def ponerElemento(MapElement, Contenedor):
        Contenedor.norte=MapElement
class Sur(Orientation):
    def recorrerEn(Block,Contenedor):
        Contenedor.recorrer(Block)
    def ponerElemento(MapElement, Contenedor):
        Contenedor.sur=MapElement
    

class MapElement:
    def __init__(self):
        pass
    def entrar(self):
        pass
class Contenedor(MapElement):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
    

class Maze(Contenedor):
    def __init__(self):
        self.rooms = []
        
    def addRoom(self, room):
        self.rooms.append(room)
    
    def entrar(self):
        hab=self.rooms[0]
        hab.entrar() 

    def numeroHabitaciones(self):
        return len(self.rooms)

    def obtenerHabitacion(self, unNum):
        return self.rooms[unNum-1]

class Room(Contenedor):
    def __init__(self,num):
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.num = num
    
    def entrar(self):
        print("Entraste a la habitacion ", self.num)
    def esHabitacion(self):
        return True
    def printOn(self):
        print('Hab')
        print(str(self.num))
class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False
    def entrar(self):
        if self.opened:
            self.side2.entrar()
        else:
            print("La puerta esta cerrada")
    def abrirPuertas(self):
        self.opened = True
    def cerrarPuertas(self):    
        self.opened = False
    def esPuerta(self):   
        return True 
    def recorrer(self, unBloque):
        unBloque(self)
    def printOn(self):
        print('Puerta: ', self.side1, self.side2)

class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("No puedes atravesar la pared")
    def esPared(self):
        return True
    def recorrer(self, unBloque):
        unBloque(self)
class Hoja(MapElement):
    def __init__(self):
        pass
    def accept(self, visitor):
        visitor.visitHoja(self)
    def recorrer(self):
        return self

class Decorator(Hoja):
    def __init__(self, component):
        self.component=component
class Bomba(Decorator):
    def __init__(self):
        self.activa=False
    def activar(self):
        self.activa=True
        print("Bomba activada")
    def desactivar(self):
        self.activa=False
        print("Bomba desactivada")
    def es_bomba(self):
        return True
    def entrar(self, alguien):
        if self.activa:
            print("La bomba ha explotado")
            # quitar vidas a alguien: en función del poder de la bomba
        else:
            if self.component is not None:
                self.component.entrar()
            else:
                print("No puedes atravesar la bomba")

class Contenedor(MapElement):
    def __init__(self):
        self.hijos =[]
        self.orientaciones = []
        self.este =None
        self.oeste =None
        self.norte =None
        self.sur =None
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)
    def caminarAleatorio(self, unBicho):
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
        for each in self.orientaciones:
            each.recorrerEn(unBloque, self)

class BomberWall(Wall):
    def __init__(self):
        return self
    def entrar(self):
        if isinstance(self, Bomba) and self.activa:
            print("¡Boom! Te has chocado con una pared-bomba")
            # Perform explosion logic here
        else:
            super().entrar()
    
class BomberGame(Game):
    def create_wall(self):
        return BomberWall()
    
class Bicho():
    def __init__(self, modo="Normal", vidas=3, poder=1, posicion=(0, 0)):
        self.modo = modo
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion

    def ir_al_este(self):
        x, y = self.posicion
        self.posicion = (x + 1, y)
        self.actua()
        
    def ir_al_norte(self):
        x, y = self.posicion
        self.posicion = (x, y + 1)
        self.actua()
        
    def ir_al_oeste(self):
        x, y = self.posicion
        self.posicion = (x - 1, y)
        self.actua()
       
    def ir_al_sur(self):
        x, y = self.posicion
        self.posicion = (x, y - 1)
        self.actua()
        
    def actua(self):
        print("¡El bicho se mueve!")
        print(f"Posición actual: {self.posicion}")

    def print_on(self):
        print(f"Bicho-{self.modo}")

    def caminar_aleatorio(self):
        # Generar nueva posición aleatoria
        nueva_posicion = (random.randint(1, 10), random.randint(1, 10))
        # Actualizar la posición y llamar a actua
        self.posicion = nueva_posicion
        self.actua()

class Modo():
    def __init__(self):
        pass
    def actua(self, Bicho):
        self.dormir(Bicho)
        self.caminar(Bicho)
    def dormir(self, unBicho):
        print(unBicho.__class__.__name__, "duerme")
        time.sleep(2)
    def caminar(self, unBicho):
        unBicho.caminarAleatorio()
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
game=Game()
game=BomberGame()
game.make2RoomsMaze()
game.make2RoomsMazeFM()
game.maze.entrar() 

bicho = Bicho()
bicho.ir_al_este()  # Llamando a actua después de cambiar la posición
bicho.caminar_aleatorio()
bicho.ir_al_norte()  # Llamando a actua después de cambiar la posición
bicho.ir_al_oeste()  # Llamando a actua después de cambiar la posición
bicho.ir_al_sur()  # Llamando a actua después de cambiar la posición

