"""
# Titulo: Desafío 5 Listas
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Usa una "list comprehension" para crear una
# lista llamada potencias que contenga las
# potencias de 2 de los números del 0 al 9 (es
# decir, 2 elevado a la potencia de cada número).
# Imprime la lista resultante.
"""

# Crea una lista llamada potencias que contenga las potencias de 2 de los números del 0 al 9
potencias = [2 ** i for i in range(10)]

# Imprime la lista resultante
print("Potencias de 2:")
print(potencias)