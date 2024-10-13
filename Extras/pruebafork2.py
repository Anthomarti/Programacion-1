"""
Condicionales y Estructuras de Control:
Escribe un programa en Python que:
Solicite al usuario ingresar un número entero.
Determine si el número es positivo, negativo o cero.
Imprima un mensaje indicando si el número es positivo, negativo o cero.
Fuente: Pérez, D. & Viera, M.B. (2023). 1001 Problemas y Temas de Programación en C. Página 65, Problema 163.
"""

# Se solicita un numero al usuario 
numero = int(input("Ingrese un número entero:"))

# Si el numero es mayor a 0, es positivo
if numero > 0:
  print("Su número es positivo")

# Si el numero es menor a 0, es negativo
elif numero < 0:
  print("Su número es negativo")

# Sino, el numero es 0
else:
  print("Su número es cero")