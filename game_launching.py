from functions import *

def game_launching():

    # Création de la fenêtre de jeu
    size_x = get_var("screen_width")
    size_y = get_var("screen_height")

    screen = pygame.display.set_mode((size_x, size_y))
    pygame.display.set_caption("Efrei Lander")



    #Pour les étoiles
    etoiles = [(random.randint(0, size_x), random.randint(0, size_y)) for _ in range(100)]

    background_image = pygame.image.load("Assets/space.png").convert()

    # Coordonnées de la lune
    x_lune = size_x
    y_lune = size_y

    # Rayon de la lune
    rayon_lune = get_var("moon_radius")


    image_lune = pygame.image.load('Assets/planet.png').convert_alpha()
    image_lune = pygame.transform.scale(image_lune, (rayon_lune*2, rayon_lune*2))  # Ajuster la taille de l'image


    running = True
    screen.blit(background_image, (0, 0))
    x1, x2, y1, y2, hauteur_plateforme = generer_plateforme(screen)
    generer_montagne(screen, x1, x2, y1, y2)
    generer_montagne(screen, x2, 1280, y2, 650)
    largeur_plateforme = platform_properties()[0]
    generer_montagne(screen, 0-largeur_plateforme, x1, 500, y1)

    fill_mountain(screen)
    mountain_coords = get_relief_coord(screen)
    print(mountain_coords)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        screen.blit(image_lune, (x_lune - rayon_lune, y_lune - rayon_lune))


    pygame.quit()