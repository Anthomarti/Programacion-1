"""
# Titulo: Desafío 1 Algoritmos fundamentales
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Dado un árbol que representa los grupos de estudiantes
# en una escuela, implementa un recorrido por niveles para
# mostrar los estudiantes de cada grupo, comenzando por el
# nivel más alto (ej. grado 12) y descendiendo hasta el nivel
# más bajo (ej. grado 1). Cada nodo del árbol representa un
# grado y sus estudiantes.
"""

# Clase Nodo: representa un nodo en el árbol binario
class Nodo:
    def __init__(self, key, estudiantes):

        # Inicializa el nodo con un valor, una lista de estudiantes y dos hijos (izquierdo y derecho)
        self.izq = None  # Hijo izquierdo
        self.der = None  # Hijo derecho
        self.val = key  # Valor del nodo
        self.estudiantes = estudiantes  # Lista de estudiantes del nodo

# Clase ArbolBinario: representa un árbol binario
class ArbolBinario:
    def __init__(self):

        # Crea el nodo raíz del árbol
        self.raiz = Nodo(12, ["Estudiante 1: Pepe", "Estudiante 2: Manuel"])

        # Añade nodos hijos al nodo raíz
        self.raiz.izq = Nodo(11, ["Estudiante 3: Sara", "Estudiante 4: Noemi"])  # Hijo izquierdo del raíz
        self.raiz.der = Nodo(10, ["Estudiante 5: Alberto", "Estudiante 6: Miguel"])  # Hijo derecho del raíz

        # Añade nodos hijos al nodo izquierdo del raíz
        self.raiz.izq.izq = Nodo(9, ["Estudiante 7: Domingo", "Estudiante 8: Agustin"])  # Nieto izquierdo del raíz
        self.raiz.izq.der = Nodo(8, ["Estudiante 9: Lucas", "Estudiante 10: Anthony"])  # Nieto derecho del raíz

        # Añade nodos hijos al nodo derecho del raíz
        self.raiz.der.izq = Nodo(7, ["Estudiante 11: Abril", "Estudiante 12: Estela"])  # Nieto izquierdo del raíz
        self.raiz.der.der = Nodo(6, ["Estudiante 13: Marcos", "Estudiante 14: Angelo"])  # Nieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
        self.raiz.izq.der.izq = Nodo(5, ["Estudiante 15: Jonathan", "Estudiante 16: Pamela"])  # Bisnieto izquierdo del raíz
        self.raiz.izq.der.der = Nodo(4, ["Estudiante 17: Ruperto", "Estudiante 18: Griselda"])  # Bisnieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo derecho del raíz
        self.raiz.der.der.izq = Nodo(3, ["Estudiante 19: Gabriela", "Estudiante 20: Gabriel"])  # Bisnieto izquierdo del raíz
        self.raiz.der.der.der = Nodo(2, ["Estudiante 21: Barbara", "Estudiante 22: Maria"])  # Bisnieto derecho del raíz

        # Añade nodos hijos al nodo hijo derecho del hijo derecho del hijo derecho del raíz
        self.raiz.der.der.der.izq = Nodo(1, ["Estudiante 23: Facundo", "Estudiante 24: Andres"])  # Tataranieto izquierdo del raíz

# Función print_por_niveles: imprime los valores de los nodos y sus estudiantes por niveles
def print_por_niveles(raiz):
    
    # Si el nodo raíz es None, no hay nada que imprimir
    if not raiz:
        return

    # Crea una cola para almacenar los nodos a visitar
    cola = [raiz]

    # Mientras haya nodos en la cola, sigue visitando
    while cola:
        # Saca el nodo actual de la cola
        nodo_actual = cola.pop(0)

        # Imprime el valor del nodo actual y sus estudiantes
        print(f"Nivel {nodo_actual.val}: {nodo_actual.estudiantes}")

        # Si el nodo actual tiene hijos, añádelos a la cola
        if nodo_actual.izq:
            cola.append(nodo_actual.izq)
        if nodo_actual.der:
            cola.append(nodo_actual.der)

# Instancia la clase ArbolBinario
arbol = ArbolBinario()

# Llama a la función print_por_niveles con la raíz del árbol
print_por_niveles(arbol.raiz)