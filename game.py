"consola para saber como funcionan los hilos"
import time
from laberinto import Game


game=Game()
game.create4Rooms4BeastFM()
sm="pepe"
game.maze.entrar(sm)
game.launchThreads()
time.sleep(5)
game.stopThreads()
