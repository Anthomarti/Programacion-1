"""
Desafio 3.
Autor: Anthony Martinelli
"""

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print("La temperatura celsius: ", celsius, ", es equivalente a: ", fahrenheit, "grados Fahrenheit y ", kelvin, " grados Kelvin")