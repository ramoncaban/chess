import pygame

def draw_board(screen, tile_size=100):
    colors = [(238, 238, 210), (118, 150, 86)] # Light and dark squares
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * tile_size, row * tile_size,
                                                tile_size, tile_size))

def load_piecees():
    pieces = {}
    piece_names = ['b', 'k', 'n', 'p', 'q', 'r']
    colors = ['w', 'b'] # White and black
    for color in colors:
        for name in piece_names:
            image =