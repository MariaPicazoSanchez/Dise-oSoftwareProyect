class Comandos:
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        pass

class Abrir(Comandos):
    def __init__(self, receptor):
        super().__init__(receptor)
        
    def ejecutar(self):
        self.receptor.eleminarComando(self)
        self.receptor.agregarComando(Cerrar(self.receptor))
        self.receptor.abrirPuertas()

class Cerrar(Comandos):
    def __init__(self, receptor):
        super().__init__(receptor)
    def ejecutar(self):
        self.receptor.eleminarComando(self)
        self.receptor.agregarComando(Abrir(self.receptor))
        self.receptor.cerrarPuertas()

class Entrar(Comandos):
    def ejecutar(self):
        # Lógica para ejecutar el comando de entrar
        pass