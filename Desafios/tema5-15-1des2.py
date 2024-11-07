"""
# Titulo: Desafío 2 Listas
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Un sistema de inventario tiene una lista con
# los códigos de productos. Desarrolla un programa
# que permita al usuario introducir un código de
# producto y que determine si ese código está en la
# lista. Si el código se encuentra, el programa debe
# devolver la posición en la que aparece; si no está,
# debe mostrar un mensaje indicando que no se ha
# encontrado el código.
"""

# Lista de códigos de productos
codigos_productos = ["P001", "P002", "P003", "P004", "P005"]

# Función para buscar un código de producto en la lista
def buscar_codigo(codigo):

    # Intenta encontrar el código en la lista
    try:

        # Utiliza el método index para obtener la posición del código
        posicion = codigos_productos.index(codigo)

        # Devuelve la posición del código
        return posicion
    
    # Si el código no se encuentra, se produce una excepción ValueError
    except ValueError:

        # Devuelve -1 para indicar que el código no se ha encontrado
        return -1

# Función principal del programa
def main():

    # Muestra un mensaje de bienvenida
    print("Sistema de inventario")
    print("---------------------")
    
    # Bucle para repetir el programa hasta que el usuario decida salir
    while True:

        # Pide al usuario que ingrese un código de producto
        codigo = input("Ingrese el código de producto a buscar (o 'salir' para terminar): ")
        
        # Verifica si el usuario quiere salir
        if codigo.lower() == "salir":
            # Sale del bucle y termina el programa
            break
        
        # Busca el código en la lista
        posicion = buscar_codigo(codigo)
        
        # Verifica si el código se ha encontrado
        if posicion != -1:

            # Muestra la posición del código
            print(f"El código '{codigo}' se encuentra en la posición {posicion + 1}.")
        else:

            # Muestra un mensaje indicando que el código no se ha encontrado
            print(f"No se ha encontrado el código '{codigo}'.")

# Verifica si el programa se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    
    # Llama a la función principal
    main()