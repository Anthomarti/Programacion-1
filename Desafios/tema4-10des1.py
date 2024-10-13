"""
# Titulo: Sistemas con múltiples entidades interconectadas
# Autor: Anthony Martinelli
# Fecha: 10/10/2024
# Descripción:
# Imagina un sistema de gestión de biblioteca que maneja
# libros, usuarios, préstamos y multas. Usar TADs separados
# para cada uno de estos elementos podría complicar la
# interacción y gestión de relaciones entre ellos.
"""

libros = []
usuarios = []
prestamos = []
multas = []

# Funcion agregar libro

# se definen los atributos que utilizara agregar libro
def agregar_libro(titulo, autor, genero, stock, codigolibro):

    # Se crea el libro que cuenta con los atributos dados, en orden
    libro = {"Título": titulo, "Autor": autor, "Género": genero, "Stock": stock, "CódigoL": codigolibro}
   
    # Se agrega el libro a la lista libros
    libros.append(libro)

    # Se imprime un mensaje de confirmación de la acción
    print(f"Libro '{titulo}' agregado correctamente.")

def agregar_usuario(nombre, codigousuario):
    usuario = {"Nombre": nombre, "CódigoU": codigousuario}
    usuarios.append(usuario)
    print(f"Usuario '{nombre}' agregado correctamente.")

def agregar_prestamo(codigolibro, codigousuario, fechaprestamo, fechadevolucion, codigoprestamo):
    # Verificar que el código de usuario exista
    usuario = next((u for u in usuarios if u["CódigoU"] == codigousuario), None)
    if usuario is None:
        print("Error: El código de usuario no existe.")
        return

    # Verificar que el código de libro exista
    libro = next((l for l in libros if l["CódigoL"] == codigolibro), None)
    if libro is None:
        print("Error: El código de libro no existe.")
        return

    # Verificar que el libro tenga stock disponible
    if libro["Stock"] <= 0:
        print("Error: El libro no tiene stock disponible.")
        return

    prestamo = {"CódigoP": codigoprestamo, "Libro": codigolibro, "Usuario": codigousuario, "Fecha préstamo": fechaprestamo, "Fecha devolución": fechadevolucion}
    prestamos.append(prestamo)
    print(f"Préstamo de libro de título '{libro['Título']}', con código: '{libro['CódigoL']}' para el usuario de nombre '{usuario['Nombre']}, código: '{usuario['CódigoU']}' agregado correctamente.")

def agregar_multa(codigoprestamo, monto):
    # Verificar que el código de préstamo exista
    prestamo = next((p for p in prestamos if p["CódigoP"] == codigoprestamo), None)
    if prestamo is None:
        print("Error: El código de préstamo no existe.")
        return

    multa = {"CódigoP": codigoprestamo, "Monto": monto, "Usuario": prestamo["Usuario"]}
    multas.append(multa)
    print(f"Multa de monto {monto} pesos, agregada correctamente al usuario con código: '{prestamo['Usuario']}'.")

def borrar_libro(codigolibro):
    # Verificar que el código de libro exista
    libro = next((l for l in libros if l["CódigoL"] == codigolibro), None)
    if libro is None:
        print("Error: El código de libro no existe.")
        return

    # Verificar que el libro tenga stock disponible
    if libro["Stock"] > 1:
        libro["Stock"] -= 1
        print(f"Un ejemplar del libro '{libro['Título']}' ha sido eliminado. Quedan {libro['Stock']} ejemplares.")
    elif libro["Stock"] == 1:
        # Verificar si hay préstamos pendientes para este libro
        prestamos_pendientes = [p for p in prestamos if p["Libro"] == codigolibro]
        if prestamos_pendientes:
            print("Error: No se puede eliminar el libro porque hay préstamos pendientes.")
            return
        else:
            libros.remove(libro)
            print(f"El libro '{libro['Título']}' ha sido eliminado.")
    else:
        print("Error.")
        return

def borrar_usuario(codigousuario):
    # Verificar que el código de usuario exista
    usuario = next((u for u in usuarios if u["CódigoU"] == codigousuario), None)
    if usuario is None:
        print("Error: El código de usuario no existe.")
        return

    # Verificar que el usuario no tenga préstamos pendientes
    prestamos_pendientes = [p for p in prestamos if p["Usuario"] == codigousuario]
    if prestamos_pendientes:
        print("Error: El usuario tiene préstamos pendientes.")
        return

    usuarios.remove(usuario)
    print(f"El usuario '{usuario['Nombre']}' ha sido eliminado.")

