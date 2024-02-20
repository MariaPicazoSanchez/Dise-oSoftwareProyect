class Game:

    def __init__(self):
        self.maze = None

    def new_wall(self):
        return Wall()
    
    def new_door(self):
        return Door()

    def new_room(self, room_name, description, id):
        return Room(room_name, description, id)


    def createMaze2Hab(self):
        maze = Maze()
        self.maze = maze
        room1 = Room(1, "Room 1", "This is the first room")
        room2 = Room(2, "Room 2", "This is the second room")

        door=Door(room1, room2)

        room1.s_to = door  
        room2.n_to = door

        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

class MapElement:
    def __init__(self):
        pass

class Maze(MapElement):
    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        self.rooms.append(room)

class Room(MapElement):
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

class Wall(MapElement):
    def __init__(self):
        pass

class Door(MapElement):
    def __init__(self, from_room, to_room):
        self.from_room = from_room
        self.to_room = to_room

game = Game()


