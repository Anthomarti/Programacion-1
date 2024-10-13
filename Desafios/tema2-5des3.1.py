"""
Autor: Anthony Martinelli

Letra: Escriba un programa que pueda tomar los detalles
de los productos (nombre, cantidad, precio) y
produzca una factura bien formateada.
"""

# Se ingresan los datos de los productos
nombreproducto = input("Ingrese el nombre del producto: ")

cantidad = input("Ingrese la cantidad: ")
cantidad = float(cantidad)

precioindividual = input("Ingrese el precio individual del producto (en pesos): ")
precioindividual = float(precioindividual)

preciototal = precioindividual * cantidad

# Se muestra la factura bien formateada
print(f"Producto: {nombreproducto}")
print(f"Cantidad: {cantidad}")
print(f"Precio de cada producto: {precioindividual}")
print(f"Precio total: {preciototal}")