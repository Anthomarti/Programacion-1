"""
# Titulo: Desafío 2 Arboles
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Dado un árbol binario con números enteros en
# cada nodo, implementa una función que recorra
# el árbol en inorden y calcule la suma de todos
# los valores almacenados en los nodos.
# El programa debe devolver el resultado final de la suma.
"""

# Clase Nodo: representa un nodo en el árbol binario
class Nodo:
    def __init__(self, key):
        # Inicializa el nodo con un valor y dos hijos (izquierdo y derecho)
        self.izq = None  # Hijo izquierdo
        self.der = None  # Hijo derecho
        self.val = key  # Valor del nodo

# Clase ArbolBinario: representa un árbol binario
class ArbolBinario:
    def __init__(self):
        # Crea el nodo raíz del árbol
        self.raiz = Nodo(1)

        # Añade nodos hijos al nodo raíz
        self.raiz.izq = Nodo(2)  # Hijo izquierdo del raíz
        self.raiz.der = Nodo(3)  # Hijo derecho del raíz

        # Añade nodos hijos al nodo izquierdo del raíz
        self.raiz.izq.izq = Nodo(4)  # Nieto izquierdo del raíz
        self.raiz.izq.der = Nodo(5)  # Nieto derecho del raíz

        # Añade nodos hijos al nodo derecho del raíz
        self.raiz.der.izq = Nodo(6)  # Nieto izquierdo del raíz
        self.raiz.der.der = Nodo(7)  # Nieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
        self.raiz.izq.der.izq = Nodo(8)  # Bisnieto izquierdo del raíz
        self.raiz.izq.der.der = Nodo(9)  # Bisnieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo derecho del raíz
        self.raiz.der.der.izq = Nodo(10)  # Bisnieto izquierdo del raíz
        self.raiz.der.der.der = Nodo(11)  # Bisnieto derecho del raíz

# Función suma_inorden: recorre el árbol en inorden y calcula la suma de todos los valores
def suma_inorden(raiz):
    # Inicializa la suma a 0
    suma = 0

    # Si el nodo raíz no es None, recorre el árbol en inorden
    if raiz:
        # Recorre el subárbol izquierdo
        suma += suma_inorden(raiz.izq)

        # Suma el valor del nodo actual
        suma += raiz.val

        # Recorre el subárbol derecho
        suma += suma_inorden(raiz.der)

    # Devuelve la suma final
    return suma

# Instancia la clase ArbolBinario
arbol = ArbolBinario()

# Llama a la función suma_inorden con la raíz del árbol
suma = suma_inorden(arbol.raiz)

# Imprime el resultado final
print("La suma de todos los valores en el árbol es:", suma)