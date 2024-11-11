"""
# Titulo: Desafío 3 Listas
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Tienes una lista de números en la que algunos
# elementos están repetidos. Desarrolla un programa
# que elimine todos los elementos duplicados y deje
# únicamente una aparición de cada uno. La salida
# debe mostrar la lista original y la lista sin duplicados.
"""

# Lista de números con elementos duplicados
numeros = [1, 2, 2, 2, 40, 55, 64, 21, 33, 33, 80, 90, 1]

# Función principal del programa
def main():

    # Muestra la lista original
    print("Lista original:")
    print(numeros)
    
    # Elimina los elementos duplicados de la lista utilizando un set
    lista_unica = list(set(numeros))
    
    # Muestra la lista sin duplicados
    print("\nLista sin duplicados:")
    print(lista_unica)

# Verifica si el programa se está ejecutando directamente (no como módulo)
if __name__ == "__main__":

    # Llama a la función principal
    main()