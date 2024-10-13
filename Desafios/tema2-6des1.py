"""
Autor: Anthony Martinelli
Letra: Desafío 1: Calificaciones Aprobatorias y Desaprobatorias.

Supón que estás analizando las calificaciones de los estudiantes y quieres saber
cuántos aprobaron y cuántos desaprobaron. Se considera que una calificación
de 7 o superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria.
Utiliza lo que aprendiste sobre bucles y condicionales para resolver este problema.
"""

# Se asume que al correr el codigo, el usuario quiere utilizarlo
decision = "si"

# Se crea la lista "estudiantes" vacia
estudiantes = []

print("Bienvenido al programa de calificaciones ")

# Se revisa que el usuario quiere agregar estudiantes
while decision == "si":
  
  nombre = input("Ingrese el nombre del alumno: ")
  
  calificacion = input("Ingrese la calificación del alumno: ")
  calificacion = float(calificacion)
  calificacion = round(calificacion)

  # Se agregan los datos de estudiante en la lista "estudiantes"
  estudiantes.append((nombre, calificacion))

  # Se revisa que el usuario siga queriendo agregar estudiantes
  decision = input("Desea agregar más estudiantes? ('si'/'no') ")

  # Si el usuario no quiere seguir agregando estudiantes
  if decision != "si":
    
    # Se usa un for para revisar la lista de estudiantes
    for nombre, calificacion in estudiantes:
      if calificacion >= 7:
        resultado = "aprobó"

        # Se muestran quienes aprobaron
        print(f"El alumno {nombre}, con calificación {calificacion}, {resultado}. ")

      elif calificacion <= 6:
        resultado = "reprobó"

          # Se muestran quienes reprobaron
        print(f"El alumno {nombre}, con calificación {calificacion}, {resultado}. ")