"""
# Titulo: Desafío 4 Herencia
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Implementa una clase EscritorAcademico que herede de Escritor y Academico,
# e incluya un método adicional para publicar artículos académicos.
# Asegúrate de utilizar correctamente la función super() para inicializar las clases base.
"""

# Definimos la clase base Escritor
class Escritor:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def escribir_libro(self):
        print(f"\n{self.nombre} está escribiendo un libro de {self.genero}")


# Definimos la clase base Academico
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

    def enseñar_clase(self):
        print(f"\nDa clase en la {self.universidad}")


# Creamos una clase EscritorAcademico que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad)

    def publicar_articulo(self):
        print(f"\n{self.nombre} ha publicado un artículo académico en la {self.universidad}")


# Instanciamos un objeto de la clase EscritorAcademico
escritor_academico = EscritorAcademico("Juan Carlos Onetti", "Realismo Mágico", "Universidad de la República")
escritor_academico.escribir_libro()
escritor_academico.enseñar_clase()
escritor_academico.publicar_articulo()