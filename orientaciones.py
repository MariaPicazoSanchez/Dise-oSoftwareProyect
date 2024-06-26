from punto import Punto
class Orientation:
    def __init__(self):
        pass
    def calcularPosicionDesde(self, unaForma):
        pass
    def obtenerComandoDe(self, unaForma):
        pass
    def caminar(self, Bicho):
        pass
    def obtenerElementoDe(self, unaForma):
        pass
    def ponerElementoEn(self, EM, unCont):
        pass
    def recorrer(self, unBloque, unCont):
        pass

class Este(Orientation):
    def __init__(self):
        super().__init__()
    def calcularPosicionDesde(self, unaForma):
        p = unaForma.punto
        #if isinstance(p, Punto):
        unPunto = (p.x+1,p.y)#aquii
        unaForma.este.calcularPosicionDesdeEn(unaForma,unPunto)
        print("Calculando posicion desde",unPunto)
    #mirar como hacerlo en python
    def obtenerComandoDe(self, unaForma):
        return unaForma.este.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlEste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.este
    def ponerElementoEn(self, EM, unCont):
        unCont.este = EM
    def recorrer(self, unBloque, unCont):
        unCont.este.recorrer(unBloque)
class Oeste(Orientation):
    def __init__(self):
        super().__init__()
    def calcularPosicionDesde(self, unaForma):
        p = unaForma.punto
        #if isinstance(p, Punto):
        unPunto = (p.x-1,p.y)
        unaForma.oeste.calcularPosicionDesdeEn(unaForma,unPunto)
    def obtenerComandoDe(self, unaForma):
        return unaForma.oeste.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlOeste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.oeste
    def ponerElementoEn(self, EM, unCont):
        unCont.oeste = EM
    def recorrer(self, unBloque, unCont):
        unCont.oeste.recorrer(unBloque)

class Norte(Orientation):
    def __init__(self):
        super().__init__()
    def calcularPosicionDesde(self, unaForma):
        p = unaForma.punto
        #if isinstance(p, Punto):
        unPunto = (p.x,p.y-1)
        unaForma.norte.calcularPosicionDesdeEn(unaForma,unPunto)
    def obtenerComandoDe(self, unaForma):
        return unaForma.norte.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlNorte()
    def obtenerElementoDe(self, unaForma):
        return unaForma.norte
    def ponerElementoEn(self, EM, unCont):
        unCont.norte = EM
    def recorrer(self, unBloque, unCont):
        unCont.norte.recorrer(unBloque)
class Sur(Orientation):
    def __init__(self):
        super().__init__()
    def calcularPosicionDesde(self, unaForma):
        p = unaForma.punto
        #if isinstance(p, Punto):
        unPunto = (p.x,p.y+1)
        unaForma.sur.calcularPosicionDesdeEn(unaForma,unPunto)
    def obtenerComandoDe(self, unaForma):
        return unaForma.sur.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlSur()
    def obtenerElementoDe(self, unaForma):
        return unaForma.sur
    def ponerElementoEn(self, EM, unCont):
        unCont.sur = EM
    def recorrer(self, unBloque, unCont):
        unCont.sur.recorrer(unBloque)
class NorEste(Orientation):
    def __init__(self):
        super().__init__()
    def obtenerComandoDe(self, unaForma):
        return unaForma.noreste.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlNoreste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.noreste
    def ponerElementoEn(self, EM, unCont):
        unCont.noreste = EM
    def recorrer(self, unBloque, unCont):
        unCont.noreste.recorrer(unBloque)

class NorOeste(Orientation):
    def __init__(self):
        super().__init__()
    def obtenerComandoDe(self, unaForma):
        return unaForma.noroeste.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlNoroeste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.noroeste
    def ponerElementoEn(self, EM, unCont):
        unCont.noroeste = EM
    def recorrer(self, unBloque, unCont):
        unCont.noroeste.recorrer(unBloque)

class SurEste(Orientation):
    def __init__(self):
        super().__init__()
    def obtenerComandoDe(self, unaForma):
        return unaForma.sureste.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlSureste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.sureste
    def ponerElementoEn(self, EM, unCont):
        unCont.sureste = EM
    def recorrer(self, unBloque, unCont):      
        unCont.sureste.recorrer(unBloque)

class SurOeste(Orientation):
    def __init__(self):
        super().__init__()
    def obtenerComandoDe(self, unaForma):
        return unaForma.suroeste.obtenerComandos()
    def caminar(self, alguien):
        alguien.irAlSuroeste()
    def obtenerElementoDe(self, unaForma):
        return unaForma.suroeste
    def ponerElementoEn(self, EM, unCont):
        unCont.suroeste = EM
    def recorrer(self, unBloque, unCont):
        unCont.suroeste.recorrer(unBloque)