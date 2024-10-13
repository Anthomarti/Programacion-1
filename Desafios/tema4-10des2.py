"""
# Titulo: Cambio frecuente en requisitos
# Autor: Anthony Martinelli
# Fecha: 13/10/2024
# Descripción:
# Supón que estás desarrollando un juego de video con distintos tipos de
# personajes y armas. Los requerimientos cambian con frecuencia, añadiendo
# nuevos personajes y habilidades. Mantener y actualizar TADs en este
# escenario podría ser una tarea titánica.
"""

# Inicializar listas vacías para personajes y armas
personajes = []
armas = []

# Función para crear un arma
def crear_arma(nombre, daño):
    # Crear un diccionario para el arma con nombre y daño
    arma = {
        "nombre": nombre,
        "daño": daño
    }
    # Agregar el arma a la lista de armas
    armas.append(arma)

# Función para crear un personaje
def crear_personaje(nombre, vida, ataque, habilidad, arma):
    # Verificar que el arma exista en la lista de armas
    arma_elegida = next((a for a in armas if a["nombre"] == arma), None)
    if arma_elegida is None:
        # Si el arma no existe, mostrar un mensaje de error
        print("Error: El arma no existe.")
        return

    # Crear un diccionario para el personaje con nombre, vida, ataque, habilidad y arma
    personaje = {
        "nombre": nombre,
        "vida": vida,
        "ataque": ataque,
        "habilidad": habilidad,
        "arma": arma_elegida
    }
    # Agregar el personaje a la lista de personajes
    personajes.append(personaje)

# Función para mostrar la lista de personajes
def mostrar_personajes():
    print("\nPersonajes:")
    for personaje in personajes:
        # Mostrar la información del personaje, incluyendo el nombre del arma y su daño
        print(f"{personaje['nombre']} - Vida: {personaje['vida']} - Ataque: {personaje['ataque']} - Habilidad: {personaje['habilidad']} - Arma: {personaje['arma']['nombre']} (Daño: {personaje['arma']['daño']})")

# Función para mostrar la lista de armas
def mostrar_armas():
    print("\nArmas:")
    for arma in armas:
        # Mostrar la información del arma, incluyendo su nombre y daño
        print(f"{arma['nombre']} - Daño: {arma['daño']}")

# Crear armas
crear_arma("Espada", 10)
crear_arma("Varita", 8)
crear_arma("Arco", 12)

# Crear personajes
crear_personaje("Guerrero", 100, 20, "Golpe crítico", "Espada")
crear_personaje("Mago", 80, 15, "Lanzar hechizo", "Varita")
crear_personaje("Arquero", 90, 18, "Disparar flecha", "Arco")

# Mostrar personajes y armas
mostrar_personajes()
mostrar_armas()

# Agregar nuevos personajes y habilidades
crear_personaje("Asesino", 95, 22, "Ataque sigiloso", "Espada")

# Mostrar personajes y armas actualizados
mostrar_personajes()
mostrar_armas()