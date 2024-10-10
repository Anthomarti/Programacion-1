""" 
Titulo: Calculadora de área de un rectángulo
Autor: @anthonymarti200
Fecha: 02/04/2024
Descripción:    -Definir 2 variables numericas que representen el ancho y el largo del rectangulo
                -Mostrar mensajes amigables al usuario
                -Calcular el área
                -Mostrar el resultado de forma que se entienda
"""

# Se definen las variables ancho y largo, y se les da un valor
ancho = 4
largo = 5

# Se define la funcion calculararea
def calculararea(ancho, largo):
    return ancho * largo

# Se asigna el valor en la variable area
area = calculararea(ancho, largo)

# Se muestra el resultado de forma amigable
print ("El area del rectangulo con ancho:", ancho,"Y largo:", largo,"Es:", area)