"""
Autor: Anthony Martinelli
Letra: Toma el ejemplo del cálculo del promedio de calificaciones y mejóralo. En lugar de pedir las calificaciones una por una, modifica el código para pedir todas las calificaciones al mismo tiempo (el estudiante puede ingresar las calificaciones separadas por comas) y luego calcular el promedio.
"""

suma_calificaciones = 0
contador_asignaturas = 0

while True:
    
    entrada = input("Ingrese una o más calificaciones (entre 1 y 12) separadas por comas, o 0 para ver el promedio: ")

    # Se revisa que el usuario solo haya ingresado "0", para dejar de ingresar calificaciones
    if entrada.strip() == "0":
        break

    # Se especifica que los valores de calififcacion van estar separados por coma
    calificaciones = entrada.split(",")

    # Se usa un for para revisar todas las calificaciones (como string)
    for calificacionTexto in calificaciones:
        
        try:

            # Se separan los valores de calificacion, y se convierten en integer
            calificacion = int(calificacionTexto.strip())

        # En caso de que se ingresen valores que no sean numeros
        except ValueError:
            
            print("Asegurate que todas las calificaciones son valores válidos. Inténtalo de nuevo.")
            
            continue

        # En caso que las calificaciones no esten en el rango de 1 - 12
        if calificacion < 1 or calificacion > 12:
            
            print("Asegurate que todas las calificaciones esten entre 1 y 12. Inténtalo de nuevo.")
            
            continue

        suma_calificaciones += calificacion
        contador_asignaturas += 1

promedio = suma_calificaciones / contador_asignaturas
print(f"El promedio de las calificaciones es: {promedio}")