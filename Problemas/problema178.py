"""
Autor: Anthony Martinelli
PROBLEMA 178: Escribir un programa que determine si un número es capicúa.
"""

numero = 101

# Se revisa que el numero se lea tanto al derecho como al reves, se convierte a string para compararlo a su reves
if str(numero) == str(numero)[::-1]:
    print("El numero es capicua")

else:
    print("El numero no es capicua")