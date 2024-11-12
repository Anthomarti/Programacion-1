"""
# Titulo: Desafío 3 Excepciones y errores
# Autor: Anthony Martinelli
# Fecha: 05/11/2024
# Descripción:
# Escribe una función que calcule el factorial
# de un número entero positivo. Maneja las excepciones
# si el número ingresado es negativo, no es entero, o
# es demasiado grande para ser procesado.
"""

import math

def factorial(numero):
    try:

        # Verifica si el número es entero
        if not isinstance(numero, int):
            raise TypeError("El número debe ser un entero.")
        
        # Verifica si el número es negativo
        if numero < 0:
            raise ValueError("El número debe ser positivo.")
        
        # Verifica si el número es demasiado grande
        if numero > 100:
            raise OverflowError("El número es demasiado grande para ser procesado.")
        
        # Calcula el factorial
        resultado = math.factorial(numero)
        return resultado
    
    except TypeError as error:
        print(f"Error: {error}")
        return None
    except ValueError as error:
        print(f"Error: {error}")
        return None
    except OverflowError as error:
        print(f"Error: {error}")
        return None

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            break
        except ValueError:
            print("Error: El número debe ser un entero.")
    
    resultado = factorial(numero)
    if resultado is not None:
        print(f"El factorial de {numero} es: {resultado}")

if __name__ == "__main__":
    main()