"""
# Titulo: Desafío 2
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Modifica la clase Autor para que pueda tener una
# lista de libros escritos por el autor. Proporciona
# un método para agregar libros a esta lista.
"""

# Clase Libro: Representa un libro con título y año de publicación
class Libro:
    # Constructor: Inicializa un objeto Libro con título y año de publicación
    def __init__(self, titulo, año_publicacion):
        # Atributos privados para título y año de publicación
        self.__titulo = titulo
        self.__año_publicacion = año_publicacion

    # Método getter para obtener el título del libro
    def get_titulo(self):
        return self.__titulo

    # Método setter para establecer el título del libro
    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Método getter para obtener el año de publicación del libro
    def get_año_publicacion(self):
        return self.__año_publicacion

    # Método setter para establecer el año de publicación del libro
    def set_año_publicacion(self, año_publicacion):
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
    def get_nombre(self):
        return self.__nombre

    # Método setter para establecer el nombre del autor
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para obtener la nacionalidad del autor
    def get_nacionalidad(self):
        return self.__nacionalidad

    # Método setter para establecer la nacionalidad del autor
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        self.__libros.append(libro)  # Agrega el libro a la lista

    # Método getter para obtener la lista de libros del autor
    def get_libros(self):
        return self.__libros


# Ejemplo de uso
autor = Autor("Gabriel García Márquez", "Colombiano")

libro1 = Libro("Cien años de soledad", 1967)
libro2 = Libro("El amor en los tiempos del cólera", 1985)

autor.agregar_libro(libro1)  # Agrega el libro1 a la lista de libros del autor
autor.agregar_libro(libro2)  # Agrega el libro2 a la lista de libros del autor

print("Libros escritos por", autor.get_nombre())
for libro in autor.get_libros():  # Itera sobre la lista de libros del autor
    print(libro.get_titulo(), "(", libro.get_año_publicacion(), ")")