"""
# Titulo: Desafío 4 Listas
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Tienes dos listas de números enteros de diferentes
# longitudes. Desarrolla un programa que sume los
# elementos de las listas en las posiciones correspondientes.
# Si una lista es más corta que la otra, los elementos
# que falten deben considerarse como 0 en la suma.
"""

# Listas de números enteros de diferentes longitudes
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 2, 20, 4]

# Función para sumar los elementos de las listas en las posiciones correspondientes
def sumar_listas(lista1, lista2):

    # Obtiene la longitud máxima de las listas
    max_len = max(len(lista1), len(lista2))
    
    # Crea una lista vacía para almacenar los resultados de la suma
    resultado = []
    
    # Recorre las listas hasta la longitud máxima
    for i in range(max_len):
        # Verifica si el índice está dentro de los límites de cada lista
        num1 = lista1[i] if i < len(lista1) else 0
        num2 = lista2[i] if i < len(lista2) else 0
        
        # Suma los elementos en la posición correspondiente
        suma = num1 + num2
        
        # Agrega el resultado a la lista
        resultado.append(suma)
    
    # Devuelve la lista con los resultados de la suma
    return resultado

# Función principal del programa
def main():

    # Muestra las listas originales
    print("Lista 1:")
    print(lista1)
    print("\nLista 2:")
    print(lista2)
    
    # Suma los elementos de las listas en las posiciones correspondientes
    resultado = sumar_listas(lista1, lista2)
    
    # Muestra el resultado de la suma
    print("\nResultado de la suma:")
    print(resultado)

# Verifica si el programa se está ejecutando directamente (no como módulo)
if __name__ == "__main__":
    # Llama a la función principal
    main()