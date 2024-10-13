"""
Bucles y Entrada/Salida de Datos:

Escribe un programa en Python que:
Solicite al usuario ingresar un número entero positivo n.
Imprima los primeros n números de la serie de Fibonacci.
Fuente: Pérez, D. & Viera, M.B. (2023). 1001 Problemas y Temas de Programación en C. Página 66, Problema 204.
"""

a, b = 0, 1

# Se solicita un numero entero positivo al usuario 
n = int(input("Ingrese un número entero positivo:"))

# Si el numero es menor a 0, no se puede calcular Fibonacci
if n < 0:
  print("Su número debe ser positivo, sino no se puede calcular la secuencia")

# En caso de que el numero sea positivo, se calcula la secuencia de Fibonacci hasta la posicion n
else:
  for _ in range(n):
    print(a)
    #a = b
    #b = a + b
    a, b = b, a + b
    # Muestro a y b
    #print (a, " ",b)