import csv
from tkinter import *

ventana = Tk()
ventana.title("LIBROS")
ventana.geometry("400x400")

libros = []
libro = ""
textoInput = StringVar()

labelTexto = Label(ventana, text="¡Ingrese un libro!")
labelTexto.grid(row=0, column=0, pady=15)

labelTexto = Label(ventana, text="Nombre:")
labelTexto.grid(row=2, column=0, pady=15)

cuadroDeTexto = Entry(ventana, textvariable=textoInput, width= 20)
cuadroDeTexto.grid(row=2, column=0)

ventana.mainloop()

################################################################

# Definimos la funcion para agregar un estudiante y su promedio
def agregarLibro (file, libro, genero):
	with open(file, 'a+') as archivo_libro:
			archivo_libro.write(f"\n{libro}, {genero}")

	# Definir la funcion que crea el archivo CSV, con las cabeceras "Nombre, Calificacion"

################################################################

def crearArchivo(file, campos):
	try:
		with open(file, 'x') as archivo_csv:
				archivo_csv.write(f"{campos}")
	except FileExistsError:
		pass

################################################################

if __name__ == '__main__':
	# Se crean las variables con el nombre de los ficheros
	file = 'libros.csv'
	
	# Creo el archivo csv con los Campos "Nombre, Calificacion"
	campos = "Nombre, Genero"
	crearArchivo(file, campos)

	opcion = 'S' 
	while opcion =='S':

		nombrelibro = input("Ingrese el nombre del libro: ")
		genero = input("Genero: ")

		agregarLibro(file, nombrelibro, genero)
		
		opcion = input("¿Desea agregar otro libro? (S/N): ")
		opcion = opcion.upper()