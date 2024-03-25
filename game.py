"consola para saber como funcionan los hilos"
import time
from laberinto import Juego,Bicho,Agresivo,Habitacion,Personaje


game=Juego()
game.fabLab4Hab4BichosFM()
per=Personaje()
per.nombre="Juan"
game.laberinto.entrarAlguien(per)
game = Juego()
bicho = Bicho()
bicho.modo = Agresivo()
bicho.vidas = 3
bicho.poder = 5
bicho.posicion = Habitacion(1)
game.lanzarHilo(bicho)
time.sleep(15)
game.terminarHilo(bicho)