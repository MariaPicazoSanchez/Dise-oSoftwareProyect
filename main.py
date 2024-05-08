from builder import Director
import keyboard


def main(): #stdscr
 
    director=Director()
    director.procesar('C:\\Users\\jgallud\\CloudStation\\asignaturas\\diseño de sofware\\curso23-24\\laberintos\\maze2room.json')
    game=director.getGame()
    game.addPerson("Pepe")
    person=game.person
    game.openDoors()
    game.launchThreds()
    while True:
        if keyboard.is_pressed('q'):
            break  # Exit the program
        elif keyboard.is_pressed("w"): #curses.KEY_UP:
            person.goNorth()
        elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
            person.goSouth()
        elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
            person.goWest()
        elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
            person.goEast()
        elif keyboard.is_pressed("enter"):#curses.KEY_ENTER or key in [10, 13]:
            person.attack()
    game.stopThreds()
#main()