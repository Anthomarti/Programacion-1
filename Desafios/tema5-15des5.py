"""
# Titulo: Desafío 5 Arboles
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Los árboles de expresiones son una herramienta poderosa
# en ciencias de la computación y se utilizan comúnmente
# para evaluar expresiones matemáticas. En este desafío,
# te propongo construir y evaluar un árbol de expresiones
# para una expresión matemática dada.
"""

# Clase Nodo: representa un nodo en el árbol de expresiones
class Nodo:
    def __init__(self, valor):

        # Inicializa el nodo con un valor y dos hijos (izquierdo y derecho)
        self.valor = valor
        self.izq = None
        self.der = None

# Función construir_arbol: construye el árbol de expresiones para una expresión matemática dada
def construir_arbol(expresion):

    # Divide la expresión en tokens (operandos y operadores)
    tokens = expresion.split()
    
    # Pila para almacenar los operadores
    pila_operadores = []
    
    # Pila para almacenar los operandos (nodos del árbol)
    pila_operandos = []

    # Itera sobre los tokens de la expresión
    for token in tokens:

        # Si el token es un número, crea un nuevo nodo y lo agrega a la pila de operandos
        if token.isdigit():
            nodo = Nodo(int(token))
            pila_operandos.append(nodo)
        
        # Si el token es un operador, lo agrega a la pila de operadores
        elif token in ['+', '-', '*', '/']:

            # Mientras la pila de operadores no esté vacía y el último operador tenga mayor precedencia que el token actual
            while len(pila_operadores) > 0 and pila_operadores[-1] in ['*', '/'] and token in ['+', '-']:

                # Crea un nuevo nodo con el último operador y los dos últimos operandos
                op = pila_operadores.pop()
                der = pila_operandos.pop()
                izq = pila_operandos.pop()
                nodo = Nodo(op)
                nodo.izq = izq
                nodo.der = der

                # Agrega el nuevo nodo a la pila de operandos
                pila_operandos.append(nodo)

            # Agrega el token actual a la pila de operadores
            pila_operadores.append(token)

    # Mientras la pila de operadores no esté vacía
    while len(pila_operadores) > 0:
        
        # Crea un nuevo nodo con el último operador y los dos últimos operandos
        op = pila_operadores.pop()
        der = pila_operandos.pop()
        izq = pila_operandos.pop()
        nodo = Nodo(op)
        nodo.izq = izq
        nodo.der = der
        # Agrega el nuevo nodo a la pila de operandos
        pila_operandos.append(nodo)

    # Devuelve el único nodo que queda en la pila de operandos, que es la raíz del árbol
    return pila_operandos[0]

# Función evaluar_arbol: evalúa el árbol de expresiones y devuelve el resultado
def evaluar_arbol(raiz):
    # Si la raíz es None, devuelve 0
    if raiz is None:
        return 0
    
    # Si la raíz es un número, devuelve el número
    elif isinstance(raiz.valor, int):
        return raiz.valor
    
    # Si la raíz es un operador, evalúa los hijos izquierdo y derecho y aplica el operador
    else:
        izq = evaluar_arbol(raiz.izq)
        der = evaluar_arbol(raiz.der)
        if raiz.valor == '+':
            return izq + der
        elif raiz.valor == '-':
            return izq - der
        elif raiz.valor == '*':
            return izq * der
        elif raiz.valor == '/':
            return izq / der

# Prueba el programa con la expresión "5 + 3 * 4"
expresion = "5 + 3 * 4"
raiz = construir_arbol(expresion)
resultado = evaluar_arbol(raiz)
print("El resultado de la expresión es:", resultado)