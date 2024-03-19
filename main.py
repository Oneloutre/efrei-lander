from functions import generer_plateforme
import pygame

pygame.init()

# Création de la fenêtre de jeu
size_x = 1280
size_y = 720
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Efrei Lander")
background_color = (0, 0, 0)

running = True
screen.fill(background_color)
x1, x2, largeur_plateforme = generer_plateforme(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

