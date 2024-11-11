"""
# Titulo: Desafío 3
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Considera cómo podrías implementar una biblioteca que
# almacene múltiples autores y libros.
# ¿Qué estructuras de datos usarías?
"""

# Clase Autor
class Autor:
    def __init__(self, nombre, nacionalidad):
 
        # Inicializa un objeto Autor con nombre y nacionalidad.
        
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista para almacenar los libros del autor

    def agregar_libro(self, libro):

        # Agrega un libro a la lista de libros del autor.

        self.libros.append(libro)

    def mostrar_libros(self):
       
        # Muestra los libros del autor.
        
        print(f"\nLibros de {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

    def eliminar_libro(self, titulo_libro):
        
        # Elimina un libro de la lista de libros del autor.
        
        self.libros = [libro for libro in self.libros if libro.titulo != titulo_libro]

# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        
        # Inicializa un objeto Libro con título, género, ISBN y autor.

        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

    def mostrar_detalle(self):
        
        # Muestra los detalles del libro.
        
        print(f"\nTítulo: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor.nombre}")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        
        # Inicializa una biblioteca vacía.
        
        self.autores = {}  # Diccionario para almacenar los autores
        self.libros = {}  # Diccionario para almacenar los libros

    def agregar_autor(self, autor):
        
        # Agrega un autor a la biblioteca.
        
        self.autores[autor.nombre] = autor

    def agregar_libro(self, libro):
        
        # Agrega un libro a la biblioteca y lo asocia con su autor.
        
        self.libros[libro.titulo] = libro
        libro.autor.agregar_libro(libro)

    def mostrar_autores(self):
        
        # Muestra los autores de la biblioteca.
        
        print("\nAutores:")
        for autor in self.autores.values():
            print(f"- {autor.nombre}")

    def mostrar_libros(self):
        
        # Muestra los libros de la biblioteca.
        
        print("\nLibros:")
        for libro in self.libros.values():
            print(f"- {libro.titulo}")

    def buscar_libros_por_autor(self, nombre_autor):
        
        # Busca los libros de un autor en la biblioteca.
        
        if nombre_autor in self.autores:
            return self.autores[nombre_autor].libros
        return []

    def buscar_autores_por_libro(self, titulo_libro):
        
        # Busca el autor de un libro en la biblioteca.
        
        if titulo_libro in self.libros:
            return self.libros[titulo_libro].autor
        return None

# Crear biblioteca
biblioteca = Biblioteca()

# Crear autores y libros
autor1 = Autor("Juan Pérez", "Mexicano")
autor2 = Autor("María García", "Española")

libro1 = Libro("La vida es un sueño", "Ficción", "1234567890", autor1)
libro2 = Libro("La casa de los espíritus", "Ficción", "9876543210", autor1)
libro3 = Libro("El amor en los tiempos del cólera", "Ficción", "1111111111", autor2)

# Agregar autores y libros a la biblioteca
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Mostrar autores y libros
biblioteca.mostrar_autores()
biblioteca.mostrar_libros()

# Buscar libros por autor
libros_autor1 = biblioteca.buscar_libros_por_autor("Juan Pérez")
for libro in libros_autor1:
    libro.mostrar_detalle()

# Buscar autores por libro
autor_libro1 = biblioteca.buscar_autores_por_libro("La vida es un sueño")
if autor_libro1:
    autor_libro1.mostrar_libros()

# Eliminar un libro de la biblioteca y del diccionario libros de la misma
biblioteca.libros.pop("La casa de los espíritus")
autor1.eliminar_libro("La casa de los espíritus")

# Mostrar autores y libros después de eliminar un libro
print("\nLibros de la biblioteca luego de borrar un libro:")
biblioteca.mostrar_autores()
biblioteca.mostrar_libros()