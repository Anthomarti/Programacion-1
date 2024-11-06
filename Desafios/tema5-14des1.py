"""
# Titulo: Desafío 1 Excepciones y errores
# Autor: Anthony Martinelli
# Fecha: 05/11/2024
# Descripción:
# Solicita al usuario dos números enteros e implementa un
# try-except que maneje la división por cero y los valores
# no numéricos. Muestra mensajes de error apropiados en cada caso.
"""

# Solicita dos números enteros al usuario
print("Ingrese dos números enteros:")

try:
    # Intenta convertir los valores ingresados a números enteros
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    # Verifica que el primer número no sea 0
    if num1 == 0:
        print("Error: El primer número no puede ser 0.")
    
    else:
        # Calcula el resultado de la división
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)

# Maneja la excepción de división por cero
except ZeroDivisionError:
    print("Error: La división por cero no es permitida.")

# Maneja la excepción de valores no numéricos
except ValueError:
    print("Error: Los valores ingresados no son numéricos.")

# Maneja cualquier otra excepción inesperada
except Exception as e:
    print("Error inesperado:", e)
    