"""
# Titulo: Desafío 3 Herencia
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Diseña una clase LibroDigital que herede de Libro y añada atributos como formato (e.g., PDF, EPUB) y tamaño_archivo.
# Además, implementa una subclase EBook que sobrescriba un método para mostrar información específica, como enlaces de descarga.
"""

# Definimos la clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")


# Creamos una subclase LibroDigital que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamaño_archivo):
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Formato: {self.formato}")
        print(f"Tamaño archivo: {self.tamaño_archivo} MB")


# Creamos una subclase EBook que hereda de LibroDigital
class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Enlace de descarga: {self.enlace_descarga}")


# Instanciamos un objeto de la clase Libro
libro = Libro("El señor de los anillos", "J.R.R. Tolkien")
libro.mostrar_informacion()

# Instanciamos un objeto de la clase LibroDigital
libro_digital = LibroDigital("El señor de los anillos", "J.R.R. Tolkien", "PDF", 10)
libro_digital.mostrar_informacion()

# Instanciamos un objeto de la clase EBook
ebook = EBook("El señor de los anillos", "J.R.R. Tolkien", "EPUB", 5, "https://ejemplo.com/ebook")
ebook.mostrar_informacion()