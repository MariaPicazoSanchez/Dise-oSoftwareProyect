"consola para saber como funcionan los hilos"
import time
from laberinto import Game


game=Game()
game.make4Rooms4BichosFM()
sm="pepe"
game.maze.entrarAlguien(sm)
game.lanzarHilo()
time.sleep(5)
game.terminarHilo()
