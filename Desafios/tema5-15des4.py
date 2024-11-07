"""
# Titulo: Desafío 4 Arboles
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Dado un conjunto de números enteros únicos,
# construye un árbol de búsqueda binaria (ABB)
# que inserte los valores de manera que el
# subárbol izquierdo de cada nodo contenga
# solo nodos con valores menores, y el subárbol
# derecho solo nodos con valores mayores.
# Una vez construido el árbol, implementa una
# función para buscar un número dado y devuelva
# si ese número existe en el árbol o no.
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

    # Función buscar: busca un valor en el árbol de búsqueda binaria
    def buscar(self, valor):
        # Llama a la función buscar_nodo para buscar el valor en el árbol
        return self.buscar_nodo(self.raiz, valor)

    # Función buscar_nodo: busca un valor en el árbol de búsqueda binaria
    def buscar_nodo(self, nodo, valor):
        # Si el nodo es None, el valor no existe en el árbol
        if nodo is None:
            return False
        # Si el valor es igual al valor del nodo, el valor existe en el árbol
        elif valor == nodo.val:
            return True
        # Si el valor es menor que el valor del nodo, busca en el subárbol izquierdo
        elif valor < nodo.val:
            return self.buscar_nodo(nodo.izq, valor)
        # Si el valor es mayor que el valor del nodo, busca en el subárbol derecho
        else:
            return self.buscar_nodo(nodo.der, valor)

# Crea un árbol binario
arbol = ArbolBinario()

# Busca un valor en el árbol
valor_buscar = 13
existe = arbol.buscar(valor_buscar)

# Imprime el resultado
if existe:
    print(f"El valor {valor_buscar} existe en el árbol.")
else:
    print(f"El valor {valor_buscar} no existe en el árbol.")

# Busca un valor en el árbol que no existe
valor_buscar = 100
existe = arbol.buscar(valor_buscar)

# Imprime el resultado
if existe:
    print(f"El valor {valor_buscar} existe en el árbol.")
else:
    print(f"El valor {valor_buscar} no existe en el árbol.")