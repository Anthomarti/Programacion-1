"""
Autor: Anthony Martinelli
Desafío 6, Tema 3_8_funciones, 13/08/2024
"""

def es_primo(numero):
  if numero <= 1:
      return False
  for i in range(2, numero):
      if numero % i == 0:
          return False
  return True
    
def contar_primos(lista):
  contador = 0
  for numero in lista:
      if es_primo(numero):
          contador += 1        
  return contador

def main():
    lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 19, 23]

    for numero in lista:
        if es_primo(numero):
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")
    
    cantidad_primos = contar_primos(lista)
    print(f"\nCantidad total de números primos en la lista: {cantidad_primos}")

if __name__ == "__main__":
    main()