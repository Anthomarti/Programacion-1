"""
# Titulo: Desafío 3 Encapsulamiento
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Implementa la clase Autor con métodos getter y setter utilizando decoradores @property
# para manejar los atributos privados nombre y nacionalidad.
"""

# Clase Libro: Representa un libro con título y año de publicación
class Libro:
    # Constructor: Inicializa un objeto Libro con título y año de publicación
    def __init__(self, titulo, año_publicacion):
        # Atributos privados para título y año de publicación
        self.__titulo = titulo
        self.__año_publicacion = año_publicacion

    # Método getter para obtener el título del libro
    @property
    def titulo(self):
        return self.__titulo

    # Método setter para establecer el título del libro
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    # Método getter para obtener el año de publicación del libro
    @property
    def año_publicacion(self):
        return self.__año_publicacion

    # Método setter para establecer el año de publicación del libro
    @año_publicacion.setter
    def año_publicacion(self, año_publicacion):
        self.__año_publicacion = año_publicacion


# Clase Autor: Representa un autor con nombre, nacionalidad y lista de libros
class Autor:
    # Constructor: Inicializa un objeto Autor con nombre, nacionalidad y lista vacía de libros
    def __init__(self, nombre, nacionalidad):
        # Atributos privados para nombre, nacionalidad y lista de libros
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista vacía para almacenar libros

    # Método getter para obtener el nombre del autor
    @property
    def nombre(self):
        return self.__nombre

    # Método setter para establecer el nombre del autor
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para obtener la nacionalidad del autor
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Método setter para establecer la nacionalidad del autor
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        self.__libros.append(libro)  # Agrega el libro a la lista

    # Método getter para obtener la lista de libros del autor
    @property
    def libros(self):
        return self.__libros


# Ejemplo de uso
autor = Autor("Gabriel García Márquez", "Colombiano")

libro1 = Libro("Cien años de soledad", 1967)
libro2 = Libro("El amor en los tiempos del cólera", 1985)

autor.agregar_libro(libro1)  # Agrega el libro1 a la lista de libros del autor
autor.agregar_libro(libro2)  # Agrega el libro2 a la lista de libros del autor

print("Libros escritos por", autor.nombre)
for libro in autor.libros:  # Itera sobre la lista de libros del autor
    print(libro.titulo, "(", libro.año_publicacion, ")")