"""
# Titulo: Desafío 4 Algoritmos fundamentales
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Tienes una lista de estudiantes y su promedio de calificaciones.
# Implementa un algoritmo que ordene a los estudiantes de acuerdo
# con su promedio utilizando el algoritmo de ordenamiento por selección.
# Al final, el estudiante con el promedio más alto debe estar en
# primer lugar.
"""

# Definimos la función ordenar_estudiantes que toma como argumento la lista de estudiantes y sus promedios
def ordenar_estudiantes(estudiantes):
 
 # Recorremos la lista de estudiantes
 for i in range(len(estudiantes)):
  
  # Inicializamos la variable maximo para almacenar el índice del estudiante con el promedio más alto
  maximo = i
  
  # Recorremos la lista de estudiantes a partir del índice actual
  for j in range(i + 1, len(estudiantes)):
   
   # Comparamos el promedio del estudiante actual con el promedio del estudiante en el índice j
   if estudiantes[j][1] > estudiantes[maximo][1]:

    # Si el promedio del estudiante en el índice j es mayor, actualizamos la variable maximo
    maximo = j
  
  # Intercambiamos el estudiante en el índice i con el estudiante en el índice maximo
  estudiantes[i], estudiantes[maximo] = estudiantes[maximo], estudiantes[i]

 # Devolvemos la lista de estudiantes ordenada
 return estudiantes

# Ejemplo de uso:

# Definimos una lista de estudiantes y sus promedios
estudiantes = [
 ["Alejandro", 8.5],
 ["Benjamín", 7.2],
 ["Carlos", 9.1],
 ["Daniel", 8.8],
 ["Eduardo", 7.5],
 ["Francisco", 9.5],
 ["Gabriel", 8.2],
 ["Hugo", 7.8]
]

# Llamamos a la función ordenar_estudiantes y imprimimos el resultado
estudiantes_ordenados = ordenar_estudiantes(estudiantes)

# Imprimimos la lista de estudiantes ordenada
for i, estudiante in enumerate(estudiantes_ordenados):
 print(f"{i + 1}. {estudiante[0]} - Promedio: {estudiante[1]}")