from menu import menu
from utils.logs import Log

logs = Log()
try:
    menu()
except BaseException as e:
    logs.escribir("ERROR", e)
    print(f"Se ha producido un error de aplicacion{e}")



