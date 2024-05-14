from functions import *
import pygame

pygame.init()
#physics
fuel = 100
clock = pygame.time.Clock()

# Création de la fenêtre de jeu
size_x = 1280
size_y = 720
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Efrei Lander")
background_image = pygame.image.load("Assets/space.png").convert()
fuel_image = pygame.image.load("Assets/fuel.png").convert_alpha()

# Coordonnées de la lune
x_lune = size_x - 100
y_lune = 100

# Rayon de la lune
rayon_lune = 50

image_lune = pygame.image.load('Assets/planet.png').convert_alpha()
image_lune = pygame.transform.scale(image_lune, (rayon_lune*2, rayon_lune*2))  # Ajuster la taille de l'image

font = pygame.font.Font("Assets/ethnocentric rg.otf",16)

running = True

x1, x2, y1, y2, hauteur_plateforme = generer_plateforme(screen)

mountain_coords = get_relief_coord(screen)
print(mountain_coords)
#for i in range(len(mountain_coords)):
    #pygame.screen.set_at((i, mountain_coords[i]), (255, 0, 0))

while running:
    clock.tick(60)
    screen.blit(background_image, (0, 0))
    screen.blit(fuel_image, (40, 40))
    dessiner_plateforme(x1, x2, y1, y2, hauteur_plateforme,screen)
    generer_montagne(screen, x1, x2, y1, y2)
    generer_montagne(screen, x2, 1280, y2, 650)
    generer_montagne(screen, 0 - largeur_plateforme, x1, 500, y1)
    fill_mountain(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                fuel-=1
    pygame.display.update()
    screen.blit(image_lune, (x_lune - rayon_lune, y_lune - rayon_lune))
    text_fuel = font.render(str(fuel),True,(255,255,255))
    fuel_rect = text_fuel.get_rect()

    fuel_rect.topleft = (140,60)

    screen.blit(text_fuel,fuel_rect)
    pygame.display.flip()



pygame.quit()