"""
# Titulo: Desafío 5 Algoritmos fundamentales
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Dado un conjunto de estudiantes y sus promedios, implementa una
# función que cree un árbol binario de búsqueda en el que los nodos
# representan los promedios de los estudiantes. Luego, implementa
# una función que recorra el árbol en inorden para mostrar los
# estudiantes en orden ascendente de rendimiento académico.
"""

# Clase Nodo: representa un nodo en el árbol binario
class Nodo:
 def __init__(self, key, nombre):
 
  # Inicializa el nodo con un valor y dos hijos (izquierdo y derecho)
  self.izq = None  # Hijo izquierdo
  self.der = None  # Hijo derecho
  self.val = key  # Valor del nodo (promedio)
  self.nombre = nombre  # Nombre del estudiante

# Clase ArbolBinario: representa un árbol binario
class ArbolBinario:
 def __init__(self):
 
  # Crea el nodo raíz del árbol
  self.raiz = None

 # Función insertar: inserta un nuevo nodo en el árbol
 def insertar(self, key, nombre):
  if self.raiz is None:
   self.raiz = Nodo(key, nombre)
  else:
   self._insertar(key, nombre, self.raiz)

 # Función _insertar: inserta un nuevo nodo en el árbol de manera recursiva
 def _insertar(self, key, nombre, nodo):
  if key < nodo.val:
   if nodo.izq is None:
    nodo.izq = Nodo(key, nombre)
   else:
    self._insertar(key, nombre, nodo.izq)
  else:
   if nodo.der is None:
    nodo.der = Nodo(key, nombre)
   else:
    self._insertar(key, nombre, nodo.der)

# Función print_inorden: imprime los valores de los nodos en inorden
def print_inorden(raiz):
 
 # Si el nodo raíz no es None, llama a la función recursivamente
 # para el nodo hijo izquierdo, imprime el valor del nodo y llama
 # a la función recursivamente para el nodo hijo derecho
 if raiz:
  print_inorden(raiz.izq)  # Llama a la función para el hijo izquierdo
  print(f"{raiz.nombre}: {raiz.val}")  # Imprime el valor del nodo
  print_inorden(raiz.der)  # Llama a la función para el hijo derecho

# Instancia la clase ArbolBinario
arbol = ArbolBinario()

# Inserta nodos en el árbol
arbol.insertar(8.5, "Alejandro")
arbol.insertar(7.2, "Benjamín")
arbol.insertar(9.1, "Carlos")
arbol.insertar(8.8, "Daniel")
arbol.insertar(7.5, "Eduardo")
arbol.insertar(9.5, "Francisco")
arbol.insertar(8.2, "Gabriel")
arbol.insertar(7.8, "Hugo")

# Llama a la función print_inorden con la raíz del árbol
print_inorden(arbol.raiz)