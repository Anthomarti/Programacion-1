"""
# Titulo: Desafío 5 Manejo de archivos
# Autor: Anthony Martinelli
# Fecha: 07/11/2024
# Descripción:
# Desarrolla una función que lea un archivo de texto
# grande, como libros.txt, y cuente cuántas veces
# aparece cada palabra. Luego, muestra las 5 palabras
# más comunes y cuántas veces aparecen.
"""

# Importa la biblioteca collections para utilizar la clase Counter
import collections

# Función para leer el archivo y contar las palabras
def contar_palabras():
    try:

        # Abre el archivo en modo lectura
        with open("libros.txt", "r") as archivo:

            # Lee el contenido del archivo
            texto = archivo.read()

            # Convierte el texto a minúsculas y elimina los signos de puntuación
            texto = texto.lower().replace(",", "").replace(".", "").replace("-", "").replace(":", "")

            # Divide el texto en palabras
            palabras = texto.split()

            # Cuenta las palabras utilizando la clase Counter
            contador = collections.Counter(palabras)

            # Muestra las 5 palabras más comunes
            print("Las 5 palabras más comunes son:")
            for palabra, frecuencia in contador.most_common(5):
                print(f"{palabra}: {frecuencia}")

    except FileNotFoundError:

        # Si el archivo no existe, muestra un mensaje de error
        print("El archivo libros.txt no existe.")

# Función principal del programa
def main():
    
    # Llama a la función para contar las palabras
    contar_palabras()

# Verifica si el archivo se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    
    # Llama a la función principal del programa
    main()