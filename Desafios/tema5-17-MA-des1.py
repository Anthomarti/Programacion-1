"""
# Titulo: Desafío 1 Manejo de archivos
# Autor: Anthony Martinelli
# Fecha: 07/11/2024
# Descripción:
# Desarrolla un programa que cree un archivo
# prestamos.txt y permita al usuario agregar
# el registro de un préstamo. El registro debe
# incluir el nombre del libro, el nombre del
# prestatario y la fecha del préstamo.
# Asegúrate de no sobrescribir el archivo cada
# vez que se agrega un nuevo préstamo.
"""

# Función para agregar un préstamo al archivo
def agregar_prestamo():

    # Solicita al usuario el nombre del libro
    nombre_libro = input("Ingrese el nombre del libro: ")
    
    # Solicita al usuario el nombre del prestatario
    nombre_prestatario = input("Ingrese el nombre del prestatario: ")
    
    # Solicita al usuario la fecha del préstamo
    fecha_prestamo = input("Ingrese la fecha del préstamo (dd/mm/aaaa): ")

    # Abre el archivo en modo "a" (append) para agregar contenido sin sobrescribir
    with open("prestamos.txt", "a") as archivo:
        # Escribe el nombre del libro en el archivo
        archivo.write(f"Nombre del libro: {nombre_libro}\n")
        
        # Escribe el nombre del prestatario en el archivo
        archivo.write(f"Nombre del prestatario: {nombre_prestatario}\n")
        
        # Escribe la fecha del préstamo en el archivo
        archivo.write(f"Fecha del prestamo: {fecha_prestamo}\n")
        
        # Agrega una línea en blanco para separar los registros
        archivo.write("\n")

# Función principal del programa
def main():
    # Ciclo infinito para mantener el programa en ejecución
    while True:
        # Muestra el menú al usuario
        print("\n1. Agregar préstamo")
        print("2. Salir")
        
        # Solicita al usuario una opción
        opcion = input("Ingrese una opción: ")

        # Verifica la opción seleccionada por el usuario
        if opcion == "1":
            # Llama a la función para agregar un préstamo
            agregar_prestamo()
            
            # Muestra un mensaje de confirmación
            print("Préstamo agregado con éxito.")
        elif opcion == "2":
            # Sale del ciclo infinito y termina el programa
            break
        else:
            # Muestra un mensaje de error si la opción es inválida
            print("Opción inválida. Por favor, ingrese una opción válida.")

# Verifica si el archivo se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    # Llama a la función principal del programa
    main()