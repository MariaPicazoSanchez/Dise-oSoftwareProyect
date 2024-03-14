"consola para saber como funcionan los hilos"
import time
from laberinto import Game,Bicho,Agresivo,Room


game=Game()
game.make4Rooms4BichosFM()
sm="pepe"

game.maze.entrarAlguien(sm)
game = Game()
bicho = Bicho(Agresivo(), 3, 5, Room(1))
game.lanzarHilo(bicho)
time.sleep(15)
game.terminarHilo(bicho)