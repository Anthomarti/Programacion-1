"""
# Titulo: Desafío 2 Algoritmos fundamentales
# Autor: Anthony Martinelli
# Fecha: 06/11/2024
# Descripción:
# Tienes una tabla de calificaciones representada
# como una matriz, donde cada fila contiene las
# calificaciones de un estudiante en distintas materias.
# Implementa una función que busque una calificación
# específica en toda la matriz y devuelva el estudiante
# y la materia en la que se encuentra.
"""

# Función buscar_calificacion: busca una calificación específica en una matriz de calificaciones
def buscar_calificacion(matriz, calificacion):
    
    # Define las materias
    materias = ["Matemáticas", "Lengua", "Ciencias", "Historia", "Geografía"]
    
    # Crea una lista para almacenar los resultados
    resultados = []
    
    # Recorre cada fila de la matriz (cada estudiante)
    for i, fila in enumerate(matriz):
        # Recorre cada columna de la fila (cada materia)
        for j, nota in enumerate(fila):
            # Si la nota coincide con la calificación buscada
            if nota == calificacion:
                # Agrega el resultado a la lista
                resultados.append(f"Estudiante {i+1}, Materia: {materias[j]}")

    # Si no se encuentra la calificación, devuelve un mensaje de no encontrado
    if not resultados:
        return "Calificación no encontrada"

    # Devuelve la lista de resultados
    return resultados

# Define la matriz de calificaciones
matriz_calificaciones = [
    [8, 7, 9, 6, 8],
    [9, 8, 7, 9, 6],
    [7, 9, 8, 7, 9],
    [6, 8, 9, 8, 7],
    [8, 7, 6, 9, 8]
]

# Busca la calificación 6 en la matriz
calificacion_buscada = 6
resultado = buscar_calificacion(matriz_calificaciones, calificacion_buscada)

# Imprime el resultado
if isinstance(resultado, list):
    print("Resultados:")
    for i, res in enumerate(resultado):
        print(f"{i+1}. {res}")
else:
    print(resultado)