def borrar_prestamo(codigoprestamo):
    # Verificar que el código de préstamo exista
    prestamo = next((p for p in prestamos if p["CódigoP"] == codigoprestamo), None)
    if prestamo is None:
        print("Error: El código de préstamo no existe.")
        return

    prestamos.remove(prestamo)
    print(f"El préstamo con código '{codigoprestamo}' ha sido eliminado.")

def borrar_multa(codigoprestamo):
    # Verificar que el código de préstamo exista
    multa = next((m for m in multas if m["CódigoP"] == codigoprestamo), None)
    if multa is None:
        print("Error: El código de préstamo no existe.")
        return

    multas.remove(multa)
    print(f"La multa con código '{codigoprestamo}' ha sido eliminada.")

# Ejemplos de uso

agregar_libro("El Quijote de la Mancha", "J.U. Salinger", "Fantasía", 3, 1)
agregar_libro("To Kill a Mockingbird", "Harper Lee", "Novela", 2, 2)
agregar_libro("1984", "George Orwell", "Drama", 3, 3)

agregar_usuario("Juan Pablo", 1)

agregar_prestamo(1, 1, "2024-05-01", "2024-05-15", 1)

agregar_multa(1, 50)

print("\n** Libros en sistema **")
print("==============")
for libro in libros:
    print(f"** Título:** {libro['Título']}")
    print(f"** Autor:** {libro['Autor']}")
    print(f"** Género:** {libro['Género']}")
    print(f"** Stock:** {libro['Stock']}")
    print(f"** Código:** {libro['CódigoL']}")
    print("------------------------")

print("\n** Usuarios en sistema **")
print("===============")
for usuario in usuarios:
    print(f"** Nombre:** {usuario['Nombre']}")
    print(f"** Código:** {usuario['CódigoU']}")
    print("------------------------")

print("\n** Préstamos en sistema **")
print("===============")
for prestamo in prestamos:
    print(f"** Código de préstamo:** {prestamo['CódigoP']}")
    print(f"** Libro:** {prestamo['Libro']}")
    print(f"** Usuario:** {prestamo['Usuario']}")
    print(f"** Fecha de préstamo:** {prestamo['Fecha préstamo']}")
    print(f"** Fecha de devolución:** {prestamo['Fecha devolución']}")
    print("------------------------")

print("\n** Multas en sistema **")
print("=============")
for multa in multas:
    print(f"** Código de préstamo:** {multa['CódigoP']}")
    print(f"** Monto:** {multa['Monto']}")
    print(f"** Usuario:** {multa['Usuario']}")
    print("------------------------")

print("\n** Borrando libro, usuario, préstamo y multa... **")
borrar_libro(1)
borrar_prestamo(1)
borrar_usuario(1)
borrar_multa(1)

print("\n** Libros después de borrar **")
print("================================")
for libro in libros:
    print(f"** Título:** {libro['Título']}")
    print(f"** Autor:** {libro['Autor']}")
    print(f"** Género:** {libro['Género']}")
    print(f"** Stock:** {libro['Stock']}")
    print(f"** Código:** {libro['CódigoL']}")
    print("------------------------")

print("\n** Usuarios después de borrar **")
print("=================================")
for usuario in usuarios:
    print(f"** Nombre:** {usuario['Nombre']}")
    print(f"** Código:** {usuario['CódigoU']}")
    print("------------------------")

print("\n** Préstamos después de borrar **")
print("=================================")
for prestamo in prestamos:
    print(f"** Código de préstamo:** {prestamo['CódigoP']}")
    print(f"** Libro:** {prestamo['Libro']}")
    print(f"** Usuario:** {prestamo['Usuario']}")
    print(f"** Fecha de préstamo:** {prestamo['Fecha préstamo']}")
    print(f"** Fecha de devolución:** {prestamo['Fecha devolución']}")
    print("------------------------")

print("\n** Multas después de borrar **")
print("==============================")
for multa in multas:
    print(f"** Código de préstamo:** {multa['CódigoP']}")
    print(f"** Monto:** {multa['Monto']}")
    print(f"** Usuario:** {multa['Usuario']}")
    print("------------------------")