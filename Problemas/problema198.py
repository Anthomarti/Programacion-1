"""
Autor: Anthony Martinelli
PROBLEMA 198, 1001problemas.com, 11/07/24
"""

# Se solicita al usuario ingresar un número entero
numero = int(input("Ingrese un numero entero: "))

# Se verifica si el numero es primo

# Primero se ve si el numero es negativo o uno
if numero <= 1:
  print ("El numero no es primo")

else:

  # Se verifica si el numero es divisible por algun numero entre 2 y la raiz cuadrada del numero
  
  for i in range(2, int(numero ** 0.5) + 1):

    # Si la resta de las divisiones es 0, el numero no es primo
    
    if numero % i == 0:
      print ("El numero no es primo")
      break
      
    # Si no es divisible por estos numeros, el numero es primo
  
  else:
    print ("El numero es primo")