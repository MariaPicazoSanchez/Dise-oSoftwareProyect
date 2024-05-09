


class EstadoEnte:
    def __init__ (self):
        pass
    def atacar(self,alguien):
        pass
    def estaVivo(self):
        pass

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()
    def atacar(self, alguien):
        #print("Los muertos no pueden atacar")
        pass
    def estaVivo(self):
        return False
    
class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()
    def atacar(self, alguien):
        alguien.puedeAtacar()
    def estaVivo(self):
        return True
    


class EstadoPuerta:
    def __init__(self):
        pass
    def abrirPuertas(self, unaPuerta):
        pass
    def cerrarPuertas(self, unaPuerta):
        pass
    def estaAbierta(self):
        pass

class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()
    def abrirPuertas(self, unaPuerta):
        #print("La puerta ya está abierta")
        pass
    def cerrarPuertas(self,unaPuerta):
        unaPuerta.estado = Cerrada()
        print("La puerta " + str(unaPuerta) + " está cerrada")
    def estaAbierta(self):
        return True
    
class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()
    def abrirPuertas(self,unaPuerta):
        unaPuerta.estado = Abierta()
        print("La puerta " + str(unaPuerta) + " está abierta")

    def cerrarPuertas(self, unaPuerta):
        #print("La puerta ya está cerrada")
        pass
    def estaAbierta(self):
        return False

class EstadoEnte:
    def __init__ (self):
        pass
    def atacar(self,alguien):
        pass
    def estaVivo(self):
        pass
    def actua(self,unBicho):
        pass

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def estaVivo(self):
        return False
    
    def atacar(self, alguien):
        #print("Los muertos no pueden atacar")
        pass

    def actua(self,unBicho):
        print("Los muertos no pueden actuar")
        
class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    def estaVivo(self):
        return True
    
    def atacar(self, alguien):
        alguien.puedeAtacar()
        
    def actua(self,unBicho):
        unBicho.puedeActuar()
