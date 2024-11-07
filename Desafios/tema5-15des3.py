"""
# Titulo: Desafío 3 Arboles
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Construye un árbol binario en el que cada nodo
# contiene un número entero. Implementa una función
# que recorra el árbol en postorden y devuelva el
# valor máximo encontrado entre todos los nodos del árbol.
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
        self.raiz.der = Nodo(13)  # Hijo derecho del raíz

        # Añade nodos hijos al nodo izquierdo del raíz
        self.raiz.izq.izq = Nodo(44)  # Nieto izquierdo del raíz
        self.raiz.izq.der = Nodo(75)  # Nieto derecho del raíz

        # Añade nodos hijos al nodo derecho del raíz
        self.raiz.der.izq = Nodo(6)  # Nieto izquierdo del raíz
        self.raiz.der.der = Nodo(17)  # Nieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
        self.raiz.izq.der.izq = Nodo(25)  # Bisnieto izquierdo del raíz
        self.raiz.izq.der.der = Nodo(9)  # Bisnieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo derecho del raíz
        self.raiz.der.der.izq = Nodo(10)  # Bisnieto izquierdo del raíz
        self.raiz.der.der.der = Nodo(11)  # Bisnieto derecho del raíz

# Función maximo_postorden: recorre el árbol en postorden y devuelve el valor máximo
def maximo_postorden(raiz):
    # Inicializa el máximo a un valor muy pequeño
    maximo = float('-inf')

    # Si el nodo raíz no es None, recorre el árbol en postorden
    if raiz:
        # Recorre el subárbol izquierdo
        maximo_izq = maximo_postorden(raiz.izq)

        # Recorre el subárbol derecho
        maximo_der = maximo_postorden(raiz.der)

        # Actualiza el máximo con el valor del nodo actual
        maximo = max(maximo, raiz.val, maximo_izq, maximo_der)

    # Devuelve el máximo final
    return maximo

# Instancia la clase ArbolBinario
arbol = ArbolBinario()

# Llama a la función maximo_postorden con la raíz del árbol
maximo = maximo_postorden(arbol.raiz)

# Imprime el resultado final
print("El valor máximo en el árbol es:", maximo)