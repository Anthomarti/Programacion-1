"""
Autor: Anthony Martinelli
PROBLEMA 183: Escribir un programa que determine si un número es múltiplo de 6.
"""

numero = 5

# Se divide el numero entre 6 y se verifica si el resto es 0
if numero % 6 == 0:
  print("El número es múltiplo de 6")

# En caso que no sea resto 0
else:
  print("El número no es múltiplo de 6")