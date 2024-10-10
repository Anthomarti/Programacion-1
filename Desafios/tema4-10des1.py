""" 
Titulo: Sistemas con múltiples entidades interconectadas
Autor: Anthony Martinelli
Fecha: 10/10/2024
Descripción:
Imagina un sistema de gestión de biblioteca que maneja
libros, usuarios, préstamos y multas. Usar TADs separados
para cada uno de estos elementos podría complicar la
interacción y gestión de relaciones entre ellos.
"""

libros = []
usuarios = []
prestamos = []
multas = []

# Funcion agregar libro

# se definen los atributos que utilizara agregar libro
def agregar_libro(titulo, autor, genero, stock,codigolibro):

    # Se crea el libro que cuenta con los atributos dados, en orden
    libro = {"Título": titulo, "Autor": autor, "Género": genero, "Stock": stock, "Código": codigolibro}
   
    # Se agrega el libro a la lista libros
    libros.append(libro)

    # Se imprime un mensaje de confirmación de la acción
    print(f"Libro '{titulo}' agregado correctamente.")

def agregar_usuario(nombre, codigousuario):
    usuario = {"Nombre": nombre, "Código": codigousuario}
    usuarios.append(usuario)
    print(f"Usuario '{nombre}' agregado correctamente.")

def agregar_prestamo(libro, usuario, fecha_prestamo, fecha_devolucion):
    prestamo = {"Libro": libro, "Usuario": usuario, "Fecha préstamo": fecha_prestamo, "Fecha devolución": fecha_devolucion}
    prestamos.append(prestamo)
    print(f"Préstamo de libro '{libro['Título']}' para el usuario '{usuario['Nombre']}' agregado correctamente.")

def agregar_multa(prestamo, monto, usuario):
    multa = {"Préstamo": prestamo, "Monto": monto, "Usuario": usuario}
    multas.append(multa)
    print(f"Multa de monto {monto} agregada correctamente al usuario '{usuario['Nombre']}'.")

# Ejemplos de uso

agregar_libro("El Quijote de la Mancha", "J.U. Salinger", "Fantasía", 3, 1)
agregar_libro("To Kill a Mockingbird", "Harper Lee", "Novela", 2, 2)
agregar_libro("1984", "George Orwell", "Drama", 3, 3)

agregar_usuario("Juan Pablo", 1)

agregar_prestamo(libros[0], usuarios[0], "2024-05-01", "2024-05-15")

agregar_multa(prestamos[0], 50, usuarios[0])

print("libros")
print(libros)

print("usuarios")
print(usuarios)

print("prestamos")
print(prestamos)

print("multas")
print(multas)
