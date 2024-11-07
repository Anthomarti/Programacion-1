"""
# Titulo: Desafío 4 Manejo de archivos
# Autor: Anthony Martinelli
# Fecha: 07/11/2024
# Descripción:
# Escribe un programa que permita eliminar el registro de
# un préstamo de un archivo prestamos.txt. El programa debe
# mostrar los registros actuales, permitir al usuario seleccionar
# cuál eliminar, y luego actualizar el archivo sin el registro
# eliminado.
"""

# Función para leer los registros del archivo
def leer_registros():

    # Abre el archivo en modo lectura y lee su contenido
    try:
        with open("prestamos.txt", "r") as archivo:

            # Divide el contenido en registros separados por líneas en blanco
            registros = archivo.read().split("\n\n")
            # Elimina los espacios vacíos
            registros = [registro for registro in registros if registro.strip()]
            return registros
    except FileNotFoundError:

        # Si el archivo no existe, muestra un mensaje de error y devuelve una lista vacía
        print("El archivo prestamos.txt no existe.")
        return []

# Función para mostrar los registros
def mostrar_registros(registros):

    # Muestra los registros en la consola, numerándolos para que el usuario pueda seleccionar uno
    for i, registro in enumerate(registros):
        if registro:
            print(f"\nRegistro {i+1}:")
            print(registro)

# Función para eliminar un registro
def eliminar_registro(registros):

    # Muestra los registros para que el usuario pueda seleccionar uno
    mostrar_registros(registros)
    while True:
        try:

            # Pide al usuario que ingrese el número del registro que desea eliminar
            numero_registro = int(input("Ingrese el número del registro que desea eliminar: "))

            # Verifica si el número de registro es válido
            if 1 <= numero_registro <= len(registros):

                # Elimina el registro de la lista
                registros.pop(numero_registro - 1)

                # Muestra un mensaje de confirmación
                print("Registro eliminado con éxito.")
                break
            else:

                # Si el número de registro no es válido, muestra un mensaje de error
                print("Número de registro inválido. Por favor, ingrese un número válido.")
        except ValueError:

            # Si el usuario ingresa algo que no es un número entero, muestra un mensaje de error
            print("Ingrese un número entero.")

# Función para actualizar el archivo
def actualizar_archivo(registros):

    # Abre el archivo en modo escritura y escribe los registros
    with open("prestamos.txt", "w") as archivo:

        # Escribe cada registro en el archivo, seguido de una línea en blanco
        for i, registro in enumerate(registros):
            archivo.write(registro)
            if i < len(registros) - 1:
                archivo.write("\n\n")

# Función principal del programa
def main():

    # Ciclo infinito para mantener el programa en ejecución
    while True:

        # Muestra el menú al usuario
        print("\n1. Mostrar registros")
        print("2. Eliminar registro")
        print("3. Salir")
        
        # Pide al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        # Verifica la opción seleccionada por el usuario
        if opcion == "1":

            # Lee los registros del archivo y los muestra
            registros = leer_registros()
            mostrar_registros(registros)
        elif opcion == "2":

            # Lee los registros del archivo, elimina uno y actualiza el archivo
            registros = leer_registros()
            eliminar_registro(registros)
            actualizar_archivo(registros)
        elif opcion == "3":

            # Sale del ciclo infinito y termina el programa
            break
        else:

            # Si la opción no es válida, muestra un mensaje de error
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Verifica si el archivo se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    
    # Llama a la función principal del programa
    main()