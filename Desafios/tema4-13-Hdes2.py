"""
# Titulo: Desafío 2 Herencia
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Crea una clase Bibliotecario que herede de Usuario y tenga atributos específicos como sección y años_experiencia.
"""

# Definimos la clase base Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una subclase Bibliotecario que hereda de Usuario
class Bibliotecario(Usuario):
    def __init__(self, nombre, seccion, años_experiencia):
        super().__init__(nombre)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

# Instanciamos un objeto de la clase Bibliotecario
bibliotecario = Bibliotecario("Juan Pérez", "Sección de Literatura", 10)
print(bibliotecario.nombre, bibliotecario.seccion, bibliotecario.años_experiencia)