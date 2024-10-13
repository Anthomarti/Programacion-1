"""
Autor: Anthony Martinelli
PROBLEMA 191, 1001problemas.com, 11/07/24
"""

# Se solicita un numero al usuario

numero = int (input("Introduce un numero: "))

# Se define el rango de la tabla de multiplicar

rango = 10

# Se genera y muestra la tabla de multiplicar

print ("Tabla de multiplicar del numero", numero, ": ")

for i in range (1,rango + 1):
  
  print(numero, "x", i, "=", numero * i)