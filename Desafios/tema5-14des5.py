"""
# Titulo: Desafío 5 Excepciones y errores
# Autor: Anthony Martinelli
# Fecha: 05/11/2024
# Descripción:
# Desarrolla un programa que abra un archivo de texto,
# lea su contenido y lo muestre. Implementa manejo de
# excepciones para archivos que no existan y usa finally
# para asegurarte de que el archivo se cierre
# adecuadamente en cualquier caso.
"""

def leer_archivo(ruta_archivo):
    try:
        # Intenta abrir el archivo en modo lectura
        archivo = open(ruta_archivo, 'r')
        
        # Lee el contenido del archivo
        contenido = archivo.read()
        
        # Muestra el contenido del archivo
        print(contenido)
    
    except FileNotFoundError:
        # Si el archivo no existe, muestra un mensaje de error
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
    
    except PermissionError:
        # Si no se tiene permiso para leer el archivo, muestra un mensaje de error
        print(f"Error: No se tiene permiso para leer el archivo '{ruta_archivo}'.")
    
    except Exception as e:
        # Si ocurre cualquier otra excepción, muestra un mensaje de error
        print(f"Error: {e}")
    
    finally:
        # Asegúrate de que el archivo se cierre adecuadamente en cualquier caso
        try:
            archivo.close()
        except NameError:
            # Si el archivo no se abrió, no hay nada que cerrar
            pass

def main():

    # Pide al usuario que ingrese la ruta del archivo (completo o relativo)
    ruta_archivo = input("Ingrese la ruta del archivo: ")
    leer_archivo(ruta_archivo)

if __name__ == "__main__":
    main()