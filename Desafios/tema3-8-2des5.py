import os

# Guardar texto en un archivo
def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

# Leer texto de un archivo
def leer_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return archivo.read()
    else:
        return "El archivo no existe."

# Uso
guardar_archivo("texto_ejemplo.txt", "Texto de prueba.")
contenido = leer_archivo('texto_ejemplo.txt')
print(contenido)
