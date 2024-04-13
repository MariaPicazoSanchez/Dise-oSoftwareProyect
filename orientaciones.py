class Orientation:
    def __init__(self):
        pass
    def caminar(self, Bicho):
        pass
    def ponerEn(self, EM, Contenedor):
        pass
    def recorrer(self,unBloque):
        pass
    
class Este(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlEste()
    def recorrerElementoEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
       #este metodo no se ha implementado
       """  if alguien.posicion.este:
            if alguien.posicion.esPuerta and alguien.posicion.abierta:
                print("Entraste a la habitacion que esta al este")
            else: 
                print("La puerta esta cerrada") """
       pass
class Oeste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlOeste()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.oeste=EM
    def entrar(self, alguien):
        #este metodo no se ha implementado
        """ if alguien.posicion.oeste:
            if alguien.posicion.oeste.abierta:
                print("Entraste a la habitacion que esta al oeste")
            else: 
                print("La puerta esta cerrada") """
        pass
class Norte(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlNorte()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
        #este metodo no se ha implementado
        """ if alguien.posicion.norte:
            if alguien.posicion.norte.abierta:
                print("Entraste a la habitacion que esta al norte")
            else: 
                print("La puerta esta cerrada") """
        pass
class Sur(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlSur()
    def recorrerEn(self,unBloque,unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self,EM, unCont):
        unCont.este=EM
    def entrar(self, alguien):
       #este metodo no se ha implementado
       """ if alguien.posicion.sur:
            if alguien.posicion.sur.abierta:
                print("Entraste a la habitacion que esta al sur")
            else: 
                print("La puerta esta cerrada") """
       pass
class NorEste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlNoreste()
    def recorrerEn(self, unBloque, unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self, EM, unCont):
        unCont.noreste = EM
    def entrar(self, alguien):
        # este metodo no se ha implementado
        """ if alguien.posicion.noreste:
            if alguien.posicion.noreste.abierta:
                print("Entraste a la habitacion que esta al noreste")
            else: 
                print("La puerta esta cerrada") """
        pass

class NorOeste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlNoroeste()
    def recorrerEn(self, unBloque, unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self, EM, unCont):
        unCont.noroeste = EM
    def entrar(self, alguien):
        # este metodo no se ha implementado
        """ if alguien.posicion.noroeste:
            if alguien.posicion.noroeste.abierta:
                print("Entraste a la habitacion que esta al noroeste")
            else: 
                print("La puerta esta cerrada") """
        pass

class SurEste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlSureste()
    def recorrerEn(self, unBloque, unCont):
        unCont.recorrer(unBloque)
    def ponerElemento(self, EM, unCont):
        unCont.sureste = EM
    def entrar(self, alguien):
        # este metodo no se ha implementado
        """ if alguien.posicion.sureste:
            if alguien.posicion.sureste.abierta:
                print("Entraste a la habitacion que esta al sureste")
            else: 
                print("La puerta esta cerrada") """
        pass

class SurOeste(Orientation):
    def __init__(self):
        super().__init__()
    def caminar(self, alguien):
        alguien.irAlSuroeste()
    def recorrerEn(self, unBloque, unCont):
        unCont.recorrer(unBloque)
    def ponerEn(self, EM, unCont):
        unCont.suroeste = EM
    def entrar(self, alguien):
        # este metodo no se ha implementado
        """ if alguien.posicion.suroeste:
            if alguien.posicion.suroeste.abierta:
                print("Entraste a la habitacion que esta al suroeste")
            else: 
                print("La puerta esta cerrada") """
        pass