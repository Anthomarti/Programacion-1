def cuenta_vocales(cadena):

  # Tu código aquí
  cadena = cadena.lower()
  vocales = "aeiou"
  diccionario= {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

  for letra in vocales: 
    diccionario[letra] = cadena.count(letra)

  return diccionario

def total_vocales(diccionario):
  total = 0
  for valor in diccionario.values():
    total += valor
  return total

cadena = input("ingrese la palabra que desee: ")

print(cuenta_vocales(cadena))
print("Esta palabra tiene un total de:", total_vocales(cuenta_vocales(cadena)), "vocales")

#print(cuenta_vocales("hipototamo"))
# Salida: {'a': 3, 'e': 1, 'i': 0, 'o': 2, 'u': 1}