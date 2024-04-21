import random
from laberinto import Contenedor
class Forma:
    def __init__(self):
        self.orientaciones = []

    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)
    def irAlEste(self,alguien):
        pass
    def irAlOeste(self,alguien):    
        pass
    def irAlNorte(self,alguien):
        pass
    def irAlSur(self,alguien):
        pass
    def ponerElementoEn(self, unaOrientacion, unEM):
        unaOrientacion.ponerElementoEn(self,unEM)
    def recorrer(self, unBloque):
        for orientation in self.orientaciones:
            orientation.recorrer(unBloque, self)
    def obtenerElemento(self, unaOrientacion):
        return unaOrientacion.obtenerElementoDe(self)
    def obtenerOrientacionAleatoria(self):
        num_or = len(self.orientaciones)
        num_al = random.randint(0, num_or - 1)
        or_al = self.orientaciones[num_al]

        return or_al

class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        
    def irAlEste(self,alguien):
        self.este.entrar(alguien)
    def irAlOeste(self,alguien):
        self.oeste.entrar(alguien)


class Hexagono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
                
    def irAlNorEste(self, alguien):
        self.noreste.entrar(alguien)
                
    def irAlNorOeste(self, alguien):
        self.noroeste.entrar(alguien)
                
    def irAlSurEste(self, alguien):
        self.sureste.entrar(alguien)
                
    def irAlSurOeste(self, alguien):
        self.suroeste.entrar(alguien)

