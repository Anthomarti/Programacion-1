"""
# Titulo: Desafío 3 Polimorfismo
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# En este desafío, vamos a extender la clase Libro para crear una subclase LibroEspecializado.
# Un LibroEspecializado, además de tener un título y un autor, también tiene un campo de estudio y un nivel de especialización (básico, intermedio, avanzado).
"""

# Definimos la clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


# Creamos una subclase LibroEspecializado que hereda de Libro
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    def informacion(self):
        return f"{super().informacion()}, Campo de estudio: {self.campo_estudio}, Nivel de especialización: {self.nivel_especializacion}"


# Instanciamos un objeto de la clase LibroEspecializado
libro_especializado = LibroEspecializado("Introducción a la Inteligencia Artificial", "Andrew Ng", "Inteligencia Artificial", "Avanzado")

# Llamamos al método informacion del objeto libro_especializado
print(libro_especializado.informacion())