"""
# Titulo: Desafío 1 Herencia
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Implementa una clase Poeta que herede de Autor y
# tenga un atributo para el tipo de poesía que escribe.
"""

# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

# Definimos una segunda clase base
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

# Creamos una clase que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad)

# Creamos una subclase Poeta que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, tipo_poesia):
        super().__init__(nombre)
        self.tipo_poesia = tipo_poesia

# Instanciamos un objeto de la clase Escritor
escritor = Escritor("Mario Benedetti", "Realismo Social")
print(escritor.nombre, escritor.genero)

# Instanciamos un objeto de la clase EscritorAcademico
escritor_academico = EscritorAcademico("Juan Carlos Onetti", "Realismo Mágico", "Universidad de la República")
print(escritor_academico.nombre, escritor_academico.genero, escritor_academico.universidad)

# Instanciamos un objeto de la clase Poeta
poeta = Poeta("Pablo Neruda", "Poesía lírica")
print(poeta.nombre, poeta.tipo_poesia)