import tkinter as tk

import keyboard
from builder import Director
from tkinter import Button,Canvas, Text
from punto import Punto
class TextMorph(Text):
    def __init__(self, master, width, height, borderwidth, background, foreground, **kwargs):
        super().__init__(master, width=width, height=height, borderwidth=borderwidth, background=background, foreground=foreground, **kwargs)

class BorderedMorph(Canvas):
    def __init__(self, master, width, height, border_width=2, border_color="black", **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.border_width = border_width
        self.border_color = border_color
        self.create_rectangle(0, 0, width, height, outline=border_color, width=border_width)
class SimpleButtonMorph(Button):
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

class LaberintoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.person = None
        self.juego = None
        self.win = None
        self.ancho = 1150
        self.alto = 900
        self.vidasM = None
        self.mAP = None
        self.mCP = None
        self.mLB = None
        self.personM = None
        self.bichosM = {}
        self.canvas = Canvas(self, width=self.ancho, height=self.alto, bg="white", borderwidth=2, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.bind("<KeyPress>", self.keyDown)
        self.bind("<Enter>", self.mouseEnter)
        self.bind("<Leave>", self.mouseLeave)   

    def reset(self):
        self.personM = None
        self.bichos= {}
        if self.win is not None:
            self.win.destroy()
        self.iniciarJuego()

    def update(self, unObjeto):
        self.mostrarVidasPersonaje()
        self.mostrarPersonaje()
        self.mostrarBichos()

    def abrirPuertas(self):
        self.juego.abrirPuertas()
    def cerrarPuertas(self):
        self.juego.cerrarPuertas()

    def agregarPersonaje(self, unaCadena):
        self.juego.agregarPersonaje(unaCadena)
        self.person = self.juego.person
        self.person.addDependent(self)
    def openInWindowLabeled(self, unaCadena):
        if self.win is not None:
            self.win.destroy()
        win = tk.Toplevel()
        win.title(unaCadena)
        return win
    def iniciarJuego(self):
        director = Director()
        director.procesar("C:\\Users\\maria\\Documents\\2 Ing\\Diseño software\\DiferentesLaberintos\\1erLaberinto\\laberinto2hab.json")
        self.juego = director.obtenerJuego()
        self.mostrarLaberinto()
        self.win = self.openInWindowLabeled('LaberintoGUI')
        self.agregarPersonaje('Prota')
        self.dibujarLaberinto()

    def terminarBichos(self):
        self.juego.terminarTodosHilos()
    def asignarPuntosReales(self):
        origen = Punto(70, 10)
        for each in self.juego.laberinto.hijos:
            x = origen.getX() + (each.forma.punto.getX() * self.ancho)
            y = origen.getY() + (each.forma.punto.getY() * self.alto)
            each.punto = Punto(x, y)
            each.extent = Punto(self.ancho, self.alto)

    def calcularDimensiones(self):
        maxX, maxY = 0, 0
        for each in self.juego.laberinto.hijos:
            maxX = max(maxX, each.forma.punto.x)
            maxY = max(maxY, each.forma.punto.y)
        maxX += 1
        maxY += 1
        self.ancho = round(1050 / maxX)
        self.alto = round(600 / maxY)

    def calcularPosicion(self):
        h1 = self.juego.obtenerHabitacion(1)
        h1.punto = Punto(0, 0)
        h1.calcularPosicion()

    def dibujarContenedorRectangular(self, unaForma, escala):
        unPunto = unaForma.punto
        an = unaForma.extend[0] / escala
        al = unaForma.extend[1] / escala
        rec = BorderedMorph(self, width=an, height=al)
        rec.color = "white"
        rec.borderWidth = 2
        rec.pack()  # Ajusta el método de posicionamiento según tu diseño
        rec.place(x=self.winfo_x() + unPunto[0], y=self.winfo_y() + unPunto[1])

    def dibujarLaberinto(self):
        if self.juego is None:
            return self
        self.juego.laberinto.aceptar(self.juego.laberinto)
        self.mostrarVidasPersonaje()
        self.mostrarAbrirPuertas()
        self.mostrarCerrarPuertas()
        self.mostrarLanzarBichos()
        self.mostrarPersonaje()
        self.mostrarBichos()
        self.mostrarVolverAJugar()
        self.win.mainloop()

    def mostrarVolverAJugar(self):
        aP = SimpleButtonMorph(self, text='Reset', command=self.reset)
        aP.pack()  # Ajusta el método de posicionamiento según tu diseño
        aP.place(x=self.winfo_x() + 5, y=self.winfo_y() + 180)
        
    def mostrarDetenerBichos(self):
        self.mLB = SimpleButtonMorph(self, text='Detener', command=self.terminarBichos)
        self.mLB.pack()  # Ajusta el método de posicionamiento según tu diseño
        self.mLB.place(x=self.winfo_x() + 5, y=self.winfo_y() + 160)

    def mostrarLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()

    def normalizar(self):
        minX = 0
        minY = 0
        eje=Punto(11,12)
        print(eje.getX(),eje.getY())
        for each in self.juego.laberinto.hijos:
            puntoEje = each.forma.punto
            x = puntoEje.getX()
            y = puntoEje.getY()
            if x < minX:
                minX = x
            if y < minY:
                minY = y

        for each in self.juego.laberinto.hijos:
            newx, newy = x, y
            each.puntoSet(Punto(newx + abs(minX), newy + abs(minY)))

    def visitarHabitacion(self, unaHab):
        self.dibujarContenedorRectangular(unaHab.forma, escala=1)
    def visitarArmario(self, unArmario):
        pass
    def visitarBomba(self, unaBomba):
        pass
    def visitarTunel(self, unTunel):
        pass
    def lanzarBichos(self):
        self.juego.bichos = [each.addDependent(self) for each in self.juego.bichos]
        self.juego.lanzarTodosHilos()
    def mostrarAbrirPuertas(self):
        self.mAP = SimpleButtonMorph(self, text="Abrir", command=self.abrirPuertas)
        self.mAP.pack()  # Ajusta el método de posicionamiento según tu diseño
        self.mAP.place(x=self.winfo_x() + 5, y=self.winfo_y() + 70)
    def mostrarCerrarPuertas(self):
        self.mCP = SimpleButtonMorph(self, text="Cerrar", command=self.cerrarPuertas)
        self.mCP.pack()  # Ajusta el método de posicionamiento según tu diseño
        self.mCP.place(x=self.winfo_x() + 5, y=self.winfo_y() + 95)
    def mostrarBicho(self, unBicho):
        if unBicho.estaVivo:
            unCont = unBicho.posicion
            col = unBicho.modo.color
            an = unCont.obtenerExtend().getX()
            al = unCont.obtenerExtend().getY()
            a = unCont.obtenerExtend().getX() + (an // 3) + (an // 9)
            b = unCont.obtenerExtend().getY() + (al // 3) + 3
            c = an // 9
            d = al // 8
            color = col  # Utiliza directamente el nombre del color
            rect = self.canvas.create_rectangle(a, b, a + c, b + d, fill=color, outline="black")
            self.bichosM[unBicho] = rect
        else:
            rect = self.bichosM.pop(unBicho, None)
            if rect is not None:
                self.canvas.delete(rect)

    def mostrarBichos(self):
        for each in self.juego.bichos:
            self.mostrarBicho(each)
    
    def mostrarLanzarBichos(self):
        self.mLB = Button(self, text='Iniciar', command=self.lanzarBichos)
        self.mLB.pack()
        self.mLB.place(x=self.winfo_x() + 5, y=self.winfo_y() + 130)

    def mostrarPersonaje(self):
        if self.juego.person is None:
            return
        unCont = self.juego.person.posicion
        an = unCont.obtenerExtend().getX()
        al = unCont.obtenerExtend().getY()
        a = unCont.obtenerExtend().getX() + (an // 2)
        b = unCont.obtenerExtend().getY() + (al // 2)
        c = an // 9
        d = al // 8
        if self.personM is None:
            rec = BorderedMorph(self, width=c, height=d, border_width=2, border_color="black")
            rec.pack()  # Ajusta el método de posicionamiento según tu diseño
            self.personM = rec
        self.personM.place(x=self.winfo_x() + a, y=self.winfo_y() + b)

    def mostrarVidasPersonaje(self):
        if self.vidasM is None:
            tM = TextMorph(self, width=10, height=1, borderwidth=1, background="green", foreground="black")
            tM.pack()  # Ajusta el método de posicionamiento según tu diseño
            tM.place(x=self.winfo_x() + 5, y=self.winfo_y() + 40)
            self.vidasM = tM
        self.vidasM.delete("1.0", "end")
        self.vidasM.insert("end", " " + str(self.person.vidas) + " ")
    


    #protocolo event handling
    def keyDown(self, event):
        key = event.keysym
        if key == "Up":
            self.person.irAlNorte()
        elif key == "Down":
            self.person.irAlSur()
        elif key == "Right":
            self.person.irAlEste()
        elif key == "Left":
            self.person.irAlOeste()
        elif event.keycode == 65:  # Código de tecla ASCII para 'A'
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

