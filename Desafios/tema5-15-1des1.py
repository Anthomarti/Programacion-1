"""
# Titulo: Desafío 1 Listas
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Desarrolla un programa que, dado un conjunto
# de tres números enteros introducidos por el
# usuario, determine cuál de ellos es el mayor.
# Considera la posibilidad de que algunos o todos
# los números sean iguales. El programa debe
# imprimir un mensaje claro con el número mayor
# o indicar si todos los números son iguales.
"""

# Definir una función para encontrar el número mayor
def encontrar_mayor():

    # Inicializar una lista vacía para almacenar los números
    numeros = []

    # Pedir al usuario que ingrese tres números enteros
    for i in range(3):

        # Utilizar un bucle while para asegurarse de que el usuario ingrese un número entero
        while True:
            try:
                # Pedir al usuario que ingrese un número
                numero = int(input(f"Ingresa el número {i+1}: "))
                # Agregar el número a la lista
                numeros.append(numero)
                # Salir del bucle while
                break

            except ValueError:
                # Imprimir un mensaje de error si el usuario no ingresa un número entero
                print("Error: Debe ingresar un número entero.")

    # Encontrar el mayor de los números utilizando la función max
    mayor = max(numeros)

    # Verificar si todos los números son iguales
    # Convertir la lista a un conjunto y verificar si su longitud es 1
    if len(set(numeros)) == 1:

        # Imprimir un mensaje indicando que todos los números son iguales
        print("Todos los números son iguales.")
    else:
        
        # Imprimir el número mayor
        print(f"El número mayor es: {mayor}")

# Llamar a la función para ejecutar el programa
encontrar_mayor()