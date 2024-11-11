import random
import string

def generar_contrasena(longitud=8):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

contrasena_aleatoria = generar_contrasena()
print(f"Contraseña aleatoria: {contrasena_aleatoria}")
