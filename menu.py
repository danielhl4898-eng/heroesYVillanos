import factorias
from models import models
import random
from utils.logs import Log
from datetime import datetime

log= Log()

def menu():
    arrayPersonas = []
    heroes =[]
    villanos=[]
    opcion = 0
    heroeAct=None
    villanoAct=None
    log.escribir("WARNING", "PROGRAMA INICIADO")
    while opcion!= 12:
        print("¿Qué es lo que quieres hacer?:\n"
              "1. Generar héroes y villanos\n"
              "2. Buscar héroe por nombre\n"
              "3. Buscar villano por nombre\n"
              "4. Elegir heroe aleatorio\n"
              "5. Elegir villano aleatorio\n"
              "6. Iniciar pelea\n"
              "7. Mostrar estadísticas del héroe seleccionado\n"
              "8. Mostrar estadísticas del villano seleccionado\n"
              "9. Buscar persona por dni\n"
              "10. Buscar persona por apellido\n"
              "11. Buscar persona por fecha de nacimiento\n"
              "12. Salir")
        opcion = int(input())

        if opcion == 1:

            log.escribir("INFO", "OPCIÓN ELEGIDA: 1")

            decision = 0
            while decision >7 or decision <= 0:
                print("Cuantas quieres crear? (se harán el doble de las que pongas, 1 héroe por villano, máx. 7)\n")
                decision= int(input())
            arrayPersonas = factorias.crearPersonas(decision)
            for i in arrayPersonas:
                if isinstance(i, models.Heroe):
                    heroes.append(i)
                elif isinstance(i, models.Villano):
                    villanos.append(i)
            log.escribir("WARNING", "PERSONAS CREADAS")


        elif opcion == 2:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 2")
            if arrayPersonas == []:
                print("Las personas no han sido creadas cachondo")
                log.escribir("WARNING", "LAS PERSONAS NO HAN SIDO CREADAS AÚN")
            else:
                print("Dime el nombre del héroe al que quieres buscar:\n")

                decision2 = input()
                encontrado=None
                for i in heroes:
                    if i.nombre == decision2:
                        encontrado = i
                        break
                if encontrado is None:
                    print(f"No se ha encontrado el héroe {decision2}")
                    log.escribir("INFO", f"No se ha encontrado el héroe {decision2}")
                else:
                    print(encontrado.__dict__)
                    log.escribir("INFO", f"Se ha encontrado el héroe {decision2} y se ha mostrado por pantalla")


        elif opcion == 3:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 3")
            if arrayPersonas == []:
                print("Las personas no han sido creadas cachondo")
                log.escribir("WARNING", "LAS PERSONAS NO HAN SIDO CREADAS AÚN")
            else:
                decision3 = input("Dime el nombre del villano al que quieres buscar:\n")
                encontrado = None
                for i in villanos:
                    if i.nombre == decision3:
                        encontrado = i
                        break
                if encontrado is None:
                    print(f"No se ha encontrado el villano {decision3}")
                    log.escribir("INFO", f"No se ha encontrado el villano {decision3}")
                else:
                    print(encontrado.__dict__)
                    log.escribir("INFO", f"Se ha encontrado el villano {decision3} y se ha mostrado por pantalla")

        elif opcion == 4:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 4")
            if arrayPersonas == []:
                print("Las personas no han sido creadas cachondo")
                log.escribir("WARNING", "LAS PERSONAS NO HAN SIDO CREADAS AÚN")
            else:
                heroeAct = random.choice(heroes)
                log.escribir("INFO", f"HEROE ELEGIDO: {heroeAct.nombre}")

        elif opcion == 5:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 5")
            if arrayPersonas == []:
                print("Las personas no han sido creadas cachondo")
                log.escribir("WARNING", "LAS PERSONAS NO HAN SIDO CREADAS AÚN")
            else:
                villanoAct = random.choice(villanos)
                log.escribir("INFO", f"VILLANO ELEGIDO: {villanoAct.nombre}")

        elif opcion == 6:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 6")
            if villanoAct is not None and heroeAct is not None:
                log.escribir("INFO", "PELEA INICIADA")
                ganador= heroeAct.pelea(villanoAct)
                print(f"{ganador.nombre} HA GANADO LA PELEA\n")
                log.escribir("WARNING", f"{ganador.nombre} HA GANADO LA PELEA")
                if ganador in heroes:
                    villanos.remove(villanoAct)
                    villanoAct = None
                else:
                    heroes.remove(heroeAct)
                    heroeAct = None
            else:
                log.escribir("WARNING", "PELEA NO INICIADA")
                print("Necesitas tener un heroe random y un villano random para iniciar una pelea\n")
        elif opcion == 7:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 7")
            if heroeAct is not None:
                heroeAct.mostrarStats()
                log.escribir("INFO", "SE HA MOSTRADO LAS ESTADÍSTICAS DEL HEROE SELECCIONADO")
        elif opcion == 8:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 8")
            if villanoAct is not None:
                villanoAct.mostrarStats()
                log.escribir("INFO", "SE HA MOSTRADO LAS ESTADÍSTICAS DEL VILLANO SELECCIONADO")

        elif opcion == 9:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 9")
            dniABuscar= int(input())
            persona = None
            for i in arrayPersonas:
                if(i.dni == dniABuscar):
                    persona = i
                    break
            if persona is not None:
                print(persona.__dict__)
                log.escribir("INFO", f"SE HA MOSTRADO POR PANTALLA LA PERSONA {persona.nombre}")
            else:
                print(f"No se ha encontrado a la persona que tiene de dni {dniABuscar}")
                log.escribir("INFO", f"NO SE HA ENCONTRADO A LA PERSONA")

        elif opcion == 10:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 10")
            apellidoABuscar = input()
            persona = None
            for i in arrayPersonas:
                if (i.apellido == apellidoABuscar):
                    persona = i
                    break
            if persona is not None:
                print(persona.__dict__)
                log.escribir("INFO", f"SE HA MOSTRADO POR PANTALLA LA PERSONA {persona.nombre}")
            else:
                print(f"No se ha encontrado a la persona que tiene de apellido {apellidoABuscar}")
                log.escribir("INFO", f"NO SE HA ENCONTRADO A LA PERSONA")

        elif opcion == 11:
            log.escribir("INFO", "OPCIÓN ELEGIDA: 11")
            fechaABuscar= datetime.strptime(input("Dime la fecha de nacimiento del que quieras buscar (dd/mm/aaa)\n"), "%d/%m/%Y")
            persona = None
            for i in arrayPersonas:
                if i.fecha_nac.strftime("%d/%m/%Y") == fechaABuscar.strftime("%d/%m/%Y"):
                    persona = i
                    break
            if persona is not None:
                print(persona.__dict__)
                log.escribir("INFO", f"SE HA MOSTRADO POR PANTALLA LA PERSONA {persona.nombre}")
            else:
                print(f"No se ha encontrado a la persona que tiene de fecha de nacimiento {fechaABuscar.strftime("%d/%m/%Y")}")
                log.escribir("INFO", f"NO SE HA ENCONTRADO A LA PERSONA")

        elif opcion == 12:
            log.escribir("WARNING", "PROGRAMA TERMINADO")

        if heroeAct is not None:
            print(f"Héroe actual {heroeAct.nombre}\n")
        if villanoAct is not None:
            print(f"Villano actual {villanoAct.nombre}\n")


