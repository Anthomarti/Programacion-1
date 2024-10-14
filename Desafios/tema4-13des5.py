"""
# Titulo: Desafío 5 Encapsulamiento
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Desarrolla una función que reciba una lista de objetos Autor y devuelva el autor que ha escrito el mayor número de libros.
# Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.
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
    def get_libros(self):
        return self.__libros


# Función que devuelve el autor que ha escrito el mayor número de libros
def get_autor_con_mas_libros(autores):
    autor_con_mas_libros = None
    max_libros = 0
    for autor in autores:
        num_libros = len(autor.get_libros())
        if num_libros > max_libros:
            max_libros = num_libros
            autor_con_mas_libros = autor
    return autor_con_mas_libros


# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor2 = Autor("Isabel Allende", "Chilena")
autor3 = Autor("Mario Vargas Llosa", "Peruano")

libro1 = Libro("Cien años de soledad", 1967)
libro2 = Libro("El amor en los tiempos del cólera", 1985)
libro3 = Libro("La casa de los espíritus", 1982)
libro4 = Libro("La ciudad y los perros", 1963)
libro5 = Libro("La guerra del fin del mundo", 1981)
libro6 = Libro("La fiesta del chivo", 2000)

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor2.agregar_libro(libro3)
autor3.agregar_libro(libro4)
autor3.agregar_libro(libro5)
autor3.agregar_libro(libro6)

autores = [autor1, autor2, autor3]

autor_con_mas_libros = get_autor_con_mas_libros(autores)

print("El autor que ha escrito el mayor número de libros es:", autor_con_mas_libros.nombre)