import os

def listar_archivos(ruta_directorio):
    try:
        # Consigue una lista de archivos dentro de un directorio especificado
        directorios = os.listdir(ruta_directorio)
        
        # Filtra los archivos que no terminen en "'.ipynb"
        directorios = [directorio for directorio in directorios if os.path.isfile(os.path.join(ruta_directorio, directorio)) and directorio.endswith('.ipynb')]
        
        return directorios
    except Exception as e:
        return str(e)
    
def escribirArchivo(directorios, rutaOut):
    try:
        # Abre el archivo markdown para escribirlo
        with open(rutaOut, mode='w') as mddirectorio:
            # Escribe el header
            mddirectorio.write('## Archivos Notebook:\n')
            
            # Escribe los nombres de los archivos
            for directorio in directorios:
                mddirectorio.write('## [' + directorio + '](' + directorio + ')\n')
                
    except Exception as e:
        return str(e)

ruta_directorio = 'JupyterNotebook/'  # Reemplazarlo con la ruta donde estan los archivos ".ipynb"
rutaOut = 'JupyterNotebook/0_0_Resumen.md'  # Reemplazarlo con la ruta donde desea guardar el archivo markdown

directorios = listar_archivos(ruta_directorio)

print("Archivos Notebook encontrados:")
for directorio in directorios:
    print(directorio)

escribirArchivo(directorios, rutaOut)

print(f"Los archivos fueron guardados en: {rutaOut}")