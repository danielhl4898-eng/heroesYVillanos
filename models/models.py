class Persona:
    def __init__(self, dni, nombre, apellido, fecha_nac):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.puntTotal = 0

class Villano(Persona):
    def setAtrVill(self, chatgepeteador, entregadorTardio, ausencias, hablador):
        self.chatgepeteador = chatgepeteador
        self.entregadorTardio = entregadorTardio
        self.ausencias = ausencias
        self.hablador = hablador

    def calcularMediaVill(self):
        self.puntTotal =(self.chatgepeteador+self.entregadorTardio+self.ausencias+self.hablador)/ 4
    def mostrarStats(self):
        print(self.__dict__)

class Heroe(Persona):
    def setAtrHeroe(self, codLimpio,codBienDoc,gitGod, arquitecto, detallista):
        self.codLimpio = codLimpio
        self.codBienDoc = codBienDoc
        self.gitGod = gitGod
        self.arquitecto = arquitecto
        self.detallista = detallista

    def calcularMediaHer(self):
        self.puntTotal = (self.codBienDoc+ self.codLimpio+self.arquitecto+self.detallista+self.gitGod)/5

    def pelea(self, villanoP):
        ganador=None
        if(self.puntTotal > villanoP.puntTotal):
            ganador = self
        else:
            ganador = villanoP
        return ganador

    def mostrarStats(self):
        print(self.__dict__)


