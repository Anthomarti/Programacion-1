"""
# Titulo: Desafío 3 Algoritmos fundamentales
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Tienes una lista ordenada alfabéticamente con los nombres
# de los estudiantes de una clase. Implementa una función que
# realice una búsqueda binaria para encontrar un estudiante
# específico en la lista. Si el estudiante no está, la función
# debe mostrar un mensaje adecuado.
"""

# Definimos la función busqueda_binaria que toma como argumentos la lista de estudiantes y el nombre del estudiante que se busca
def busqueda_binaria(lista, objetivo):
 
 # Inicializamos las variables bajo y alto para definir el rango de búsqueda
 bajo = 0
 alto = len(lista) - 1

 # Realizamos la búsqueda binaria mientras el rango de búsqueda sea válido
 while bajo <= alto:
  
  # Calculamos el índice del elemento del medio de la lista
  medio = (bajo + alto) // 2
  
  # Comparamos el elemento del medio con el objetivo
  if lista[medio] == objetivo:
   
   # Si el elemento del medio es igual al objetivo, devolvemos un mensaje que indica que el estudiante se encontró
   return f"El estudiante {objetivo} se encontró en la lista."
  elif lista[medio] < objetivo:
   
   # Si el elemento del medio es menor que el objetivo, ajustamos el límite inferior de la búsqueda
   bajo = medio + 1
  else:
   
   # Si el elemento del medio es mayor que el objetivo, ajustamos el límite superior de la búsqueda
   alto = medio - 1

 # Si la búsqueda no encuentra el estudiante, devolvemos un mensaje que indica que el estudiante no se encontró
 return f"El estudiante {objetivo} no se encontró en la lista."

# Ejemplo de uso:

# Definimos una lista de estudiantes ordenada alfabéticamente
estudiantes = ["Alejandro", "Benjamín", "Carlos", "Daniel", "Eduardo", "Francisco", "Gabriel", "Hugo"]

# Definimos el nombre del estudiante que se busca
objetivo = "Daniel"

# Llamamos a la función busqueda_binaria y imprimimos el resultado
print(busqueda_binaria(estudiantes, objetivo))

# Definimos el nombre del estudiante que se busca y no está en la lista
objetivo = "Anthony"

# Llamamos a la función busqueda_binaria y imprimimos el resultado
print(busqueda_binaria(estudiantes, objetivo))