import tkinter as tk
from builder import Director

class LaberintoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.person = None
        self.juego = None
        self.win = None
        self.ancho = None
        self.alto = None
        self.geometry("1150x900")
        self.config(borderwidth=2, relief="ridge")
        self.config(bg="white")

    def agregarPersonaje(self, unaCadena):
        self.juego.agregarPersonaje(unaCadena)
        self.person = self.juego.person
        self.person.addDependent(self)

    def iniciarJuego(self):
        director = Director()
        director.procesar(r'C:\Users\maria\Documents\2 Ing\Diseño software\DiferentesLaberintos\1erLaberinto\laberinto2habTunel2Bichos.json')
        self.juego = director.obtenerJuego()
        self.mostrarLaberinto()
        self.win = self.openInWindowLabeled('LaberintoGUI')
        self.agregarPersonaje('Prota')
        self.dibujarLaberinto()

    def asignarPuntosReales(self):
        origen = (70, 10)
        for each in self.juego.laberinto.hijos:
            x = origen[0] + (each.punto[0] * self.ancho)
            y = origen[1] + (each.punto[1] * self.alto)
            each.punto = (x, y)
            each.extent = (self.ancho, self.alto)

    def calcularDimensiones(self):
        maxX, maxY = 0, 0
        for each in self.juego.laberinto.hijos:
            maxX = max(maxX, each.punto[0])
            maxY = max(maxY, each.punto[1])
        maxX += 1
        maxY += 1
        self.ancho = round(1050 / maxX)
        self.alto = round(600 / maxY)

    def calcularPosicion(self):
        h1 = self.juego.obtenerHabitacion(1)
        h1.punto = (0, 0)
        h1.calcularPosicion()

    def dibujarLaberinto(self):
        if self.juego is None:
            return
        self.juego.laberinto.aceptar(self)

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()

    def normalizar(self):
        minX, minY = float('inf'), float('inf')
        for each in self.juego.laberinto.hijos:
            if each.punto[0] < minX:
                minX = each.punto[0]
            if each.punto[1] < minY:
                minY = each.punto[1]
        for each in self.juego.laberinto.hijos:
            x, y = each.punto
            each.punto = (x + abs(minX), y + abs(minY))

    def visitarHabitacion(self, unaHab):
        pass  # Implementación pendiente



vista = LaberintoGUI()
vista.iniciarJuego()
