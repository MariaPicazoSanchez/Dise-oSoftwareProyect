class Comandos:
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self,alguien):
        pass

class Abrir(Comandos):
    def __init__(self, receptor):
        super().__init__(receptor)
        
    def ejecutar(self,alguien):
        self.receptor.eleminarComando(self)
        self.receptor.agregarComando(Cerrar(self.receptor))
        self.receptor.agregarComando(Entrar(self.receptor))
        self.receptor.abrirPuertas()
    def printOn(self):
        print("Abrir-", self.receptor)

class Cerrar(Comandos):
    def __init__(self, receptor):
        super().__init__(receptor)
    def ejecutar(self,alguien):
        self.receptor.eleminarComando(self)
        self.receptor.agregarComando(Abrir(self.receptor))
        self.receptor.cerrarPuertas()
    def printOn(self):
        print("Cerrar-", self.receptor)

class Entrar(Comandos):
    def __init__(self, receptor):
        super().__init__(receptor)
    
    def ejecutar(self,alguien):
        self.receptor.entrarAlguien(alguien)