class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        for libro in self.libros:
            print(f"- {libro}")

    # Método para agregar un libro a la lista de libros del autor
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado correctamente.")

    # Método para eliminar un libro de la lista de libros del autor
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado correctamente.")
        else:
            print(f"El libro '{libro}' no se encuentra en la lista de libros del autor.")

# Ejemplo de uso
nombre_autor = input("Ingrese el nombre del autor: ")
nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")

autor = Autor(nombre_autor, nacionalidad_autor)
autor.mostrar_autor()

while True:
    print("\nOpciones:")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Mostrar autor")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        libro = input("Ingrese el título del libro: ")
        autor.agregar_libro(libro)
    elif opcion == "2":
        libro = input("Ingrese el título del libro a eliminar: ")
        autor.eliminar_libro(libro)
    elif opcion == "3":
        autor.mostrar_autor()
    elif opcion == "4":
        print("Adiós!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")