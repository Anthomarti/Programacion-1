"""
# Titulo: Desafío 2 Polimorfismo
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor.
# Instancia un objeto de la clase Escritor y muestra cómo se puede acceder al método biografia de ambas clases.
"""

# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def biografia(self):
        return f"{self.nombre} es un autor"


# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

    def biografia(self):
        return f"{self.nombre} es un escritor de {self.genero}"


# Instanciamos un objeto de la clase Escritor
escritor = Escritor("Gabriel García Márquez", "Realismo Mágico")

# Accedemos al método biografia de la clase Escritor
print(escritor.biografia())

# Accedemos al método biografia de la clase Autor utilizando super()
print(Escritor.__bases__[0].biografia(escritor))

# Otra forma de acceder al método biografia de la clase Autor
print(Autor.biografia(escritor))