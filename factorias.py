from models import models
import random
from faker import Faker
from utils.nombres_personalizados import FakerPersonalizado

from faker.providers import BaseProvider
faker = Faker()
faker.add_provider(FakerPersonalizado)
def crearVillano():
    villanoNuevo= models.Villano(random.randint(0000000,9999999),
                                 faker.nombre_personalizado(), faker.apellido(),
                                 faker.date_of_birth())
    villanoNuevo.setAtrVill(random.randint(1,100), random.randint(1,100),
                            random.randint(1,100), random.randint(1,100))
    villanoNuevo.calcularMediaVill()
    return villanoNuevo

def crearHeroe():
    heroeNuevo = models.Heroe(random.randint(0000000,9999999),
                                 faker.nombre_personalizado(), faker.apellido(),
                                 faker.date_of_birth())
    heroeNuevo.setAtrHeroe(random.randint(1,100), random.randint(1,100),
                            random.randint(1,100), random.randint(1,100), random.randint(1,100))
    heroeNuevo.calcularMediaHer()
    return heroeNuevo

def crearPersonas(numPersonas):
    array = []
    contador = 0
    while contador < numPersonas:
        array.append(crearHeroe())
        array.append(crearVillano())
        contador += 1
    return array



def mostrarTodasPersonas(array):
    for p in array:
        print(p.__dict__)