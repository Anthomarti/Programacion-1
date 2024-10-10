"""
Grupo: Programación 1
Colaboradores: @lucasaguiar181 @anthonymarti200 @bau21062014
Fecha: 04-04-2024
"""

# Define la variable num_secreto como un numero aleatorio entre 1 y 10
import random
num_secreto = random.randint(1, 10)

num_jugador = 0


#quiero que la comparacion sea hasta que las variables sean iguales
while num_jugador != num_secreto:

  #solicitar al usuario un numero y guardarlo en la variable num_jugador
  num_jugador = int(input("Ingresa un numero del 1 al 10: "))

  #si el numero es mayor que el secreto 
  if num_jugador > num_secreto:
      print("El número es menor")

  #si el numero es menor que el secreto
  if num_jugador < num_secreto:
      print("El número es mayor")

  if num_jugador != num_secreto:
      print("Vuelve a intentarlo")

print("¡Felicidades has ganado!")