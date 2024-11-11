"""
# Titulo: Desafío 1 Arboles
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Construye un árbol binario simple con al menos 3
# niveles de profundidad. Cada nodo debe contener
# un número entero como valor. Una vez construido
# el árbol, implementa una función que imprima los
# valores de los nodos siguiendo un recorrido en
# preorden.
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

# Función print_preorder: imprime los valores de los nodos en preorden
def print_preorder(raiz):
    
    # Si el nodo raíz no es None, imprime su valor y llama a la función recursivamente
    # para los nodos hijos izquierdo y derecho
    if raiz:
        print(raiz.val, end=" ")  # Imprime el valor del nodo
        print_preorder(raiz.izq)  # Llama a la función para el hijo izquierdo
        print_preorder(raiz.der)  # Llama a la función para el hijo derecho

# Instancia la clase ArbolBinario
arbol = ArbolBinario()

# Llama a la función print_preorder con la raíz del árbol
print_preorder(arbol.raiz)  # Salida esperada: 1 2 4 5 8 9 3 6 7 10 11