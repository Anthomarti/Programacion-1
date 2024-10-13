"""
# Titulo: Desafío 1
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Crea una clase Libro que tenga atributos privados
# para el título, autor y ISBN. Proporciona métodos
# getter y setter para cada atributo.
"""

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Métodos getter
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # Métodos setter
    def set_titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            raise TypeError("El título debe ser una cadena de texto")

    def set_autor(self, autor):
        if isinstance(autor, str):
            self.__autor = autor
        else:
            raise TypeError("El autor debe ser una cadena de texto")

    def set_isbn(self, isbn):
        if isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit():
            self.__isbn = isbn
        else:
            raise ValueError("El ISBN debe ser una cadena de texto de 13 dígitos")

# Ejemplo de uso
libro = Libro("El señor de los anillos", "J.R.R. Tolkien", "9780261102385")
print(libro.get_titulo())  # Imprime: El señor de los anillos
print(libro.get_autor())   # Imprime: J.R.R. Tolkien
print(libro.get_isbn())    # Imprime: 9780261102385

libro.set_titulo("\nEl hobbit")
libro.set_autor("J.R.R. Tolkien")
libro.set_isbn("9780261102194")
print(libro.get_titulo())  # Imprime: El hobbit
print(libro.get_autor())   # Imprime: J.R.R. Tolkien
print(libro.get_isbn())    # Imprime: 9780261102194