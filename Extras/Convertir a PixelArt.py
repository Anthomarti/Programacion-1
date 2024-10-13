import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import os

# Función para cargar una imagen y aplicarle el efecto de pixelación
def pixelate_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Pedir al usuario el tamaño de los píxeles
    pixel_size = simpledialog.askinteger("Tamaño de píxeles", "Ingrese el tamaño de los píxeles:", minvalue=1)
    if not pixel_size:
        return

    # Cargar la imagen
    original_image = Image.open(file_path)

    # Pixelar la imagen
    small_image = original_image.resize(
        (original_image.width // pixel_size, original_image.height // pixel_size), 
        Image.NEAREST
    )
    pixelated_image = small_image.resize(original_image.size, Image.NEAREST)

    # Guardar la imagen pixelada
    original_name, original_ext = os.path.splitext(os.path.basename(file_path))
    save_path = f'{original_name}_pixeleada{original_ext}'
    pixelated_image.save(save_path)

    # Redimensionar la imagen para mostrarla en la interfaz gráfica
    max_size = 225
    display_image = pixelated_image.copy()
    display_image.thumbnail((max_size, max_size), Image.NEAREST)

    # Mostrar la imagen en la interfaz gráfica
    pixelated_photo = ImageTk.PhotoImage(display_image)
    label.config(image=pixelated_photo)
    label.image = pixelated_photo

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Pixelador de Imágenes")

# Botón para cargar la imagen
button = tk.Button(root, text="Cargar imagen y pixelar", command=pixelate_image)
button.pack(pady=20)

# Etiqueta para mostrar la imagen pixelada
label = tk.Label(root)
label.pack()

# Ejecutar la aplicación
root.mainloop()