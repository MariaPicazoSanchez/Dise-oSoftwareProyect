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
    def irAlNorte(self,alguien):
        self.norte.entrar(alguien)
    def irAlSur(self,alguien):
        self.sur.entrar(alguien)



