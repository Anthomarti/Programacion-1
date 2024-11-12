"""
# Titulo: Desafío 2 Manejo de archivos
# Autor: Anthony Martinelli
# Fecha: 07/11/2024
# Descripción:
# Dado un archivo libros.txt que contiene una lista
# de libros y sus autores, implementa una función que
# busque todos los libros escritos por un autor específico
# y los muestre. Si el autor no tiene libros en la
# lista, debe mostrar un mensaje indicando que no
# hay coincidencias.
"""

# Función para buscar libros por autor
def buscar_libros_por_autor(autor):

    # Inicializa una lista vacía para almacenar los libros encontrados
    libros_encontrados = []

    # Abre el archivo en modo lectura
    with open("libros.txt", "r") as archivo:

        # Lee el archivo línea por línea
        for linea in archivo:

            # Elimina el salto de línea al final de la línea
            linea = linea.strip()

            # Verifica si la línea no está vacía
            if linea:

                # Divide la línea en libro y autor
                libro, autor_libro = linea.split(" - ")

                # Verifica si el autor coincide con el autor buscado
                if autor_libro.lower() == autor.lower():

                    # Agrega el libro a la lista de libros encontrados
                    libros_encontrados.append(libro)

    # Verifica si se encontraron libros
    if libros_encontrados:
        
        # Muestra los libros encontrados
        print(f"Libros escritos por {autor}:")
        for libro in libros_encontrados:
            print(libro)
    else:

        # Muestra un mensaje indicando que no hay coincidencias
        print(f"No se encontraron libros escritos por {autor}.")

# Función principal del programa
def main():

    # Se determina el nombre del autor
    autor = "Gabriel Garcia Marquez"

    # Llama a la función para buscar libros por autor
    buscar_libros_por_autor(autor)

# Verifica si el archivo se está ejecutando directamente (no como módulo)
if __name__ == "__main__":

    # Llama a la función principal del programa
    main()