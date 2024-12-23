import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fill screen with white
        screen.fill(WHITE)

        # Update display
        pygame.display.flip()

pygame.quit()