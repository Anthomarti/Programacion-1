"""
Autor: Anthony Martinelli
PROBLEMA 378, 1001problemas.com, 13/06/24
"""

# Se crea la lista donde estan las tallas en stock
talla_disp = ["S", "M", "L"]

# Se pide al usuario que ingrese que talla busca
talla_soli = input("Ingrese su talla (XS, S, M, L, XL): ")

# Se revisa que la talla solicitada esté en la lista de tallas disponibles
if talla_soli in talla_disp: # Se utiliza in para poder verificar la existencia del elemento 
  print("La talla está disponible en stock.")
  
else:
  print("Lo siento, la talla no está disponible en stock.")