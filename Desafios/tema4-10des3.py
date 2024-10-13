"""
# Titulo: Sistema de manejo de inventario para tiendas minoristas
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Considera un sistema de manejo de inventario para una cadena de tiendas minoristas.
# Tienes que tratar con datos de productos, tiendas, empleados, y transacciones,
# donde cada tienda podría tener múltiples productos y empleados.
"""

# Inicializar listas vacías para tiendas, productos, empleados y transacciones
tiendas = []
productos = []
empleados = []
transacciones = []

# Función para crear una tienda
def crear_tienda(nombre, ubicacion):
    # Crear un diccionario para la tienda con nombre, ubicación, productos y empleados
    tienda = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "productos": [],
        "empleados": []
    }
    # Agregar la tienda a la lista de tiendas
    tiendas.append(tienda)

# Función para crear un producto
def crear_producto(nombre, precio, cantidad):
    # Crear un diccionario para el producto con nombre, precio y cantidad
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    # Agregar el producto a la lista de productos
    productos.append(producto)

# Función para crear un empleado
def crear_empleado(nombre, cargo):
    # Crear un diccionario para el empleado con nombre y cargo
    empleado = {
        "nombre": nombre,
        "cargo": cargo
    }
    # Agregar el empleado a la lista de empleados
    empleados.append(empleado)

# Función para agregar un producto a una tienda
def agregar_producto_tienda(tienda_nombre, producto_nombre):
    # Buscar la tienda en la lista de tiendas
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        # Si la tienda no existe, mostrar un mensaje de error
        print("Error: La tienda no existe.")
        return

    # Buscar el producto en la lista de productos
    producto = next((p for p in productos if p["nombre"] == producto_nombre), None)
    if producto is None:
        # Si el producto no existe, mostrar un mensaje de error
        print("Error: El producto no existe.")
        return

    # Agregar el producto a la lista de productos de la tienda
    tienda["productos"].append(producto)

# Función para agregar un empleado a una tienda
def agregar_empleado_tienda(tienda_nombre, empleado_nombre):
    # Buscar la tienda en la lista de tiendas
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        # Si la tienda no existe, mostrar un mensaje de error
        print("Error: La tienda no existe.")
        return

    # Buscar el empleado en la lista de empleados
    empleado = next((e for e in empleados if e["nombre"] == empleado_nombre), None)
    if empleado is None:
        # Si el empleado no existe, mostrar un mensaje de error
        print("Error: El empleado no existe.")
        return

    # Agregar el empleado a la lista de empleados de la tienda
    tienda["empleados"].append(empleado)

# Función para crear una transacción
def crear_transaccion(tienda_nombre, producto_nombre, cantidad, empleado_nombre):
    # Buscar la tienda en la lista de tiendas
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        # Si la tienda no existe, mostrar un mensaje de error
        print("Error: La tienda no existe.")
        return

    # Buscar el producto en la lista de productos
    producto = next((p for p in productos if p["nombre"] == producto_nombre), None)
    if producto is None:
        # Si el producto no existe, mostrar un mensaje de error
        print("Error: El producto no existe.")
        return

    # Buscar el empleado en la lista de empleados
    empleado = next((e for e in empleados if e["nombre"] == empleado_nombre), None)
    if empleado is None:
        # Si el empleado no existe, mostrar un mensaje de error
        print("Error: El empleado no existe.")
        return

    # Crear un diccionario para la transacción con tienda, producto, cantidad y empleado
    transaccion = {
        "tienda": tienda_nombre,
        "producto": producto_nombre,
        "cantidad": cantidad,
        "empleado": empleado_nombre
    }
    # Agregar la transacción a la lista de transacciones
    transacciones.append(transaccion)

# Función para mostrar la lista de tiendas
def mostrar_tiendas():
    print("\nTiendas:")
    for tienda in tiendas:
        print(f"{tienda['nombre']} - Ubicación: {tienda['ubicacion']}")

# Función para mostrar la lista de productos
def mostrar_productos():
    print("\nProductos:")
    for producto in productos:
        print(f"{producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

# Función para mostrar la lista de empleados
def mostrar_empleados():
    print("\nEmpleados:")
    for empleado in empleados:
        print(f"{empleado['nombre']} - Cargo: {empleado['cargo']}")

# Función para mostrar la lista de transacciones
def mostrar_transacciones():
    print("\nTransacciones:")
    for transaccion in transacciones:
        print(f"Tienda: {transaccion['tienda']} - Producto: {transaccion['producto']} - Cantidad: {transaccion['cantidad']} - Empleado: {transaccion['empleado']}")

# Crear tiendas
crear_tienda("Walmart", "Calle 123, Ciudad de México")
crear_tienda("Costco", "Avenida 456, Guadalajara")
crear_tienda("Soriana", "Calle 789, Monterrey")

# Crear productos
crear_producto("Laptop HP", 15000, 50)
crear_producto("Smartphone Samsung", 8000, 100)
crear_producto("Tableta Apple", 12000, 20)
crear_producto("Consola PlayStation", 10000, 30)
crear_producto("Televisor LG", 25000, 15)

# Crear empleados
crear_empleado("Juan Pérez", "Gerente")
crear_empleado("María García", "Vendedor")
crear_empleado("Carlos López", "Vendedor")
crear_empleado("Ana Hernández", "Gerente")
crear_empleado("Luis Martínez", "Vendedor")

# Agregar productos a tiendas
agregar_producto_tienda("Walmart", "Laptop HP")
agregar_producto_tienda("Walmart", "Smartphone Samsung")
agregar_producto_tienda("Walmart", "Tableta Apple")
agregar_producto_tienda("Costco", "Consola PlayStation")
agregar_producto_tienda("Costco", "Televisor LG")
agregar_producto_tienda("Soriana", "Laptop HP")
agregar_producto_tienda("Soriana", "Smartphone Samsung")

# Agregar empleados a tiendas
agregar_empleado_tienda("Walmart", "Juan Pérez")
agregar_empleado_tienda("Walmart", "María García")
agregar_empleado_tienda("Walmart", "Carlos López")
agregar_empleado_tienda("Costco", "Ana Hernández")
agregar_empleado_tienda("Costco", "Luis Martínez")
agregar_empleado_tienda("Soriana", "Juan Pérez")
agregar_empleado_tienda("Soriana", "María García")

# Crear transacciones
crear_transaccion("Walmart", "Laptop HP", 5, "Juan Pérez")
crear_transaccion("Walmart", "Smartphone Samsung", 10, "María García")
crear_transaccion("Costco", "Consola PlayStation", 8, "Ana Hernández")
crear_transaccion("Soriana", "Laptop HP", 3, "Juan Pérez")
crear_transaccion("Soriana", "Smartphone Samsung", 12, "María García")

# Mostrar tiendas, productos, empleados y transacciones
mostrar_tiendas()
mostrar_productos()
mostrar_empleados()
mostrar_transacciones()