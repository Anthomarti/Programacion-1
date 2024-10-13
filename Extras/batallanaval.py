"""
Titulo: Batalla Naval
Curso: Programación 1
Autores: Sol Méndez, Anthony Martinelli, Agustín Muñoz y Lucas Aguiar.
"""
import math  # Importa funciones matemáticas como sqrt (raíz cuadrada) y pow (potencia)
import numpy as np  # Importa numpy para manejar matrices
import pygame  # Importa pygame para crear la interfaz gráfica

pygame.display.set_caption('     Batalla Naval     ')

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_size_x = 550  # Ancho de la pantalla en píxeles
screen_size_y = 250  # Alto de la pantalla en píxeles

# Cantidad de cuadrados en la cuadrícula (en este caso 5x5)
grid_size = 5


# Se calcula y determina el tamaño de las celdas
cell_size = (screen_size_x - 50) // (grid_size * 2)

# Crear la pantalla con la resolución especificada
screen = pygame.display.set_mode((screen_size_x, screen_size_y)) 

# Definir colores
WHITE = (255, 255, 255)  # Blanco
BLACK = (0, 0, 0)  # Negro
RED = (255, 0, 0)  # Rojo
BLUE = (0, 0, 255)  # Azul
GREEN = (0, 255, 0)  # Verde

# Crear dos tableros con matrices de ceros
tableros = [np.zeros((grid_size, grid_size)) for _ in range(2)]

def generar_barcos_al_azar(tablero, num_barcos):
    # i = 0
    for _ in range(num_barcos): 
        while True:
            x = np.random.randint(0, grid_size)
            y = np.random.randint(0, grid_size)
            # i += 1
            # print (x, y, i)
        
            if tablero[x][y] == 0:
                tablero[x][y] = 1
                break

# Generar barcos aleatorios en los tableros
num_barcos = 3
barcos_restantes = [num_barcos, num_barcos]

generar_barcos_al_azar(tableros[1], num_barcos)
generar_barcos_al_azar(tableros[0], num_barcos)

# Función para dibujar la cuadrícula del primer tablero
def draw_grid_tablero1(nombre):
    for x in range(0, (cell_size * grid_size), cell_size):
        for y in range(0, screen_size_y, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GREEN, rect, 1)

# Función para dibujar la cuadrícula del segundo tablero
def draw_grid_tablero2(nombre):
    for x in range(300, screen_size_x, cell_size):
        for y in range(0, screen_size_y, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GREEN, rect, 1)

def recargar_tableros(tablero):
    screen.fill(BLACK)
    draw_grid_tablero1("Tablero 1")
    draw_grid_tablero2("Tablero 2")
    draw_shots(0)
    draw_shots(1)
    pygame.display.flip()

def mostrar_mensaje(mensaje, tablero):
    screen.fill(BLACK)
    rect = pygame.Rect(0, 0, (screen_size_x/3), (screen_size_y/3))
    rect.center = ((screen_size_x // 2), (screen_size_y // 2))
    pygame.draw.rect(screen, WHITE, rect)

    font = pygame.font.Font(None, 26)
    text = font.render(mensaje, True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  # Espera 3 segundos

    recargar_tableros(tablero)
    
def mostrar_mensaje_ganador(mensaje):
    screen.fill(BLACK)
    rect = pygame.Rect(0, 0, (screen_size_x/3), (screen_size_y/3))
    rect.center = (screen_size_x // 2), (screen_size_y // 2)
    pygame.draw.rect(screen, WHITE, rect)

    font = pygame.font.Font(None, 26)
    text = font.render(mensaje, True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Espera 3 segundos

    pygame.quit()

# Función para dibujar los disparos en el tablero
def draw_shots(tablero):
    for x in range(grid_size):
        for y in range(grid_size):
            if tableros[tablero][x, y] == 2:  # Disparo fallido
                center_x = (x * cell_size + cell_size // 2) + 300 * tablero
                center_y = (y * cell_size + cell_size // 2)
                half_diag = cell_size * math.sqrt(2) // 4
                pygame.draw.line(screen, RED, 
                                 (center_x - half_diag, center_y - half_diag), 
                                 (center_x + half_diag, center_y + half_diag), 
                                 5)
                pygame.draw.line(screen, RED, 
                                 (center_x - half_diag, center_y + half_diag), 
                                 (center_x + half_diag, center_y - half_diag), 
                                 5)
            elif tableros[tablero][x, y] == 4:  # Disparo acertado
                pygame.draw.circle(screen, BLUE, ((x * cell_size + cell_size // 2) + 300 * tablero, y * cell_size + cell_size // 2), cell_size // 3)

# Función para procesar el clic del ratón
def handle_click(pos, tablero):
    x, y = pos
    if tablero == 0:
        if 0 <= x < 250 and 0 <= y < 250:  # Dentro del primer tablero
            grid_x = x // cell_size
            grid_y = y // cell_size
        else:
            mostrar_mensaje("Tablero equivocado", tablero)
            return  # Clic fuera del primer tablero
    else:
        if 300 <= x < 550 and 0 <= y < 250:  # Dentro del segundo tablero
            grid_x = (x - 300) // cell_size
            grid_y = y // cell_size
        else:
            mostrar_mensaje("Tablero equivocado", tablero)
            return  # Clic fuera del segundo tablero

    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
        if tableros[tablero][grid_x, grid_y] == 0:
            tableros[tablero][grid_x, grid_y] = 2  # Marca disparo fallido
        elif tableros[tablero][grid_x, grid_y] == 1:
            tableros[tablero][grid_x, grid_y] = 4  # Marca disparo acertado
            barcos_restantes[tablero] -= 1  # Resta 1 a barcos_restantes

# Bucle principal del juego

def main():
    running = True
    tablero = 0

    mostrar_mensaje("¡Comienza el juego!", tablero)
    mostrar_mensaje(f"Turno de tablero {tablero + 1}", tablero)

    while running:
        draw_grid_tablero1("Tablero 1")
        draw_grid_tablero2("Tablero 2")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                handle_click(event.pos, tablero)
                draw_shots(tablero)
                pygame.display.flip()  # Muestra la cruz o el círculo azul
                pygame.time.wait(500)  # Espera un poco antes de mostrar el pop up

                if barcos_restantes[tablero] == 0:
                    mostrar_mensaje_ganador(f"¡Tablero {tablero + 1} ganó!")
                    return  # Agrega esto para salir de la función main()
                # Verifica si se hizo clic en el tablero correcto
                if (tablero == 0 and 0 <= event.pos[0] < 250) or (tablero == 1 and 300 <= event.pos[0] < 550):
                    tablero = 1 if tablero == 0 else 0  
                    # Cambiar de tablero
                    mostrar_mensaje(f"Turno del tablero {tablero + 1}", tablero)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()