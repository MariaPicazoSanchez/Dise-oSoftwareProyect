import tkinter as tk
from builder import Director
from tkinter import KeyboardKey
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class LaberintoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.person = None
        self.juego = None
        self.win = None
        self.ancho = None
        self.alto = None
        self.vidasM=None
        self.mAP=None
        self.mCP=None
        self.mLB=None
        self.personM=None
        self.bichosM = {}
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
        origen = Punto(70, 10)
        for each in self.juego.laberinto.hijos:
            x = origen.x + (each.punto.x * self.ancho)
            y = origen.y + (each.punto.y * self.alto)
            each.punto = Punto(x, y)
            each.extent = Punto(self.ancho, self.alto)

    def calcularDimensiones(self):
        maxX, maxY = 0, 0
        for each in self.juego.laberinto.hijos:
            maxX = max(maxX, each.punto.x)
            maxY = max(maxY, each.punto.y)
        maxX += 1
        maxY += 1
        self.ancho = round(1050 / maxX)
        self.alto = round(600 / maxY)

    def calcularPosicion(self):
        h1 = self.juego.obtenerHabitacion(1)
        h1.punto = Punto(0, 0)
        h1.calcularPosicion()

    def dibujarLaberinto(self):
        if self.juego is None:
            return self
        self.juego.laberinto.aceptar(self)
        self.mostrarVidasPersonaje(self)
        self.mostrarAbrirPuertas()
        self.mostrarCerrarPuertas()
        self.mostrarLanzarBichos()
        self.mostrarPersonaje()
        self.mostrarBichos()

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()

    def normalizar(self):
        minX, minY = float('inf'), float('inf')
        for each in self.juego.laberinto.hijos:
            if each.punto.x < minX:
                minX = each.punto.x
            if each.punto.y < minY:
                minY = each.punto.y
        for each in self.juego.laberinto.hijos:
            x, y = each.punto.x, each.punto.y
            each.punto = Punto(x + abs(minX), y + abs(minY))

    def visitarHabitacion(self, unaHab):
        pass  # Implementación pendiente
    def lanzarBicho(self):
        self.juego.bichos = [each.addDependent(self) for each in self.juego.bichos]
        self.juego.lanzarTodosHilos()

    def mostrarBicho(self, unBicho):
        if unBicho.estaVivo:
            unCont = unBicho.posicion
            col = unBicho.modo.color
            an = unCont.extend.x
            al = unCont.extend.y
            a = (unCont.punto.x) + (an // 3) + (an // 9)
            b = (unCont.punto.y) + (al // 3) + 3
            c = an // 9
            d = al // 8
            if bichoM is None:
                rec = BalloonMorph.new(extent=(c, c))
                rec.borderWidth = 1
                rec.color = Color.perform(col)
                self.addMorph(rec)
                bichoM = rec
                self.bichosM[unBicho] = rec
            bichoM.position = self.position + (a, b)
        else:
            bichoM.delete()
            # self.bichosM[unBicho] = None
    #protocolo event handling
    def keyDown(self, anEvent):
        key = anEvent.key
        if key == KeyboardKey.up:
            self.person.irAlNorte()
        elif key == KeyboardKey.down:
            self.person.irAlSur()
        elif key == KeyboardKey.right:
            self.person.irAlEste()
        elif key == KeyboardKey.left:
            self.person.irAlOeste()
        elif key.value == 65:
            self.person.atacar()
    def handlesKeyDown(self, anEvent):
        return True
    def mouseEnter(self, anEvent):
        anEvent.hand.newKeyboardFocus(self)

    def mouseLeave(self, anEvent):
        anEvent.hand.releaseKeyboardFocus(self)
    def handlesMouseOver(self, anEvent):
        return True
    def handlesMouseDown(self, anEvent):
        return True
    
vista = LaberintoGUI()
vista.iniciarJuego()
