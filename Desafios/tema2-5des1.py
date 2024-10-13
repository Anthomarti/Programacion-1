"""
Tema 2_5 Desafio 1
Autor: Anthony Martinelli
Letra: Escriba un programa que pida al usuario su nombre y su ciudad de origen,
luego imprima un saludo personalizado con esa información.
"""

# Se crea la variable nombre y se le asigna el valor que el usuario ingrese
nombre = input("Ingrese su nombre: ")

# Se crea la variable ciudad y se le asigna el valor que el usuario ingrese
ciudad = input("Ingrese su ciudad de origen: ")

# Se muestra un saludo personalizado con los datos anteriores
print("Hola", nombre,"de la ciudad", ciudad,", este es tu saludo personalizado de bienvenida!")
# Se utiliza el operador "," para concatenar los valores, por su adaptabilidad