'''
## Problema 4: Lectura y Escritura en Archivos
Supongamos que somos profesores y necesitamos procesar
las calificaciones de nuestros alumnos. 
Los datos se almacenan en un archivo CSV, y nuestro 
trabajo es leer ese archivo, calcular el promedio 
de las calificaciones y luego escribir ese promedio 
en un nuevo archivo.
input() y print() no son adecuados aquí porque estamos
trabajando con archivos y no con entradas de usuario 
o impresiones en la consola.
'''

import csv

#Definimos la funcion que calcula el promedio
def calcularPromedio(file):
    # Leemos el archivo CSV
    with open(file, 'r') as archivo_calificaciones:
            lector = csv.reader(archivo_calificaciones)
            next(lector)  # Saltamos la cabecera del archivo

            suma_total = 0
            contador = 0
            for fila in lector:
                    suma_total += float(fila[1])  # Asumimos que la calificación está en la segunda columna
                    contador += 1 #contador = contador + 1

    # Calculamos el promedio
    promedio = suma_total / contador if contador != 0 else 0	
    print("El promedio es: ", promedio)
    return promedio

#Definimos la funcion que escribe el promedio en un nuevo archivo
def escribirPromedio(file, promedio):
    # Escribimos el promedio de calificaciones en un nuevo archivo
    with open(file, 'w') as archivo_promedio:
            archivo_promedio.write(f"El promedio de las calificaciones es: {promedio}\n")



if __name__ == '__main__':
    file = 'calificaciones.csv'
    file_promedio = 'promedio_calificaciones.txt'

    promedio = calcularPromedio(file)
    escribirPromedio(file_promedio, promedio)