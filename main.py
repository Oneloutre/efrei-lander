from functions import *
import pygame
from variables import *
pygame.init()

# Création de la fenêtre de jeu
size_x = get_vars("variables.json")["screen_width"]
size_y = get_vars("variables.json")["screen_height"]

screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Efrei Lander")

# Will be deleted because of the background asset

background_color = (0, 0, 0)

#Pour les étoiles
etoiles = [(random.randint(0, size_x), random.randint(0, size_y)) for _ in range(100)]

# Coordonnées de la lune
x_lune = size_x - 100
y_lune = 100

# Rayon de la lune
rayon_lune = 50

image_lune = pygame.image.load('Assets/lune.png').convert_alpha()
image_lune = pygame.transform.scale(image_lune, (rayon_lune*2, rayon_lune*2))  # Ajuster la taille de l'image



running = True
screen.fill(background_color)
x1, x2, y1, y2, hauteur_plateforme = generer_plateforme(screen)
generer_montagne(screen, x1, x2, y1, y2)
generer_montagne(screen, x2, 1280, y2, 650)
generer_montagne(screen, 0-largeur_plateforme, x1, 500, y1)

fill_mountain(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    for x, y in etoiles:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
    screen.blit(image_lune, (x_lune - rayon_lune, y_lune - rayon_lune))

pygame.quit()