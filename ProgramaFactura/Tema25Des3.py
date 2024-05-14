"""
Autor: Anthony Martinelli

Escriba un programa que pueda tomar los detalles
de los productos (nombre, cantidad, precio) y
produzca una factura bien formateada.
"""

import csv

################################################################

# Se define la función para agregar un producto, con su nombre, cantidad, precio y precio total
def agregarProducto(file, nombreproducto, cantidad, precio, preciototal):
    with open(file, 'a+') as archivo_producto:
        archivo_producto.write(f"\n{nombreproducto}, {cantidad}, {precio}, {preciototal}")

################################################################

# Se define la función que crea el archivo CSV, con las cabeceras "Nombre, Cantidad, Precio, Preciototal"
# Se utiliza un archivo CSV, ya que considero que una factura debe ser presentada de forma amigable al usuario, fuera de la consola
def crearArchivo(file, campos):
    try:
        with open(file, 'x') as archivo_csv:
            archivo_csv.write(f"{campos}")
    except FileExistsError:
        pass

################################################################

# Esta línea verifica si el programa actual se está ejecutando como un script principal o si se está importando como un módulo en otro script
if __name__ == '__main__':

    # Se crean las variables con el nombre de los ficheros
    file = 'factura.csv'
    
    # Se crea el archivo CSV con los campos "Nombre, Cantidad, Precio y Preciototal"
    campos = "Nombre, Cantidad, Precio, Preciototal"
    crearArchivo(file, campos)

    opcion = 'S' 
    
    while opcion == 'S':
        preciototal = 0.00
        nombreproducto = input("Ingrese el nombre del producto: ")
    
        cantidad = input("Cantidad: ")
        cantidad = int(cantidad)
        
        precioindividual = input("Precio del producto individual: ")
        precioindividual = float(precioindividual)
        
        preciototal = precioindividual * cantidad
        preciototalredondeado = round(preciototal, 2)

        agregarProducto(file, nombreproducto, cantidad, precioindividual, preciototalredondeado)
        
        opcion = input("¿Desea agregar otro producto? (S/N): ")
        opcion = opcion.upper()