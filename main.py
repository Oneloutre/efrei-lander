import pygame
import random
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LANDER_WIDTH = 50
LANDER_HEIGHT = 50
GRAVITY = 0.1
THRUST = 0.5
ROTATION_SPEED = 2
FUEL = 100

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lunar Lander")
clock = pygame.time.Clock()

# Load images
background = "Assets/space.png"
lander = "Assets/lander.png"
background_img = pygame.image.load(background)
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
lander_img = pygame.image.load(lander)
lander_img = pygame.transform.scale(lander_img, (LANDER_WIDTH, LANDER_HEIGHT))

# Game variables
lander_x = SCREEN_WIDTH // 2
lander_y = 50
velocity_x = 0
velocity_y = 0
fuel = FUEL
rotation_angle = 0

# Flags for continuous rotation and thrust
rotate_left = False
rotate_right = False
thrusting = False

# Main game loop
running = True
while running:
    # Game variables
    lander_x = SCREEN_WIDTH // 2
    lander_y = 50
    velocity_x = 0
    velocity_y = 0
    fuel = FUEL
    rotation_angle = 0

    # Inner game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and fuel > 0:
                    thrusting = True
                    fuel -= 1
                elif event.key == pygame.K_DOWN and fuel > 0:
                    velocity_y += THRUST
                    fuel -= 1
                elif event.key == pygame.K_LEFT and fuel > 0:
                    rotate_left = True
                elif event.key == pygame.K_RIGHT and fuel > 0:
                    rotate_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    thrusting = False
                elif event.key == pygame.K_LEFT:
                    rotate_left = False
                elif event.key == pygame.K_RIGHT:
                    rotate_right = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        # Apply gravity
        velocity_y += GRAVITY

        # Update rotation angle based on flags
        if rotate_left:
            rotation_angle += ROTATION_SPEED
        if rotate_right:
            rotation_angle -= ROTATION_SPEED

        # Apply thrust
        if thrusting and fuel > 0:
            # Calculate horizontal and vertical components of thrust based on rotation angle
            thrust_x = -math.sin(math.radians(rotation_angle)) * THRUST
            thrust_y = -math.cos(math.radians(rotation_angle)) * THRUST
            velocity_x += thrust_x
            velocity_y += thrust_y
            fuel -= 1

        # Update lander position
        lander_x += velocity_x
        lander_y += velocity_y

        # Clear the screen
        screen.blit(background_img, (0, 0))

        # Rotate the lander image
        rotated_lander = pygame.transform.rotate(lander_img, rotation_angle)

        # Draw the rotated lander
        lander_rect = rotated_lander.get_rect(center=(lander_x, lander_y))
        screen.blit(rotated_lander, lander_rect.topleft)

        # Draw fuel bar
        fuel_bar_width = fuel * (SCREEN_WIDTH / FUEL)
        fuel_rect = pygame.Rect(0, 0, fuel_bar_width, 20)
        pygame.draw.rect(screen, GREEN, fuel_rect)

        # Check for collision with ground
        if lander_y >= SCREEN_HEIGHT - LANDER_HEIGHT:
            velocity_y = 0
            lander_y = SCREEN_HEIGHT - LANDER_HEIGHT
            fuel = 0
            pygame.draw.rect(screen, RED, (0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait 2 seconds before restarting
            break  # Restart the inner game loop

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Quit Pygame
pygame.quit()
