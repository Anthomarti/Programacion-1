import pygame
import os
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colores RGB
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
POPUP_BG_COLOR = (255, 255, 255)
POPUP_TEXT_COLOR = (0, 0, 0)

# Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Tablero
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]

# Fuente para el texto
font = pygame.font.Font(None, 32)

def draw_lines():
    # Líneas horizontales
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Líneas verticales
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == None

def is_board_full():
    return all(all(row) for row in board)

def check_win(player):
    # Verificar victorias verticales y horizontales
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Verificar diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def draw_popup(message):
    popup_width, popup_height = 250, 100
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2

    # Dibujar un rectángulo semi-transparente que cubra toda la pantalla
    s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    s.fill((0, 0, 0, 128))  # Negro semi-transparente
    screen.blit(s, (0, 0))

    # Dibujar el popup
    pygame.draw.rect(screen, POPUP_BG_COLOR, (popup_x, popup_y, popup_width, popup_height))
    pygame.draw.rect(screen, POPUP_TEXT_COLOR, (popup_x, popup_y, popup_width, popup_height), 2)

    text_surface = font.render(message, True, POPUP_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text_surface, text_rect)

def restart():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None
    return 'X', False, None

# Configuración para Replit
if 'REPL_SLUG' in os.environ:
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

player = 'X'
game_over = False
winner_message = None

# Bucle principal del juego
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row, clicked_col = int(mouseY // SQUARE_SIZE), int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                    winner_message = f"¡Felicidades! Ganó el jugador {player}"
                elif is_board_full():
                    game_over = True
                    winner_message = "¡Empate!"
                else:
                    player = 'O' if player == 'X' else 'X'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, game_over, winner_message = restart()

    # Dibujar el juego
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()

    # Dibujar la ventana emergente si hay un ganador
    if winner_message:
        draw_popup(winner_message)

    pygame.display.update()

    # Para Replit: guardar la pantalla como imagen
    if 'REPL_SLUG' in os.environ:
        pygame.image.save(screen, "game_state.png")

    clock.tick(30)