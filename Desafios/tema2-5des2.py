"""
Autor: Anthony Martinelli

Letra: Escriba un programa que pida al usuario que ingrese dos números y luego imprima
la suma, la resta, la multiplicación y la división de esos números.
"""

# Se solicitan ambos números de parte del usuario
numero = input ("Ingrese el primer número: ")
numero = float (numero)

numero2 = input ("Ingrese el segundo número: ")
numero2 = float (numero2)

# Suma
resultado = numero + numero2
print("El resultado de la suma de ", numero, " y ", numero2, " es: ", resultado)

# Resta
resultado = numero - numero2
print("El resultado de la resta de ", numero, " y ", numero2, " es: ", resultado)

# Multiplicación
resultado = numero * numero2
print("El resultado de la multiplicación de ", numero, " y ", numero2, " es: ", resultado)

# División
resultado = numero / numero2
print("El resultado de la división de ", numero, " y ", numero2, " es: ", resultado)