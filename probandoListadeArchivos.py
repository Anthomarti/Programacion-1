import os

def listar_archivos(ruta_directorio):
    try:
        # Get a list of all files and directories in the specified directory
        directorios = os.listdir(ruta_directorio)
        
        # Filter out directories, keep only files
        directorios = [directorio for directorio in directorios if os.path.isfile(os.path.join(ruta_directorio, directorio)) and directorio.endswith('.ipynb')]
        
        return directorios
    except Exception as e:
        return str(e)

# Example usage
ruta_directorio = 'JupyterNotebook'  # Replace with your directory path
directorios = listar_archivos(ruta_directorio)

print("Archivos:", directorios)