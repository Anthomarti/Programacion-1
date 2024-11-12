"""
# Titulo: Desafío 3 Manejo de archivos
# Autor: Anthony Martinelli
# Fecha: 07/11/2024
# Descripción:
# Tienes un archivo inventario.csv que contiene una
# lista de libros y el número de copias disponibles.
# Escribe un programa que permita actualizar la cantidad
# de copias de un libro específico. El programa debe
# leer el archivo, modificar el número de copias y
# volver a escribir el archivo.
"""

import csv

# Función para actualizar la cantidad de copias de un libro
def actualizar_cantidad_de_copias(titulo_libro, cantidad_de_copias):

    # Inicializa una lista vacía para almacenar los libros
    libros = []

    # Abre el archivo en modo lectura
    with open("inventario.csv", "r") as archivo:

        # Lee el archivo línea por línea
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:

            # Verifica si el título del libro coincide con el título buscado
            if fila[0].lower() == titulo_libro.lower():

                # Actualiza la cantidad de copias
                fila[1] = str(cantidad_de_copias)

            # Agrega el libro a la lista de libros
            libros.append(fila)

    # Abre el archivo en modo escritura
    with open("inventario.csv", "w", newline="") as archivo:

        # Escribe los libros en el archivo
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(libros)

    # Muestra un mensaje de confirmación
    print(f"La cantidad de copias de '{titulo_libro}' ha sido actualizada a {cantidad_de_copias}.")

# Función principal del programa
def main():

    # Solicita al usuario el título del libro
    titulo_libro = input("Ingrese el título del libro: ")

    # Solicita al usuario la cantidad de copias
    while True:
        try:
            cantidad_de_copias = int(input("Ingrese la cantidad de copias: "))
            if cantidad_de_copias < 0:
                print("La cantidad de copias no puede ser negativa.")
            else:
                break
        except ValueError:
            print("La cantidad de copias debe ser un número entero.")

    # Llama a la función para actualizar la cantidad de copias
    actualizar_cantidad_de_copias(titulo_libro, cantidad_de_copias)

# Verifica si el archivo se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    
    # Llama a la función principal del programa
    main()