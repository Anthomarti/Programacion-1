"""
Grupo: Programación 1
Autor: @anthonymarti200
Colaboradores: @lucasaguiar181 @bau21062014
Fecha: 04-04-2024
"""

# Define la variable num_secreto como un numero aleatorio entre 1 y 100
import random
num_secreto = random.randint(1, 100)

num_jugador = 0

num_intentos = 1 

print("Sean todos y todas bienvenidos al juego de adivinar el numero")

#quiero que la comparacion sea hasta que las variables sean iguales
while num_jugador != num_secreto:

  print("Intento N°", num_intentos)
  
  #solicitar al usuario un numero y guardarlo en la variable num_jugador
  num_jugador = int(input("Ingresa un numero del 1 al 100: "))
  
  #si el numero es mayor que el secreto 
  if num_jugador > num_secreto:
      print("El número es menor")

  #si el numero es menor que el secreto
  if num_jugador < num_secreto:
      print("El número es mayor")

  if num_jugador != num_secreto:
      print("Vuelve a intentarlo")
      num_intentos = num_intentos + 1

print("¡Felicidades has ganado!")
