from datetime import datetime
import os


class Log:
    tiposValidos = ("INFO", "WARNING", "ERROR")

    def __init__(self):
        fecha = datetime.now().strftime("%Y%m%d")
        self.ruta = f"log/{fecha}-villHeroe.log"

        if not os.path.exists("../log"):
            os.mkdir("../log")

    def escribir(self, tipo, mensaje):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        if tipo not in self.tiposValidos:
            tipo = "INFO"

        with open(self.ruta, "a") as fichero:
            fichero.write(f"[{fecha_hora}] [{tipo.upper()}] {mensaje}\n")