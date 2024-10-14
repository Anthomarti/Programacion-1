"""
# Titulo: Desafío 4 Polimorfismo
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# En este desafío, se te pide que implementes el polimorfismo con métodos de clase en figuras geométricas.
# Deberás crear una clase base Figura con un método area y dos subclases Circulo y Cuadrado que sobrescriban este método para calcular el área de cada figura.
"""

import math

# Definimos la clase base Figura
class Figura:
    def __init__(self):
        pass

    def area(self):
        return "La figura no tiene área definida"


# Creamos una subclase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Creamos una subclase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Instanciamos objetos de las clases Circulo y Cuadrado
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# Llamamos al método area de cada objeto
print(f"Área del círculo: {circulo.area():.2f}")
print(f"Área del cuadrado: {cuadrado.area():.2f} \n")

# Creamos una lista de figuras
figuras = [circulo, cuadrado]

# Llamamos al método area de cada figura en la lista
for figura in figuras:
    print(f"Área de la figura: {figura.area():.2f}")