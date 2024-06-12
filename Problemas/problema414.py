"""
Autor: Anthony Martinelli
Problema 414: Escriba un programa que declare un arreglo de enteros y encuentre el segundo número más grande del arreglo.
"""

# Se define la funcion segundo_mas_grande que se encarga de encontrar el segundo número más grande
def segundo_mas_grande(arr):

    # Se inicializan los primeros dos valores del arreglo, para poder utilizarlos para comparar en el futuro
    if arr[0] > arr[1]:
        primero, segundo = arr[0], arr[1]
    else:
        primero, segundo = arr[1], arr[0]

    # Recorrer el resto del arreglo (desde la tercera posicion en adelante), y los compara con los elementos que ya definimos
    for numero in arr[2:]:
        if numero > primero:
            segundo = primero
            primero = numero
        elif numero > segundo and numero != primero:
            segundo = numero
    return segundo

arreglo = [240, 150, 8, 12, 15, 7, 32, 99]
resultado = segundo_mas_grande(arreglo)

print(f"El segundo número más grande del arreglo es: {resultado}")
