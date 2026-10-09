import random

from faker import Faker
from faker.providers import BaseProvider


class FakerPersonalizado(BaseProvider):
    def nombre_personalizado(self):
        nombres_propios = ['Jeffrey', 'Diddy', 'Adolf', 'Benito', 'Francisco', 'Iosef', 'Nicolas']
        return self.random_element(nombres_propios)

    def apellido(self):
        apellido_propio = ['Mendoza', 'Villarreal', 'Castañeda', 'Garrido', 'Santana', 'Palacios', 'Miranda', 'Olivares']
        return self.random_element(apellido_propio)