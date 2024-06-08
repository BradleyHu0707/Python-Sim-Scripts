# A physics simulation in Python using Pygame with interactive controls

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAVITY = 0.5  # Reduced gravity
BOUNCINESS = 0.7  # Floor bounciness

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Physics variables
position = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
velocity = pygame.Vector2(-5, 0)  # Initial push to the left
acceleration = pygame.Vector2()

# Slider variables
gravity_slider = pygame.Rect(10, 10, 100, 10)
bounciness_slider = pygame.Rect(10, 30, 100, 10)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouse interaction
    mouse_down = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()
    if mouse_down:
        acceleration = (pygame.Vector2(mouse_pos) - position) * 0.1

    # Update physics
    velocity += acceleration
    position += velocity + 0.5 * acceleration
    acceleration *= 0  # Reset acceleration

    # Boundary checks
    if position.y >= HEIGHT:
        velocity.y *= -BOUNCINESS
        position.y = HEIGHT
    if position.x <= 0 or position.x >= WIDTH:
        velocity.x *= -BOUNCINESS
        position.x = max(0, min(position.x, WIDTH))

    # Drawing
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(position.x), int(position.y)), 20)

    # Sliders
    pygame.draw.rect(screen, (180, 180, 180), gravity_slider)
    pygame.draw.rect(screen, (180, 180, 180), bounciness_slider)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
