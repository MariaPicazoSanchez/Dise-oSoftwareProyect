class Game:
    def __init__(self):
        self.maze = None

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
        self.maze = Maze()
        room1 = Room(1)
        room2 = Room(2)
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
        
        self.laberinto = self.create_maze()
        
        self.laberinto.addRoom(hab1)
        self.laberinto.addRoom(hab2)

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
        
        self.laberinto = self.create_maze()
        
        self.laberinto.addRoom(hab1)
        self.laberinto.addRoom(hab2)
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
            
            self.laberinto = self.create_maze()
            
            self.laberinto.addRoom(hab1)
            self.laberinto.addRoom(hab2)
            self.laberinto.addRoom(hab3)
            self.laberinto.addRoom(hab4)
            
            self.agregar_bicho(self.fabricarBichoAgresivo(hab1))
            self.agregar_bicho(self.fabricarBichoAgresivo(hab3))
            self.agregar_bicho(self.fabricarBichoPerezoso(hab2))
            self.agregar_bicho(self.fabricarBichoPerezoso(hab4))
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
        return self.laberinto.obtenerHabitacion(unNum)
    
    
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
        self.rooms[0].entrar()  
    def numeroHabitaciones(self):
        return len(self.rooms)

    def obtenerHabitacion(self, unNum):
        return self.rooms[unNum]

class Room(Contenedor):
    def __init__(self,id):
        self.north = Wall()
        self.east = Wall()
        self.west = Wall()
        self.south = Wall()
        self.id = id
    
    def entrar(self):
        print("Entraste a la habitacion ", self.id)
    def esHabitacion(self):
        return True
    def printOn(self):
        print('Hab')
        print(str(self.id))
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
    
class Wall(MapElement):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("No puedes atravesar la pared")
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
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

class BomberWall(Wall):
    def __init__(self):
        return self
    
class BomberGame(Game):
    def create_wall(self):
        return BomberWall()
    
class Bicho():
    def __init__(self):
        self.modo = None
        self.vidas = 0
        self.poder = 0
        self.posicion = None

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



